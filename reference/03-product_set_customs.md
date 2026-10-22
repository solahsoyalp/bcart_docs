# 商品セットカスタム項目

商品のセット情報で任意に設定できる項目

## GET {{api_url}}/api/v1/product_set_customs/17

**レスポンス一覧**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| id | 商品セットカスタム項目ID | 整数 | 11 |  |
| no | 商品セットカスタム項目No. | 整数 | 11 |  |
| name | 商品セットカスタム項目名 | 文字列 | 255 |  |
| is_active | 状態 | 整数 | 1 | 0=無効,1=有効 |
| show_flag | サイトへの表示設定 | 整数 | 1 | 0=非表示,1=表示,2=会員のみ表示 |
| mail_flag | メールへの表示設定 | 整数 | 1 | 0=非表示,1=表示,2=会員のみ表示 |
| pdf_flag | 帳票への表示設定 | 整数 | 1 | 0=非表示,1=表示 |
| is_html | HTML利用 | 整数 | 1 | 0=利用しない,1=利用する |
| sort_priority | 表示優先度 | 整数 | 4 | \-127\~127 |
| created_at | 作成日 | 日付 | 19 | Y-m-d H:i:s |
| updated_at | 更新日 | 日付 | 19 | Y-m-d H:i:s |

**レスポンス例（200 OK）:**

```json
{
  "product_set_custom": {
    "id": 17,
    "no": 1,
    "name": "倉庫番号",
    "is_active": 1,
    "show_flag": 1,
    "mail_flag": 1,
    "pdf_flag": 1,
    "is_html": 1,
    "sort_priority": 0,
    "created_at": "2021-04-08 11:03:38",
    "updated_at": "2021-06-11 14:43:45"
  }
}
```

## GET {{api_url}}/api/v1/product_set_customs

**URIパラメータ**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| limit | limit | 整数 |  | 指定した件数分のデータを取得します。指定なしの場合は20件、最大100件 |
| offset | offset | 整数 |  | 指定した値+1件目のデータからlimit分を取得します。指定しない場合は0 |
| ids | ID複数 | 整数 |  | 複数の商品セットカスタム項目IDをカンマ区切りで指定 |
| fields | フィールド | 文字列 |  | 取得したいフィールドカンマ区切りで指定 |
| name | 商品セットカスタム項目名 | 文字列 | 255 |  |

## 拡張パラメータによる高度な絞り込み

拡張パラメータを使用することで、より高度な絞り込みが可能です。

詳しくは、[パラメータ](../docs/04-parameters.md)の「拡張パラメータ」欄をご参照ください。

**レスポンス例（200 OK）:**

```json
{
  "product_set_customs": [
    {
      "id": 17,
      "no": 1,
      "name": "倉庫番号",
      "is_active": 1,
      "show_flag": 1,
      "mail_flag": 1,
      "pdf_flag": 1,
      "is_html": 1,
      "sort_priority": 0,
      "created_at": "2021-04-08 11:03:38",
      "updated_at": "2021-06-11 14:43:45"
    },
    {
      "id": 18,
      "no": 2,
      "name": "棚番号",
      "is_active": 1,
      "show_flag": 2,
      "mail_flag": 0,
      "pdf_flag": 1,
      "is_html": 1,
      "sort_priority": 0,
      "created_at": "2021-04-08 11:03:38",
      "updated_at": "2021-06-11 14:43:45"
    },
    {
      "id": 19,
      "no": 3,
      "name": "発売日",
      "is_active": 1,
      "show_flag": 0,
      "mail_flag": 0,
      "pdf_flag": 1,
      "is_html": 1,
      "sort_priority": 0,
      "created_at": "2021-04-08 11:03:38",
      "updated_at": "2021-06-11 14:43:45"
    },
    {
      "id": 21,
      "no": 4,
      "name": "セットカスタム4",
      "is_active": 1,
      "show_flag": 1,
      "mail_flag": 1,
      "pdf_flag": 0,
      "is_html": 0,
      "sort_priority": 0,
      "created_at": "2021-04-08 13:20:51",
      "updated_at": "2021-06-11 14:43:45"
    }
  ],
  "meta": {
    "limit": 20,
    "offset": 0,
    "total": 4
  }
}
```

## PATCH {{api_url}}/api/v1/product_set_customs/21

**リクエストBODY**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| no | 商品セットカスタム項目No. | 整数 | 11 |  |
| name | 商品セットカスタム項目名 | 文字列 | 255 |  |
| is_active | 状態 | 整数 | 1 | 0=無効,1=有効 |
| show_flag | サイトへの表示設定 | 整数 | 1 | 0=非表示,1=表示,2=会員のみ表示 |
| mail_flag | メールへの表示設定 | 整数 | 1 | 0=非表示,1=表示,2=会員のみ表示 |
| pdf_flag | 帳票への表示設定 | 整数 | 1 | 0=非表示,1=表示 |
| is_html | HTML利用 | 整数 | 1 | 0=利用しない,1=利用する |
| sort_priority | 表示優先度 | 整数 | 4 | \-127\~127 |

**リクエストボディ例:**

```json
{
  "no": 4,
  "name": "セットカスタム4",
  "is_active": 0,
  "show_flag": 0,
  "mail_flag": 0,
  "pdf_flag": 1,
  "is_html": 1,
  "sort_priority": 5
}
```

**レスポンス例（200 OK）:**

