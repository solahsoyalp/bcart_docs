# 受注商品

受注された商品

## GET {{api_url}}/api/v1/order_products/2

**レスポンス一覧**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| id | 受注商品ID | 整数 | 11 |  |
| order_id | 受注ID | 整数 | 11 |  |
| logistics_id | Bカート発送ID（出荷ID） | 整数 | 11 |  |
| product_id | 商品ID | 整数 | 11 |  |
| main_no | 商品管理番号 | 文字列 | 255 |  |
| product_no | 品番 | 文字列 | 255 |  |
| jan_code | JANコード | 文字列 | 255 |  |
| location_no | ロケーション番号 | 文字列 | 255 |  |
| product_name | 商品名 | 文字列 | 255 |  |
| product_set_id | 商品セットID | 整数 | 11 |  |
| set_name | 商品セット名 | 文字列 | 255 |  |
| unit_price | 単価 | 数値 | 11 |  |
| set_quantity | 入数 | 数値 | 64 |  |
| set_unit | 単位 | 文字列 | 255 |  |
| order_pro_count | 注文数 | 整数 | 8 |  |
| shipping_size | 配送サイズ | 数値 | 11 |  |
| tax_rate | 税率 | 数値 | 255 | 10%は0.1、8%は0.08、0%は0 |
| tax_type_id | 税区分 | 整数 | 1 | 1=標準税率,2=軽減税率,3=非課税 |
| tax_incl | 税込フラグ | 整数 | 1 | 0=税別,1=税込 |
| item_type | 商品区分 | 文字列 | 255 | 'product','shipping','payment_fees','point' |
| product_customs | 商品カスタム項目 | 配列 |  |  |
| product_set_customs | 商品セットカスタム項目 | 配列 |  |  |
| options | 商品オプション | 配列 |  |  |

**レスポンス例（200 OK）:**

```json
{
  "order_product": {
    "id": 2,
    "order_id": 128,
    "logistics_id": 20000000,
    "product_id": 2,
    "main_no": "SF-001",
    "product_no": "SF-001-02-O",
    "jan_code": "1234567891123",
    "location_no": "B3-01",
    "product_name": "クラシックソファー（一人がけ）",
    "product_set_id": 8,
    "set_name": "2個セット カラー：オーク",
    "unit_price": 800,
    "set_quantity": 5,
    "set_unit": "脚",
    "order_pro_count": 2,
    "shipping_size": 0,
    "tax_rate": "0.05",
    "tax_type_id": 1,
    "tax_incl": 0,
    "item_type": "product",
    "product_customs": [
      {
        "field_id": 14,
        "value": "p_custom1"
      },
      {
        "field_id": 15,
        "value": "p_custom2"
      }
    ],
    "product_set_customs": [
      {
        "field_id": 17,
        "value": "s_custom1"
      },
      {
        "field_id": 18,
        "value": "s_custom2"
      }
    ],
    "options": [
      {
        "field_id": 3,
        "value": "1"
      }
    ]
  }
}
```

## GET {{api_url}}/api/v1/order_products

**URIパラメータ**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| limit | limit | 整数 |  | 指定した件数分のデータを取得します。指定なしの場合は20件、最大100件 |
| offset | offset | 整数 |  | 指定した値+1件目のデータからlimit分を取得します。指定しない場合は0 |
| ids | ID複数 | 整数 |  | 複数の商品セットIDをカンマ区切りで指定 |
| fields | フィールド | 文字列 |  | 取得したいフィールドカンマ区切りで指定 |
| order_id | 受注ID | 整数 | 11 |  |
| logistics_id | Bカート発送ID（出荷ID） | 整数 | 11 |  |
| product_id | 商品ID | 整数 | 11 |  |
| main_no | 商品管理番号 | 文字列 | 255 |  |
| product_no | 品番 | 文字列 | 255 |  |
| jan_code | JANコード | 文字列 | 255 |  |
| location_no | ローケーション番号 | 文字列 | 255 |  |
| product_set_id | 商品セットID | 文字列 | 11 |  |
| shipping_size | 配送サイズ | 数値 | 11 |  |
| tax_rate | 税率 | 数値 | 255 | 10%は0.10、8%は0.08、0%は0 |
| tax_type_id | 税区分 | 整数 | 1 | 1=標準税率,2=軽減税率,3=非課税 |
| tax_incl | 税込フラグ | 整数 | 1 | 0=税別,1=税込 |
| item_type | 商品区分 | 文字列 | 255 | product,shipping,payment_fees,point |
| product_customs | 商品カスタム項目 | 配列 |  | 配列のキーにfield_id、値にvalue。例) product_customs\[14\]=検索する値 |
| product_set_customs | 商品セットカスタム項目 | 配列 |  | 配列のキーにfield_id、値にvalue。例) product_set_customs\[17\]=検索する値 |

