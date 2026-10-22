# 会員カスタム項目

会員登録フォームで任意に設定できる項目

## GET {{api_url}}/api/v1/customer_customs/11

**レスポンス一覧**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| id | 会員カスタム項目ID | 整数 | 11 |  |
| no | 会員カスタム項目No. | 整数 | 11 |  |
| name | 会員カスタム項目名 | 文字列 | 255 |  |
| is_active | 状態 | 整数 | 1 | 0=無効,1=有効 |
| input_type | フォームタイプ | 文字列 | 7 | text/texarea/select/check/radio |
| input_choices | 選択肢の値と表示名 | 配列 |  | view_name=表示名  <br>value=値 |
| show_flag | 会員への表示・変更 | 整数 | 1 | 0=表示・変更させる,1=表示させる・変更させない,2=表示しない |
| required | 入力確認 | 論理 | 5 | true=必須,false=任意 |
| sort_priority | 表示優先度 | 整数 | 4 | \-127\~127 |
| created_at | 作成日 | 日付 | 19 | Y-m-d H:i:s |
| updated_at | 更新日 | 日付 | 19 | Y-m-d H:i:s |

**レスポンス例（200 OK）:**

```json
{
  "customer_custom": {
    "id": 11,
    "no": 1,
    "name": "銀行名（会員カスタム項目1）",
    "is_active": 1,
    "input_type": "text",
    "input_choices": null,
    "show_flag": 2,
    "required": true,
    "sort_priority": 1,
    "created_at": "2021-03-05 16:24:10",
    "updated_at": "2021-06-11 14:51:35"
  }
}
```

## GET {{api_url}}/api/v1/customer_customs

**URIパラメータ**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| limit | limit | 整数 |  | 指定した件数分のデータを取得します。指定なしの場合は20件、最大100件 |
| offset | offset | 整数 |  | 指定した値+1件目のデータからlimit分を取得します。指定しない場合は0 |
| ids | ID複数 | 整数 |  | 複数の会員カスタム項目IDをカンマ区切りで指定 |
| fields | フィールド | 文字列 |  | 取得したいフィールドカンマ区切りで指定 |
| name | 会員カスタム項目名 | 文字列 | 255 |  |

## 拡張パラメータによる高度な絞り込み

拡張パラメータを使用することで、より高度な絞り込みが可能です。

詳しくは、[パラメータ](../docs/04-parameters.md)の「拡張パラメータ」欄をご参照ください。

**レスポンス例（200 OK）:**

```json
{
  "customer_customs": [
    {
      "id": 11,
      "no": 1,
      "name": "銀行名（会員カスタム項目1）",
      "is_active": 1,
      "input_type": "text",
      "input_choices": null,
      "show_flag": 2,
      "required": true,
      "sort_priority": 1,
      "created_at": "2021-03-05 16:24:10",
      "updated_at": "2021-06-11 14:51:35"
    },
    {
      "id": 12,
      "no": 2,
      "name": "取り扱い商品（会員カスタム項目2）",
      "is_active": 1,
      "input_type": "textarea",
      "input_choices": null,
      "show_flag": 1,
      "required": true,
      "sort_priority": 0,
      "created_at": "2021-03-05 16:24:10",
      "updated_at": "2021-06-11 14:51:35"
    },
    {
      "id": 13,
      "no": 3,
      "name": "実店舗の有無（会員カスタム項目3）",
      "is_active": 1,
      "input_type": "select",
      "input_choices": [
        {
          "view_name": "無し",
          "value": 0
        },
        {
          "view_name": "有",
          "value": 1
        }
      ],
      "show_flag": 1,
      "required": true,
      "sort_priority": 0,
      "created_at": "2021-03-05 16:24:10",
      "updated_at": "2021-06-11 14:44:15"
    },
    {
      "id": 22,
      "no": 4,
      "name": "会員特典",
      "is_active": 1,
      "input_type": "check",
      "input_choices": [
        {
          "view_name": "鉛筆",
          "value": 1
        },
        {
          "view_name": "消しゴム",
          "value": 2
        },
        {
          "view_name": "定規",
          "value": 3
        }
      ],
      "show_flag": 0,
      "required": false,
      "sort_priority": 0,
      "created_at": "2021-06-11 14:39:44",
      "updated_at": "2021-06-11 14:51:35"
    },
    {
      "id": 23,
      "no": 5,
      "name": "会員種別",
      "is_active": 1,
      "input_type": "radio",
      "input_choices": [
        {
          "view_name": "リピーター",
          "value": "ok"
        },
        {
          "view_name": "新規",
          "value": "ng"
        }
      ],
      "show_flag": 0,
      "required": false,
      "sort_priority": 0,
      "created_at": "2021-06-11 14:41:19",
      "updated_at": "2021-06-11 14:51:35"
    }
  ],
  "meta": {
    "limit": 20,
    "offset": 0,
    "total": 5
  }
}
```

