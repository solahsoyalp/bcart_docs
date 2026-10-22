# 商品基本カスタム項目

商品の基本情報で任意に設定できる項目

## GET {{api_url}}/api/v1/product_customs/14

**レスポンス一覧**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| id | 商品カスタム項目ID | 整数 | 11 |  |
| name | 商品カスタム項目名 | 文字列 | 255 |  |
| is_active | 状態 | 整数 | 1 | 0=無効,1=有効 |
| show_flag | サイトへの表示設定 | 整数 | 1 | 0=非表示,1=表示,2=会員のみ表示 |
| mail_flag | メールへの表示設定 | 整数 | 1 | 0=非表示,1=表示,2=会員のみ表示 |
| is_html | HTML利用 | 整数 | 1 | 0=利用しない,1=利用する |
| sort_priority | 表示優先度 | 整数 | 4 | \-127\~127 |
| created_at | 作成日 | 日付 | 19 | Y-m-d H:i:s |
| updated_at | 更新日 | 日付 | 19 | Y-m-d H:i:s |

**レスポンス例（200 OK）:**

```json
{
  "product_custom": {
    "id": 14,
    "no": 1,
    "name": "生産者",
    "is_active": 1,
    "show_flag": 1,
    "mail_flag": 1,
    "is_html": 1,
    "sort_priority": 0,
    "created_at": "2021-04-08 11:03:38",
    "updated_at": "2021-06-11 14:43:45"
  }
}
```

## GET {{api_url}}/api/v1/product_customs

**URIパラメータ**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| limit | limit | 整数 |  | 指定した件数分のデータを取得します。指定なしの場合は20件、最大100件 |
| offset | offset | 整数 |  | 指定した値+1件目のデータからlimit分を取得します。指定しない場合は0 |
| ids | ID複数 | 整数 |  | 複数の商品カスタム項目IDをカンマ区切りで指定 |
| fields | フィールド | 文字列 |  | 取得したいフィールドカンマ区切りで指定 |
| name | 商品カスタム項目名 | 文字列 | 255 |  |

## 拡張パラメータによる高度な絞り込み

拡張パラメータを使用することで、より高度な絞り込みが可能です。

詳しくは、[パラメータ](../docs/04-parameters.md)の「拡張パラメータ」欄をご参照ください。

**レスポンス例（200 OK）:**

