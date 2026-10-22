#!/usr/bin/env python3
"""Postman コレクション（docs.api.bcart.jp の公開データ）から OpenAPI 3.1 を生成する初期版ジェネレータ。

使い方: gen_openapi.py <collection.json> <normalized.md> <out.yaml>
  collection.json: https://docs.api.bcart.jp/api/collections/8793158/T1Dwbtbh?versionTag=latest
  normalized.md  : 公式の bcart-api_document_v1_normalized.md（スコープ一覧の取得に使う）
"""
import html
import json
import re
import sys
from collections import OrderedDict

import yaml

coll_path, md_path, out_path = sys.argv[1:4]
coll = json.load(open(coll_path, encoding="utf-8"))
md = open(md_path, encoding="utf-8").read()

SCOPES = OrderedDict(re.findall(r"^\| ([a-z_]+-(?:read|write)) \| (.+?) \|$", md, re.M))
warnings = []


def strip(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s)).replace("\x08", "").strip()


def html_to_text(s):
    s = re.sub(r"<table.*?</table>", "", s or "", flags=re.S)
    s = re.sub(r"<br\s*/?>", "\n", s)
    s = re.sub(r"</p>", "\n", s)
    return strip(s)


# ---- 型変換 -----------------------------------------------------------
def conv_type(t):
    t = t.strip()
    nullable = False
    if "/null" in t:
        nullable = True
        t = t.replace("/null", "")
    base = {
        "文字列": {"type": "string"},
        "整数": {"type": "integer"},
        "数値": {"type": "number"},
        "配列": {"type": "array", "items": {}},
        "オブジェクト": {"type": "object"},
        "論理": {"type": "boolean"},
        "真偽値": {"type": "boolean"},
        "日付": {"type": "string"},
        "日時": {"type": "string"},
        "年月日": {"type": "string"},
        "UUID": {"type": "string", "format": "uuid"},
    }.get(t)
    if base is None:
        base = {"type": "string"}
        warnings.append(f"unknown type {t!r}")
    base = dict(base)
    if nullable:
        base["type"] = [base["type"], "null"]
    return base


# ---- 説明 HTML の表パース ---------------------------------------------
TYPE_WORDS = {"文字列", "整数", "数値", "配列", "オブジェクト", "論理", "真偽値", "日付", "日時", "年月日", "UUID"}


