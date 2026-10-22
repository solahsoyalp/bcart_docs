# 商品オプション

商品注文時に任意に設定できるフォームの項目

## GET {{api_url}}/api/v1/product_set_options/1

**レスポンス一覧**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| id | 商品オプションID | 整数 | 11 |  |
| name | 商品オプション名 | 文字列 | 255 |  |
| is_active | 状態 | 整数 | 1 | 0=無効,1=有効 |
| input_type | フォームタイプ | 文字列 | 7 | text/texarea/select/check/radio |
| input_choices | 選択肢の値と表示名、金額 | 配列 |  | view_name=表示名  <br>value=値  <br>price=金額（設定されていない場合は非表示） |
| input_rules | 文字種、文字数の制限 | オブジェクト |  | type=文字種の制限（全文字種/半角英字/半角英数字/整数/数値）  <br>limit_type=値の制限（size=数値で指定,digit=桁数で指定）※typeが整数か数値の場合のみ  <br>limit_min=最小  <br>limit_max=最大 |
| unit | 単位 | 文字列 | 255 |  |
| is_description_html | HTML利用 | 整数 | 1 | 0=利用しない,1=利用する |
| description | 説明 | 文字列 | 65,535 |  |
| required | 入力確認 | 論理 | 5 | true=必須,false=任意 |
| sort_priority | 表示優先度 | 整数 | 4 | \-127\~127 |
| created_at | 作成日 | 日付 | 19 | Y-m-d H:i:s |
| updated_at | 更新日 | 日付 | 19 | Y-m-d H:i:s |

**レスポンス例（200 OK）:**

```json
{
  "product_set_option": {
    "id": 1,
    "name": "名入れ",
    "is_active": 1,
    "input_type": "text",
    "input_choices": null,
    "input_rules": {
      "type": "全文字種",
      "limit_min": "1",
      "limit_max": "10"
    },
    "unit": null,
    "is_description_html": 0,
    "description": "名入れ用の文字を入力してください。\r\n最大10文字までです。",
    "required": false,
    "sort_priority": 0,
    "created_at": "2020-05-27 11:18:23",
    "updated_at": "2021-03-05 16:24:10"
  }
}
```

## GET {{api_url}}/api/v1/product_set_options/

**URIパラメータ**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| limit | limit | 整数 |  | 指定した件数分のデータを取得します。指定なしの場合は20件、最大100件 |
| offset | offset | 整数 |  | 指定した値+1件目のデータからlimit分を取得します。指定しない場合は0 |
| ids | ID複数 | 整数 |  | 複数の商品セットIDをカンマ区切りで指定 |
| fields | フィールド | 文字列 |  | 取得したいフィールドカンマ区切りで指定 |
| name | 商品オプション名 | 文字列 | 255 |  |

## 拡張パラメータによる高度な絞り込み

拡張パラメータを使用することで、より高度な絞り込みが可能です。

詳しくは、[パラメータ](../docs/04-parameters.md)の「拡張パラメータ」欄をご参照ください。

**レスポンス例（200 OK）:**

