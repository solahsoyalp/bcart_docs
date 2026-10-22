# 受注カスタム項目

受注情報に設定できる任意の項目

## GET {{api_url}}/api/v1/order_customs

**URIパラメータ**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| limit | limit | 整数 |  | 指定した件数分のデータを取得します。指定なしの場合は20件、最大100件 |
| offset | offset | 整数 |  | 指定した値+1件目のデータからlimit分を取得します。指定しない場合は0 |
| ids | ID複数 | 整数 |  | 複数の商品セットIDをカンマ区切りで指定 | 
| fields | フィールド | 文字列 |  | 取得したいフィールドカンマ区切りで指定 | 
| name | 受注カスタム項目名 | 文字列 | 255 |  |

**レスポンス例（200 OK）:**

```json
{
  "order_customs": [
    {
      "id": 6,
      "name": "受注カスタム項目1",
      "is_active": 1,
      "input_type": "text",
      "input_choices": null,
      "sort_priority": 0,
      "created_at": "2020-05-27 11:27:04",
      "updated_at": "2020-05-27 11:27:04"
    },
    {
      "id": 7,
      "name": "受注カスタム項目2",
      "is_active": 1,
      "input_type": "textarea",
      "input_choices": null,
      "sort_priority": 0,
      "created_at": "2020-05-27 11:27:15",
      "updated_at": "2020-05-27 11:27:15"
    },
    {
      "id": 8,
      "name": "受注カスタム項目3",
      "is_active": 1,
      "input_type": "select",
      "input_choices": [
        {
          "view_name": "セレクト1",
          "value": 1
        },
        {
          "view_name": "セレクト2",
          "value": 2
        }
      ],
      "sort_priority": 5,
      "created_at": "2020-05-27 11:27:52",
      "updated_at": "2020-05-27 11:27:52"
    },
    {
      "id": 9,
      "name": "受注カスタム項目4",
      "is_active": 1,
      "input_type": "check",
      "input_choices": [
        {
          "view_name": "チェックボックス1",
          "value": 1
        },
        {
          "view_name": "チェックボックス2",
          "value": 2
        }
      ],
      "sort_priority": -1,
      "created_at": "2020-05-27 11:28:24",
      "updated_at": "2020-05-27 11:28:24"
    },
    {
      "id": 10,
      "name": "受注カスタム項目5",
      "is_active": 1,
      "input_type": "radio",
      "input_choices": [
        {
          "view_name": "ラジオ1",
          "value": "a"
        },
        {
          "view_name": "ラジオ2",
          "value": "b"
        }
      ],
      "sort_priority": 10,
      "created_at": "2020-05-27 11:28:52",
      "updated_at": "2020-05-27 11:28:52"
    }
  ],
  "meta": {
    "limit": 20,
    "offset": 0,
    "total": 5
  }
}
```

## GET {{api_url}}/api/v1/order_customs/6

**レスポンス一覧**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| id | 受注カスタム項目ID | 整数 | 11 |  |
| name | 受注カスタム項目名 | 文字列 | 255 |  |
| is_active | 状態 | 整数 | 1 | 0=無効,1=有効 |
| input_type | フォームタイプ | 文字列 | 7 | text/texarea/select/check/radio |
| input_choices | 選択肢の値と表示名 | 配列 |  | view_name=表示名  <br>value=値 |
| sort_priority | 表示優先度 | 整数 | 4 | \-127\~127 |
| created_at | 作成日 | 日付 | 19 | Y-m-d H:i:s |
| updated_at | 更新日 | 日付 | 19 | Y-m-d H:i:s |

## 拡張パラメータによる高度な絞り込み

拡張パラメータを使用することで、より高度な絞り込みが可能です。

詳しくは、[パラメータ](../docs/04-parameters.md)の「拡張パラメータ」欄をご参照ください。

**レスポンス例（200 OK）:**

```json
{
  "order_custom": {
    "id": 8,
    "name": "受注カスタム項目3",
    "is_active": 1,
    "input_type": "select",
    "input_choices": [
      {
        "view_name": "セレクト1",
        "value": 1
      },
      {
        "view_name": "セレクト2",
        "value": 2
      }
    ],
    "sort_priority": 5,
    "created_at": "2020-05-27 11:27:52",
    "updated_at": "2020-05-27 11:27:52"
  }
}
```

## PATCH {{api_url}}/api/v1/order_customs/6

**リクエストBODY**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| name | 受注カスタム項目名 | 文字列 | 255 | 項目存在時必須 |
| is_active | 状態 | 整数 | 1 | 0=無効,1=有効 |
| input_type | フォームタイプ | 文字列 | 7 | text/texarea/select/check/radio |
| input_choices | 選択肢の値と表示名 | 配列 |  | input_typeがselect/check/radioの場合、必須 |
| input_choices\[{{i}}\]\[view_name\] | 選択肢の表示名 | 文字列 | 32 |  |
| input_choices\[{{i}}\]\[value\] | 選択肢の値 | 文字列 | 32 |  |
| sort_priority | 表示優先度 | 整数 | 4 | \-127\~127 |

**リクエストボディ例:**

```json
{
  "input_type": "radio",
  "input_choices": [
    {
      "view_name": "鉛筆_変更後",
      "value": "a"
    },
    {
      "view_name": "消しゴム_変更後",
      "value": "b"
    },
    {
      "view_name": "定規_変更後",
      "value": "c"
    }
  ]
}
```