## PATCH {{api_url}}/api/v1/customer_customs/22

**リクエストBODY**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| no | 会員カスタム項目No. | 整数 | 11 | 項目存在時必須 |
| name | 会員カスタム項目名 | 文字列 | 255 | 項目存在時必須 |
| is_active | 状態 | 整数 | 1 | 0=無効,1=有効 |
| input_type | フォームタイプ | 文字列 | 7 | text/texarea/select/check/radio |
| input_choices | 選択肢の値と表示名 | 配列 |  | input_typeがselect/check/radioの場合、必須 |
| input_choices\[{{i}}\]\[view_name\] | 選択肢の表示名 | 文字列 | 32 |  |
| input_choices\[{{i}}\]\[value\] | 選択肢の値 | 文字列 | 32 |  |
| show_flag | 会員への表示・変更 | 整数 | 1 | 0=表示・変更させる,1=表示させる・変更させない,2=表示しない |
| required | 入力確認 | 論理 | 5 | true=必須,false=任意 |
| sort_priority | 表示優先度 | 整数 | 4 | \-127\~127 |

**リクエストボディ例:**

```json
{
  "no": 4,
  "name": "会員特典",
  "is_active": 0,
  "input_type": "radio",
  "input_choices": [
    {
      "view_name": "鉛筆",
      "value": "a"
    },
    {
      "view_name": "消しゴム",
      "value": "b"
    },
    {
      "view_name": "定規",
      "value": "c"
    }
  ],
  "show_flag": 1,
  "required": true,
  "sort_priority": 5
}
```

**レスポンス例（200 OK）:**

```json
{
  "customer_custom": {
    "id": 22,
    "no": 4,
    "name": "会員特典",
    "is_active": 0,
    "input_type": "radio",
    "input_choices": [
      {
        "view_name": "鉛筆",
        "value": "a"
      },
      {
        "view_name": "消しゴム",
        "value": "b"
      },
      {
        "view_name": "定規",
        "value": "c"
      }
    ],
    "show_flag": 1,
    "required": true,
    "sort_priority": 5,
    "created_at": "2021-06-11 14:39:44",
    "updated_at": "2023-12-12 18:21:13"
  }
}
```

## PATCH {{api_url}}/api/v1/customer_customs/

**リクエストBODY**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| customer_customs\[{{i}}\]\[id\] | 会員カスタム項目ID | 整数 | 11 | 必須 |
| customer_customs\[{{i}}\]\[no\] | 会員カスタム項目No. | 整数 | 11 | 項目存在時必須 |
| customer_customs\[{{i}}\]\[name\] | 会員カスタム項目名 | 文字列 | 255 | 項目存在時必須 |
| customer_customs\[{{i}}\]\[is_active\] | 状態 | 整数 | 1 | 0=無効,1=有効 |
| customer_customs\[{{i}}\]\[input_type\] | フォームタイプ | 文字列 | 7 | text/texarea/select/check/radio |
| customer_customs\[{{i}}\]\[input_choices\] | 選択肢の値と表示名 | 配列 |  | input_typeがselect/check/radioの場合、必須 |
| customer_customs\[{{i}}\]\[input_choices\]\[{{j}}\]\[view_name\] | 選択肢の表示名 | 文字列 | 32 |  |
| customer_customs\[{{i}}\]\[input_choices\]\[{{j}}\]\[value\] | 選択肢の値 | 文字列 | 32 |  |
| customer_customs\[{{i}}\]\[show_flag\] | 会員への表示・変更 | 整数 | 1 | 0=表示・変更させる,1=表示させる・変更させない,2=表示しない |
| customer_customs\[{{i}}\]\[required\] | 入力確認 | 論理 | 5 | true=必須,false=任意 |
| customer_customs\[{{i}}\]\[sort_priority\] | 表示優先度 | 整数 | 4 | \-127\~127 |

**リクエストボディ例:**

```json
{
  "customer_customs": [
    {
      "id": 22,
      "no": 4,
      "name": "会員特典",
      "is_active": 1,
      "input_type": "check",
      "input_choices": [
        {
          "view_name": "鉛筆",
          "value": 1
        },
        {
          "view_name": "消しゴム",
          "value": 2
        },
        {
          "view_name": "定規",
          "value": 3
        }
      ],
      "show_flag": 0,
      "required": false,
      "sort_priority": 0
    },
    {
      "id": 23,
      "no": 5,
      "name": "会員種別",
      "is_active": 1,
      "input_type": "radio",
      "input_choices": [
        {
          "view_name": "リピーター",
          "value": "ok"
        },
        {
          "view_name": "新規",
          "value": "ng"
        }
      ],
      "show_flag": 0,
      "required": false,
      "sort_priority": 0
    },
    {
      "id": 24,
      "input_type": "text"
    }
  ]
}
```