def parse_tables(desc):
    """description から [(見出し, [row dict])] を返す。"""
    out = []
    parts = re.split(r"<p><strong>(.*?)</strong></p>", desc or "")
    # parts: [pre, head1, body1, head2, body2, ...]
    chunks = [("", parts[0])] + [(parts[i], parts[i + 1]) for i in range(1, len(parts) - 1, 2)]
    for head, body in chunks:
        for tbl in re.findall(r"<table.*?</table>", body, re.S):
            rows = re.findall(r"<tr>(.*?)</tr>", tbl, re.S)
            if not rows:
                continue
            hdr = [strip(c) for c in re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", rows[0], re.S)]
            recs = []
            for r in rows[1:]:
                cells = [strip(c) for c in re.findall(r"<td[^>]*>(.*?)</td>", r, re.S)]
                if cells and len(cells) > 1 and " " in cells[0] and cells[1] in TYPE_WORDS:
                    # 公式表の欠陥: Key 列と 名称 列が1セルに結合されている行を補正
                    k, n = cells[0].split(" ", 1)
                    cells = [k, n] + cells[1:]
                if cells:
                    recs.append(dict(zip(hdr, cells)))
            out.append((strip(head), hdr, recs))
    return out


def row_fields(r):
    key = r.get("Key") or r.get("KEY") or r.get("パラメータ名") or ""
    return key, r.get("名称", ""), r.get("型", ""), r.get("最大桁数", ""), r.get("内容", "")


def describe(name, maxlen, note):
    parts = []
    if name:
        parts.append(name)
    if note:
        parts.append(note)
    if maxlen:
        parts.append(f"最大桁数: {maxlen}")
    return " / ".join(parts)


# ---- 例からのスキーマ推論 -------------------------------------------------
def infer(v):
    if v is None:
        return {}
    if isinstance(v, bool):
        return {"type": "boolean"}
    if isinstance(v, int):
        return {"type": "integer"}
    if isinstance(v, float):
        return {"type": "number"}
    if isinstance(v, str):
        return {"type": "string"}
    if isinstance(v, list):
        return {"type": "array", "items": infer(v[0]) if v else {}}
    if isinstance(v, dict):
        keys = list(v.keys())
        # キーが ID の辞書（{"1": {...}, "2": {...}}）は additionalProperties に畳む
        if keys and all(re.fullmatch(r"\d+", k) for k in keys):
            return {"type": "object", "additionalProperties": infer(v[keys[0]])}
        return {"type": "object", "properties": {k: infer(x) for k, x in v.items()}}
    return {}


def merge_nullable(schema, tbl):
    """表が示す型を優先し、例で推論した構造(properties/items)があれば引き継ぐ。"""
    new = dict(tbl)
    t = new["type"]
    base_t = t[0] if isinstance(t, list) else t
    for k in ("properties", "items", "additionalProperties"):
        if k in schema and base_t in ("object", "array"):
            new[k] = schema[k]
    if base_t == "array" and "items" not in new:
        new["items"] = {}
    return new


def apply_table(schema, rows):
    """レスポンス表を、最初に該当キーを持つオブジェクト階層へ反映する。"""
    keys = {row_fields(r)[0]: r for r in rows}
    queue = [schema]
    while queue:
        s = queue.pop(0)
        if not isinstance(s, dict):
            continue
        props = s.get("properties")
        if props is not None and any(k in props for k in keys):
            for k, r in keys.items():
                _, nm, ty, ml, note = row_fields(r)
                d = describe(nm, ml, note)
                if k in props:
                    props[k] = merge_nullable(props[k], conv_type(ty)) if ty else props[k]
                else:
                    props[k] = conv_type(ty) if ty else {}
                if d:
                    props[k]["description"] = d
            return True
        if props:
            queue.extend(props.values())
        if "items" in s:
            queue.append(s["items"])
    return False


# ---- コレクション走査 -------------------------------------------------
def norm_path(raw):
    p = re.sub(r"^.*?(/api/v1)", r"\1", raw.split("?")[0])
    p = re.sub(r"%[0-9A-Fa-f]{2}", "x", p) if "%" in p else p
    return p


def camel(s):
    return "".join(w.capitalize() for w in s.split("_"))


ops = OrderedDict()  # (method, path) -> dict
tags = []
for folder in coll["item"]:
    tag = folder["name"].strip()
    tags.append({"name": tag, "description": html_to_text(folder.get("description"))})
    for it in folder["item"]:
        rq = it["request"]
        raw = rq["url"] if isinstance(rq["url"], str) else rq["url"].get("raw", "")
        path = norm_path(raw)
        m = re.fullmatch(r"/api/v1/([a-z_]+)(?:/(.*))?", path)
        res, tail = m.group(1), m.group(2)
        pname = None
        if tail:
            mm = re.search(r":([A-Za-z_]+)", it["name"])
            pname = mm.group(1) if mm else "id"
            path = f"/api/v1/{res}/{{{pname}}}"
        else:
            path = f"/api/v1/{res}"
        method = rq["method"].lower()
        key = (method, path)
        rec = {"item": it, "tag": tag, "res": res, "pname": pname, "path": path, "method": method,
               "bulk": method in ("patch", "post") and not tail, "sample_tail": tail}
        if key in ops:
            ops[key].setdefault("extra", []).append(rec)
        else:
            ops[key] = rec


def scope_for(res, method):
    base = {"stock": "product_stock"}.get(res, res)
    suffix = "read" if method == "get" else "write"
    s = f"{base}-{suffix}"
    return s if s in SCOPES else None


COMMON_QUERY = {
    "limit": {"name": "limit", "in": "query", "schema": {"type": "integer", "default": 20, "maximum": 100},
              "description": "取得件数。指定なしは20件、最大100件"},
    "offset": {"name": "offset", "in": "query", "schema": {"type": "integer", "default": 0},
               "description": "指定した値+1件目のデータから limit 分を取得。指定しない場合は0"},
    "ids": {"name": "ids", "in": "query", "schema": {"type": "string"},
            "description": "IDをカンマ区切りで指定。範囲や条件で指定する場合は拡張パラメータを利用"},
    "fields": {"name": "fields", "in": "query", "schema": {"type": "string"},
               "description": "取得したいフィールドをカンマ区切りで指定"},
}

EXT_NOTE = ("拡張パラメータ（`A__gte` `A__lt` `A__in` `A__has` `or__A` など）で絞り込み可能。"
            "詳細は docs/04-parameters.md を参照。")

used_ids = set()


def op_id(rec):
    base = {"get": "get", "patch": "update", "post": "create", "delete": "delete"}[rec["method"]]
    if rec["method"] == "get" and not rec["pname"]:
        base = "list"
    if rec["method"] == "patch" and rec["bulk"]:
        base = "bulkUpdate"
    oid = base + camel(rec["res"]) + ("ById" if rec["pname"] and base != "get" else "")
    if base == "get" and rec["pname"]:
        oid = "get" + camel(rec["res"]) + "ById"
    oid = oid[0].lower() + oid[1:]
    n, o = 2, oid
    while oid in used_ids:
        oid = f"{o}{n}"
        n += 1
    used_ids.add(oid)
    return oid


def parse_json(s):
    try:
        return json.loads(s)
    except Exception:
        return None


def build_body(rec):
    it = rec["item"]
    rq = it["request"]
    body = rq.get("body") or {}
    raw = body.get("raw") if body.get("mode") == "raw" else None
    example = parse_json(raw) if raw else None
    rows = []
    for head, hdr, recs in parse_tables(rq.get("description")):
        if head == "リクエストBODY":
            rows = recs
    props = OrderedDict()
    for r in rows:
        key, nm, ty, ml, note = row_fields(r)
        if not key:
            continue
        # 一括登録・更新の表は `product_sets[{{i}}][name]` 形式 → 要素のキー `name` に直す
        key = re.sub(r"^[a-z_]+\[\{\{i\}\}\]\[([^\]]+)\]", r"\1", key)
        top = key.split("[")[0]
        sch = conv_type(ty) if ty else {"type": "string"}
        d = describe(nm, ml, note)
        if "[" in key:  # ネスト表記は親項目の説明に畳む
            base_t = sch["type"] if not isinstance(sch["type"], list) else sch["type"][0]
            cur = props.get(top)
            line = f"`{key}`: {d}" if d else f"`{key}`"
            if cur is None:
                cur = {"type": "object", "additionalProperties": True} if base_t != "array" else \
                    {"type": "array", "items": {"type": "object", "additionalProperties": True}}
                cur["description"] = line
            else:
                cur["description"] += "\n" + line
            props[top] = cur
        else:
            if d:
                sch["description"] = d
            props[top] = sch
    return rows, props, example, raw


def request_body(rec):
    rows, props, example, raw = build_body(rec)
    if not rows and example is None and not raw:
        return None
    item_schema = {"type": "object", "properties": dict(props)} if props else (infer(example) if example else {"type": "object"})
    wrapper = None
    if isinstance(example, dict) and len(example) == 1 and isinstance(next(iter(example.values())), list):
        wrapper = next(iter(example))
    elif rec["bulk"]:
        wrapper = rec["res"]
    if rec["bulk"] and wrapper:
        if rec["method"] == "patch" and "id" in item_schema.get("properties", {}) is False:
            pass
        schema = {"type": "object", "required": [wrapper],
                  "properties": {wrapper: {"type": "array", "items": item_schema}}}
    else:
        schema = item_schema
    examples = OrderedDict()
    if example is not None:
        examples["default"] = {"value": example}
    for ex in rec.get("extra", []):
        _, _, e2, _ = build_body(ex)
        if e2 is not None:
            examples[ex["item"]["name"]] = {"value": e2}
    content = {"schema": schema}
    if examples:
        content["examples"] = dict(examples)
    return {"required": True, "content": {"application/json": content}}


def responses_for(rec):
    it = rec["item"]
    res = OrderedDict()
    tables = []
    for head, hdr, recs in parse_tables(it["request"].get("description")):
        if head == "レスポンス一覧":
            tables = recs
    done = False
    for r in it.get("response", []):
        code = str(r.get("code", 200))
        if code in res:
            continue
        body = parse_json(r.get("body") or "")
        entry = {"description": r.get("status") or "OK"}
        if body is not None:
            sch = infer(body)
            if tables and not done:
                apply_table(sch, tables)
                done = True
            entry["content"] = {"application/json": {"schema": sch, "example": body}}
        res[code] = entry
    if not res:
        res["200"] = {"description": "OK"}
    return res


paths = OrderedDict()
for (method, path), rec in ops.items():
    it = rec["item"]
    rq = it["request"]
    o = OrderedDict()
    o["tags"] = [rec["tag"]]
    o["operationId"] = op_id(rec)
    desc = html_to_text(rq.get("description"))
    kind = {"get": "取得" if rec["pname"] else "一覧取得", "patch": "更新", "post": "登録", "delete": "削除"}[method]
    if method == "patch" and rec["bulk"]:
        kind = "一括更新"
    o["summary"] = f"{rec['tag']} {kind}"
    notes = []
    if method == "get" and not rec["pname"]:
        notes.append(EXT_NOTE)
    if notes:
        o["description"] = "\n\n".join(notes)
    params = []
    if rec["pname"]:
        pdesc = {"product_no": "品番", "id": "ID"}.get(rec["pname"], rec["pname"])
        params.append({"name": rec["pname"], "in": "path", "required": True, "schema": {"type": "string" if rec["pname"] != "id" else "string"}, "description": pdesc})
    if method == "get" and not rec["pname"]:
        seen = set()
        for head, hdr, recs in parse_tables(rq.get("description")):
            if head in ("URIパラメータ", "URLパラメータ"):
                for r in recs:
                    key, nm, ty, ml, note = row_fields(r)
                    if not key or key in seen:
                        continue
                    seen.add(key)
                    if key in COMMON_QUERY:
                        params.append({"$ref": f"#/components/parameters/{key}"})
                        continue
                    sch = conv_type(ty) if ty else {"type": "string"}
                    if sch.get("type") == "array":
                        sch = {"type": "string"}
                    sch.pop("items", None)
                    p = {"name": key, "in": "query", "schema": sch}
                    d = describe(nm, ml, note)
                    if d:
                        p["description"] = d
                    params.append(p)
        for k in COMMON_QUERY:
            if k not in seen:
                params.append({"$ref": f"#/components/parameters/{k}"})
    if params:
        o["parameters"] = params
    if method in ("patch", "post"):
        rb = request_body(rec)
        if rb:
            o["requestBody"] = rb
    o["responses"] = responses_for(rec)
    for code, ref in (("401", "Unauthorized"), ("422", "ValidationError"), ("429", "RateLimited")):
        o["responses"].setdefault(code, {"$ref": f"#/components/responses/{ref}"})
    sc = scope_for(rec["res"], method)
    o["security"] = [{"bearerAuth": []}] + ([{"oauth2": [sc]}] if sc else [{"oauth2": []}])
    paths.setdefault(path, OrderedDict())[method] = o

# OAuth トークンエンドポイント（別ホスト）
token_servers = [{"url": "https://app.bcart.jp"}]
paths["/oauth/token"] = {
    "post": {
        "tags": ["認証"],
        "operationId": "issueToken",
        "summary": "アクセストークン発行／更新",
        "description": "`grant_type=authorization_code` で認可コードをアクセストークンに交換、"
                       "`grant_type=refresh_token` でアクセストークンを更新する。"
                       "アクセストークンの有効期限は14日。リフレッシュトークン使用時は新しいリフレッシュトークンも発行され、"
                       "使用済みリフレッシュトークンと古いアクセストークンは無効になる。",
        "servers": token_servers,
        "security": [],
        "requestBody": {"required": True, "content": {"application/x-www-form-urlencoded": {"schema": {
            "type": "object", "required": ["grant_type", "client_id", "client_secret"],
            "properties": {
                "grant_type": {"type": "string", "enum": ["authorization_code", "refresh_token"]},
                "client_id": {"type": "string", "description": "アプリ登録時に発行されたクライアントID"},
                "client_secret": {"type": "string", "description": "アプリ登録時に発行されたクライアントシークレット"},
                "redirect_uri": {"type": "string", "description": "authorization_code 時: 登録したリダイレクトURI"},
                "code": {"type": "string", "description": "authorization_code 時: 認可コード"},
                "refresh_token": {"type": "string", "description": "refresh_token 時: リフレッシュトークン"},
            }}}}},
        "responses": {
            "200": {"description": "OK", "content": {"application/json": {"schema": {
                "type": "object", "properties": {
                    "token_type": {"type": "string", "example": "Bearer"},
                    "expires_in": {"type": "integer", "example": 1209600},
                    "access_token": {"type": "string"},
                    "refresh_token": {"type": "string"}}}}}},
            "400": {"description": "失敗", "content": {"application/json": {"schema": {
                "type": "object", "properties": {
                    "error": {"type": "string"}, "error_description": {"type": "string"},
                    "hint": {"type": "string"}, "message": {"type": "string"}}}}}},
        },
    }
}
tags.insert(0, {"name": "認証", "description": "OAuth2.0 トークン発行（パーソナルアクセストークンの場合は不要）"})

spec = OrderedDict()
spec["openapi"] = "3.1.0"
spec["info"] = OrderedDict([
    ("title", "BカートAPI"),
    ("version", "1.0.0"),
    ("summary", "BカートAPI V1（非公式の OpenAPI 変換版）"),
    ("description", (
        "https://docs.api.bcart.jp/ の公開データから機械変換した非公式の OpenAPI 定義。仕様の正本は公式ドキュメント。\n\n"
        "- レート制限: 300秒につき300回。超過すると300秒間ロックされ、`Retry-After` ヘッダーが付く（サイトIDとクライアントIDの組み合わせ単位）\n"
        "- クロスドメイン接続は許可されておらず、ブラウザ上の JavaScript からは利用できない\n"
        "- PATCH/POST の Content-Type は `application/x-www-form-urlencoded` も指定可能\n"
        "- 後方互換な変更（エンドポイント・プロパティ・任意パラメータの追加）は予告なく行われるため、未知のプロパティを許容すること\n"
        "- 型・必須の判定は公式ドキュメントの表（日本語）からの変換のため、`required` は付けていない。"
        "「項目存在時必須」等の条件は各項目の description を参照\n"
        "- レスポンスのスキーマはサンプルJSONからの推論を、公式の「レスポンス一覧」表で補ったもの")),
])
spec["servers"] = [{"url": "https://api.bcart.jp", "description": "本番"}]
spec["tags"] = tags
spec["security"] = [{"bearerAuth": []}]
spec["paths"] = paths
spec["components"] = OrderedDict([
    ("securitySchemes", {
        "bearerAuth": {"type": "http", "scheme": "bearer", "description": "パーソナルアクセストークン、またはOAuth2.0で取得したアクセストークン"},
        "oauth2": {"type": "oauth2", "flows": {"authorizationCode": {
            "authorizationUrl": "https://app.bcart.jp/oauth/authorize",
            "tokenUrl": "https://app.bcart.jp/oauth/token",
            "refreshUrl": "https://app.bcart.jp/oauth/token",
            "scopes": dict(SCOPES)}}},
    }),
    ("parameters", COMMON_QUERY),
    ("schemas", {
        "ValidationErrors": {"type": "object", "properties": {"errors": {"type": "array", "items": {
            "type": "object", "additionalProperties": {"type": "array", "items": {"type": "string"}}}}}},
        "Error": {"type": "object", "properties": {"error": {"type": "string"}}},
    }),
    ("headers", {
        "RetryAfter": {"description": "リクエスト上限超過時のみ付与。ロック解除までの時間", "schema": {"type": "integer"}},
    }),
    ("responses", {
        "Unauthorized": {"description": "認証・権限エラー（`Unauthenticated.`）", "content": {"application/json": {
            "schema": {"$ref": "#/components/schemas/Error"}, "example": {"error": "Unauthenticated."}}}},
        "ValidationError": {"description": "パラメータの値が不正", "content": {"application/json": {
            "schema": {"$ref": "#/components/schemas/ValidationErrors"},
            "example": {"errors": [{"param1": ["param1には〇〇を指定してください。"]}]}}}},
        "RateLimited": {"description": "レート制限超過", "headers": {"Retry-After": {"$ref": "#/components/headers/RetryAfter"}}},
    }),
])


def plain(o):
    if isinstance(o, dict):
        return {k: plain(v) for k, v in o.items()}
    if isinstance(o, list):
        return [plain(v) for v in o]
    return o


class D(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def str_rep(dumper, s):
    if "\n" in s:
        return dumper.represent_scalar("tag:yaml.org,2002:str", s, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", s)


D.add_representer(str, str_rep)
with open(out_path, "w", encoding="utf-8") as f:
    f.write("# Generated by tools/gen_openapi.py — see README.md\n")
    yaml.dump(plain(spec), f, Dumper=D, allow_unicode=True, sort_keys=False, width=120)
n_ops = sum(len(v) for v in paths.values())
print(f"paths={len(paths)} operations={n_ops} scopes={len(SCOPES)} warnings={sorted(set(warnings))}")
