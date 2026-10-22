# 出荷

出荷情報

## GET {{api_url}}/api/v1/logistics/20000000

**レスポンス一覧**

| パラメータ名 | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| id | Bカート発送ID | 整数 | 11 |  |
| shipment_code | 出荷管理番号 | 文字列 | 255 |  |
| delivery_code | 送り状番号 | 文字列 | 255 |  |
| destination_code | 配送先ID | 文字列 | 255 |  |
| shipping_group_id | 配送グループID | 文字列 | 255 |  |
| comp_name | 配送先 会社名 | 文字列 | 255 |  |
| department | 配送先 部署名 | 文字列 | 255 |  |
| name | 配送先 担当者名 | 文字列 | 255 |  |
| zip | 配送先郵便番号 | 文字列 | 16 |  |
| pref | 配送先都道府県 | 文字列 | 32 |  |
| address1 | 配送先 市町区村 | 文字列 | 255 |  |
| address2 | 配送先 町域・番地 | 文字列 | 255 |  |
| address3 | 配送先 ビル・建物名 | 文字列 | 255 |  |
| tel | 配送先電話番号 | 文字列 | 255 |  |
| due_date | 配送希望日 | 日付 | 10 | Y-m-d |
| due_time | 配送希望時間 | 文字列 | 32 |  |
| memo | 発送メモ | 文字列 | 65,535 |  |
| shipment_date | 発送日 | 日付 | 10 | Y-m-d |
| arrival_date | 納品日 | 日付 | 10 | Y-m-d |
| status | 発送状況 | 文字列 | 4 | 未発送/発送指示/発送済 |
| complete | 出荷情報一式 | 整数 |  | 1 を指定すると出荷に紐付いた受注商品と受注情報も取得 |

**レスポンス例（200 OK）:**

```json
{
  "logistic": {
    "id": 20000000,
    "shipment_code": "",
    "delivery_code": "",
    "destination_code": null,
    "shipping_group_id": 1,
    "comp_name": "株式会社サンプル",
    "department": "営業部",
    "name": "鈴木太郎",
    "zip": "111-1111",
    "pref": "東京都",
    "address1": "○○区△町 3-24 〇〇ビル",
    "address2": "",
    "address3": "",
    "tel": "222-222-2222",
    "due_date": null,
    "due_time": null,
    "memo": "",
    "shipment_date": null,
    "arrival_date": "2022-08-02",
    "status": "未発送"
  }
}
```

## GET {{api_url}}/api/v1/logistics

**URIパラメータ**

| パラメータ名 | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| limit | limit | 整数 |  | 指定した件数分のデータを取得します。指定なしの場合は20件、最大100件 |
| offset | offset | 整数 |  | 指定した値+1件目のデータからlimit分を取得します。指定しない場合は0 |
| ids | ID複数 | 整数 |  | 複数のBカート発送IDをカンマ区切りで指定 |
| fields | フィールド | 文字列 |  | 取得したいフィールドカンマ区切りで指定 |
| shipment_code | 出荷管理番号 | 文字列 | 255 |  |
| delivery_code | 送り状番号 | 文字列 | 255 |  |
| destination_code | 配送先ID | 文字列 | 255 |  |
| shipping_group_id | 配送グループID | 文字列 | 255 |  |
| zip | 配送先郵便番号 | 文字列 | 16 |  |
| pref | 配送先都道府県 | 文字列 | 32 |  |
| tel | 配送先電話番号 | 文字列 | 255 |  |
| status | 発送状況 | 文字列 | 4 | 未発送/発送指示/発送済 |
| due_date | 配送希望日 | 文字列 | 19 | Y-m-d |
| due_date_min | 配送希望日〜 | 文字列 | 19 | Y-m-d　指定日以降 |
| due_date_max | 〜配送希望日 | 文字列 | 19 | Y-m-d　指定日以前 |
| shipment_date | 発送日 | 文字列 | 19 | Y-m-d |
| shipment_date_min | 発送日〜 | 文字列 | 19 | Y-m-d　指定日以降 |
| shipment_date_max | 〜発送日 | 文字列 | 19 | Y-m-d　指定日以前 |
| arrival_date | 納品日 | 文字列 | 19 | Y-m-d |
| arrival_date_min | 納品日〜 | 文字列 | 19 | Y-m-d　指定日以降 |
| arrival_date_max | 〜納品日 | 文字列 | 19 | Y-m-d　指定日以前 |
| complete | 出荷情報一式 | 整数 |  | 1 指定すると出荷に紐付いた受注商品と受注情報も取得 |