```json
{
  "product_customs": [
    {
      "id": 14,
      "no": 1,
      "name": "生産者",
      "is_active": 1,
      "show_flag": 1,
      "mail_flag": 1,
      "is_html": 1,
      "sort_priority": 0,
      "created_at": "2021-04-08 11:03:38",
      "updated_at": "2021-06-11 14:43:45"
    },
    {
      "id": 15,
      "no": 2,
      "name": "ブランド",
      "is_active": 1,
      "show_flag": 2,
      "mail_flag": 1,
      "is_html": 1,
      "sort_priority": 0,
      "created_at": "2021-04-08 11:03:38",
      "updated_at": "2021-06-11 14:43:45"
    },
    {
      "id": 16,
      "no": 3,
      "name": "カタログ頁",
      "is_active": 1,
      "show_flag": 0,
      "mail_flag": 0,
      "is_html": 1,
      "sort_priority": 0,
      "created_at": "2021-04-08 11:03:38",
      "updated_at": "2021-06-11 14:43:45"
    },
    {
      "id": 20,
      "no": 4,
      "name": "基本カスタム4",
      "is_active": 1,
      "show_flag": 1,
      "mail_flag": 1,
      "is_html": 0,
      "sort_priority": 0,
      "created_at": "2021-04-08 13:20:15",
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

## PATCH {{api_url}}/api/v1/product_customs/20

**リクエストBODY**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| no | 商品カスタム項目No. | 整数 | 11 |  |
| name | 商品カスタム項目名 | 文字列 | 255 |  |
| is_active | 状態 | 整数 | 1 | 0=無効,1=有効 |
| show_flag | サイトへの表示設定 | 整数 | 1 | 0=非表示,1=表示,2=会員のみ表示 |
| mail_flag | メールへの表示設定 | 整数 | 1 | 0=非表示,1=表示,2=会員のみ表示 |
| is_html | HTML利用 | 整数 | 1 | 0=利用しない,1=利用する |
| sort_priority | 表示優先度 | 整数 | 4 | \-127\~127 |

**リクエストボディ例:**

```json
{
  "no": 7,
  "name": "基本カスタム4_変更後",
  "is_active": 1,
  "show_flag": 2,
  "mail_flag": 1,
  "is_html": 0,
  "sort_priority": 8
}
```

**レスポンス例（200 OK）:**

```json
{
  "product_custom": {
    "id": 20,
    "no": 7,
    "name": "基本カスタム4_変更後",
    "is_active": 1,
    "show_flag": 2,
    "mail_flag": 1,
    "is_html": 0,
    "sort_priority": 8,
    "created_at": "2021-04-08 13:20:15",
    "updated_at": "2023-12-12 18:42:41"
  }
}
```

## PATCH {{api_url}}/api/v1/product_customs/

**リクエストBODY**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| product_customs\[{{i}}\]\[id\] | 商品カスタム項目ID | 整数 | 11 | 必須 |
| product_customs\[{{i}}\]\[no\] | 商品カスタム項目No. | 整数 | 11 |  |
| product_customs\[{{i}}\]\[name\] | 商品カスタム項目名 | 文字列 | 255 |  |
| product_customs\[{{i}}\]\[is_active\] | 状態 | 整数 | 1 | 0=無効,1=有効 |
| product_customs\[{{i}}\]\[show_flag\] | サイトへの表示設定 | 整数 | 1 | 0=非表示,1=表示,2=会員のみ表示 |
| product_customs\[{{i}}\]\[mail_flag\] | メールへの表示設定 | 整数 | 1 | 0=非表示,1=表示,2=会員のみ表示 |
| product_customs\[{{i}}\]\[is_html\] | HTML利用 | 整数 | 1 | 0=利用しない,1=利用する |
| product_customs\[{{i}}\]\[sort_priority\] | 表示優先度 | 整数 | 4 | \-127\~127 |

**リクエストボディ例:**

```json
{
  "product_customs": [
    {
      "id": 14,
      "no": 1,
      "name": "基本カスタム1_変更後",
      "is_active": 0,
      "show_flag": 0,
      "mail_flag": 0,
      "is_html": 1,
      "sort_priority": -10
    },
    {
      "id": 15,
      "no": 2,
      "name": "基本カスタム2_変更後",
      "is_active": 1,
      "show_flag": 1,
      "mail_flag": 1,
      "is_html": 0,
      "sort_priority": 10
    }
  ]
}
```

**レスポンス例（200 OK）:**

```json
{
  "product_customs": [
    {
      "id": 14,
      "no": 1,
      "name": "基本カスタム1_変更後",
      "is_active": 0,
      "show_flag": 0,
      "mail_flag": 0,
      "is_html": 1,
      "sort_priority": -10,
      "created_at": "2021-04-08 11:03:38",
      "updated_at": "2023-12-12 18:46:39"
    },
    {
      "id": 15,
      "no": 2,
      "name": "基本カスタム2_変更後",
      "is_active": 1,
      "show_flag": 1,
      "mail_flag": 1,
      "is_html": 0,
      "sort_priority": 10,
      "created_at": "2021-04-08 11:03:38",
      "updated_at": "2023-12-12 18:46:39"
    }
  ]
}
```

## POST {{api_url}}/api/v1/product_customs/

**リクエストBODY**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| product_customs\[{{i}}\]\[no\] | 商品カスタム項目No. | 整数 | 11 | 必須 |
| product_customs\[{{i}}\]\[name\] | 商品カスタム項目名 | 文字列 | 255 | 必須 |
| product_customs\[{{i}}\]\[is_active\] | 状態 | 整数 | 1 | 0=無効,1=有効  <br>初期値: 0 |
| product_customs\[{{i}}\]\[show_flag\] | サイトへの表示設定 | 整数 | 1 | 0=非表示,1=表示,2=会員のみ表示  <br>初期値: 0 |
| product_customs\[{{i}}\]\[mail_flag\] | メールへの表示設定 | 整数 | 1 | 0=非表示,1=表示,2=会員のみ表示  <br>初期値: 0 |
| product_customs\[{{i}}\]\[is_html\] | HTML利用 | 整数 | 1 | 0=利用しない,1=利用する  <br>初期値: 0 |
| product_customs\[{{i}}\]\[sort_priority\] | 表示優先度 | 整数 | 4 | \-127\~127  <br>初期値: 0 |

**リクエストボディ例:**

```json
{
  "product_customs": [
    {
      "no": 5,
      "name": "基本カスタム5",
      "is_active": 1,
      "show_flag": 1,
      "mail_flag": 1,
      "is_html": 0,
      "sort_priority": 0
    },
    {
      "no": 6,
      "name": "基本カスタム6"
    }
  ]
}
```

**レスポンス例（201 Created）:**

```json
{
  "product_customs": [
    {
      "id": 26,
      "no": 5,
      "name": "基本カスタム5",
      "is_active": 1,
      "show_flag": 1,
      "mail_flag": 1,
      "is_html": 0,
      "sort_priority": 0,
      "created_at": "2023-12-12 18:48:53",
      "updated_at": "2023-12-12 18:48:53"
    },
    {
      "id": 27,
      "no": 6,
      "name": "基本カスタム6",
      "is_active": 0,
      "show_flag": 0,
      "mail_flag": 0,
      "is_html": 0,
      "sort_priority": 0,
      "created_at": "2023-12-12 18:48:53",
      "updated_at": "2023-12-12 18:48:53"
    }
  ]
}
```
