# 会員別配送先

会員の登録住所とは別に登録できる配送先住所

## GET {{api_url}}/api/v1/other_addresses/1

**レスポンス一覧**

| パラメータ名 | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| id | Bカート配送先ID | 整数 | 8 |  |
| customer_id | 会員ID | 整数 | 8 |  |
| destination_code | 配送先ID | 文字列 | 255 |  |
| comp_name | 配送先会社名 | 文字列 | 255 |  |
| department | 配送先部署名 | 文字列 | 255 |  |
| name | 配送先名 | 文字列 | 255 |  |
| zip | 配送先郵便番号 | 文字列 | 255 |  |
| pref | 配送先都道府県 | 文字列 | 255 |  |
| address1 | 配送先市区町村 | 文字列 | 50 |  |
| address2 | 配送先町域・番地 | 文字列 | 50 |  |
| address3 | 配送先ビル・建物名 | 文字列 | 50 |  |
| tel | 配送先電話番号 | 文字列 | 255 |  |

**レスポンス例（200 OK）:**

```json
{
  "other_address": {
    "id": 1,
    "customer_id": 1,
    "destination_code": null,
    "comp_name": "テスト株式会社",
    "department": "流通部",
    "name": "佐藤太郎",
    "zip": "530-0001",
    "pref": "大阪府",
    "address1": "○○市△△区□□",
    "address2": "000番地",
    "address3": "テストビル",
    "tel": "999-999-9999"
  }
}
```

## GET {{api_url}}/api/v1/other_addresses

**URIパラメータ**

| パラメータ名 | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| limit | limit | 整数 |  | 指定した件数分のデータを取得します。指定なしの場合は20件、最大100件 |
| offset | offset | 整数 |  | 指定した値+1件目のデータからlimit分を取得します。指定しない場合は0 |
| ids | ID複数 | 整数 |  | 複数のBカート配送先IDをカンマ区切りで指定 |
| fields | フィールド | 文字列 |  | 取得したいフィールドカンマ区切りで指定 |
| customer_id | 会員ID | 整数 | 8 |  |
| destination_code | 配送先ID | 文字列 | 255 |  |
| comp_name | 配送先会社名 | 文字列 | 255 |  |
| department | 配送先部署名 | 文字列 | 255 |  |
| name | 配送先名 | 文字列 | 255 |  |
| zip | 配送先郵便番号 | 文字列 | 255 | 000-0000 |
| pref | 配送先都道府県 | 文字列 | 255 |  |
| address1 | 配送先市区町村 | 文字列 | 50 |  |
| address2 | 配送先町域・番地 | 文字列 | 50 |  |
| address3 | 配送先ビル・建物名 | 文字列 | 50 |  |
| tel | 配送先電話番号 | 文字列 | 255 |  |

## 拡張パラメータによる高度な絞り込み

拡張パラメータを使用することで、より高度な絞り込みが可能です。

詳しくは、[パラメータ](../docs/04-parameters.md)の「拡張パラメータ」欄をご参照ください。

**レスポンス例（200 OK）:**

```json
{
  "other_addresses": [
    {
      "id": 1,
      "customer_id": 1,
      "destination_code": null,
      "comp_name": "テスト株式会社",
      "department": "流通部",
      "name": "佐藤太郎",
      "zip": "530-0001",
      "pref": "大阪府",
      "address1": "○○市△△区□□",
      "address2": "000番地",
      "address3": "テストビル",
      "tel": "999-999-9999"
    },
    {
      "id": 3,
      "customer_id": 10021,
      "destination_code": null,
      "comp_name": "株式会社ミニコンビニ",
      "department": "倉庫管理部",
      "name": "出荷担当者",
      "zip": "150-0001",
      "pref": "東京都",
      "address1": "渋谷区",
      "address2": "神宮前",
      "address3": "神宮前ビルB1",
      "tel": "03-0000-0000"
    },
    {
      "id": 4,
      "customer_id": 10022,
      "destination_code": null,
      "comp_name": "地元オークション株式会社（委託倉庫宛）",
      "department": "業務管理部",
      "name": "西川　みすず",
      "zip": "240-0005",
      "pref": "神奈川県",
      "address1": "横浜市保土ケ谷区",
      "address2": "神戸町",
      "address3": "株式会社委託倉庫1F",
      "tel": "024-000-0000"
    },
    {
      "id": 5,
      "customer_id": 10037,
      "destination_code": null,
      "comp_name": "大塚寝具株式会社",
      "department": "関東倉庫",
      "name": "倉庫長",
      "zip": "241-0024",
      "pref": "神奈川県",
      "address1": "横浜市旭区",
      "address2": "本村町テストテスト",
      "address3": "",
      "tel": "00-0000-0000"
    }
  ],
  "meta": {
    "limit": 20,
    "offset": 0,
    "total": 4
  }
}
```

## PATCH {{api_url}}/api/v1/other_addresses/1

**リクエストBODY**

| KEY | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| customer_id | 会員ID | 整数 | 8 | 項目存在時必須 |
| destination_code | 配送先ID | 文字列 | 255 |  |
| comp_name | 配送先会社名 | 文字列 | 255 |  |
| department | 配送先部署名 | 文字列 | 255 |  |
| name | 配送先名 | 文字列 | 255 | 項目存在時必須 |
| zip | 配送先郵便番号 | 文字列 | 255 | 項目存在時必須  <br>000-0000 |
| pref | 配送先都道府県 | 文字列 | 255 | 項目存在時必須 |
| address1 | 配送先市区町村 | 文字列 | 50 | 項目存在時必須 |
| address2 | 配送先町域・番地 | 文字列 | 50 | 項目存在時必須 |
| address3 | 配送先ビル・建物名 | 文字列 | 50 |  |
| tel | 配送先電話番号 | 文字列 | 255 | ハイフン有り |