## 拡張パラメータによる高度な絞り込み

拡張パラメータを使用することで、より高度な絞り込みが可能です。

詳しくは、[パラメータ](../docs/04-parameters.md)の「拡張パラメータ」欄をご参照ください。

**レスポンス例:**

```json
{
  "logistics": [
    {
      "id": 20000000,
      "shipment_code": "",
      "delivery_code": "",
      "destination_code": null,
      "shipping_group_id": 1,
      "comp_name": "株式会社サンプル",
      "department": "営業部",
      "name": "鈴木太郎",
      "zip": "111-1111",
      "pref": "東京都",
      "address1": "○○区△町 3-24 〇〇ビル",
      "address2": "",
      "address3": "",
      "tel": "222-222-2222",
      "due_date": null,
      "due_time": null,
      "memo": "",
      "shipment_date": null,
      "arrival_date": null,
      "status": "未発送"
    },
    {
      "id": 20000001,
      "shipment_code": "",
      "delivery_code": "",
      "destination_code": null,
      "shipping_group_id": 1,
      "comp_name": "株式会社サンプル",
      "department": "営業部",
      "name": "鈴木太郎",
      "zip": "111-1111",
      "pref": "東京都",
      "address1": "○○区△町 3-24 〇〇ビル",
      "address2": "",
      "address3": "",
      "tel": "222-222-2222",
      "due_date": null,
      "due_time": null,
      "memo": "",
      "shipment_date": null,
      "arrival_date": null,
      "status": "未発送"
    },
    {
      "id": 20000002,
      "shipment_code": "",
      "delivery_code": "",
      "destination_code": null,
      "shipping_group_id": 1,
      "comp_name": "株式会社サンプル",
      "department": "営業部",
      "name": "鈴木太郎",
      "zip": "111-1111",
      "pref": "東京都",
      "address1": "○○区△町 3-24 〇〇ビル",
      "address2": "",
      "address3": "",
      "tel": "222-222-2222",
      "due_date": null,
      "due_time": null,
      "memo": "",
      "shipment_date": null,
      "arrival_date": null,
      "status": "発送済"
    },
    {
      "id": 20000003,
      "shipment_code": "",
      "delivery_code": "",
      "destination_code": null,
      "shipping_group_id": 1,
      "comp_name": "株式会社サンプル",
      "department": "営業部",
      "name": "鈴木太郎",
      "zip": "111-1111",
      "pref": "東京都",
      "address1": "○○区△町 3-24 〇〇ビル",
      "address2": "",
      "address3": "",
      "tel": "222-222-2222",
      "due_date": null,
      "due_time": null,
      "memo": "",
      "shipment_date": null,
      "arrival_date": null,
      "status": "未発送"
    },
    {
      "id": 20000004,
      "shipment_code": "",
      "delivery_code": "",
      "destination_code": null,
      "shipping_group_id": 1,
      "comp_name": "株式会社サンプル",
      "department": "営業部",
      "name": "鈴木太郎",
      "zip": "111-1111",
      "pref": "東京都",
      "address1": "○○区△町 3-24 〇〇ビル",
      "address2": "",
      "address3": "",
      "tel": "222-222-2222",
      "due_date": null,
      "due_time": null,
      "memo": "",
      "shipment_date": null,
      "arrival_date": null,
      "status": "未発送"
    },
    {
      "id": 20000005,
      "shipment_code": "",
      "delivery_code": "",
      "destination_code": null,
      "shipping_group_id": 1,
      "comp_name": "株式会社サンプル",
      "department": "営業部",
      "name": "鈴木太郎",
      "zip": "111-1111",
      "pref": "東京都",
      "address1": "○○区△町 3-24 〇〇ビル",
      "address2": "",
      "address3": "",
      "tel": "222-222-2222",
      "due_date": null,
      "due_time": "午前中（8時～12時）",
      "memo": "",
      "shipment_date": null,
      "arrival_date": null,
      "status": "発送済"
    },
    {
      "id": 20000006,
      "shipment_code": "",
      "delivery_code": "",
      "destination_code": null,
      "shipping_group_id": 1,
      "comp_name": "株式会社サンプル",
      "department": "営業部",
      "name": "鈴木太郎",
      "zip": "111-1111",
      "pref": "東京都",
      "address1": "○○区△町 3-24 〇〇ビル",
      "address2": "",
      "address3": "",
      "tel": "222-222-2222",
      "due_date": null,
      "due_time": "午前中（8時～12時）",
      "memo": "",
      "shipment_date": null,
      "arrival_date": null,
      "status": "未発送"
    },
    {
      "id": 20000007,
      "shipment_code": "",
      "delivery_code": "",
      "destination_code": null,
      "shipping_group_id": 1,
      "comp_name": "株式会社サンプル",
      "department": "営業部",
      "name": "鈴木太郎",
      "zip": "111-1111",
      "pref": "東京都",
      "address1": "○○区△町 3-24 〇〇ビル",
      "address2": "",
      "address3": "",
      "tel": "222-222-2222",
      "due_date": null,
      "due_time": "午前中（8時～12時）",
      "memo": "",
      "shipment_date": null,
      "arrival_date": null,
      "status": "未発送"
    },
    {
      "id": 20000008,
      "shipment_code": "",
      "delivery_code": "",
      "destination_code": null,
      "shipping_group_id": 1,
      "comp_name": "株式会社サンプル",
      "department": "営業部",
      "name": "鈴木太郎",
      "zip": "111-1111",
      "pref": "東京都",
      "address1": "○○区△町 3-24 〇〇ビル",
      "address2": "",
      "address3": "",
      "tel": "222-222-2222",
      "due_date": null,
      "due_time": null,
      "memo": "",
      "shipment_date": null,
      "arrival_date": null,
      "status": "未発送"
    },
    {
      "id": 20000010,
      "shipment_code": "",
      "delivery_code": "",
      "destination_code": null,
      "shipping_group_id": 1,
      "comp_name": "株式会社サンプル",
      "department": "営業部",
      "name": "鈴木太郎",
      "zip": "111-1111",
      "pref": "東京都",
      "address1": "○○区△町 3-24 〇〇ビル",
      "address2": "",
      "address3": "",
      "tel": "222-222-2222",
      "due_date": null,
      "due_time": "14時～16時",
      "memo": "",
      "shipment_date": null,
      "arrival_date": null,
      "status": "未発送"
    },
    {
      "id": 20000011,
      "shipment_code": "",
      "delivery_code": "",
      "destination_code": null,
      "shipping_group_id": 1,
      "comp_name": "大竹家具株式会社",
      "department": "仕入れ課",
      "name": "山口宗二",
      "zip": "150-0013",
      "pref": "東京都",
      "address1": "渋谷区",
      "address2": "恵比寿",
      "address3": "3-24",
      "tel": "03-1111-1111",
      "due_date": "2012-08-31",
      "due_time": "12時～14時",
      "memo": "",
      "shipment_date": null,
      "arrival_date": null,
      "status": "未発送"
    },
    {
      "id": 20000012,
      "shipment_code": "",
      "delivery_code": "",
      "destination_code": null,
      "shipping_group_id": 1,
      "comp_name": "大竹家具株式会社",
      "department": "仕入れ課",
      "name": "山口宗二",
      "zip": "150-0013",
      "pref": "東京都",
      "address1": "渋谷区",
      "address2": "恵比寿",
      "address3": "3-24",
      "tel": "03-1111-1111",
      "due_date": null,
      "due_time": "16時～18時",
      "memo": "",
      "shipment_date": null,
      "arrival_date": null,
      "status": "未発送"
    },
    {
      "id": 20000013,
      "shipment_code": "",
      "delivery_code": "",
      "destination_code": null,
      "shipping_group_id": 1,
      "comp_name": "有限会社佐藤商店",
      "department": "仕入れ担当",
      "name": "勝間和子",
      "zip": "100-0000",
      "pref": "東京都",
      "address1": "千代田区",
      "address2": " ",
      "address3": "111 ",
      "tel": "0000-00-0000",
      "due_date": "2012-09-01",
      "due_time": "19時～21時",
      "memo": "",
      "shipment_date": null,
      "arrival_date": null,
      "status": "未発送"
    },
    {
      "id": 20000014,
      "shipment_code": "",
      "delivery_code": "",
      "destination_code": null,
      "shipping_group_id": 1,
      "comp_name": "有限会社佐藤商店",
      "department": "仕入れ担当",
      "name": "勝間和子",
      "zip": "100-0000",
      "pref": "東京都",
      "address1": "千代田区",
      "address2": " ",
      "address3": "111 ",
      "tel": "0000-00-0000",
      "due_date": null,
      "due_time": "18時～20時",
      "memo": "",
      "shipment_date": null,
      "arrival_date": null,
      "status": "未発送"
    },
    {
      "id": 20000015,
      "shipment_code": "",
      "delivery_code": "",
      "destination_code": null,
      "shipping_group_id": 1,
      "comp_name": "有限会社佐藤商店",
      "department": "仕入れ担当",
      "name": "勝間和子",
      "zip": "100-0000",
      "pref": "東京都",
      "address1": "千代田区",
      "address2": " ",
      "address3": "111 ",
      "tel": "0000-00-0000",
      "due_date": null,
      "due_time": "14時～16時",
      "memo": "",
      "shipment_date": null,
      "arrival_date": null,
      "status": "未発送"
    },
    {
      "id": 20000016,
      "shipment_code": "",
      "delivery_code": "",
      "destination_code": null,
      "shipping_group_id": 1,
      "comp_name": "インポートオブユーロ株式会社",
      "department": "",
      "name": "垣内博文",
      "zip": "111-1111",
      "pref": "大阪府",
      "address1": "吹田市江坂町 3－23 江坂第1ビル",
      "address2": "",
      "address3": "",
      "tel": "0000-00-0000",
      "due_date": null,
      "due_time": null,
      "memo": "",
      "shipment_date": null,
      "arrival_date": null,
      "status": "未発送"
    },
    {
      "id": 20000017,
      "shipment_code": "",
      "delivery_code": "",
      "destination_code": null,
      "shipping_group_id": 1,
      "comp_name": "インポートオブユーロ株式会社",
      "department": "",
      "name": "垣内博文",
      "zip": "111-1111",
      "pref": "大阪府",
      "address1": "吹田市江坂町 3－23 江坂第1ビル",
      "address2": "",
      "address3": "",
      "tel": "0000-00-0000",
      "due_date": null,
      "due_time": "12時～14時",
      "memo": "",
      "shipment_date": null,
      "arrival_date": null,
      "status": "未発送"
    },
    {
      "id": 20000018,
      "shipment_code": "",
      "delivery_code": "",
      "destination_code": null,
      "shipping_group_id": 1,
      "comp_name": "株式会社カンサイ機械",
      "department": "購買部",
      "name": "新山綱彦",
      "zip": "100-0000",
      "pref": "東京都",
      "address1": "千代田区",
      "address2": " ",
      "address3": "1-１　 ",
      "tel": "0000-1111-0000",
      "due_date": null,
      "due_time": null,
      "memo": "",
      "shipment_date": null,
      "arrival_date": null,
      "status": "未発送"
    },
    {
      "id": 20000019,
      "shipment_code": "",
      "delivery_code": "",
      "destination_code": null,
      "shipping_group_id": 1,
      "comp_name": "株式会社カンサイ機械",
      "department": "購買部",
      "name": "新山綱彦",
      "zip": "100-0000",
      "pref": "東京都",
      "address1": "千代田区",
      "address2": " ",
      "address3": "1-１　 ",
      "tel": "0000-1111-0000",
      "due_date": null,
      "due_time": null,
      "memo": "",
      "shipment_date": null,
      "arrival_date": null,
      "status": "未発送"
    },
    {
      "id": 20000020,
      "shipment_code": "11111111111111",
      "delivery_code": "11111111111111",
      "destination_code": null,
      "shipping_group_id": 1,
      "comp_name": "株式会社カンサイ機械",
      "department": "購買部",
      "name": "新山綱彦",
      "zip": "100-0000",
      "pref": "東京都",
      "address1": "千代田区",
      "address2": "",
      "address3": "1-１　",
      "tel": "0000-1111-0000",
      "due_date": null,
      "due_time": "18時～20時",
      "memo": "",
      "shipment_date": "2017-07-31",
      "arrival_date": null,
      "status": "発送済"
    }
  ],
  "meta": {
    "limit": 20,
    "offset": 0,
    "total": 68
  }
}
```