## 拡張パラメータによる高度な絞り込み

拡張パラメータを使用することで、より高度な絞り込みが可能です。

詳しくは、[パラメータ](../docs/04-parameters.md)の「拡張パラメータ」欄をご参照ください。

**レスポンス例（200 OK）:**

```json
{
  "order_products": [
    {
      "id": 2,
      "order_id": 128,
      "logistics_id": 20000000,
      "product_id": 2,
      "main_no": "SF-001",
      "product_no": "SF-001-02-O",
      "jan_code": "1234567891123",
      "location_no": "B3-01",
      "product_name": "クラシックソファー（一人がけ）",
      "product_set_id": 8,
      "set_name": "2個セット カラー：オーク",
      "unit_price": 800,
      "set_quantity": 5,
      "set_unit": "脚",
      "order_pro_count": 2,
      "shipping_size": 0,
      "tax_rate": "0.05",
      "tax_type_id": 1,
      "tax_incl": 0,
      "item_type": "product",
      "product_customs": [
        {
          "field_id": 14,
          "value": "p_custom1"
        },
        {
          "field_id": 15,
          "value": "p_custom2"
        }
      ],
      "product_set_customs": [
        {
          "field_id": 17,
          "value": "s_custom1"
        },
        {
          "field_id": 18,
          "value": "s_custom2"
        }
      ],
      "options": [
        {
          "field_id": 3,
          "value": "1"
        }
      ]
    },
    {
      "id": 3,
      "order_id": 129,
      "logistics_id": 20000000,
      "product_id": 1,
      "main_no": "SF-002",
      "product_no": "SF-002-01-B",
      "jan_code": "",
      "location_no": "",
      "product_name": "クラシックソファー（2人がけ）",
      "product_set_id": 1,
      "set_name": "単品販売 カラー：ブラウン",
      "unit_price": 1200,
      "set_quantity": 12,
      "set_unit": "脚",
      "order_pro_count": 50,
      "shipping_size": 0,
      "tax_rate": "0.05",
      "tax_type_id": 1,
      "tax_incl": 0,
      "item_type": "product",
      "product_customs": null,
      "product_set_customs": null,
      "options": null
    },
    {
      "id": 4,
      "order_id": 129,
      "logistics_id": 20000001,
      "product_id": 3,
      "main_no": "B0001",
      "product_no": "セット品番",
      "jan_code": "",
      "location_no": "",
      "product_name": "絵の具",
      "product_set_id": 8,
      "set_name": "赤色",
      "unit_price": 1000,
      "set_quantity": 50,
      "set_unit": "",
      "order_pro_count": 1,
      "shipping_size": 0,
      "tax_rate": "0.05",
      "tax_type_id": 1,
      "tax_incl": 0,
      "item_type": "product",
      "product_customs": null,
      "product_set_customs": null,
      "options": null
    },
    {
      "id": 5,
      "order_id": 130,
      "logistics_id": 20000002,
      "product_id": 16,
      "main_no": "SF-002",
      "product_no": "",
      "jan_code": "",
      "location_no": "",
      "product_name": "ソファー　ホワイト",
      "product_set_id": 30,
      "set_name": "単品販売",
      "unit_price": 6000,
      "set_quantity": 1,
      "set_unit": "個",
      "order_pro_count": 1,
      "shipping_size": 0,
      "tax_rate": "0.05",
      "tax_type_id": 1,
      "tax_incl": 0,
      "item_type": "product",
      "product_customs": null,
      "product_set_customs": null,
      "options": null
    },
    {
      "id": 7,
      "order_id": 131,
      "logistics_id": 20000003,
      "product_id": 16,
      "main_no": "SF-002",
      "product_no": "",
      "jan_code": "",
      "location_no": "",
      "product_name": "ソファー　ホワイト",
      "product_set_id": 30,
      "set_name": "単品販売",
      "unit_price": 6000,
      "set_quantity": 1,
      "set_unit": "個",
      "order_pro_count": 1,
      "shipping_size": 0,
      "tax_rate": "0.05",
      "tax_type_id": 1,
      "tax_incl": 0,
      "item_type": "product",
      "product_customs": null,
      "product_set_customs": null,
      "options": null
    },
    {
      "id": 9,
      "order_id": 132,
      "logistics_id": 20000004,
      "product_id": 16,
      "main_no": "SF-002",
      "product_no": "",
      "jan_code": "",
      "location_no": "",
      "product_name": "ソファー　ホワイト",
      "product_set_id": 30,
      "set_name": "単品販売",
      "unit_price": 6000,
      "set_quantity": 1,
      "set_unit": "個",
      "order_pro_count": 1,
      "shipping_size": 0,
      "tax_rate": "0.05",
      "tax_type_id": 1,
      "tax_incl": 0,
      "item_type": "product",
      "product_customs": null,
      "product_set_customs": null,
      "options": null
    },
    {
      "id": 10,
      "order_id": 133,
      "logistics_id": 20000005,
      "product_id": 22,
      "main_no": "I00003",
      "product_no": "",
      "jan_code": "",
      "location_no": "",
      "product_name": "兜・置台セット",
      "product_set_id": 41,
      "set_name": "単品販売",
      "unit_price": 6000,
      "set_quantity": 1,
      "set_unit": "個",
      "order_pro_count": 1,
      "shipping_size": 0,
      "tax_rate": "0.05",
      "tax_type_id": 1,
      "tax_incl": 0,
      "item_type": "product",
      "product_customs": null,
      "product_set_customs": null,
      "options": null
    },
    {
      "id": 11,
      "order_id": 133,
      "logistics_id": 20000005,
      "product_id": 19,
      "main_no": "I00001",
      "product_no": "",
      "jan_code": "",
      "location_no": "",
      "product_name": "雛人形セット",
      "product_set_id": 36,
      "set_name": "限定販売：一式セット",
      "unit_price": 29800,
      "set_quantity": 1,
      "set_unit": "セット",
      "order_pro_count": 1,
      "shipping_size": 0,
      "tax_rate": "0.05",
      "tax_type_id": 1,
      "tax_incl": 0,
      "item_type": "product",
      "product_customs": null,
      "product_set_customs": null,
      "options": null
    },
    {
      "id": 13,
      "order_id": 135,
      "logistics_id": 20000006,
      "product_id": 19,
      "main_no": "I00001",
      "product_no": "",
      "jan_code": "",
      "location_no": "",
      "product_name": "雛人形セット",
      "product_set_id": 36,
      "set_name": "限定販売：一式セット",
      "unit_price": 29800,
      "set_quantity": 1,
      "set_unit": "セット",
      "order_pro_count": 1,
      "shipping_size": 0,
      "tax_rate": "0.05",
      "tax_type_id": 1,
      "tax_incl": 0,
      "item_type": "product",
      "product_customs": null,
      "product_set_customs": null,
      "options": null
    },
    {
      "id": 16,
      "order_id": 137,
      "logistics_id": 20000007,
      "product_id": 22,
      "main_no": "I00003",
      "product_no": "",
      "jan_code": "",
      "location_no": "",
      "product_name": "兜・置台セット",
      "product_set_id": 41,
      "set_name": "単品販売",
      "unit_price": 6000,
      "set_quantity": 1,
      "set_unit": "個",
      "order_pro_count": 1,
      "shipping_size": 0,
      "tax_rate": "0.05",
      "tax_type_id": 1,
      "tax_incl": 0,
      "item_type": "product",
      "product_customs": null,
      "product_set_customs": null,
      "options": null
    },
    {
      "id": 17,
      "order_id": 137,
      "logistics_id": 20000007,
      "product_id": 19,
      "main_no": "I00001",
      "product_no": "",
      "jan_code": "",
      "location_no": "",
      "product_name": "雛人形セット",
      "product_set_id": 36,
      "set_name": "限定販売：一式セット",
      "unit_price": 29800,
      "set_quantity": 1,
      "set_unit": "セット",
      "order_pro_count": 1,
      "shipping_size": 0,
      "tax_rate": "0.05",
      "tax_type_id": 1,
      "tax_incl": 0,
      "item_type": "product",
      "product_customs": null,
      "product_set_customs": null,
      "options": null
    },
    {
      "id": 18,
      "order_id": 138,
      "logistics_id": 20000008,
      "product_id": 17,
      "main_no": "SF-003",
      "product_no": "",
      "jan_code": "",
      "location_no": "",
      "product_name": "クラシックソファー（2人がけ）",
      "product_set_id": 32,
      "set_name": "単品販売",
      "unit_price": 20000,
      "set_quantity": 1,
      "set_unit": "",
      "order_pro_count": 1,
      "shipping_size": 0,
      "tax_rate": "0.05",
      "tax_type_id": 1,
      "tax_incl": 0,
      "item_type": "product",
      "product_customs": null,
      "product_set_customs": null,
      "options": null
    },
    {
      "id": 20,
      "order_id": 140,
      "logistics_id": 20000010,
      "product_id": 24,
      "main_no": "n0002",
      "product_no": "",
      "jan_code": "",
      "location_no": "",
      "product_name": "下駄（女性用）",
      "product_set_id": 43,
      "set_name": "単品販売（L）",
      "unit_price": 1500,
      "set_quantity": 1,
      "set_unit": "足",
      "order_pro_count": 4,
      "shipping_size": 0,
      "tax_rate": "0.05",
      "tax_type_id": 1,
      "tax_incl": 0,
      "item_type": "product",
      "product_customs": null,
      "product_set_customs": null,
      "options": null
    },
    {
      "id": 21,
      "order_id": 141,
      "logistics_id": 20000011,
      "product_id": 17,
      "main_no": "SF-003",
      "product_no": "",
      "jan_code": "",
      "location_no": "",
      "product_name": "クラシックソファー（2人がけ）",
      "product_set_id": 33,
      "set_name": "2個セット",
      "unit_price": 19500,
      "set_quantity": 2,
      "set_unit": "",
      "order_pro_count": 10,
      "shipping_size": 0,
      "tax_rate": "0.05",
      "tax_type_id": 1,
      "tax_incl": 0,
      "item_type": "product",
      "product_customs": null,
      "product_set_customs": null,
      "options": null
    },
    {
      "id": 23,
      "order_id": 143,
      "logistics_id": 20000012,
      "product_id": 16,
      "main_no": "SF-002",
      "product_no": "",
      "jan_code": "",
      "location_no": "",
      "product_name": "ソファー　ホワイト",
      "product_set_id": 30,
      "set_name": "単品販売",
      "unit_price": 6000,
      "set_quantity": 1,
      "set_unit": "個",
      "order_pro_count": 4,
      "shipping_size": 0,
      "tax_rate": "0.05",
      "tax_type_id": 1,
      "tax_incl": 0,
      "item_type": "product",
      "product_customs": null,
      "product_set_customs": null,
      "options": null
    },
    {
      "id": 24,
      "order_id": 144,
      "logistics_id": 20000013,
      "product_id": 8,
      "main_no": "",
      "product_no": "SSM-5",
      "jan_code": "",
      "location_no": "",
      "product_name": "芸人獅子舞セット",
      "product_set_id": 19,
      "set_name": "5個セット",
      "unit_price": 4200,
      "set_quantity": 5,
      "set_unit": "個",
      "order_pro_count": 1,
      "shipping_size": 0,
      "tax_rate": "0.05",
      "tax_type_id": 1,
      "tax_incl": 0,
      "item_type": "product",
      "product_customs": null,
      "product_set_customs": null,
      "options": null
    },
    {
      "id": 25,
      "order_id": 145,
      "logistics_id": 20000014,
      "product_id": 15,
      "main_no": "I0004",
      "product_no": "",
      "jan_code": "",
      "location_no": "",
      "product_name": "餅つきセット",
      "product_set_id": 28,
      "set_name": "2個セット",
      "unit_price": 5900,
      "set_quantity": 2,
      "set_unit": "個",
      "order_pro_count": 12,
      "shipping_size": 0,
      "tax_rate": "0.05",
      "tax_type_id": 1,
      "tax_incl": 0,
      "item_type": "product",
      "product_customs": null,
      "product_set_customs": null,
      "options": null
    },
    {
      "id": 26,
      "order_id": 146,
      "logistics_id": 20000015,
      "product_id": 7,
      "main_no": "",
      "product_no": "XM-24",
      "jan_code": "",
      "location_no": "",
      "product_name": "クリスマスツリー",
      "product_set_id": 17,
      "set_name": "24個セット",
      "unit_price": 3200,
      "set_quantity": 24,
      "set_unit": "個",
      "order_pro_count": 1,
      "shipping_size": 0,
      "tax_rate": "0.05",
      "tax_type_id": 1,
      "tax_incl": 0,
      "item_type": "product",
      "product_customs": null,
      "product_set_customs": null,
      "options": null
    },
    {
      "id": 27,
      "order_id": 147,
      "logistics_id": 20000016,
      "product_id": 17,
      "main_no": "SF-003",
      "product_no": "",
      "jan_code": "",
      "location_no": "",
      "product_name": "クラシックソファー（2人がけ）",
      "product_set_id": 33,
      "set_name": "2個セット",
      "unit_price": 19500,
      "set_quantity": 2,
      "set_unit": "",
      "order_pro_count": 3,
      "shipping_size": 0,
      "tax_rate": "0.05",
      "tax_type_id": 1,
      "tax_incl": 0,
      "item_type": "product",
      "product_customs": null,
      "product_set_customs": null,
      "options": null
    },
    {
      "id": 28,
      "order_id": 148,
      "logistics_id": 20000017,
      "product_id": 9,
      "main_no": "C0002",
      "product_no": "TB-6",
      "jan_code": "",
      "location_no": "",
      "product_name": "旅行カバン",
      "product_set_id": 20,
      "set_name": "6個セット",
      "unit_price": 9500,
      "set_quantity": 6,
      "set_unit": "個",
      "order_pro_count": 1,
      "shipping_size": 0,
      "tax_rate": "0.05",
      "tax_type_id": 1,
      "tax_incl": 0,
      "item_type": "product",
      "product_customs": null,
      "product_set_customs": null,
      "options": null
    }
  ],
  "meta": {
    "limit": 20,
    "offset": 0,
    "total": 131
  }
}
```

