# スクリプトタグ

Bカートの一般画面の各ページに出力するJavascipt, CSS, HTMLなどのクライアントサイドスクリプトを登録することができます。

## 独自タグの使用について

`body_html` に設定するコード内で、[独自タグ](https://userguide.bcart.jp/tag/)が利用できます。  
各タグが使用できるページは、`display_scope`（出力ページ）で指定するページと対応しています。  
詳しくは独自タグの[ドキュメント](https://userguide.bcart.jp/tag/)をご確認ください。

## 他スクリプトとの干渉によるエラー防止のお願い

Bカートの管理画面や他アプリから登録された**他のJavascript等と干渉してエラーを発生させないように**、即時関数を使用するなど、実装方法には十分に注意してください。

## GET {{api_url}}/api/v1/script_tags/1

**レスポンス一覧**

| パラメータ名 | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| id | スクリプトタグID | 整数 | 11 |  |
| name | 識別名 | 文字列 | 255 |  |
| display_position | 出力位置 | 文字列 | 255 | head=headタグ内,body-first=body開始タグの直後,body-last=body終了タグの直前 |
| display_scope | 出力ページ | 文字列 | 255 | all=サイト内の全ページ,product-detail=商品詳細ページ,product-list=商品一覧ページ,cart=カートページ,order-finish=注文完了ページ |
| body_html | 出力内容 | 文字列 | 65,535 |  |
| created_at | 登録日時 | 日時 | 19 | Y-m-d H:i:s |
| updated_at | 更新日時 | 日時 | 19 | Y-m-d H:i:s |

**レスポンス例（200 OK）:**

```json
{
  "script_tag": {
    "id": 1,
    "name": "console-log",
    "display_position": "head",
    "display_scope": "product-detail",
    "body_html": "<script>console.log('hoge');</script>",
    "created_at": "2024-01-01 00:00:00",
    "updated_at": "2024-01-01 00:00:00"
  }
}
```

## GET {{api_url}}/api/v1/script_tags

**URLパラメータ**

| パラメータ名 | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| limit | limit | 整数 |  | 指定した件数分のデータを取得します。指定なしの場合は20件、最大100件 |
| offset | offset | 整数 |  | 指定した値+1件目のデータからlimit分を取得します。指定しない場合は0 |
| ids | ID複数 | 整数 |  | 複数の商品セットIDをカンマ区切りで指定 |
| fields | フィールド | 文字列 |  | 取得したいフィールドカンマ区切りで指定 |
| name | 識別名 | 文字列 | 255 |  |
| display_position | 出力位置 | 文字列 | 255 | head=headタグ内,body-first=body開始タグの直後,body-last=body終了タグの直前 |
| display_scope | 出力ページ | 文字列 | 255 | all=サイト内の全ページ,product-detail=商品詳細ページ,product-list=商品一覧ページ,cart=カートページ,order-finish=注文完了ページ |
| body_html | 出力内容 | 文字列 | 65,535 |  |
| created_at | 登録日時 | 日時 | 19 | Y-m-d H:i:s |
| updated_at | 更新日時 | 日時 | 19 | Y-m-d H:i:s |
| created_at_min | 登録日時〜 | 日時 | 19 | Y-m-d H:i:s　以降を絞込 |
| created_at_max | 〜登録日時 | 日時 | 19 | Y-m-d H:i:s　以前を絞込 |
| updated_at_min | 更新日時〜 | 日時 | 19 | Y-m-d H:i:s　以降を絞込 |
| updated_at_max | 〜更新日時 | 日時 | 19 | Y-m-d H:i:s　以前を絞込 |

**レスポンス例（200 OK）:**

```json
{
  "script_tags": [
    {
      "id": 1,
      "name": "console-log",
      "display_position": "head",
      "display_scope": "product-detail",
      "body_html": "<script>console.log('hoge');</script>",
      "created_at": "2024-01-01 00:00:00",
      "updated_at": "2024-01-01 00:00:00"
    },
    {
      "id": 2,
      "name": "external-script",
      "display_position": "body-first",
      "display_scope": "cart",
      "body_html": "<script src=\"https://example.com/example.js\"></script>",
      "created_at": "2024-01-01 00:00:00",
      "updated_at": "2024-01-01 00:00:00"
    },
    {
      "id": 3,
      "name": "alert-current-page-url",
      "display_position": "body-last",
      "display_scope": "all",
      "body_html": "<script>alert('{{ page.url }}');</script>",
      "created_at": "2024-01-01 00:00:00",
      "updated_at": "2024-01-01 00:00:00"
    }
  ],
  "meta": {
    "limit": 20,
    "offset": 0,
    "total": 3
  }
}
```

## PATCH {{api_url}}/api/v1/script_tags/1

**リクエストBODY**

| KEY | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| name | 識別名 | 文字列 | 255 | 項目存在時必須 |
| display_position | 出力位置 | 文字列 | 255 | 項目存在時必須  <br>  <br>head=headタグ内,body-first=body開始タグの直後,body-last=body終了タグの直前 |
| display_scope | 出力ページ | 文字列 | 255 | 項目存在時必須  <br>  <br>all=サイト内の全ページ,product-detail=商品詳細ページ,product-list=商品一覧ページ,cart=カートページ,order-finish=注文完了ページ |
| body_html | 出力内容 | 文字列 | 65,535 |  |
| created_at | 登録日時 | 日時 | 19 | Y-m-d H:i:s |
| updated_at | 更新日時 | 日時 | 19 | 項目が存在しない場合は現在日時を設定  <br>  <br>Y-m-d H:i:s |

**リクエストボディ例:**

```json
{
  "body_html": ""
}
```

**レスポンス例（200 OK）:**

```json
{
  "script_tag": {
    "id": 1,
    "name": "console-log",
    "display_position": "head",
    "display_scope": "product-detail",
    "body_html": "",
    "created_at": "2024-01-01 00:00:00",
    "updated_at": "2024-01-08 12:00:00"
  }
}
```

## PATCH {{api_url}}/api/v1/script_tags

**リクエストBODY**

| KEY | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| script_tags\[{{i}}\]\[name\] | 識別名 | 文字列 | 255 | 項目存在時必須 |
| script_tags\[{{i}}\]\[display_position\] | 出力位置 | 文字列 | 255 | 項目存在時必須  <br>  <br>head=headタグ内,body-first=body開始タグの直後,body-last=body終了タグの直前 |
| script_tags\[{{i}}\]\[display_scope\] | 出力ページ | 文字列 | 255 | 項目存在時必須  <br>  <br>all=サイト内の全ページ,product-detail=商品詳細ページ,product-list=商品一覧ページ,cart=カートページ,order-finish=注文完了ページ |
| script_tags\[{{i}}\]\[body_html\] | 出力内容 | 文字列 | 65,535 |  |
| script_tags\[{{i}}\]\[created_at\] | 登録日時 | 日時 | 19 | Y-m-d H:i:s |
| script_tags\[{{i}}\]\[updated_at\] | 更新日時 | 日時 | 19 | 項目が存在しない場合は現在日時を設定  <br>  <br>Y-m-d H:i:s |

※ {{i}}は配列のキー

**リクエストボディ例:**

```json
{
  "script_tags": [
    {
      "id": 1,
      "body_html": "<script>console.log('fuga');</script>"
    },
    {
      "id": 2,
      "display_position": "head",
      "display_scope": "all"
    }
  ]
}
```

**レスポンス例（200 OK）:**

```json
{
  "script_tags": [
    {
      "id": 1,
      "name": "console-log",
      "display_position": "head",
      "display_scope": "product-detail",
      "body_html": "<script>console.log('fuga');</script>",
      "created_at": "2024-01-01 00:00:00",
      "updated_at": "2024-01-08 12:00:00"
    },
    {
      "id": 2,
      "name": "external-script",
      "display_position": "head",
      "display_scope": "all",
      "body_html": "<script src=\"https://example.com/example.js\"></script>",
      "created_at": "2024-01-01 00:00:00",
      "updated_at": "2024-01-08 12:00:00"
    }
  ]
}
```

## POST {{api_url}}/api/v1/script_tags

**リクエストBODY**

| KEY | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| script_tags\[{{i}}\]\[name\] | 識別名 | 文字列 | 255 | 必須 |
| script_tags\[{{i}}\]\[display_position\] | 出力位置 | 文字列 | 255 | 必須  <br>  <br>head=headタグ内,body-first=body開始タグの直後,body-last=body終了タグの直前 |
| script_tags\[{{i}}\]\[display_scope\] | 出力ページ | 文字列 | 255 | 必須  <br>  <br>all=サイト内の全ページ,product-detail=商品詳細ページ,product-list=商品一覧ページ,cart=カートページ,order-finish=注文完了ページ |
| script_tags\[{{i}}\]\[body_html\] | 出力内容 | 文字列 | 65,535 |  |
| script_tags\[{{i}}\]\[created_at\] | 登録日時 | 日時 | 19 | 項目が存在しない場合は現在日時を設定  <br>  <br>Y-m-d H:i:s |
| script_tags\[{{i}}\]\[updated_at\] | 更新日時 | 日時 | 19 | 項目が存在しない場合は現在日時を設定  <br>  <br>Y-m-d H:i:s |

※ {{i}}は配列のキー

**リクエストボディ例:**

```json
{
  "script_tags": [
    {
      "name": "console-log",
      "display_position": "head",
      "display_scope": "product",
      "body_html": "<script>console.log('hoge');</script>"
    },
    {
      "name": "external-script",
      "display_position": "body-first",
      "display_scope": "cartd",
      "body_html": "<script src=\"https://example.com/example.js\"></script>"
    },
    {
      "name": "alert-current-page-url",
      "display_position": "body-last",
      "display_scope": "alld",
      "body_html": "<script>alert('{{ page.url }}');</script>"
    }
  ]
}
```

**レスポンス例（201 Created）:**

```json
{
  "script_tags": [
    {
      "id": 1,
      "name": "console-log",
      "display_position": "head",
      "display_scope": "product-detail",
      "body_html": "<script>console.log('hoge');</script>",
      "created_at": "2024-01-01 00:00:00",
      "updated_at": "2024-01-01 00:00:00"
    },
    {
      "id": 2,
      "name": "external-script",
      "display_position": "body-first",
      "display_scope": "cart",
      "body_html": "<script src=\"https://example.com/example.js\"></script>",
      "created_at": "2024-01-01 00:00:00",
      "updated_at": "2024-01-01 00:00:00"
    },
    {
      "id": 3,
      "name": "alert-current-page-url",
      "display_position": "body-last",
      "display_scope": "all",
      "body_html": "<script>alert('{{ page.url }}');</script>",
      "created_at": "2024-01-01 00:00:00",
      "updated_at": "2024-01-01 00:00:00"
    }
  ]
}
```

## DELETE {{api_url}}/api/v1/script_tags/1

**レスポンス例（200 OK）:**

```json
{}
```