## PATCH {{api_url}}/api/v1/logistics/20000000

**リクエストBODY**

| パラメータ名 | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| shipment_code | 配送管理番号 | 文字列 | 255 |  |
| delivery_code | 送り状番号 | 文字列 | 255 |  |
| destination_code | 配送先ID | 文字列 | 255 |  |
| shipping_group_id | 配送グループID | 文字列 | 255 |  |
| comp_name | 配送先会社名 | 文字列 | 255 |  |
| department | 配送先部署 | 文字列 | 255 |  |
| name | 配送先名 | 文字列 | 255 |  |
| zip | 配送先郵便番号 | 文字列 | 16 |  |
| pref | 配送先都道府県 | 文字列 | 32 |  |
| address1 | 配送先市区町村 | 文字列 | 255 |  |
| address2 | 配送先町域・番地 | 文字列 | 255 |  |
| address3 | 配送先ビル・建物名 | 文字列 | 255 |  |
| tel | 配送先電話番号 | 文字列 | 255 |  |
| due_date | 配送希望日 | 文字列 | 19 | Y-m-d |
| due_time | 配送希望時間 | 文字列 | 32 |  |
| memo | 発送メモ | 文字列 | 65,536 |  |
| shipment_date | 発送日 | 日付 | 19 | Y-m-d |
| arrival_date | 納品日 | 文字列 | 19 | Y-m-d |
| status | 発送状況 | 文字列 | 4 | 未発送/発送指示/発送済 |