## PATCH {{api_url}}/api/v1/order_products/2

**リクエストBODY**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| order\_id | 受注ID | 整数 | 11 | 存在するorder\_idを指定 |
| logistics\_id | Bカート発送ID（出荷ID） | 整数 | 11 | 登録されていな商品はnullを指定 |
| product\_id | 商品ID | 整数 | 11 | 登録されていな商品はnullを指定 |
| main\_no | 商品管理番号 | 文字列 | 255 |  |
| product\_no | 品番 | 文字列 | 255 |  |
| jan\_code | JANコード | 文字列 | 255 |  |
| location\_no | ローケーション番号 | 文字列 | 255 |  |
| product\_name | 商品名 | 文字列 | 255 |  |
| product\_set\_id | 商品セットID | 整数/null | 11 | 登録されていな商品セットはnullを指定 |
| set\_name | セット名 | 文字列 | 255 |  |
| set\_unit | 単位 | 文字列 | 255 |  |
| shipping\_size | 配送サイズ | 数値 | 11 |  |
| product\_customs\[{field\_id, value}\] | 商品カスタム項目 | 配列 | 65,535 |  |
| product\_set\_customs\[{field\_id, value}\] | 商品セットカスタム項目 | 配列 | 65,535 |  |

**リクエストボディ例:**