```json
{
  "product_set_options": [
    {
      "id": 1,
      "name": "名入れ",
      "is_active": 1,
      "input_type": "text",
      "input_choices": null,
      "input_rules": {
        "type": "全文字種",
        "limit_min": "1",
        "limit_max": "10"
      },
      "unit": null,
      "is_description_html": 0,
      "description": "名入れ用の文字を入力してください。\r\n最大10文字までです。",
      "required": false,
      "sort_priority": 0,
      "created_at": "2020-05-27 11:18:23",
      "updated_at": "2021-03-05 16:24:10"
    },
    {
      "id": 2,
      "name": "名入れ（テキストエリア）",
      "is_active": 1,
      "input_type": "textarea",
      "input_choices": null,
      "input_rules": {
        "type": "全文字種",
        "limit_min": "1",
        "limit_max": "50"
      },
      "unit": null,
      "is_description_html": 0,
      "description": "名入れ用の文字を入力してください。\r\n最大50文字までです。",
      "required": false,
      "sort_priority": 0,
      "created_at": "2020-05-27 11:19:23",
      "updated_at": "2021-03-05 16:24:10"
    },
    {
      "id": 3,
      "name": "カラーバリエーション",
      "is_active": 1,
      "input_type": "select",
      "input_choices": [
        {
          "view_name": "red",
          "value": 1,
          "price": null
        },
        {
          "view_name": "blue",
          "value": 2,
          "price": null
        },
        {
          "view_name": "green",
          "value": 3,
          "price": null
        }
      ],
      "input_rules": null,
      "unit": "個",
      "is_description_html": 0,
      "description": "一つ選んでください",
      "required": false,
      "sort_priority": 1,
      "created_at": "2020-05-27 11:20:34",
      "updated_at": "2021-03-05 16:24:10"
    },
    {
      "id": 4,
      "name": "無料サンプル",
      "is_active": 1,
      "input_type": "check",
      "input_choices": [
        {
          "view_name": "無料サンプル有り",
          "value": "有り",
          "price": null
        },
        {
          "view_name": "無料サンプル無し",
          "value": "無し",
          "price": null
        }
      ],
      "input_rules": null,
      "unit": "個",
      "is_description_html": 0,
      "description": "無料サンプルをつけることができます。",
      "required": false,
      "sort_priority": -1,
      "created_at": "2020-05-27 11:22:29",
      "updated_at": "2021-03-05 16:24:10"
    },
    {
      "id": 5,
      "name": "無料お試し選択",
      "is_active": 1,
      "input_type": "radio",
      "input_choices": [
        {
          "view_name": "保湿クリーム",
          "value": 1,
          "price": null
        },
        {
          "view_name": "美容クリーム",
          "value": 2,
          "price": null
        }
      ],
      "input_rules": null,
      "unit": "つ",
      "is_description_html": 0,
      "description": null,
      "required": true,
      "sort_priority": 0,
      "created_at": "2020-05-27 11:23:51",
      "updated_at": "2021-03-05 16:24:10"
    }
  ],
  "meta": {
    "limit": 20,
    "offset": 0,
    "total": 5
  }
}
```

## PATCH {{api_url}}/api/v1/product_set_options/1

**リクエストBODY**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| name | 商品オプション名 | 文字列 | 255 |  |
| is_active | 状態 | 整数 | 1 | 0=無効,1=有効 |
| input_type | フォームタイプ | 文字列 | 7 | text/texarea/select/check/radio |
| input_choices | 選択肢の値と表示名、金額 | 配列 |  | input_typeがselect/check/radioの場合、必須 |
| input_choices\[{{i}}\]\[view_name\] | 選択肢の表示名 | 文字列 | 32 |  |
| input_choices\[{{i}}\]\[value\] | 選択肢の値 | 文字列 | 32 |  |
| input_choices\[{{i}}\]\[price\] | 選択肢の価格 | 整数 | 11 |  |
| input_rules | 文字種、文字数の制限 | オブジェクト |  | input_typeがtext/textareaの場合、必須 |
| input_rules\[type\] | 文字種の制限の種類 | 文字列 |  | 全文字種/半角英字/半角英数字/整数/数値 |
| input_rules\[limit_type\] | 値の制限の種類 | 文字列 |  | size/digit  <br>（size=数値で指定、digit=桁数で指定）  <br>※typeが整数か数値の場合のみ指定可 |
| input_rules\[limit_min\] | 値の制限の最小値 | 数値 | 11 |  |
| input_rules\[limit_max\] | 値の制限の最大値 | 数値 | 11 |  |
| unit | 単位 | 文字列 | 255 |  |
| is_description_html | HTML利用 | 整数 | 1 | 0=利用しない,1=利用する |
| description | 説明 | 文字列 | 65,535 |  |
| required | 入力確認 | 論理 | 5 | true=必須,false=任意 |
| sort_priority | 表示優先度 | 整数 | 4 | \-127\~127 |