**リクエストボディ例:**

```json
{
  "shipment_date": "2016-11-18",
  "due_date": "2016-11-25",
  "tel": "075-361-1171",
  "memo": "2016/11/17 山本様より電話番号間違えと電話があり修正",
  "arrival_date": "2022-08-02"
}
```

**レスポンス例（200 OK）:**

```json
{
  "logistic": {
    "id": 20000000,
    "shipment_code": "",
    "delivery_code": "",
    "destination_code": null,
    "shipping_group_id": 1,
    "comp_name": "株式会社サンプル",
    "department": "営業部",
    "name": "鈴木太郎",
    "zip": "111-1111",
    "pref": "東京都",
    "address1": "○○区△町 3-24 〇〇ビル",
    "address2": "",
    "address3": "",
    "tel": "075-361-1171",
    "due_date": "2016-11-25",
    "due_time": null,
    "memo": "2016/11/17 山本様より電話番号間違えと電話があり修正",
    "shipment_date": "2016-11-18",
    "arrival_date": "2022-08-02",
    "status": "未発送"
  }
}
```

## PATCH {{api_url}}/api/v1/logistics

**リクエストBODY**

| KEY | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| logistics\[{{i}}\]\[id\] | Bカート発送ID | 文字列 | 11 | 必須 |
| logistics\[{{i}}\]\[shipment_code\] | 配送管理番号 | 文字列 | 255 |  |
| logistics\[{{i}}\]\[delivery_code\] | 送り状番号 | 文字列 | 255 |  |
| logistics\[{{i}}\]\[destination_code\] | 配送先ID | 文字列 | 255 |  |
| logistics\[{{i}}\]\[shipping_group_id\] | 配送グループID | 文字列 | 255 |  |
| logistics\[{{i}}\]\[comp_name\] | 配送先会社名 | 文字列 | 255 |  |
| logistics\[{{i}}\]\[department\] | 配送先部署 | 文字列 | 255 |  |
| logistics\[{{i}}\]\[name\] | 配送先名 | 文字列 | 255 |  |
| logistics\[{{i}}\]\[zip\] | 配送先郵便番号 | 文字列 | 16 |  |
| logistics\[{{i}}\]\[pref\] | 配送先都道府県 | 文字列 | 32 |  |
| logistics\[{{i}}\]\[address1\] | 配送先市区町村 | 文字列 | 255 |  |
| logistics\[{{i}}\]\[address2\] | 配送先町域・番地 | 文字列 | 255 |  |
| logistics\[{{i}}\]\[address3\] | 配送先ビル・建物名 | 文字列 | 255 |  |
| logistics\[{{i}}\]\[tel\] | 配送先電話番号 | 文字列 | 255 |  |
| logistics\[{{i}}\]\[due_date\] | 配送希望日 | 文字列 | 19 | Y-m-d |
| logistics\[{{i}}\]\[due_time\] | 配送希望時間 | 文字列 | 32 |  |
| logistics\[{{i}}\]\[memo\] | 発送メモ | 文字列 | 65,536 |  |
| logistics\[{{i}}\]\[shipment_date\] | 発送日 | 日付 | 19 | Y-m-d |
| logistics\[{{i}}\]\[arrival_date\] | 納品日 | 日付 | 19 | Y-m-d |
| logistics\[{{i}}\]\[status\] | 発送状況 | 文字列 | 4 | 未発送/発送指示/発送済 |

