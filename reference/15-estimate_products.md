# 見積商品

見積に含まれる商品

## GET {{api_url}}/api/v1/estimate_products/2

**レスポンス一覧**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| id | 見積商品ID | 整数 | 11 |  |
| estimated_id | 見積ID | 整数 | 11 |  |
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
  "estimate_product": {
    "id": 2,
    "estimate_id": 1,
    "product_id": 41,
    "main_no": "n0019",
    "product_no": "",
    "jan_code": "",
    "location_no": "",
    "product_name": "チェコ製ガラステーブル",
    "product_set_id": 65,
    "set_name": "10点入りセット",
    "unit_price": 25000,
    "set_quantity": 10,
    "set_unit": "点",
    "order_pro_count": 1,
    "shipping_size": 0,
    "tax_rate": "",
    "tax_type_id": 1,
    "tax_incl": 0,
    "item_type": "product",
    "product_customs": null,
    "product_set_customs": null,
    "options": null
  }
}
```

## GET {{api_url}}/api/v1/estimate_products

**URIパラメータ**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| limit | limit | 整数 |  | 指定した件数分のデータを取得します。指定なしの場合は20件、最大100件 |
| offset | offset | 整数 |  | 指定した値+1件目のデータからlimit分を取得します。指定しない場合は0 |
| ids | ID複数 | 整数 |  | 複数の商品セットIDをカンマ区切りで指定 |
| fields | フィールド | 文字列 |  | 取得したいフィールドカンマ区切りで指定 |
| estimate_id | 見積ID | 整数 | 11 |  |
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
  "estimate_products": [
    {
      "id": 1,
      "estimate_id": 1,
      "product_id": 20,
      "main_no": "",
      "product_no": "",
      "jan_code": "",
      "location_no": "",
      "product_name": "コマ※商品詳細の振りスペース活用例",
      "product_set_id": 37,
      "set_name": "10個セット",
      "unit_price": 500,
      "set_quantity": 10,
      "set_unit": "個",
      "order_pro_count": 1,
      "shipping_size": 0,
      "tax_rate": "",
      "tax_type_id": 1,
      "tax_incl": 0,
      "item_type": "product",
      "product_customs": null,
      "product_set_customs": null,
      "options": null
    },
    {
      "id": 2,
      "estimate_id": 1,
      "product_id": 41,
      "main_no": "n0019",
      "product_no": "",
      "jan_code": "",
      "location_no": "",
      "product_name": "チェコ製ガラステーブル",
      "product_set_id": 65,
      "set_name": "10点入りセット",
      "unit_price": 25000,
      "set_quantity": 10,
      "set_unit": "点",
      "order_pro_count": 1,
      "shipping_size": 0,
      "tax_rate": "",
      "tax_type_id": 1,
      "tax_incl": 0,
      "item_type": "product",
      "product_customs": null,
      "product_set_customs": null,
      "options": null
    },
    {
      "id": 3,
      "estimate_id": 1,
      "product_id": 32,
      "main_no": "FN0094",
      "product_no": "",
      "jan_code": "",
      "location_no": "",
      "product_name": "デザイナーズ・ウッドチェア",
      "product_set_id": 56,
      "set_name": "5点入りセット",
      "unit_price": 50000,
      "set_quantity": 5,
      "set_unit": "点",
      "order_pro_count": 10,
      "shipping_size": 0,
      "tax_rate": "",
      "tax_type_id": 1,
      "tax_incl": 0,
      "item_type": "product",
      "product_customs": null,
      "product_set_customs": null,
      "options": null
    },
    {
      "id": 4,
      "estimate_id": 2,
      "product_id": 8,
      "main_no": "",
      "product_no": "SSM-1",
      "jan_code": "",
      "location_no": "",
      "product_name": "芸人獅子舞セット※複数カテゴリ例（全てのカテゴリで表示させています）",
      "product_set_id": 18,
      "set_name": "単品",
      "unit_price": 6800,
      "set_quantity": 1,
      "set_unit": "個",
      "order_pro_count": 2,
      "shipping_size": 0,
      "tax_rate": "0.05",
      "tax_type_id": 1,
      "tax_incl": 0,
      "item_type": "product",
      "product_customs": [
        {
          "field_id": 14,
          "value": "淡水魚です。"
        }
      ],
      "product_set_customs": null,
      "options": null
    },
    {
      "id": 5,
      "estimate_id": 3,
      "product_id": 43,
      "main_no": "n0021",
      "product_no": "",
      "jan_code": "",
      "location_no": "",
      "product_name": "デザイナーズ・オフィス3点セット",
      "product_set_id": 73,
      "set_name": "個人事業主",
      "unit_price": 72000,
      "set_quantity": 1,
      "set_unit": "",
      "order_pro_count": 1,
      "shipping_size": 0,
      "tax_rate": "0.05",
      "tax_type_id": 1,
      "tax_incl": 0,
      "item_type": "product",
      "product_customs": null,
      "product_set_customs": [
        {
          "field_id": 17,
          "value": "aaaaa"
        },
        {
          "field_id": 18,
          "value": "aaaaaaaaaaaaaaaa"
        },
        {
          "field_id": 19,
          "value": "aaaaaaaaaaaaaaaaaaaaaaaa"
        }
      ],
      "options": null
    },
    {
      "id": 6,
      "estimate_id": 4,
      "product_id": 40,
      "main_no": "n0017",
      "product_no": "",
      "jan_code": "",
      "location_no": "",
      "product_name": "天然ウッドテーブル&amp;チェア※複数カテゴリ例（テーブルとチェアカテゴリに表示されています）",
      "product_set_id": 64,
      "set_name": "10点入りセット",
      "unit_price": 160000,
      "set_quantity": 10,
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
      "id": 7,
      "estimate_id": 5,
      "product_id": 25,
      "main_no": "n0004",
      "product_no": "",
      "jan_code": "",
      "location_no": "",
      "product_name": "下駄（男性用）※ネット販売会員向け商品",
      "product_set_id": 46,
      "set_name": "単品販売（M）",
      "unit_price": 1500,
      "set_quantity": 1,
      "set_unit": "足",
      "order_pro_count": 2,
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
      "id": 8,
      "estimate_id": 5,
      "product_id": 24,
      "main_no": "n0002",
      "product_no": "",
      "jan_code": "",
      "location_no": "",
      "product_name": "下駄（女性用）※ネット販売会員向け商品",
      "product_set_id": 44,
      "set_name": "単品販売（M）",
      "unit_price": 1500,
      "set_quantity": 1,
      "set_unit": "足",
      "order_pro_count": 2,
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
      "estimate_id": 6,
      "product_id": 12,
      "main_no": "ABC123",
      "product_no": "TNB-1XP",
      "jan_code": "1.21E+12",
      "location_no": "",
      "product_name": "ノートパソコン※この商品には個別でおすすめ商品を設定しています",
      "product_set_id": 23,
      "set_name": "単品：WINXP HOME付",
      "unit_price": 10000,
      "set_quantity": 1,
      "set_unit": "",
      "order_pro_count": 50,
      "shipping_size": 0,
      "tax_rate": "0.08",
      "tax_type_id": 1,
      "tax_incl": 0,
      "item_type": "product",
      "product_customs": null,
      "product_set_customs": null,
      "options": null
    },
    {
      "id": 10,
      "estimate_id": 7,
      "product_id": 39,
      "main_no": "n0016",
      "product_no": "n0016s0001",
      "jan_code": "",
      "location_no": "",
      "product_name": "4Dウッドチェスト",
      "product_set_id": 63,
      "set_name": "10点入りセット",
      "unit_price": 30000,
      "set_quantity": 10,
      "set_unit": "点",
      "order_pro_count": 20,
      "shipping_size": 0,
      "tax_rate": "0.08",
      "tax_type_id": 1,
      "tax_incl": 0,
      "item_type": "product",
      "product_customs": null,
      "product_set_customs": null,
      "options": null
    },
    {
      "id": 11,
      "estimate_id": 8,
      "product_id": 27,
      "main_no": "n0011",
      "product_no": "n0011s0001",
      "jan_code": "",
      "location_no": "",
      "product_name": "ツイン・チェア",
      "product_set_id": 50,
      "set_name": "1点入りセット",
      "unit_price": 23800,
      "set_quantity": 1,
      "set_unit": "点",
      "order_pro_count": 2,
      "shipping_size": 1,
      "tax_rate": "0.08",
      "tax_type_id": 1,
      "tax_incl": 0,
      "item_type": "product",
      "product_customs": [
        {
          "field_id": 14,
          "value": "【カスタム項目1】自由項目を作れます（生産者と設定中）"
        },
        {
          "field_id": 15,
          "value": "【カスタム項目2】自由項目を作れます（ブランドと設定中）"
        },
        {
          "field_id": 16,
          "value": "【カスタム項目3】自由項目を作れます（カタログ頁と設定中）"
        }
      ],
      "product_set_customs": null,
      "options": null
    },
    {
      "id": 12,
      "estimate_id": 2,
      "product_id": null,
      "main_no": "",
      "product_no": "",
      "jan_code": "",
      "location_no": "",
      "product_name": "送料",
      "product_set_id": null,
      "set_name": "",
      "unit_price": 525,
      "set_quantity": 1,
      "set_unit": "",
      "order_pro_count": 1,
      "shipping_size": 0,
      "tax_rate": "0.05",
      "tax_type_id": 1,
      "tax_incl": 1,
      "item_type": "shipping",
      "product_customs": null,
      "product_set_customs": null,
      "options": null
    },
    {
      "id": 13,
      "estimate_id": 5,
      "product_id": null,
      "main_no": "",
      "product_no": "",
      "jan_code": "",
      "location_no": "",
      "product_name": "送料",
      "product_set_id": null,
      "set_name": "",
      "unit_price": 525,
      "set_quantity": 1,
      "set_unit": "",
      "order_pro_count": 1,
      "shipping_size": 0,
      "tax_rate": "0.05",
      "tax_type_id": 1,
      "tax_incl": 1,
      "item_type": "shipping",
      "product_customs": null,
      "product_set_customs": null,
      "options": null
    },
    {
      "id": 14,
      "estimate_id": 8,
      "product_id": null,
      "main_no": "",
      "product_no": "",
      "jan_code": "",
      "location_no": "",
      "product_name": "送料",
      "product_set_id": null,
      "set_name": "",
      "unit_price": 1000,
      "set_quantity": 1,
      "set_unit": "",
      "order_pro_count": 1,
      "shipping_size": 0,
      "tax_rate": "0.08",
      "tax_type_id": 1,
      "tax_incl": 1,
      "item_type": "shipping",
      "product_customs": null,
      "product_set_customs": null,
      "options": null
    },
    {
      "id": 15,
      "estimate_id": 9,
      "product_id": 61,
      "main_no": "",
      "product_no": "",
      "jan_code": "",
      "location_no": "",
      "product_name": "ビジネスシューズ",
      "product_set_id": 155,
      "set_name": "26cm",
      "unit_price": 4000,
      "set_quantity": 1,
      "set_unit": "",
      "order_pro_count": 1,
      "shipping_size": 0,
      "tax_rate": "0.1",
      "tax_type_id": 1,
      "tax_incl": 0,
      "item_type": "product",
      "product_customs": null,
      "product_set_customs": null,
      "options": null
    },
    {
      "id": 16,
      "estimate_id": 9,
      "product_id": null,
      "main_no": "",
      "product_no": "",
      "jan_code": "",
      "location_no": "",
      "product_name": "送料",
      "product_set_id": null,
      "set_name": "",
      "unit_price": 500,
      "set_quantity": 1,
      "set_unit": "",
      "order_pro_count": 1,
      "shipping_size": 0,
      "tax_rate": "0.1",
      "tax_type_id": 1,
      "tax_incl": 0,
      "item_type": "shipping",
      "product_customs": null,
      "product_set_customs": null,
      "options": null
    },
    {
      "id": 17,
      "estimate_id": 10,
      "product_id": 62,
      "main_no": "",
      "product_no": "",
      "jan_code": "",
      "location_no": "",
      "product_name": "バッグ",
      "product_set_id": 157,
      "set_name": "ブラウン",
      "unit_price": 5100,
      "set_quantity": 1,
      "set_unit": "",
      "order_pro_count": 1,
      "shipping_size": 0,
      "tax_rate": "0.1",
      "tax_type_id": 1,
      "tax_incl": 0,
      "item_type": "product",
      "product_customs": [
        {
          "field_id": 14,
          "value": "カスタム1"
        },
        {
          "field_id": 15,
          "value": "カスタム2"
        },
        {
          "field_id": 20,
          "value": "カスタム4"
        }
      ],
      "product_set_customs": [
        {
          "field_id": 17,
          "value": "カスタム1"
        },
        {
          "field_id": 18,
          "value": "カスタム2"
        },
        {
          "field_id": 19,
          "value": "カスタム3"
        }
      ],
      "options": [
        {
          "field_id": 1,
          "value": "テキスト"
        },
        {
          "field_id": 2,
          "value": "テキストエリア"
        },
        {
          "field_id": 3,
          "value": "1"
        },
        {
          "field_id": 4,
          "value": "有り,無し"
        },
        {
          "field_id": 5,
          "value": "1"
        }
      ]
    },
    {
      "id": 18,
      "estimate_id": 10,
      "product_id": 62,
      "main_no": "",
      "product_no": "",
      "jan_code": "",
      "location_no": "",
      "product_name": "バッグ",
      "product_set_id": 158,
      "set_name": "ブラック",
      "unit_price": 5100,
      "set_quantity": 1,
      "set_unit": "",
      "order_pro_count": 1,
      "shipping_size": 0,
      "tax_rate": "0.1",
      "tax_type_id": 1,
      "tax_incl": 0,
      "item_type": "product",
      "product_customs": [
        {
          "field_id": 14,
          "value": "カスタム1"
        },
        {
          "field_id": 15,
          "value": "カスタム2"
        },
        {
          "field_id": 20,
          "value": "カスタム4"
        }
      ],
      "product_set_customs": null,
      "options": [
        {
          "field_id": 1,
          "value": "テキスト1"
        },
        {
          "field_id": 3,
          "value": "1"
        }
      ]
    },
    {
      "id": 19,
      "estimate_id": 10,
      "product_id": null,
      "main_no": "",
      "product_no": "",
      "jan_code": "",
      "location_no": "",
      "product_name": "送料",
      "product_set_id": null,
      "set_name": "",
      "unit_price": 500,
      "set_quantity": 1,
      "set_unit": "",
      "order_pro_count": 1,
      "shipping_size": 0,
      "tax_rate": "0.1",
      "tax_type_id": 1,
      "tax_incl": 0,
      "item_type": "shipping",
      "product_customs": null,
      "product_set_customs": null,
      "options": null
    }
  ],
  "meta": {
    "limit": 20,
    "offset": 0,
    "total": 19
  }
}
```
