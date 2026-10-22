---
date: 2026-10-22
project: bcart_docs
tags: [bcart, openapi, docs]
---

# やったこと

- docs.api.bcart.jp（Postman 公開ドキュメント）を、公式のAI向け正規化Markdownから `docs/`（共通仕様5本）と `reference/`（26リソース＋概要）に分割
- Postman コレクションから OpenAPI 3.1 を生成（`tools/gen_openapi.py` → `openapi/bcart-v1.yaml`）。109 操作（公式108エンドポイント相当＋OAuth トークン）

# 使った技術

- Postman 公開コレクション JSON（`/api/collections/8793158/T1Dwbtbh?versionTag=latest`）
- Python 3 + PyYAML、openapi-spec-validator（検証）

# トラブルと解決

- docs.api.bcart.jp は動的描画で WebFetch が title しか返さない → ページ内の prefetch URL からコレクション JSON を取得
- 公式表の欠陥: product_sets POST の `stock_few` 行で Key と名称が1セルに結合 → 生成時に補正
- 一括更新の表は `product_sets[{{i}}][name]` 形式 → 要素キーへ正規化

# 学び・記事ネタ

- Postman 公開ドキュメントはコレクション JSON が取れる。トラブル対応／技術紹介の種
- DELETE は script_tags / webhooks の2件のみ（当初「無い」と誤認、件数照合で判明）