```json
{
  "product_set_custom": {
    "id": 21,
    "no": 4,
    "name": "セットカスタム4",
    "is_active": 0,
    "show_flag": 0,
    "mail_flag": 0,
    "pdf_flag": 1,
    "is_html": 1,
    "sort_priority": 5,
    "created_at": "2021-04-08 13:20:51",
    "updated_at": "2023-12-12 18:52:37"
  }
}
```

## PATCH {{api_url}}/api/v1/product_set_customs/

**リクエストBODY**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| product_set_customs\[{{i}}\]\[id\] | 商品セットカスタム項目ID | 整数 | 11 | 必須 |
| product_set_customs\[{{i}}\]\[no\] | 商品セットカスタム項目No. | 整数 | 11 |  |
| product_set_customs\[{{i}}\]\[name\] | 商品セットカスタム項目名 | 文字列 | 255 |  |
| product_set_customs\[{{i}}\]\[is_active\] | 状態 | 整数 | 1 | 0=無効,1=有効 |
| product_set_customs\[{{i}}\]\[show_flag\] | サイトへの表示設定 | 整数 | 1 | 0=非表示,1=表示,2=会員のみ表示 |
| product_set_customs\[{{i}}\]\[mail_flag\] | メールへの表示設定 | 整数 | 1 | 0=非表示,1=表示,2=会員のみ表示 |
| product_set_customs\[{{i}}\]\[pdf_flag\] | 帳票への表示設定 | 整数 | 1 | 0=非表示,1=表示 |
| product_set_customs\[{{i}}\]\[is_html\] | HTML利用 | 整数 | 1 | 0=利用しない,1=利用する |
| product_set_customs\[{{i}}\]\[sort_priority\] | 表示優先度 | 整数 | 4 | \-127\~127 |

**リクエストボディ例:**

```json
{
  "product_set_customs": [
    {
      "id": 19,
      "name": "発売日",
      "is_active": 1,
      "show_flag": 0,
      "mail_flag": 0,
      "pdf_flag": 1,
      "is_html": 1,
      "sort_priority": 0
    },
    {
      "id": 21,
      "no": 4
    }
  ]
}
```

**レスポンス例（200 OK）:**

```json
{
  "product_set_customs": [
    {
      "id": 19,
      "no": 3,
      "name": "発売日",
      "is_active": 1,
      "show_flag": 0,
      "mail_flag": 0,
      "pdf_flag": 1,
      "is_html": 1,
      "sort_priority": 0,
      "created_at": "2021-04-08 11:03:38",
      "updated_at": "2023-12-12 18:53:34"
    },
    {
      "id": 21,
      "no": 4,
      "name": "セットカスタム4",
      "is_active": 0,
      "show_flag": 0,
      "mail_flag": 0,
      "pdf_flag": 1,
      "is_html": 1,
      "sort_priority": 5,
      "created_at": "2021-04-08 13:20:51",
      "updated_at": "2023-12-12 18:53:34"
    }
  ]
}
```

## POST {{api_url}}/api/v1/product_set_customs/

**リクエストBODY**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| product_set_customs\[{{i}}\]\[no\] | 商品セットカスタム項目No. | 整数 | 11 | 必須 |
| product_set_customs\[{{i}}\]\[name\] | 商品セットカスタム項目名 | 文字列 | 255 | 必須 |
| product_set_customs\[{{i}}\]\[is_active\] | 状態 | 整数 | 1 | 0=無効,1=有効  <br>初期値: 0 |
| product_set_customs\[{{i}}\]\[show_flag\] | サイトへの表示設定 | 整数 | 1 | 0=非表示,1=表示,2=会員のみ表示  <br>初期値: 0 |
| product_set_customs\[{{i}}\]\[mail_flag\] | メールへの表示設定 | 整数 | 1 | 0=非表示,1=表示,2=会員のみ表示  <br>初期値: 0 |
| product_set_customs\[{{i}}\]\[pdf_flag\] | 帳票への表示設定 | 整数 | 1 | 0=非表示,1=表示  <br>初期値: 0 |
| product_set_customs\[{{i}}\]\[is_html\] | HTML利用 | 整数 | 1 | 0=利用しない,1=利用する  <br>初期値: 0 |
| product_set_customs\[{{i}}\]\[sort_priority\] | 表示優先度 | 整数 | 4 | \-127\~127  <br>初期値: 0 |

**リクエストボディ例:**

```json
{
  "product_set_customs": [
    {
      "no": 5,
      "name": "セットカスタム5",
      "is_active": 1,
      "show_flag": 1,
      "mail_flag": 1,
      "pdf_flag": 1,
      "is_html": 1,
      "sort_priority": 0
    },
    {
      "no": 6,
      "name": "セットカスタム6"
    }
  ]
}
```

**レスポンス例（201 Created）:**

```json
{
  "product_set_customs": [
    {
      "id": 28,
      "no": 5,
      "name": "セットカスタム5",
      "is_active": 1,
      "show_flag": 1,
      "mail_flag": 1,
      "pdf_flag": 1,
      "is_html": 1,
      "sort_priority": 0,
      "created_at": "2023-12-12 18:55:43",
      "updated_at": "2023-12-12 18:55:43"
    },
    {
      "id": 29,
      "no": 6,
      "name": "セットカスタム6",
      "is_active": 0,
      "show_flag": 0,
      "mail_flag": 0,
      "pdf_flag": 0,
      "is_html": 0,
      "sort_priority": 0,
      "created_at": "2023-12-12 18:55:43",
      "updated_at": "2023-12-12 18:55:43"
    }
  ]
}
```