**レスポンス例（200 OK）:**

```json
{
  "customer_customs": [
    {
      "id": 22,
      "no": 4,
      "name": "会員特典",
      "is_active": 1,
      "input_type": "check",
      "input_choices": [
        {
          "view_name": "鉛筆",
          "value": 1
        },
        {
          "view_name": "消しゴム",
          "value": 2
        },
        {
          "view_name": "定規",
          "value": 3
        }
      ],
      "show_flag": 0,
      "required": false,
      "sort_priority": 0,
      "created_at": "2021-06-11 14:39:44",
      "updated_at": "2023-12-12 18:22:18"
    },
    {
      "id": 23,
      "no": 5,
      "name": "会員種別",
      "is_active": 1,
      "input_type": "radio",
      "input_choices": [
        {
          "view_name": "リピーター",
          "value": "ok"
        },
        {
          "view_name": "新規",
          "value": "ng"
        }
      ],
      "show_flag": 0,
      "required": false,
      "sort_priority": 0,
      "created_at": "2021-06-11 14:41:19",
      "updated_at": "2023-12-12 18:22:18"
    },
    {
      "id": 24,
      "no": 6,
      "name": "確認事項",
      "is_active": 1,
      "input_type": "text",
      "input_choices": null,
      "show_flag": 0,
      "required": false,
      "sort_priority": 0,
      "created_at": "2023-12-12 17:55:03",
      "updated_at": "2023-12-12 18:22:18"
    }
  ]
}
```

## POST {{api_url}}/api/v1/customer_customs/

**リクエストBODY**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| customer_customs\[{{i}}\]\[no\] | 会員カスタム項目No. | 整数 | 11 | 必須 |
| customer_customs\[{{i}}\]\[name\] | 会員カスタム項目名 | 文字列 | 255 | 必須 |
| customer_customs\[{{i}}\]\[is_active\] | 状態 | 整数 | 1 | 0=無効,1=有効  <br>初期値: 0 |
| customer_customs\[{{i}}\]\[input_type\] | フォームタイプ | 文字列 | 7 | text/texarea/select/check/radio  <br>初期値: "text" |
| customer_customs\[{{i}}\]\[input_choices\] | 選択肢の値と表示名 | 配列 |  | input_typeがselect/check/radioの場合、必須  <br>初期値: null |
| customer_customs\[{{i}}\]\[input_choices\]\[{{j}}\]\[view_name\] | 選択肢の表示名 | 文字列 | 32 |  |
| customer_customs\[{{i}}\]\[input_choices\]\[{{j}}\]\[value\] | 選択肢の値 | 文字列 | 32 |  |
| customer_customs\[{{i}}\]\[show_flag\] | 会員への表示・変更 | 整数 | 1 | 0=表示・変更させる,1=表示させる・変更させない,2=表示しない  <br>初期値: 2 |
| customer_customs\[{{i}}\]\[required\] | 入力確認 | 論理 | 5 | true=必須,false=任意  <br>初期値: false |
| customer_customs\[{{i}}\]\[sort_priority\] | 表示優先度 | 整数 | 4 | \-127\~127  <br>初期値: 0 |

**リクエストボディ例:**

```json
{
  "customer_customs": [
    {
      "no": 6,
      "name": "確認事項",
      "is_active": 1,
      "input_type": "check",
      "input_choices": [
        {
          "view_name": "Aを確認済み",
          "value": "a"
        },
        {
          "view_name": "Bを確認済み",
          "value": "b"
        },
        {
          "view_name": "Cを確認済み",
          "value": "c"
        }
      ],
      "show_flag": 0,
      "required": false,
      "sort_priority": 0
    },
    {
      "no": 7,
      "name": "会員カスタム7",
      "is_active": 1,
      "input_type": "text",
      "show_flag": 1,
      "required": false,
      "sort_priority": 0
    }
  ]
}
```

**レスポンス例（201 Created）:**

```json
{
  "customer_customs": [
    {
      "id": 24,
      "no": 6,
      "name": "確認事項",
      "is_active": 1,
      "input_type": "check",
      "input_choices": [
        {
          "view_name": "Aを確認済み",
          "value": "a"
        },
        {
          "view_name": "Bを確認済み",
          "value": "b"
        },
        {
          "view_name": "Cを確認済み",
          "value": "c"
        }
      ],
      "show_flag": 0,
      "required": false,
      "sort_priority": 0,
      "created_at": "2023-12-12 18:23:13",
      "updated_at": "2023-12-12 18:23:13"
    },
    {
      "id": 25,
      "no": 7,
      "name": "会員カスタム7",
      "is_active": 1,
      "input_type": "text",
      "input_choices": null,
      "show_flag": 1,
      "required": false,
      "sort_priority": 0,
      "created_at": "2023-12-12 18:23:13",
      "updated_at": "2023-12-12 18:23:13"
    }
  ]
}
```