※ {{i}}は配列のキー

**リクエストボディ例:**

```json
{
  "logistics": [
    {
      "id": 20000000,
      "shipment_code": "YAAAAAA",
      "delivery_code": "DC0001",
      "destination_code": null,
      "shipping_group_id": 1,
      "comp_name": "Bカートサポートセンター",
      "department": "お客様サポート",
      "name": "Bカート",
      "zip": "600-8412",
      "pref": "京都府",
      "address1": "京都市下京区",
      "address2": "二帖半敷町646番地",
      "address3": "ダイマルヤ四条烏丸ビル5F",
      "tel": "075-361-0000",
      "due_date": null,
      "due_time": "12時～14時",
      "memo": null,
      "shipment_date": null,
      "arrival_date": "2022-08-02",
      "status": "未発送"
    }
  ]
}
```

**レスポンス例（200 OK）:**

```json
{
  "logistics": [
    {
      "id": 20000000,
      "shipment_code": "YAAAAAA",
      "delivery_code": "DC0001",
      "destination_code": null,
      "shipping_group_id": 1,
      "comp_name": "Bカートサポートセンター",
      "department": "お客様サポート",
      "name": "Bカート",
      "zip": "600-8412",
      "pref": "京都府",
      "address1": "京都市下京区",
      "address2": "二帖半敷町646番地",
      "address3": "ダイマルヤ四条烏丸ビル5F",
      "tel": "075-361-0000",
      "due_date": null,
      "due_time": "12時～14時",
      "memo": "2016/11/17 山本様より電話番号間違えと電話があり修正",
      "shipment_date": null,
      "arrival_date": "2022-08-02",
      "status": "未発送"
    }
  ]
}
```