```json
{
  "id": 2,
  "location_no": "C3-01",
  "product_customs": [
    {
      "field_id": 14,
      "value": "p_custom_1"
    },
    {
      "field_id": 15,
      "value": "p_custom_2"
    }
  ],
  "product_set_customs": [
    {
      "field_id": 17,
      "value": "s_custom_1"
    },
    {
      "field_id": 18,
      "value": "s_custom_2"
    }
  ]
}
```

**レスポンス例（200 OK）:**

```json
{
  "order_product": {
    "id": 2,
    "order_id": 128,
    "logistics_id": 20000000,
    "product_id": 2,
    "main_no": "SF-001",
    "product_no": "SF-001-02-O",
    "jan_code": "1234567891123",
    "location_no": "C3-01",
    "product_name": "クラシックソファー（一人がけ）",
    "product_set_id": 8,
    "set_name": "2個セット カラー：オーク",
    "unit_price": 800,
    "set_quantity": 5,
    "set_unit": "脚",
    "order_pro_count": 2,
    "shipping_size": 0,
    "tax_rate": "0.05",
    "tax_type_id": 1,
    "tax_incl": 0,
    "item_type": "product",
    "product_customs": [
      {
        "field_id": 14,
        "value": "p_custom_1"
      },
      {
        "field_id": 15,
        "value": "p_custom_2"
      }
    ],
    "product_set_customs": [
      {
        "field_id": 17,
        "value": "s_custom_1"
      },
      {
        "field_id": 18,
        "value": "s_custom_2"
      }
    ],
    "options": [
      {
        "field_id": 3,
        "value": "1"
      }
    ]
  }
}
```