**リクエストボディ例:**

```json
{
  "customer_id": 2,
  "destination_code": "3",
  "comp_name": "My Comp"
}
```

**レスポンス例（200 OK）:**

```json
{
  "other_address": {
    "id": 1,
    "customer_id": 2,
    "destination_code": "3",
    "comp_name": "My Comp",
    "department": "流通部",
    "name": "佐藤太郎",
    "zip": "530-0001",
    "pref": "大阪府",
    "address1": "○○市△△区□□",
    "address2": "000番地",
    "address3": "テストビル",
    "tel": "999-999-9999"
  }
}
```

## PATCH {{api_url}}/api/v1/other_addresses/

**リクエストBODY**

| KEY | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| other_addresses\[{{i}}\]\[customer_id\] | 会員ID | 整数 | 8 | 項目存在時必須 |
| other_addresses\[{{i}}\]\[destination_code\] | 配送先ID | 文字列 | 255 |  |
| other_addresses\[{{i}}\]\[comp_name\] | 配送先会社名 | 文字列 | 255 |  |
| other_addresses\[{{i}}\]\[department\] | 配送先部署名 | 文字列 | 255 |  |
| other_addresses\[{{i}}\]\[name\] | 配送先名 | 文字列 | 255 | 項目存在時必須 |
| other_addresses\[{{i}}\]\[zip\] | 配送先郵便番号 | 文字列 | 255 | 項目存在時必須  <br>000-0000 |
| other_addresses\[{{i}}\]\[pref\] | 配送先都道府県 | 文字列 | 255 | 項目存在時必須 |
| other_addresses\[{{i}}\]\[address1\] | 配送先市区町村 | 文字列 | 50 | 項目存在時必須 |
| other_addresses\[{{i}}\]\[address2\] | 配送先町域・番地 | 文字列 | 50 | 項目存在時必須 |
| other_addresses\[{{i}}\]\[address3\] | 配送先ビル・建物名 | 文字列 | 50 |  |
| other_addresses\[{{i}}\]\[tel\] | 配送先電話番号 | 文字列 | 255 | ハイフン有り |

**リクエストボディ例:**

```json
{
  "other_addresses": [
    {
      "id": 1,
      "customer_id": 2,
      "destination_code": "3",
      "comp_name": "My Comp"
    },
    {
      "id": 2,
      "customer_id": 5,
      "destination_code": "test",
      "comp_name": "My Comp #2"
    }
  ]
}
```

**レスポンス例（422 Unprocessable Entity）:**

```json
{
  "errors": [
    {
      "other_addresses.1.id": "指定されたidは存在しません。"
    }
  ]
}
```

## POST {{api_url}}/api/v1/other_addresses/

**リクエストBODY**

| KEY | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| other_addresses\[{{i}}\]\[customer_id\] | 会員ID | 整数 | 8 | 必須 |
| other_addresses\[{{i}}\]\[destination_code\] | 配送先ID | 文字列 | 255 |  |
| other_addresses\[{{i}}\]\[comp_name\] | 配送先会社名 | 文字列 | 255 |  |
| other_addresses\[{{i}}\]\[department\] | 配送先部署名 | 文字列 | 255 |  |
| other_addresses\[{{i}}\]\[name\] | 配送先名 | 文字列 | 255 | 必須 |
| other_addresses\[{{i}}\]\[zip\] | 配送先郵便番号 | 文字列 | 255 | 必須  <br>000-0000 |
| other_addresses\[{{i}}\]\[pref\] | 配送先都道府県 | 文字列 | 255 | 必須 |
| other_addresses\[{{i}}\]\[address1\] | 配送先市区町村 | 文字列 | 50 | 必須 |
| other_addresses\[{{i}}\]\[address2\] | 配送先町域・番地 | 文字列 | 50 | 必須 |
| other_addresses\[{{i}}\]\[address3\] | 配送先ビル・建物名 | 文字列 | 50 |  |
| other_addresses\[{{i}}\]\[tel\] | 配送先電話番号 | 文字列 | 255 | ハイフン有り |

**リクエストボディ例:**

```json
{
  "other_addresses": [
    {
      "customer_id": 2,
      "destination_code": "5",
      "comp_name": "My Comp #3",
      "name": "My name #3",
      "zip": "000-0000",
      "pref": "東京都",
      "address1": "My address1 #3",
      "address2": "My address2 #3"
    },
    {
      "id": 2,
      "customer_id": 5,
      "destination_code": "des 2",
      "comp_name": "My Comp #4",
      "name": "My name #4",
      "zip": "000-0000",
      "pref": "神奈川県",
      "address1": "My address1 #4",
      "address2": "My address2 #4"
    }
  ]
}
```

**レスポンス例（201 Created）:**

```json
{
  "other_addresses": [
    {
      "id": 6,
      "customer_id": 2,
      "destination_code": "5",
      "comp_name": "My Comp #3",
      "department": "",
      "name": "My name #3",
      "zip": "000-0000",
      "pref": "東京都",
      "address1": "My address1 #3",
      "address2": "My address2 #3",
      "address3": "",
      "tel": ""
    },
    {
      "id": 7,
      "customer_id": 5,
      "destination_code": "des 2",
      "comp_name": "My Comp #4",
      "department": "",
      "name": "My name #4",
      "zip": "000-0000",
      "pref": "神奈川県",
      "address1": "My address1 #4",
      "address2": "My address2 #4",
      "address3": "",
      "tel": ""
    }
  ]
}
```