**リクエストボディ例:**

```json
{
  "id": 1,
  "name": "名入れ",
  "is_active": 1,
  "input_type": "textarea",
  "input_rules": {
    "type": "数値",
    "limit_type": "size",
    "limit_min": "1",
    "limit_max": "10"
  },
  "unit": "個",
  "is_description_html": 0,
  "description": "名入れ用の文字を入力してください。\r\n最大10文字までです。",
  "required": false,
  "sort_priority": 0
}
```

**レスポンス例（200 OK）:**

```json
{
  "product_set_option": {
    "id": 1,
    "name": "名入れ",
    "is_active": 1,
    "input_type": "textarea",
    "input_choices": null,
    "input_rules": {
      "type": "数値",
      "limit_type": "size",
      "limit_min": "1",
      "limit_max": "10"
    },
    "unit": "個",
    "is_description_html": 0,
    "description": "名入れ用の文字を入力してください。\r\n最大10文字までです。",
    "required": false,
    "sort_priority": 0,
    "created_at": "2020-05-27 11:18:23",
    "updated_at": "2023-12-12 18:59:36"
  }
}
```

## PATCH {{api_url}}/api/v1/product_set_options/

**リクエストBODY**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| product_set_options\[{{i}}\]\[id\] | 商品オプションID | 整数 | 11 | 必須 |
| product_set_options\[{{i}}\]\[name\] | 商品オプション名 | 文字列 | 255 | 項目存在時必須 |
| product_set_options\[{{i}}\]\[is_active\] | 状態 | 整数 | 1 | 0=無効,1=有効 |
| product_set_options\[{{i}}\]\[input_type\] | フォームタイプ | 文字列 | 7 | text/texarea/select/check/radio |
| product_set_options\[{{i}}\]\[input_choices\] | 選択肢の値と表示名、金額 | 配列 |  | input_typeがselect/check/radioの場合、必須 |
| product_set_options\[{{i}}\]\[input_choices\]\[{{j}}\]\[view_name\] | 選択肢の表示名 | 文字列 | 32 |  |
| product_set_options\[{{i}}\]\[input_choices\]\[{{j}}\]\[value\] | 選択肢の値 | 文字列 | 32 |  |
| product_set_options\[{{i}}\]\[input_choices\]\[{{j}}\]\[price\] | 選択肢の価格 | 整数 | 11 |  |
| product_set_options\[{{i}}\]\[input_rules\] | 文字種、文字数の制限 | オブジェクト |  | input_typeがtext/textareaの場合、必須 |
| product_set_options\[{{i}}\]\[input_rules\]\[type\] | 文字種の制限の種類 | 文字列 |  | 全文字種/半角英字/半角英数字/整数/数値 |
| product_set_options\[{{i}}\]\[input_rules\]\[limit_type\] | 値の制限の種類 | 文字列 |  | size/digit  <br>（size=数値で指定、digit=桁数で指定）  <br>※typeが整数か数値の場合のみ指定可 |
| product_set_options\[{{i}}\]\[input_rules\]\[limit_min\] | 値の制限の最小値 | 数値 | 11 |  |
| product_set_options\[{{i}}\]\[input_rules\]\[limit_max\] | 値の制限の最大値 | 数値 | 11 |  |
| product_set_options\[{{i}}\]\[unit\] | 単位 | 文字列 | 255 |  |
| product_set_options\[{{i}}\]\[is_description_html\] | HTML利用 | 整数 | 1 | 0=利用しない,1=利用する |
| product_set_options\[{{i}}\]\[description\] | 説明 | 文字列 | 65,535 |  |
| product_set_options\[{{i}}\]\[required\] | 入力確認 | 論理 | 5 | true=必須,false=任意 |
| product_set_options\[{{i}}\]\[sort_priority\] | 表示優先度 | 整数 | 4 | \-127\~127 |

**リクエストボディ例:**