**レスポンス例（200 OK）:**

```json
{
  "order_custom": {
    "id": 6,
    "name": "受注カスタム項目1",
    "is_active": 1,
    "input_type": "radio",
    "input_choices": [
      {
        "view_name": "鉛筆_変更後",
        "value": "a"
      },
      {
        "view_name": "消しゴム_変更後",
        "value": "b"
      },
      {
        "view_name": "定規_変更後",
        "value": "c"
      }
    ],
    "sort_priority": 0,
    "created_at": "2020-05-27 11:27:04",
    "updated_at": "2023-12-12 18:30:38"
  }
}
```

## PATCH {{api_url}}/api/v1/order_customs/

**リクエストBODY**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| order_customs\[{{i}}\]\[id\] | 受注カスタム項目ID | 整数 | 11 | 必須 |
| order_customs\[{{i}}\]\[name\] | 受注カスタム項目名 | 文字列 | 255 | 項目存在時必須 |
| order_customs\[{{i}}\]\[is_active\] | 状態 | 整数 | 1 | 0=無効,1=有効 |
| order_customs\[{{i}}\]\[input_type\] | フォームタイプ | 文字列 | 7 | text/texarea/select/check/radio |
| order_customs\[{{i}}\]\[input_choices\] | 選択肢の値と表示名 | 配列 |  | input_typeがselect/check/radioの場合、必須 |
| order_customs\[{{i}}\]\[input_choices\]\[{{j}}\]\[view_name\] | 選択肢の表示名 | 文字列 | 32 |  |
| order_customs\[{{i}}\]\[input_choices\]\[{{j}}\]\[value\] | 選択肢の値 | 文字列 | 32 |  |
| order_customs\[{{i}}\]\[sort_priority\] | 表示優先度 | 整数 | 4 | \-127\~127 |

**リクエストボディ例:**

```json
{
  "order_customs": [
    {
      "id": 6,
      "name": "受注カスタム項目1",
      "is_active": 1,
      "input_type": "text",
      "sort_priority": 0
    },
    {
      "id": 7,
      "name": "受注カスタム項目2",
      "is_active": 1,
      "input_type": "textarea",
      "sort_priority": 0
    }
  ]
}
```

**レスポンス例（200 OK）:**

```json
{
  "order_customs": [
    {
      "id": 6,
      "name": "受注カスタム項目1",
      "is_active": 1,
      "input_type": "text",
      "input_choices": null,
      "sort_priority": 0,
      "created_at": "2020-05-27 11:27:04",
      "updated_at": "2023-12-12 18:34:34"
    },
    {
      "id": 7,
      "name": "受注カスタム項目2",
      "is_active": 1,
      "input_type": "textarea",
      "input_choices": null,
      "sort_priority": 0,
      "created_at": "2020-05-27 11:27:15",
      "updated_at": "2023-12-12 18:34:34"
    }
  ]
}
```

## POST {{api_url}}/api/v1/order_customs/

**リクエストBODY**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| order_customs\[{{i}}\]\[id\] | 受注カスタム項目ID | 整数 | 11 | 必須 |
| order_customs\[{{i}}\]\[name\] | 受注カスタム項目名 | 文字列 | 255 | 項目存在時必須 |
| order_customs\[{{i}}\]\[is_active\] | 状態 | 整数 | 1 | 0=無効,1=有効  <br>初期値: 0 |
| order_customs\[{{i}}\]\[input_type\] | フォームタイプ | 文字列 | 7 | text/texarea/select/check/radio  <br>初期値: "text" |
| order_customs\[{{i}}\]\[input_choices\] | 選択肢の値と表示名 | 配列 |  | input_typeがselect/check/radioの場合、必須  <br>初期値: null |
| order_customs\[{{i}}\]\[input_choices\]\[{{j}}\]\[view_name\] | 選択肢の表示名 | 文字列 | 32 |  |
| order_customs\[{{i}}\]\[input_choices\]\[{{j}}\]\[value\] | 選択肢の値 | 文字列 | 32 |  |
| order_customs\[{{i}}\]\[sort_priority\] | 表示優先度 | 整数 | 4 | \-127\~127  <br>初期値: 0 |

**リクエストボディ例:**

```json
{
  "order_customs": [
    {
      "name": "受注カスタム項目4"
    },
    {
      "name": "受注カスタム項目5",
      "is_active": 1,
      "input_type": "select",
      "input_choices": [
        {
          "view_name": "セレクト1",
          "value": 1
        },
        {
          "view_name": "セレクト2",
          "value": 2
        }
      ],
      "sort_priority": 5
    }
  ]
}
```

**レスポンス例（201 Created）:**

```json
{
  "order_customs": [
    {
      "id": 24,
      "name": "受注カスタム項目4",
      "is_active": 0,
      "input_type": "text",
      "input_choices": null,
      "sort_priority": 0,
      "created_at": "2023-12-12 18:36:25",
      "updated_at": "2023-12-12 18:36:25"
    },
    {
      "id": 25,
      "name": "受注カスタム項目5",
      "is_active": 1,
      "input_type": "select",
      "input_choices": [
        {
          "view_name": "セレクト1",
          "value": 1
        },
        {
          "view_name": "セレクト2",
          "value": 2
        }
      ],
      "sort_priority": 5,
      "created_at": "2023-12-12 18:36:25",
      "updated_at": "2023-12-12 18:36:25"
    }
  ]
}
```