## PATCH {{api_url}}/api/v1/order_products

**リクエストBODY**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| order\_products\[{{i}}\]\[products\_id\] | 受注商品ID | 文字列 | 255 | 必須 |
| order\_products\[{{i}}\]\[order\_id\] | 受注ID | 文字列 | 11 | 存在するorder\_idを指定 |
| order\_products\[{{i}}\]\[logsitcs\_id\] | Bカート発送ID（出荷ID） | 文字列 | 11 | 存在するlogisits\_idを指定 |
| order\_products\[{{i}}\]\[product\_id\] | 商品ID | 整数 | 11 | 登録されていな商品はnullを指定 |
| order\_products\[{{i}}\]\[main\_no\] | 商品管理番号 | 整数 | 255 |  |
| order\_products\[{{i}}\]\[product\_no\] | 品番 | 整数 | 255 |  |
| order\_products\[{{i}}\]\[jan\_code\] | JANコード | 文字列 | 255 |  |
| order\_products\[{{i}}\]\[location\_no\] | ローケーション番号 | 文字列 | 255 |  |
| order\_products\[{{i}}\]\[product\_name\] | 商品名 | 文字列 | 255 |  |
| order\_products\[{{i}}\]\[product\_set\_id\] | 商品セットID | 整数/null | 11 | 登録されていな商品セットはnullを指定 |
| order\_products\[{{i}}\]\[set\_name\] | セット名 | 文字列 | 255 |  |
| order\_products\[{{i}}\]\[set\_unit\] | 単位 | 文字列 | 255 |  |
| order\_products\[{{i}}\]\[shipping\_size\] | 配送サイズ | 数値 | 11 |  |
| order\_products\[{{i}}\]\[product\_customs\]\[{field\_id, value}\] | 商品カスタム項目 | 配列 | 65,535 |  |
| order\_products\[{{i}}\]\[product\_set\_customs\]\[{field\_id, value}\] | 商品セットカスタム項目 | 配列 | 65,535 |  |