```json
{
  "product_set_options": [
    {
      "id": 1,
      "name": "無料サンプルs",
      "is_active": 1,
      "input_type": "check",
      "input_choices": [
        {
          "view_name": "無料サンプル有り",
          "value": "有り",
          "price": null
        },
        {
          "view_name": "無料サンプル無し",
          "value": "無し",
          "price": null
        }
      ],
      "unit": "個",
      "is_description_html": 0,
      "description": "無料サンプルをつけることができます。",
      "required": false,
      "sort_priority": -1
    },
    {
      "id": 5,
      "name": "無料お試し選択",
      "is_active": 1,
      "input_type": "radio",
      "input_choices": [
        {
          "view_name": "保湿クリーム",
          "value": 1,
          "price": null
        },
        {
          "view_name": "美容クリーム",
          "value": 2,
          "price": null
        }
      ],
      "unit": "つ",
      "is_description_html": 0,
      "description": null,
      "required": true,
      "sort_priority": 0
    }
  ]
}
```

**レスポンス例（200 OK）:**

```json
{
  "product_set_options": [
    {
      "id": 1,
      "name": "無料サンプルs",
      "is_active": 1,
      "input_type": "check",
      "input_choices": [
        {
          "view_name": "無料サンプル有り",
          "value": "有り",
          "price": null
        },
        {
          "view_name": "無料サンプル無し",
          "value": "無し",
          "price": null
        }
      ],
      "input_rules": null,
      "unit": "個",
      "is_description_html": 0,
      "description": "無料サンプルをつけることができます。",
      "required": false,
      "sort_priority": -1,
      "created_at": "2020-05-27 11:18:23",
      "updated_at": "2023-12-12 19:00:48"
    },
    {
      "id": 5,
      "name": "無料お試し選択",
      "is_active": 1,
      "input_type": "radio",
      "input_choices": [
        {
          "view_name": "保湿クリーム",
          "value": 1,
          "price": null
        },
        {
          "view_name": "美容クリーム",
          "value": 2,
          "price": null
        }
      ],
      "input_rules": null,
      "unit": "つ",
      "is_description_html": 0,
      "description": null,
      "required": true,
      "sort_priority": 0,
      "created_at": "2020-05-27 11:23:51",
      "updated_at": "2023-12-12 19:00:48"
    }
  ]
}
```

## POST {{api_url}}/api/v1/product_set_options/

**リクエストBODY**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| product_set_options\[{{i}}\]\[name\] | 商品オプション名 | 文字列 | 255 | 必須 |
| product_set_options\[{{i}}\]\[is_active\] | 状態 | 整数 | 1 | 0=無効,1=有効  <br>初期値: 0 |
| product_set_options\[{{i}}\]\[input_type\] | フォームタイプ | 文字列 | 7 | text/texarea/select/check/radio  <br>初期値: "text" |
| product_set_options\[{{i}}\]\[input_choices\] | 選択肢の値と表示名、金額 | 配列 |  | input_typeがselect/check/radioの場合、必須  <br>初期値: null |
| product_set_options\[{{i}}\]\[input_choices\]\[{{j}}\]\[view_name\] | 選択肢の表示名 | 文字列 | 32 |  |
| product_set_options\[{{i}}\]\[input_choices\]\[{{j}}\]\[value\] | 選択肢の値 | 文字列 | 32 |  |
| product_set_options\[{{i}}\]\[input_choices\]\[{{j}}\]\[price\] | 選択肢の価格 | 整数 | 11 |  |
| product_set_options\[{{i}}\]\[input_rules\] | 文字種、文字数の制限 | オブジェクト |  | input_typeがtext/textareaの場合、必須 |
| product_set_options\[{{i}}\]\[input_rules\]\[type\] | 文字種の制限の種類 | 文字列 |  | 全文字種/半角英字/半角英数字/整数/数値  <br>初期値: "全文字種" |
| product_set_options\[{{i}}\]\[input_rules\]\[limit_type\] | 値の制限の種類 | 文字列 |  | size=数値で指定,digit=桁数で指定  <br>※typeが整数か数値の場合のみ指定可  <br>初期値: "size" |
| product_set_options\[{{i}}\]\[input_rules\]\[limit_min\] | 値の制限の最小値 | 数値 | 11 | 初期値: null |
| product_set_options\[{{i}}\]\[input_rules\]\[limit_max\] | 値の制限の最大値 | 数値 | 11 | 初期値: null |
| product_set_options\[{{i}}\]\[unit\] | 単位 | 文字列 | 255 | 初期値: null |
| product_set_options\[{{i}}\]\[is_description_html\] | HTML利用 | 整数 | 1 | 0=利用しない,1=利用する  <br>初期値: 0 |
| product_set_options\[{{i}}\]\[description\] | 説明 | 文字列 | 65,535 | 初期値: null |
| product_set_options\[{{i}}\]\[required\] | 入力確認 | 論理 | 5 | true=必須,false=任意  <br>初期値: false |
| product_set_options\[{{i}}\]\[sort_priority\] | 表示優先度 | 整数 | 4 | \-127\~127  <br>初期値: 0 |

**リクエストボディ例:**

```json
{
  "product_set_options": [
    {
      "name": "商品セットオプション6",
      "is_active": 1,
      "input_type": "text",
      "input_rules": {
        "type": "全文字種",
        "limit_min": "1",
        "limit_max": "10"
      },
      "is_description_html": 0,
      "description": "名入れ用の文字を入力してください。\r\n最大10文字までです。",
      "required": false,
      "sort_priority": 0
    },
    {
      "name": "商品セットオプション7",
      "is_active": 1,
      "input_type": "select",
      "input_choices": [
        {
          "view_name": "保湿クリーム",
          "value": 1,
          "price": null
        },
        {
          "view_name": "美容クリーム",
          "value": 2,
          "price": 90
        },
        {
          "view_name": "クリーム",
          "value": 3
        }
      ],
      "input_rules": null,
      "unit": "つ",
      "is_description_html": 0,
      "required": true,
      "sort_priority": 0
    },
    {
      "name": "商品セットオプション8"
    }
  ]
}
```

**レスポンス例（201 Created）:**

```json
{
  "product_set_options": [
    {
      "id": 30,
      "name": "商品セットオプション6",
      "is_active": 1,
      "input_type": "text",
      "input_choices": null,
      "input_rules": {
        "type": "全文字種",
        "limit_min": "1",
        "limit_max": "10"
      },
      "unit": null,
      "is_description_html": 0,
      "description": "名入れ用の文字を入力してください。\r\n最大10文字までです。",
      "required": false,
      "sort_priority": 0,
      "created_at": "2023-12-12 19:02:01",
      "updated_at": "2023-12-12 19:02:01"
    },
    {
      "id": 31,
      "name": "商品セットオプション7",
      "is_active": 1,
      "input_type": "select",
      "input_choices": [
        {
          "view_name": "保湿クリーム",
          "value": 1,
          "price": null
        },
        {
          "view_name": "美容クリーム",
          "value": 2,
          "price": 90
        },
        {
          "view_name": "クリーム",
          "value": 3,
          "price": null
        }
      ],
      "input_rules": null,
      "unit": "つ",
      "is_description_html": 0,
      "description": null,
      "required": true,
      "sort_priority": 0,
      "created_at": "2023-12-12 19:02:01",
      "updated_at": "2023-12-12 19:02:01"
    },
    {
      "id": 32,
      "name": "商品セットオプション8",
      "is_active": 0,
      "input_type": "text",
      "input_choices": null,
      "input_rules": {
        "type": "全文字種",
        "limit_min": null,
        "limit_max": null
      },
      "unit": null,
      "is_description_html": 0,
      "description": null,
      "required": false,
      "sort_priority": 0,
      "created_at": "2023-12-12 19:02:01",
      "updated_at": "2023-12-12 19:02:01"
    }
  ]
}
```