**リクエストボディ例:**

```json
{
  "order_products": [
    {
      "id": 2,
      "location_no": "C3-01"
    },
    {
      "id": 3,
      "location_no": "D1-04",
      "order_pro_count": 2
    }
  ]
}
```

**レスポンス例（200 OK）:**

```json
{
  "order_products": [
    {
      "id": 2,
      "order_id": 128,
      "logistics_id": 20000000,
      "product_id": 2,
      "main_no": "SF-001",
      "product_no": "SF-001-02-O",
      "jan_code": "1234567891123",
      "location_no": "C3-01",
      "product_name": "クラシックソファー（一人がけ）",
      "product_set_id": 8,
      "set_name": "2個セット カラー：オーク",
      "unit_price": 800,
      "set_quantity": 5,
      "set_unit": "脚",
      "order_pro_count": 2,
      "shipping_size": 0,
      "tax_rate": "0.05",
      "tax_type_id": 1,
      "tax_incl": 0,
      "item_type": "product",
      "product_customs": [
        {
          "field_id": 14,
          "value": "p_custom_1"
        },
        {
          "field_id": 15,
          "value": "p_custom_2"
        }
      ],
      "product_set_customs": [
        {
          "field_id": 17,
          "value": "s_custom_1"
        },
        {
          "field_id": 18,
          "value": "s_custom_2"
        }
      ],
      "options": [
        {
          "field_id": 3,
          "value": "1"
        }
      ]
    },
    {
      "id": 3,
      "order_id": 129,
      "logistics_id": 20000000,
      "product_id": 1,
      "main_no": "SF-002",
      "product_no": "SF-002-01-B",
      "jan_code": "",
      "location_no": "D1-04",
      "product_name": "クラシックソファー（2人がけ）",
      "product_set_id": 1,
      "set_name": "単品販売 カラー：ブラウン",
      "unit_price": 1200,
      "set_quantity": 12,
      "set_unit": "脚",
      "order_pro_count": 50,
      "shipping_size": 0,
      "tax_rate": "0.05",
      "tax_type_id": 1,
      "tax_incl": 0,
      "item_type": "product",
      "product_customs": null,
      "product_set_customs": null,
      "options": null
    }
  ]
}
```
