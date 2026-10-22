# 商品セット

商品のセット情報（在庫数や単価など）

## GET {{api_url}}/api/v1/product_sets/1

**レスポンス一覧**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| id | 商品セットID | 整数 | 11 |  |
| product_id | 商品ID | 整数 | 11 |  |
| product_no | 品番 | 文字列 | 255 |  |
| jan_code | JANコード | 文字列 | 255 |  |
| location_no | ロケーション番号 | 文字列 | 255 |  |
| jodai_type | 参考タイプ | 文字列 | 50 | '非表示','オープン','参考上代','メーカー希望小売価格','カタログ価格','カスタム','単価' |
| jodai | 参考上代 | 数値 | 11 |  |
| name | セット名 | 文字列 | 255 |  |
| unit_price | 単価 | 数値 | 11 |  |
| min_order | 最小注文可能数 | 整数 | 8 |  |
| max_order | 最大注文可能数 | 整数 | 8 |  |
| group_price | 会員グループ別価格設定 | 配列 |  | 配列のキー=価格グループID（非会員はn）,name=価格グループ名,rate=掛け率,unit_price=掛け率適用価格,fixed_price=個別価格設定,volume_discount=数量割引（配列のキー=セット数,値=価格） |
| special_price | 特別価格 | 配列 |  | 配列のキー=会員ID,unit_price=価格,volume_discount=数量割引（配列のキー=セット数,値=価格） |
| volume_discount | 数量割引 | 配列 |  | 配列のキー=セット数,値=価格） |
| quantity | 入数 | 整数 | 255 |  |
| unit | 単位 | 文字列 | 255 |  |
| description | セット説明 | 文字列 | 65,535 |  |
| stock | 在庫 | 整数 | 11 |  |
| stock_flag | 在庫フラグ | 整数 | 4 | 0=制限有,1=無制限,100=別品番在庫参照 |
| stock_parent | 参照在庫 | 配列 |  | 配列のキー=商品セットID,値=数量 |
| stock_view_id | 在庫表示パターン | 整数 | 1 | 0〜5。標準は0 |
| stock_few | 在庫わずかになる数量 | 整数 | 1 |  |
| view_group_filter | 非表示フィルタ | 文字列 | 255 | 非会員,通常会員または表示グループIDをカンマ区切り |
| visible_customer_id | 例外的に表示させる会員ID | 文字列 | 65,535 | 会員IDをカンマ区切り |
| hide_customer_id | 商品セットを非表示とする会員ID | 文字列 | 65,535 | 会員IDをカンマ区切り |
| customs | カスタム項目 | 配列 |  |  |
| option_ids | 商品オプションID | 配列 |  |  |
| shipping_group_id | 配送グループID | 整数 | 11 |  |
| shipping_size | 配送サイズ | 数値 | 11 |  |
| priority | 並び順 | 整数 | 4 | \-128〜128 |
| set_flag | フラグ | 文字列 | 3 | ‘表示’,’非表示’ |
| tax_type_id | 税区分 | 整数 | 1 | 1=標準税率,2=軽減税率,3=非課税 |
| allowed_payments | 決済制限 | 配列 |  |  |
| updated_at | 更新日時 | 日付 | 19 | Y-m-d H:i:s |

**レスポンス例（200 OK）:**

```json
{
  "product_set": {
    "id": 1,
    "product_id": 1,
    "product_no": "XXX-1008-AA",
    "jan_code": "xxx",
    "location_no": "",
    "jodai_type": "メーカー希望小売価格",
    "jodai": 25000,
    "name": "単品販売 カラー：ブラウン",
    "unit_price": 20000,
    "min_order": null,
    "max_order": 10,
    "group_price": {
      "1": {
        "name": "リピート会員",
        "rate": "0.9000",
        "unit_price": 12400,
        "fixed_price": 12400,
        "volume_discount": {
          "2": 12000,
          "3": 11000
        }
      },
      "2": {
        "name": "特別会員",
        "rate": "0.7000",
        "unit_price": 4000,
        "fixed_price": 4000,
        "volume_discount": {
          "2": 3600
        }
      },
      "3": {
        "name": "グループ名は自由につけられます",
        "rate": "0.6000",
        "unit_price": 2000,
        "fixed_price": 2000,
        "volume_discount": {
          "5": 1800
        }
      },
      "4": {
        "name": "販売掛率もいつでも変更できます",
        "rate": "0.5500",
        "unit_price": 11000,
        "fixed_price": null,
        "volume_discount": null
      },
      "n": {
        "name": "非会員のお客様",
        "rate": "1.0000",
        "unit_price": 21000,
        "fixed_price": 21000,
        "volume_discount": {
          "5": 18000
        }
      }
    },
    "special_price": {
      "9888": {
        "unit_price": 15000,
        "volume_discount": {
          "5": 14000
        }
      },
      "9999": {
        "unit_price": 17800,
        "volume_discount": {
          "5": 10000,
          "10": 9980
        }
      },
      "10000": {
        "unit_price": 16800,
        "volume_discount": null
      }
    },
    "volume_discount": {
      "2": 14200,
      "5": 13800
    },
    "quantity": 1,
    "unit": "脚",
    "description": "",
    "stock": 8,
    "stock_flag": 0,
    "stock_parent": null,
    "stock_view_id": null,
    "stock_few": 0,
    "view_group_filter": "1,2",
    "visible_customer_id": "10000,5555",
    "hide_customer_id": "10010,10013",
    "customs": [
      {
        "field_id": 17,
        "value": "custom1"
      },
      {
        "field_id": 18,
        "value": "custom2"
      },
      {
        "field_id": 19,
        "value": "custom3"
      }
    ],
    "option_ids": [
      1,
      5
    ],
    "shipping_group_id": 3,
    "shipping_size": 0,
    "priority": 0,
    "set_flag": "表示",
    "tax_type_id": 1,
    "updated_at": "2022-01-26 14:15:51"
  }
}
```

## GET {{api_url_test}}/api/v1/product_sets

**URIパラメータ**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| limit | limit | 整数 |  | 指定した件数分のデータを取得します。指定なしの場合は20件、最大100件 |
| offset | offset | 整数 |  | 指定した値+1件目のデータからlimit分を取得します。指定しない場合は0 |
| ids | ID複数 | 整数 |  | 複数の商品セットIDをカンマ区切りで指定 |
| fields | フィールド | 文字列 |  | 取得したいフィールドカンマ区切りで指定 |
| product_id | 商品ID | 整数 | 11 |  |
| product_no | 品番 | 文字列 | 255 |  |
| jan_code | JANコード | 文字列 | 255 |  |
| location_no | ロケーション番号 | 文字列 | 255 |  |
| jodai_type | 参考タイプ | 文字列 | 50 |  |
| jodai | 参考上代 | 整数 | 11 |  |
| name | セット名 | 文字列 | 255 |  |
| unit_price | 単価 | 整数 | 11 |  |
| min_order | 最小注文可能数 | 整数 | 8 |  |
| max_order | 最大注文可能数 | 整数 | 8 |  |
| quantity | 入数 | 整数 | 255 |  |
| unit | 単位 | 文字列 | 255 |  |
| description | セット説明 | 文字列 | 65,535 |  |
| stock | 在庫 | 整数 | 11 |  |
| stock_flag | 在庫フラグ | 整数 | 4 |  |
| stock_view_id | 在庫表示パターン | 整数 | 1 |  |
| view_group_filter | 非表示フィルタ | 配列 | 255 |  |
| customs | カスタム項目 | 配列 |  | 配列のキーにfield_id、値にvalue。例) customs\[17\]=検索する値 |
| shipping_group_id | 配送グループID | 整数 | 255 |  |
| priority | 並び順 | 整数 | 4 |  |
| set_flag | フラグ | 文字列 | 3 |  |
| tax_type_id | 税区分 | 整数 | 1 | 1=標準税率,2=軽減税率,3=非課税 |
| updated_at | 更新日時 | 日付 | 19 | Y-m-d |
| updated_at_min | 更新日〜 | 日付 | 19 | Y-m-d H:i:s　指定日時以降 |
| updated_at_max | 〜更新日 | 日付 | 19 | Y-m-d H:i:s　指定日時以前 |

## 拡張パラメータによる高度な絞り込み

拡張パラメータを使用することで、より高度な絞り込みが可能です。

詳しくは、[パラメータ](../docs/04-parameters.md)の「拡張パラメータ」欄をご参照ください。

**レスポンス例（200 OK）:**

```json
{
  "product_sets": [
    {
      "id": 1,
      "product_id": 1,
      "product_no": "XXX-1008-AA",
      "jan_code": "xxx",
      "location_no": "",
      "jodai_type": "メーカー希望小売価格",
      "jodai": 25000,
      "name": "単品販売 カラー：ブラウン",
      "unit_price": 20000,
      "min_order": null,
      "max_order": 10,
      "group_price": {
        "1": {
          "name": "リピート会員",
          "rate": "0.9000",
          "unit_price": 12400,
          "fixed_price": 12400,
          "volume_discount": {
            "2": 12000,
            "3": 11000
          }
        },
        "2": {
          "name": "特別会員",
          "rate": "0.7000",
          "unit_price": 4000,
          "fixed_price": 4000,
          "volume_discount": {
            "2": 3600
          }
        },
        "3": {
          "name": "グループ名は自由につけられます",
          "rate": "0.6000",
          "unit_price": 2000,
          "fixed_price": 2000,
          "volume_discount": {
            "5": 1800
          }
        },
        "4": {
          "name": "販売掛率もいつでも変更できます",
          "rate": "0.5500",
          "unit_price": 11000,
          "fixed_price": null,
          "volume_discount": null
        },
        "n": {
          "name": "非会員のお客様",
          "rate": "1.0000",
          "unit_price": 21000,
          "fixed_price": 21000,
          "volume_discount": {
            "5": 18000
          }
        }
      },
      "special_price": {
        "9888": {
          "unit_price": 15000,
          "volume_discount": {
            "5": 14000
          }
        },
        "9999": {
          "unit_price": 17800,
          "volume_discount": {
            "5": 10000,
            "10": 9980
          }
        },
        "10000": {
          "unit_price": 16800,
          "volume_discount": null
        }
      },
      "volume_discount": {
        "2": 14200,
        "5": 13800
      },
      "quantity": 1,
      "unit": "脚",
      "description": "",
      "stock": 8,
      "stock_flag": 0,
      "stock_parent": null,
      "stock_view_id": null,
      "stock_few": 0,
      "view_group_filter": "1,2",
      "visible_customer_id": "10000,5555",
      "hide_customer_id": "10010,10013",
      "customs": [
        {
          "field_id": 17,
          "value": "custom1"
        },
        {
          "field_id": 18,
          "value": "custom2"
        },
        {
          "field_id": 19,
          "value": "custom3"
        }
      ],
      "option_ids": null,
      "shipping_group_id": 3,
      "shipping_size": 0,
      "priority": 0,
      "set_flag": "表示",
      "tax_type_id": 1,
      "updated_at": "2022-01-26 14:15:51"
    },
    {
      "id": 2,
      "product_id": 1,
      "product_no": "DUMMY2",
      "jan_code": "xxx",
      "location_no": "",
      "jodai_type": "メーカー希望小売価格",
      "jodai": 25000,
      "name": "単品販売 カラー：ブラウン2",
      "unit_price": 22000,
      "min_order": null,
      "max_order": 10,
      "group_price": {
        "1": {
          "name": "リピート会員",
          "rate": "0.9000",
          "unit_price": 12800,
          "fixed_price": 12800,
          "volume_discount": {
            "2": 12000,
            "3": 11000
          }
        },
        "2": {
          "name": "特別会員",
          "rate": "0.7000",
          "unit_price": 4000,
          "fixed_price": 4000,
          "volume_discount": {
            "2": 3600
          }
        },
        "3": {
          "name": "グループ名は自由につけられます",
          "rate": "0.6000",
          "unit_price": 2000,
          "fixed_price": 2000,
          "volume_discount": {
            "5": 1800
          }
        },
        "4": {
          "name": "販売掛率もいつでも変更できます",
          "rate": "0.5500",
          "unit_price": 12100.000000000002,
          "fixed_price": null,
          "volume_discount": null
        },
        "n": {
          "name": "非会員のお客様",
          "rate": "1.0000",
          "unit_price": 21000,
          "fixed_price": 21000,
          "volume_discount": {
            "5": 18000
          }
        }
      },
      "special_price": {
        "9888": {
          "unit_price": 15000,
          "volume_discount": {
            "5": 14000
          }
        },
        "9999": {
          "unit_price": 17800,
          "volume_discount": {
            "5": 10000,
            "10": 9980
          }
        },
        "10000": {
          "unit_price": 16800,
          "volume_discount": null
        }
      },
      "volume_discount": {
        "2": 14200,
        "5": 13800
      },
      "quantity": 1,
      "unit": "脚",
      "description": "",
      "stock": null,
      "stock_flag": 1,
      "stock_parent": null,
      "stock_view_id": 1,
      "stock_few": 0,
      "view_group_filter": null,
      "visible_customer_id": "5555",
      "hide_customer_id": "10010",
      "customs": [
        {
          "field_id": 17,
          "value": "カスタム1"
        },
        {
          "field_id": 19,
          "value": "カスタム3"
        }
      ],
      "option_ids": [
        1,
        5
      ],
      "shipping_group_id": 3,
      "shipping_size": 0,
      "priority": 0,
      "set_flag": "表示",
      "tax_type_id": 1,
      "updated_at": "2022-01-26 14:15:48"
    },
    {
      "id": 3,
      "product_id": 2,
      "product_no": "AK-S",
      "jan_code": "",
      "location_no": "",
      "jodai_type": "参考上代",
      "jodai": 5000,
      "name": "アタッシュケース【Sサイズ】",
      "unit_price": 1000,
      "min_order": null,
      "max_order": null,
      "group_price": {
        "1": {
          "name": "リピート会員",
          "rate": "0.9000",
          "unit_price": 1000,
          "fixed_price": 1000,
          "volume_discount": null
        },
        "2": {
          "name": "特別会員",
          "rate": "0.7000",
          "unit_price": 1000,
          "fixed_price": 1000,
          "volume_discount": null
        },
        "3": {
          "name": "グループ名は自由につけられます",
          "rate": "0.6000",
          "unit_price": 1000,
          "fixed_price": 1000,
          "volume_discount": null
        },
        "4": {
          "name": "販売掛率もいつでも変更できます",
          "rate": "0.5500",
          "unit_price": 550,
          "fixed_price": null,
          "volume_discount": null
        },
        "n": {
          "name": "非会員のお客様",
          "rate": "1.0000",
          "unit_price": 1000,
          "fixed_price": null,
          "volume_discount": null
        }
      },
      "special_price": null,
      "volume_discount": null,
      "quantity": 1,
      "unit": "点",
      "description": "",
      "stock": 0,
      "stock_flag": 0,
      "stock_parent": null,
      "stock_view_id": 1,
      "stock_few": 0,
      "view_group_filter": null,
      "visible_customer_id": null,
      "hide_customer_id": "10010",
      "customs": null,
      "option_ids": null,
      "shipping_group_id": 1,
      "shipping_size": 0,
      "priority": 7,
      "set_flag": "表示",
      "tax_type_id": 1,
      "updated_at": null
    },
    {
      "id": 4,
      "product_id": 3,
      "product_no": "B0001s0001",
      "jan_code": "",
      "location_no": "",
      "jodai_type": "参考上代",
      "jodai": 100,
      "name": "セット品番",
      "unit_price": 50,
      "min_order": null,
      "max_order": null,
      "group_price": {
        "1": {
          "name": "リピート会員",
          "rate": "0.9000",
          "unit_price": 40,
          "fixed_price": 40,
          "volume_discount": null
        },
        "2": {
          "name": "特別会員",
          "rate": "0.7000",
          "unit_price": 38,
          "fixed_price": 38,
          "volume_discount": null
        },
        "3": {
          "name": "グループ名は自由につけられます",
          "rate": "0.6000",
          "unit_price": 35,
          "fixed_price": 35,
          "volume_discount": null
        },
        "4": {
          "name": "販売掛率もいつでも変更できます",
          "rate": "0.5500",
          "unit_price": 27.500000000000004,
          "fixed_price": null,
          "volume_discount": null
        },
        "n": {
          "name": "非会員のお客様",
          "rate": "1.0000",
          "unit_price": 50,
          "fixed_price": null,
          "volume_discount": null
        }
      },
      "special_price": null,
      "volume_discount": null,
      "quantity": 1,
      "unit": "点",
      "description": "",
      "stock": 83,
      "stock_flag": 0,
      "stock_parent": null,
      "stock_view_id": 1,
      "stock_few": 0,
      "view_group_filter": null,
      "visible_customer_id": null,
      "hide_customer_id": null,
      "customs": null,
      "option_ids": null,
      "shipping_group_id": 1,
      "shipping_size": 0,
      "priority": 8,
      "set_flag": "表示",
      "tax_type_id": 1,
      "updated_at": null
    },
    {
      "id": 5,
      "product_id": 3,
      "product_no": "B0001s0002",
      "jan_code": "",
      "location_no": "",
      "jodai_type": "参考上代",
      "jodai": 100,
      "name": "青色",
      "unit_price": 50,
      "min_order": null,
      "max_order": null,
      "group_price": {
        "1": {
          "name": "リピート会員",
          "rate": "0.9000",
          "unit_price": 50,
          "fixed_price": 50,
          "volume_discount": null
        },
        "2": {
          "name": "特別会員",
          "rate": "0.7000",
          "unit_price": 50,
          "fixed_price": 50,
          "volume_discount": null
        },
        "3": {
          "name": "グループ名は自由につけられます",
          "rate": "0.6000",
          "unit_price": 50,
          "fixed_price": 50,
          "volume_discount": null
        },
        "4": {
          "name": "販売掛率もいつでも変更できます",
          "rate": "0.5500",
          "unit_price": 27.500000000000004,
          "fixed_price": null,
          "volume_discount": null
        },
        "n": {
          "name": "非会員のお客様",
          "rate": "1.0000",
          "unit_price": 50,
          "fixed_price": null,
          "volume_discount": null
        }
      },
      "special_price": null,
      "volume_discount": null,
      "quantity": 1,
      "unit": "点",
      "description": "",
      "stock": 101,
      "stock_flag": 0,
      "stock_parent": null,
      "stock_view_id": 1,
      "stock_few": 0,
      "view_group_filter": null,
      "visible_customer_id": null,
      "hide_customer_id": null,
      "customs": null,
      "option_ids": null,
      "shipping_group_id": 1,
      "shipping_size": 0,
      "priority": 9,
      "set_flag": "表示",
      "tax_type_id": 1,
      "updated_at": null
    },
    {
      "id": 6,
      "product_id": 3,
      "product_no": "B0001s0003",
      "jan_code": "",
      "location_no": "",
      "jodai_type": "参考上代",
      "jodai": 100,
      "name": "黄色",
      "unit_price": 50,
      "min_order": null,
      "max_order": null,
      "group_price": {
        "1": {
          "name": "リピート会員",
          "rate": "0.9000",
          "unit_price": 50,
          "fixed_price": 50,
          "volume_discount": null
        },
        "2": {
          "name": "特別会員",
          "rate": "0.7000",
          "unit_price": 50,
          "fixed_price": 50,
          "volume_discount": null
        },
        "3": {
          "name": "グループ名は自由につけられます",
          "rate": "0.6000",
          "unit_price": 50,
          "fixed_price": 50,
          "volume_discount": null
        },
        "4": {
          "name": "販売掛率もいつでも変更できます",
          "rate": "0.5500",
          "unit_price": 27.500000000000004,
          "fixed_price": null,
          "volume_discount": null
        },
        "n": {
          "name": "非会員のお客様",
          "rate": "1.0000",
          "unit_price": 50,
          "fixed_price": null,
          "volume_discount": null
        }
      },
      "special_price": null,
      "volume_discount": null,
      "quantity": 1,
      "unit": "点",
      "description": "",
      "stock": 1,
      "stock_flag": 1,
      "stock_parent": null,
      "stock_view_id": 1,
      "stock_few": 0,
      "view_group_filter": null,
      "visible_customer_id": null,
      "hide_customer_id": null,
      "customs": null,
      "option_ids": null,
      "shipping_group_id": 1,
      "shipping_size": 0,
      "priority": 10,
      "set_flag": "表示",
      "tax_type_id": 1,
      "updated_at": null
    },
    {
      "id": 7,
      "product_id": 3,
      "product_no": "B0001s0004",
      "jan_code": "",
      "location_no": "",
      "jodai_type": "参考上代",
      "jodai": 100,
      "name": "３色",
      "unit_price": 45,
      "min_order": null,
      "max_order": null,
      "group_price": {
        "1": {
          "name": "リピート会員",
          "rate": "0.9000",
          "unit_price": 45,
          "fixed_price": 45,
          "volume_discount": null
        },
        "2": {
          "name": "特別会員",
          "rate": "0.7000",
          "unit_price": 45,
          "fixed_price": 45,
          "volume_discount": null
        },
        "3": {
          "name": "グループ名は自由につけられます",
          "rate": "0.6000",
          "unit_price": 45,
          "fixed_price": 45,
          "volume_discount": null
        },
        "4": {
          "name": "販売掛率もいつでも変更できます",
          "rate": "0.5500",
          "unit_price": 24.750000000000004,
          "fixed_price": null,
          "volume_discount": null
        },
        "n": {
          "name": "非会員のお客様",
          "rate": "1.0000",
          "unit_price": 45,
          "fixed_price": null,
          "volume_discount": null
        }
      },
      "special_price": null,
      "volume_discount": null,
      "quantity": 3,
      "unit": "点",
      "description": "",
      "stock": 41,
      "stock_flag": 100,
      "stock_parent": {
        "4": 2,
        "5": 2,
        "6": 2
      },
      "stock_view_id": 1,
      "stock_few": 0,
      "view_group_filter": null,
      "visible_customer_id": null,
      "hide_customer_id": null,
      "customs": null,
      "option_ids": null,
      "shipping_group_id": 1,
      "shipping_size": 0,
      "priority": 11,
      "set_flag": "表示",
      "tax_type_id": 1,
      "updated_at": "2022-01-26 14:15:50"
    },
    {
      "id": 8,
      "product_id": 3,
      "product_no": "B0001s0005",
      "jan_code": "",
      "location_no": "",
      "jodai_type": "参考上代",
      "jodai": 100,
      "name": "赤色",
      "unit_price": 1000,
      "min_order": null,
      "max_order": null,
      "group_price": {
        "1": {
          "name": "リピート会員",
          "rate": "0.9000",
          "unit_price": 1000,
          "fixed_price": 1000,
          "volume_discount": null
        },
        "2": {
          "name": "特別会員",
          "rate": "0.7000",
          "unit_price": 1000,
          "fixed_price": 1000,
          "volume_discount": null
        },
        "3": {
          "name": "グループ名は自由につけられます",
          "rate": "0.6000",
          "unit_price": 1000,
          "fixed_price": 1000,
          "volume_discount": null
        },
        "4": {
          "name": "販売掛率もいつでも変更できます",
          "rate": "0.5500",
          "unit_price": 550,
          "fixed_price": null,
          "volume_discount": null
        },
        "n": {
          "name": "非会員のお客様",
          "rate": "1.0000",
          "unit_price": 1000,
          "fixed_price": null,
          "volume_discount": null
        }
      },
      "special_price": null,
      "volume_discount": null,
      "quantity": 50,
      "unit": "",
      "description": "",
      "stock": 10,
      "stock_flag": 0,
      "stock_parent": null,
      "stock_view_id": 1,
      "stock_few": 0,
      "view_group_filter": null,
      "visible_customer_id": null,
      "hide_customer_id": null,
      "customs": null,
      "option_ids": null,
      "shipping_group_id": 1,
      "shipping_size": 0,
      "priority": 12,
      "set_flag": "表示",
      "tax_type_id": 1,
      "updated_at": null
    },
    {
      "id": 9,
      "product_id": 4,
      "product_no": "KB-A1",
      "jan_code": "",
      "location_no": "",
      "jodai_type": "オープン",
      "jodai": null,
      "name": "1個販売",
      "unit_price": 880,
      "min_order": null,
      "max_order": null,
      "group_price": {
        "1": {
          "name": "リピート会員",
          "rate": "0.9000",
          "unit_price": 880,
          "fixed_price": 880,
          "volume_discount": null
        },
        "2": {
          "name": "特別会員",
          "rate": "0.7000",
          "unit_price": 880,
          "fixed_price": 880,
          "volume_discount": null
        },
        "3": {
          "name": "グループ名は自由につけられます",
          "rate": "0.6000",
          "unit_price": 880,
          "fixed_price": 880,
          "volume_discount": null
        },
        "4": {
          "name": "販売掛率もいつでも変更できます",
          "rate": "0.5500",
          "unit_price": 484.00000000000006,
          "fixed_price": null,
          "volume_discount": null
        },
        "n": {
          "name": "非会員のお客様",
          "rate": "1.0000",
          "unit_price": 880,
          "fixed_price": null,
          "volume_discount": null
        }
      },
      "special_price": null,
      "volume_discount": null,
      "quantity": 1,
      "unit": "個",
      "description": "",
      "stock": 45,
      "stock_flag": 0,
      "stock_parent": null,
      "stock_view_id": 1,
      "stock_few": 0,
      "view_group_filter": null,
      "visible_customer_id": null,
      "hide_customer_id": null,
      "customs": null,
      "option_ids": null,
      "shipping_group_id": 1,
      "shipping_size": 0,
      "priority": 15,
      "set_flag": "表示",
      "tax_type_id": 1,
      "updated_at": "2022-01-26 14:15:51"
    },
    {
      "id": 10,
      "product_id": 4,
      "product_no": "KB-A50",
      "jan_code": "",
      "location_no": "",
      "jodai_type": "オープン",
      "jodai": null,
      "name": "50個販売",
      "unit_price": 600,
      "min_order": null,
      "max_order": null,
      "group_price": {
        "1": {
          "name": "リピート会員",
          "rate": "0.9000",
          "unit_price": 800,
          "fixed_price": 800,
          "volume_discount": null
        },
        "2": {
          "name": "特別会員",
          "rate": "0.7000",
          "unit_price": 800,
          "fixed_price": 800,
          "volume_discount": null
        },
        "3": {
          "name": "グループ名は自由につけられます",
          "rate": "0.6000",
          "unit_price": 800,
          "fixed_price": 800,
          "volume_discount": null
        },
        "4": {
          "name": "販売掛率もいつでも変更できます",
          "rate": "0.5500",
          "unit_price": 330,
          "fixed_price": null,
          "volume_discount": null
        },
        "n": {
          "name": "非会員のお客様",
          "rate": "1.0000",
          "unit_price": 600,
          "fixed_price": null,
          "volume_discount": null
        }
      },
      "special_price": null,
      "volume_discount": null,
      "quantity": 1,
      "unit": "個",
      "description": "",
      "stock": 0,
      "stock_flag": 100,
      "stock_parent": {
        "9": 50
      },
      "stock_view_id": 1,
      "stock_few": 0,
      "view_group_filter": null,
      "visible_customer_id": null,
      "hide_customer_id": null,
      "customs": null,
      "option_ids": null,
      "shipping_group_id": 1,
      "shipping_size": 0,
      "priority": 10,
      "set_flag": "表示",
      "tax_type_id": 1,
      "updated_at": null
    },
    {
      "id": 11,
      "product_id": 5,
      "product_no": "MT12",
      "jan_code": "",
      "location_no": "",
      "jodai_type": "参考上代",
      "jodai": 3500,
      "name": "マジック用　トランプ　1ダースセット",
      "unit_price": 980,
      "min_order": null,
      "max_order": null,
      "group_price": {
        "1": {
          "name": "リピート会員",
          "rate": "0.9000",
          "unit_price": 980,
          "fixed_price": 980,
          "volume_discount": null
        },
        "2": {
          "name": "特別会員",
          "rate": "0.7000",
          "unit_price": 980,
          "fixed_price": 980,
          "volume_discount": null
        },
        "3": {
          "name": "グループ名は自由につけられます",
          "rate": "0.6000",
          "unit_price": 980,
          "fixed_price": 980,
          "volume_discount": null
        },
        "4": {
          "name": "販売掛率もいつでも変更できます",
          "rate": "0.5500",
          "unit_price": 539,
          "fixed_price": null,
          "volume_discount": null
        },
        "n": {
          "name": "非会員のお客様",
          "rate": "1.0000",
          "unit_price": 980,
          "fixed_price": null,
          "volume_discount": null
        }
      },
      "special_price": null,
      "volume_discount": null,
      "quantity": 12,
      "unit": "個",
      "description": "",
      "stock": 1,
      "stock_flag": 1,
      "stock_parent": null,
      "stock_view_id": 1,
      "stock_few": 0,
      "view_group_filter": null,
      "visible_customer_id": null,
      "hide_customer_id": null,
      "customs": null,
      "option_ids": null,
      "shipping_group_id": 1,
      "shipping_size": 0,
      "priority": 15,
      "set_flag": "表示",
      "tax_type_id": 1,
      "updated_at": null
    },
    {
      "id": 12,
      "product_id": 6,
      "product_no": "KBT-1",
      "jan_code": "",
      "location_no": "",
      "jodai_type": "参考上代",
      "jodai": 2800,
      "name": "単品",
      "unit_price": 1880,
      "min_order": null,
      "max_order": null,
      "group_price": {
        "1": {
          "name": "リピート会員",
          "rate": "0.9000",
          "unit_price": 1880,
          "fixed_price": 1880,
          "volume_discount": null
        },
        "2": {
          "name": "特別会員",
          "rate": "0.7000",
          "unit_price": 1880,
          "fixed_price": 1880,
          "volume_discount": null
        },
        "3": {
          "name": "グループ名は自由につけられます",
          "rate": "0.6000",
          "unit_price": 1880,
          "fixed_price": 1880,
          "volume_discount": null
        },
        "4": {
          "name": "販売掛率もいつでも変更できます",
          "rate": "0.5500",
          "unit_price": 1034,
          "fixed_price": null,
          "volume_discount": null
        },
        "n": {
          "name": "非会員のお客様",
          "rate": "1.0000",
          "unit_price": 1880,
          "fixed_price": null,
          "volume_discount": null
        }
      },
      "special_price": null,
      "volume_discount": null,
      "quantity": 1,
      "unit": "個",
      "description": "",
      "stock": 50,
      "stock_flag": 1,
      "stock_parent": null,
      "stock_view_id": 1,
      "stock_few": 0,
      "view_group_filter": null,
      "visible_customer_id": null,
      "hide_customer_id": null,
      "customs": null,
      "option_ids": null,
      "shipping_group_id": 1,
      "shipping_size": 0,
      "priority": 16,
      "set_flag": "表示",
      "tax_type_id": 1,
      "updated_at": null
    },
    {
      "id": 13,
      "product_id": 6,
      "product_no": "KBT-12",
      "jan_code": "",
      "location_no": "",
      "jodai_type": "参考上代",
      "jodai": 2800,
      "name": "1ダース",
      "unit_price": 1200,
      "min_order": null,
      "max_order": null,
      "group_price": {
        "1": {
          "name": "リピート会員",
          "rate": "0.9000",
          "unit_price": 1200,
          "fixed_price": 1200,
          "volume_discount": null
        },
        "2": {
          "name": "特別会員",
          "rate": "0.7000",
          "unit_price": 1200,
          "fixed_price": 1200,
          "volume_discount": null
        },
        "3": {
          "name": "グループ名は自由につけられます",
          "rate": "0.6000",
          "unit_price": 1200,
          "fixed_price": 1200,
          "volume_discount": null
        },
        "4": {
          "name": "販売掛率もいつでも変更できます",
          "rate": "0.5500",
          "unit_price": 660,
          "fixed_price": null,
          "volume_discount": null
        },
        "n": {
          "name": "非会員のお客様",
          "rate": "1.0000",
          "unit_price": 1200,
          "fixed_price": null,
          "volume_discount": null
        }
      },
      "special_price": null,
      "volume_discount": null,
      "quantity": 12,
      "unit": "個",
      "description": "",
      "stock": 49,
      "stock_flag": 1,
      "stock_parent": null,
      "stock_view_id": 1,
      "stock_few": 0,
      "view_group_filter": null,
      "visible_customer_id": null,
      "hide_customer_id": null,
      "customs": null,
      "option_ids": null,
      "shipping_group_id": 1,
      "shipping_size": 0,
      "priority": 17,
      "set_flag": "表示",
      "tax_type_id": 1,
      "updated_at": null
    },
    {
      "id": 14,
      "product_id": 6,
      "product_no": "KBT-50",
      "jan_code": "",
      "location_no": "",
      "jodai_type": "参考上代",
      "jodai": 2800,
      "name": "50個セット",
      "unit_price": 880,
      "min_order": null,
      "max_order": null,
      "group_price": {
        "1": {
          "name": "リピート会員",
          "rate": "0.9000",
          "unit_price": 880,
          "fixed_price": 880,
          "volume_discount": null
        },
        "2": {
          "name": "特別会員",
          "rate": "0.7000",
          "unit_price": 880,
          "fixed_price": 880,
          "volume_discount": null
        },
        "3": {
          "name": "グループ名は自由につけられます",
          "rate": "0.6000",
          "unit_price": 880,
          "fixed_price": 880,
          "volume_discount": null
        },
        "4": {
          "name": "販売掛率もいつでも変更できます",
          "rate": "0.5500",
          "unit_price": 484.00000000000006,
          "fixed_price": null,
          "volume_discount": null
        },
        "n": {
          "name": "非会員のお客様",
          "rate": "1.0000",
          "unit_price": 880,
          "fixed_price": null,
          "volume_discount": null
        }
      },
      "special_price": null,
      "volume_discount": null,
      "quantity": 50,
      "unit": "",
      "description": "",
      "stock": 3,
      "stock_flag": 0,
      "stock_parent": null,
      "stock_view_id": 1,
      "stock_few": 0,
      "view_group_filter": null,
      "visible_customer_id": null,
      "hide_customer_id": null,
      "customs": null,
      "option_ids": null,
      "shipping_group_id": 1,
      "shipping_size": 0,
      "priority": 18,
      "set_flag": "表示",
      "tax_type_id": 1,
      "updated_at": null
    },
    {
      "id": 15,
      "product_id": 7,
      "product_no": "XM-1",
      "jan_code": "",
      "location_no": "",
      "jodai_type": "オープン",
      "jodai": 1000,
      "name": "単品",
      "unit_price": 4800,
      "min_order": null,
      "max_order": null,
      "group_price": {
        "1": {
          "name": "リピート会員",
          "rate": "0.9000",
          "unit_price": 4800,
          "fixed_price": 4800,
          "volume_discount": null
        },
        "2": {
          "name": "特別会員",
          "rate": "0.7000",
          "unit_price": 4800,
          "fixed_price": 4800,
          "volume_discount": null
        },
        "3": {
          "name": "グループ名は自由につけられます",
          "rate": "0.6000",
          "unit_price": 4800,
          "fixed_price": 4800,
          "volume_discount": null
        },
        "4": {
          "name": "販売掛率もいつでも変更できます",
          "rate": "0.5500",
          "unit_price": 2640,
          "fixed_price": null,
          "volume_discount": null
        },
        "n": {
          "name": "非会員のお客様",
          "rate": "1.0000",
          "unit_price": 4800,
          "fixed_price": null,
          "volume_discount": null
        }
      },
      "special_price": null,
      "volume_discount": null,
      "quantity": 1,
      "unit": "個",
      "description": "",
      "stock": 101,
      "stock_flag": 1,
      "stock_parent": null,
      "stock_view_id": 1,
      "stock_few": 0,
      "view_group_filter": null,
      "visible_customer_id": null,
      "hide_customer_id": null,
      "customs": null,
      "option_ids": null,
      "shipping_group_id": 1,
      "shipping_size": 0,
      "priority": 19,
      "set_flag": "表示",
      "tax_type_id": 1,
      "updated_at": null
    },
    {
      "id": 16,
      "product_id": 7,
      "product_no": "XM-5",
      "jan_code": "",
      "location_no": "",
      "jodai_type": "オープン",
      "jodai": 1000,
      "name": "5個セット",
      "unit_price": 3800,
      "min_order": null,
      "max_order": null,
      "group_price": {
        "1": {
          "name": "リピート会員",
          "rate": "0.9000",
          "unit_price": 3800,
          "fixed_price": 3800,
          "volume_discount": null
        },
        "2": {
          "name": "特別会員",
          "rate": "0.7000",
          "unit_price": 3800,
          "fixed_price": 3800,
          "volume_discount": null
        },
        "3": {
          "name": "グループ名は自由につけられます",
          "rate": "0.6000",
          "unit_price": 3800,
          "fixed_price": 3800,
          "volume_discount": null
        },
        "4": {
          "name": "販売掛率もいつでも変更できます",
          "rate": "0.5500",
          "unit_price": 2090,
          "fixed_price": null,
          "volume_discount": null
        },
        "n": {
          "name": "非会員のお客様",
          "rate": "1.0000",
          "unit_price": 3800,
          "fixed_price": null,
          "volume_discount": null
        }
      },
      "special_price": null,
      "volume_discount": null,
      "quantity": 5,
      "unit": "個",
      "description": "",
      "stock": 50,
      "stock_flag": 0,
      "stock_parent": null,
      "stock_view_id": 1,
      "stock_few": 0,
      "view_group_filter": null,
      "visible_customer_id": null,
      "hide_customer_id": null,
      "customs": null,
      "option_ids": null,
      "shipping_group_id": 1,
      "shipping_size": 0,
      "priority": 20,
      "set_flag": "表示",
      "tax_type_id": 1,
      "updated_at": "2022-01-26 14:15:51"
    },
    {
      "id": 17,
      "product_id": 7,
      "product_no": "XM-24",
      "jan_code": "",
      "location_no": "",
      "jodai_type": "オープン",
      "jodai": 1000,
      "name": "24個セット",
      "unit_price": 3200,
      "min_order": null,
      "max_order": null,
      "group_price": {
        "1": {
          "name": "リピート会員",
          "rate": "0.9000",
          "unit_price": 3200,
          "fixed_price": 3200,
          "volume_discount": null
        },
        "2": {
          "name": "特別会員",
          "rate": "0.7000",
          "unit_price": 3200,
          "fixed_price": 3200,
          "volume_discount": null
        },
        "3": {
          "name": "グループ名は自由につけられます",
          "rate": "0.6000",
          "unit_price": 3200,
          "fixed_price": 3200,
          "volume_discount": null
        },
        "4": {
          "name": "販売掛率もいつでも変更できます",
          "rate": "0.5500",
          "unit_price": 1760.0000000000002,
          "fixed_price": null,
          "volume_discount": null
        },
        "n": {
          "name": "非会員のお客様",
          "rate": "1.0000",
          "unit_price": 3200,
          "fixed_price": null,
          "volume_discount": null
        }
      },
      "special_price": null,
      "volume_discount": null,
      "quantity": 24,
      "unit": "個",
      "description": "",
      "stock": 1,
      "stock_flag": 0,
      "stock_parent": null,
      "stock_view_id": 1,
      "stock_few": 0,
      "view_group_filter": null,
      "visible_customer_id": null,
      "hide_customer_id": null,
      "customs": null,
      "option_ids": null,
      "shipping_group_id": 1,
      "shipping_size": 0,
      "priority": 21,
      "set_flag": "表示",
      "tax_type_id": 1,
      "updated_at": null
    },
    {
      "id": 18,
      "product_id": 8,
      "product_no": "SSM-1",
      "jan_code": "",
      "location_no": "",
      "jodai_type": "参考上代",
      "jodai": 9800,
      "name": "単品",
      "unit_price": 6800,
      "min_order": null,
      "max_order": null,
      "group_price": {
        "1": {
          "name": "リピート会員",
          "rate": "0.9000",
          "unit_price": 6800,
          "fixed_price": 6800,
          "volume_discount": null
        },
        "2": {
          "name": "特別会員",
          "rate": "0.7000",
          "unit_price": 6800,
          "fixed_price": 6800,
          "volume_discount": null
        },
        "3": {
          "name": "グループ名は自由につけられます",
          "rate": "0.6000",
          "unit_price": 6800,
          "fixed_price": 6800,
          "volume_discount": null
        },
        "4": {
          "name": "販売掛率もいつでも変更できます",
          "rate": "0.5500",
          "unit_price": 3740.0000000000005,
          "fixed_price": null,
          "volume_discount": null
        },
        "n": {
          "name": "非会員のお客様",
          "rate": "1.0000",
          "unit_price": 6800,
          "fixed_price": null,
          "volume_discount": null
        }
      },
      "special_price": null,
      "volume_discount": null,
      "quantity": 1,
      "unit": "個",
      "description": "",
      "stock": 50,
      "stock_flag": 0,
      "stock_parent": null,
      "stock_view_id": 1,
      "stock_few": 0,
      "view_group_filter": null,
      "visible_customer_id": null,
      "hide_customer_id": null,
      "customs": null,
      "option_ids": null,
      "shipping_group_id": 1,
      "shipping_size": 0,
      "priority": 18,
      "set_flag": "表示",
      "tax_type_id": 1,
      "updated_at": "2022-01-26 14:15:51"
    },
    {
      "id": 19,
      "product_id": 8,
      "product_no": "SSM-5",
      "jan_code": "",
      "location_no": "",
      "jodai_type": "参考上代",
      "jodai": 9800,
      "name": "5個セット",
      "unit_price": 4200,
      "min_order": null,
      "max_order": null,
      "group_price": {
        "1": {
          "name": "リピート会員",
          "rate": "0.9000",
          "unit_price": 4200,
          "fixed_price": 4200,
          "volume_discount": null
        },
        "2": {
          "name": "特別会員",
          "rate": "0.7000",
          "unit_price": 4200,
          "fixed_price": 4200,
          "volume_discount": null
        },
        "3": {
          "name": "グループ名は自由につけられます",
          "rate": "0.6000",
          "unit_price": 4200,
          "fixed_price": 4200,
          "volume_discount": null
        },
        "4": {
          "name": "販売掛率もいつでも変更できます",
          "rate": "0.5500",
          "unit_price": 2310,
          "fixed_price": null,
          "volume_discount": null
        },
        "n": {
          "name": "非会員のお客様",
          "rate": "1.0000",
          "unit_price": 4200,
          "fixed_price": null,
          "volume_discount": null
        }
      },
      "special_price": null,
      "volume_discount": null,
      "quantity": 5,
      "unit": "個",
      "description": "",
      "stock": 0,
      "stock_flag": 0,
      "stock_parent": null,
      "stock_view_id": 1,
      "stock_few": 0,
      "view_group_filter": null,
      "visible_customer_id": null,
      "hide_customer_id": null,
      "customs": null,
      "option_ids": null,
      "shipping_group_id": 1,
      "shipping_size": 0,
      "priority": 20,
      "set_flag": "表示",
      "tax_type_id": 1,
      "updated_at": null
    },
    {
      "id": 20,
      "product_id": 9,
      "product_no": "TB-6",
      "jan_code": "",
      "location_no": "",
      "jodai_type": "参考上代",
      "jodai": 6200,
      "name": "6個セット",
      "unit_price": 9500,
      "min_order": null,
      "max_order": null,
      "group_price": {
        "1": {
          "name": "リピート会員",
          "rate": "0.9000",
          "unit_price": 9500,
          "fixed_price": 9500,
          "volume_discount": null
        },
        "2": {
          "name": "特別会員",
          "rate": "0.7000",
          "unit_price": 9500,
          "fixed_price": 9500,
          "volume_discount": null
        },
        "3": {
          "name": "グループ名は自由につけられます",
          "rate": "0.6000",
          "unit_price": 9500,
          "fixed_price": 9500,
          "volume_discount": null
        },
        "4": {
          "name": "販売掛率もいつでも変更できます",
          "rate": "0.5500",
          "unit_price": 5225,
          "fixed_price": null,
          "volume_discount": null
        },
        "n": {
          "name": "非会員のお客様",
          "rate": "1.0000",
          "unit_price": 9500,
          "fixed_price": null,
          "volume_discount": null
        }
      },
      "special_price": null,
      "volume_discount": null,
      "quantity": 6,
      "unit": "個",
      "description": "",
      "stock": 0,
      "stock_flag": 0,
      "stock_parent": null,
      "stock_view_id": 1,
      "stock_few": 0,
      "view_group_filter": null,
      "visible_customer_id": null,
      "hide_customer_id": null,
      "customs": null,
      "option_ids": null,
      "shipping_group_id": 1,
      "shipping_size": 0,
      "priority": 24,
      "set_flag": "表示",
      "tax_type_id": 1,
      "updated_at": null
    }
  ],
  "meta": {
    "limit": 20,
    "offset": 0,
    "total": 149
  }
}
```

## PATCH {{api_url}}/api/v1/product_sets/1

**リクエストBODY**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| product_id | 商品ID | 整数 | 11 | 項目存在時必須 |
| product_no | 品番 | 文字列 | 255 |  |
| jan_code | JANコード | 文字列 | 255 |  |
| location_no | ローケーションNO | 文字列 | 255 |  |
| jodai_type | 参考上代タイプ | 文字列 | 50 | 非表示/オープン/参考上代/メーカー希望希望小売価格/カタログ価格/カスタム/単価表示 |
| jodai | 参考上代 | 整数 | 11 |  |
| name | セット名 | 文字列 | 255 | 項目存在時必須 |
| unit_price | 単価 | 整数 | 11 | 項目存在時必須 |
| min_order | 最小注文可能数 | 整数 | 8 |  |
| max_order | 最大注文可能数 | 整数 | 8 |  |
| group_price\[{:n}\]\[fixed_price\] | グループ個別価格 | 整数 | 11 | {:n}に価格グループIDを指定 |
| group_price\[{:n}\]\[volume_discount\]\[{:cnt}\] | 個別価格 | 数値 | 11 | {:n}に価格グループID {:cnt}には数量を指定 |
| special_price\[{:id}\]\[unit_price\] | 会員特別価格 | 整数 | 11 | {:id}には会員IDを指定 |
| special_price\[{:id}\]\[volume_discount\]\[{:cnt}\] | 会員特別価格 | 数値 | 11 | {:id}には会員ID {:cnt}には数量を指定 |
| volume_discount\[{:cnt}\] | 数量割引価格 | 数値 | 11 | {:cnt}には数量を指定 |
| quantity | 入数 | 整数 | 255 |  |
| unit | 単位 | 文字列 | 255 | 個/箱など |
| description | セット説明 | 文字列 | 65,535 |  |
| stock | 在庫 | 整数 | 11 | 在庫フラグが0の場合に指定可能 |
| stock_flag | 在庫フラグ | 整数 | 4 | 0=在庫管理 / 1=在庫無制限 / 100=別在庫参照 |
| stock_parent\[{:id}\] | 在庫参照商品セット入数 | 整数 | 11 | {:id}に参照する商品セットID |
| stock_view_id | 在庫表示パターン | 整数 | 1 |  |
| stock_few | 在庫僅かの閾値 | 整数 | 11 |  |
| view_group_filter | 非表示フィルタ | 配列 | 255 | 非会員,通常会員又は非表示にする表示グループIDをカンマ区切りで指定 |
| visible_customer_id | 例外表示会員ID | 文字列 | 65,535 | 会員IDをカンマ区切りで指定 |
| hide_customer_id | 商品セットを非表示とする会員ID | 文字列 | 65,535 | 会員IDをカンマ区切りで指定 |
| customs\[{field_id, value}\] | カスタム項目 | 配列 | 65,535 |  |
| option_ids | 商品オプションID | 配列 | 255 | 紐付ける商品オプションのIDをカンマ区切りで指定 |
| shipping_group_id | 配送グループID | 整数 | 11 | 所属する配送グループのIDを指定 |
| shipping_size | 配送サイズ | 数値 | 11 |  |
| priority | 並び順 | 整数 | 4 | \-127〜127 |
| set_flag | フラグ | 文字列 | 3 |  |
| tax_type_id | 税区分 | 整数 | 1 | 1=標準税率,2=軽減税率,3=非課税 |
| allowed_payments | 決済制限 | 配列 |  |  |
| updated_at | 更新日時 | 日付 | 19 | Y-m-d |

**リクエストボディ例:**

```json
{
  "product_no": "XXX-1008-AA",
  "unit_price": 1000.1,
  "group_price": {
    "1": {
      "fixed_price": 10800.5,
      "volume_discount": {
        "2": 9800.6,
        "5": 4800
      }
    }
  },
  "special_price": {
    "10000": {
      "unit_price": 16800.11
    },
    "10001": {
      "unit_price": 16800
    }
  },
  "customs": [
    {
      "field_id": 17,
      "value": "custom1"
    },
    {
      "field_id": 19,
      "value": "custom3"
    }
  ],
  "option_ids": [
    1,
    2
  ]
}
```

**レスポンス例（200 OK）:**

```json
{
  "product_set": {
    "id": 1,
    "product_id": 1,
    "product_no": "XXX-1008-AA",
    "jan_code": "xxx",
    "location_no": "",
    "jodai_type": "メーカー希望小売価格",
    "jodai": 25000,
    "name": "単品販売 カラー：ブラウン",
    "unit_price": 20000,
    "min_order": null,
    "max_order": 10,
    "group_price": {
      "1": {
        "name": "リピート会員",
        "rate": "0.9000",
        "unit_price": 12400,
        "fixed_price": 12400,
        "volume_discount": {
          "2": 12000,
          "3": 11000
        }
      },
      "2": {
        "name": "特別会員",
        "rate": "0.7000",
        "unit_price": 4000,
        "fixed_price": 4000,
        "volume_discount": {
          "2": 3600
        }
      },
      "3": {
        "name": "グループ名は自由につけられます",
        "rate": "0.6000",
        "unit_price": 2000,
        "fixed_price": 2000,
        "volume_discount": {
          "5": 1800
        }
      },
      "4": {
        "name": "販売掛率もいつでも変更できます",
        "rate": "0.5500",
        "unit_price": 11000,
        "fixed_price": null,
        "volume_discount": null
      },
      "n": {
        "name": "非会員のお客様",
        "rate": "1.0000",
        "unit_price": 21000,
        "fixed_price": 21000,
        "volume_discount": {
          "5": 18000
        }
      }
    },
    "special_price": {
      "9888": {
        "unit_price": 15000,
        "volume_discount": {
          "5": 14000
        }
      },
      "9999": {
        "unit_price": 17800,
        "volume_discount": {
          "5": 10000,
          "10": 9980
        }
      },
      "10000": {
        "unit_price": 16800,
        "volume_discount": null
      }
    },
    "volume_discount": {
      "2": 14200,
      "5": 13800
    },
    "quantity": 1,
    "unit": "脚",
    "description": "",
    "stock": 8,
    "stock_flag": 0,
    "stock_parent": null,
    "stock_view_id": null,
    "stock_few": 0,
    "view_group_filter": "1,2",
    "visible_customer_id": "10000,5555",
    "hide_customer_id": "10010,10013",
    "customs": [
      {
        "field_id": "34",
        "value": "custom1"
      },
      {
        "field_id": "35",
        "value": "custom2"
      }
    ],
    "option_ids": [
      "15",
      "16"
    ],
    "shipping_group_id": 3,
    "shipping_size": 0,
    "priority": 0,
    "set_flag": "表示",
    "tax_type_id": 1,
    "updated_at": "2022-01-26 14:15:51"
  }
}
```

## PATCH {{api_url}}/api/v1/product_sets/2

**リクエストボディ例:**

```json
{
  "stock_flag": 100,
  "stock_parent": {
    "3": 2,
    "4": 2
  }
}
```

**レスポンス例（200 OK）:**

```json
{
  "product_set": {
    "id": 2,
    "product_id": 1,
    "product_no": "DUMMY2",
    "jan_code": "xxx",
    "location_no": "",
    "jodai_type": "メーカー希望小売価格",
    "jodai": 25000,
    "name": "単品販売 カラー：ブラウン2",
    "unit_price": 22000,
    "min_order": null,
    "max_order": 10,
    "group_price": {
      "1": {
        "name": "リピート会員",
        "rate": "0.9000",
        "unit_price": 12800,
        "fixed_price": 12800,
        "volume_discount": {
          "2": 12000,
          "3": 11000
        }
      },
      "2": {
        "name": "特別会員",
        "rate": "0.7000",
        "unit_price": 4000,
        "fixed_price": 4000,
        "volume_discount": {
          "2": 3600
        }
      },
      "3": {
        "name": "グループ名は自由につけられます",
        "rate": "0.6000",
        "unit_price": 2000,
        "fixed_price": 2000,
        "volume_discount": {
          "5": 1800
        }
      },
      "4": {
        "name": "販売掛率もいつでも変更できます",
        "rate": "0.5500",
        "unit_price": 12100.000000000002,
        "fixed_price": null,
        "volume_discount": null
      },
      "n": {
        "name": "非会員のお客様",
        "rate": "1.0000",
        "unit_price": 21000,
        "fixed_price": 21000,
        "volume_discount": {
          "5": 18000
        }
      }
    },
    "special_price": {
      "9888": {
        "unit_price": 15000,
        "volume_discount": {
          "5": 14000
        }
      },
      "9999": {
        "unit_price": 17800,
        "volume_discount": {
          "5": 10000,
          "10": 9980
        }
      },
      "10000": {
        "unit_price": 16800,
        "volume_discount": null
      }
    },
    "volume_discount": {
      "2": 14200,
      "5": 13800
    },
    "quantity": 1,
    "unit": "脚",
    "description": "",
    "stock": 41,
    "stock_flag": 100,
    "stock_parent": {
      "3": 2,
      "4": 2
    },
    "stock_view_id": 1,
    "stock_few": 0,
    "view_group_filter": null,
    "visible_customer_id": "5555",
    "hide_customer_id": "10010",
    "customs": [
      {
        "field_id": 17,
        "value": "カスタム1"
      },
      {
        "field_id": 19,
        "value": "カスタム3"
      }
    ],
    "option_ids": [
      1,
      5
    ],
    "shipping_group_id": 3,
    "shipping_size": 0,
    "priority": 0,
    "set_flag": "表示",
    "tax_type_id": 1,
    "updated_at": "2022-01-26 14:29:00"
  }
}
```

## PATCH {{api_url}}/api/v1/product_sets/

**リクエストBODY**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| product_sets\[{{i}}\]\[id\] | 商品セットID | 整数 | 11 | 必須 |
| product_sets\[{{i}}\]\[product_id\] | 商品ID | 整数 | 11 | 項目存在時必須 |
| product_sets\[{{i}}\]\[product_no\] | 品番 | 文字列 | 255 |  |
| product_sets\[{{i}}\]\[jan_code\] | JANコード | 文字列 | 255 |  |
| product_sets\[{{i}}\]\[location_no\] | ローケーションNO | 文字列 | 255 |  |
| product_sets\[{{i}}\]\[jodai_type\] | 参考上代タイプ | 文字列 | 50 | 非表示/オープン/参考上代/メーカー希望希望小売価格/カタログ価格/カスタム/単価表示 |
| product_sets\[{{i}}\]\[jodai\] | 参考上代 | 整数 | 11 |  |
| product_sets\[{{i}}\]\[name\] | セット名 | 文字列 | 255 | 項目存在時必須 |
| product_sets\[{{i}}\]\[unit_price\] | 単価 | 整数 | 11 | 項目存在時必須 |
| product_sets\[{{i}}\]\[min_order\] | 最小注文可能数 | 整数 | 8 |  |
| product_sets\[{{i}}\]\[max_order\] | 最大注文可能数 | 整数 | 8 |  |
| product_sets\[{{i}}\]\[group_price\]\[{{v_id}}\]\[fixed_price\] | 個別価格 | 整数 | 11 | {:n}に価格グループIDを指定 |
| product_sets\[{{i}}\]\[group_price\]\[{{v_id}}\]\[volume_discount\]\[{{cnt}}\] | グループ数量割引価格 | 数値 | 11 | {:n}に価格グループID {:cnt}には数量を指定 |
| product_sets\[{{i}}\]\[special_price\]\[{{c_id}}\]\[unit_price\] | 会員特別価格 | 整数 | 11 | {:id}には会員IDを指定 |
| product_sets\[{{i}}\]\[special_price\]\[{{c_id}}\]\[volume_discount\]\[{{cnt}}\] | 会員特別価格 | 数値 | 11 | {:id}には会員ID {:cnt}には数量を指定 |
| product_sets\[{{i}}\]\[volume_discount\]\[{{cnt}}\] | 数量割引価格 | 数値 | 11 | {:cnt}には数量を指定 |
| product_sets\[{{i}}\]\[quantity\] | 入数 | 整数 | 255 |  |
| product_sets\[{{i}}\]\[unit\] | 単位 | 文字列 | 255 | 個/箱など |
| product_sets\[{{i}}\]\[description\] | セット説明 | 文字列 | 65,535 |  |
| product_sets\[{{i}}\]\[stock\] | 在庫 | 整数 | 11 | 在庫フラグが0の場合に指定可能 |
| product_sets\[{{i}}\]\[stock_flag\] | 在庫フラグ | 整数 | 4 | 0=在庫管理 / 1=在庫無制限 / 100=別在庫参照 |
| product_sets\[{{i}}\]\[stock_parent\] | 在庫参照商品セット入数 | 整数 | 11 | {:id}に参照する商品セットID |
| product_sets\[{{i}}\]\[stock_view_id\] | 在庫表示パターン | 整数 | 1 |  |
| product_sets\[{{i}}\]\[stock_few\] | 在庫僅かの閾値 | 整数 | 11 |  |
| product_sets\[{{i}}\]\[view_group_filter\] | 非表示フィルタ | 配列 | 255 | 非会員,通常会員又は非表示にする表示グループIDをカンマ区切りで指定 |
| product_sets\[{{i}}\]\[visible_customer_id\] | 例外表示会員ID | 文字列 | 65,535 | 会員IDをカンマ区切りで指定 |
| product_sets\[{{i}}\]\[hide_customer_id\] | 商品セットを非表示とする会員ID | 文字列 | 65,535 | 会員IDをカンマ区切りで指定 |
| product_sets\[{{i}}\]\[customs\]\[{field_id, value}\] | カスタム項目 | 配列 | 65,535 |  |
| product_sets\[{{i}}\]\[option_ids\] | 商品オプションID | 配列 | 255 | 紐付ける商品オプションのIDをカンマ区切りで指定 |
| product_sets\[{{i}}\]\[shipping_group_id\] | 配送グループID | 整数 | 255 | 所属する配送グループのIDを指定 |
| product_sets\[{{i}}\]\[shipping_size\] | 配送サイズ | 数値 | 11 |  |
| product_sets\[{{i}}\]\[priority\] | 並び順 | 整数 | 4 | \-127〜127 |
| product_sets\[{{i}}\]\[set_flag\] | フラグ | 文字列 | 3 |  |
| product_sets\[{{i}}\]\[tax_type_id\] | 税区分 | 整数 | 1 | 1=標準税率,2=軽減税率,3=非課税 |
| product_sets\[{{i}}\]\[allowed_payments\] | 決済制限 | 配列 |  |  |
| product_sets\[{{i}}\]\[updated_at\] | 更新日時 | 日付 | 19 | Y-m-d |

**リクエストボディ例:**

```json
{
  "product_sets": [
    {
      "id": 1,
      "stock_flag": 0,
      "stock": 30
    },
    {
      "id": 2,
      "stock_flag": 100,
      "stock_parent": {
        "1": 5,
        "4": 1
      }
    },
    {
      "id": 1,
      "stock_flag": 0,
      "stock": "+-4"
    }
  ]
}
```

**レスポンス例（200 OK）:**

```json
{
  "product_sets": [
    {
      "id": 1,
      "product_id": 1,
      "product_no": "aXXX-1008-AA",
      "jan_code": "xxx",
      "location_no": "",
      "jodai_type": "メーカー希望小売価格",
      "jodai": 25000,
      "name": "単品販売 カラー：ブラウン",
      "unit_price": 1000.1,
      "min_order": null,
      "max_order": 10,
      "group_price": {
        "1": {
          "name": "リピート会員",
          "rate": "0.9000",
          "unit_price": 10800.5,
          "fixed_price": 10800.5,
          "volume_discount": {
            "2": 9800.6,
            "5": 4800
          }
        },
        "2": {
          "name": "特別会員",
          "rate": "0.7000",
          "unit_price": 4000,
          "fixed_price": 4000,
          "volume_discount": {
            "2": 3600
          }
        },
        "3": {
          "name": "グループ名は自由につけられます",
          "rate": "0.6000",
          "unit_price": 2000,
          "fixed_price": 2000,
          "volume_discount": {
            "5": 1800
          }
        },
        "4": {
          "name": "販売掛率もいつでも変更できます",
          "rate": "0.5500",
          "unit_price": 550.0550000000001,
          "fixed_price": null,
          "volume_discount": null
        },
        "n": {
          "name": "非会員のお客様",
          "rate": "1.0000",
          "unit_price": 21000,
          "fixed_price": 21000,
          "volume_discount": {
            "5": 18000
          }
        }
      },
      "special_price": {
        "9888": {
          "unit_price": 15000,
          "volume_discount": {
            "5": 14000
          }
        },
        "9999": {
          "unit_price": 17800,
          "volume_discount": {
            "5": 10000,
            "10": 9980
          }
        },
        "10000": {
          "unit_price": 16800,
          "volume_discount": null
        }
      },
      "volume_discount": {
        "2": 14200,
        "5": 13800
      },
      "quantity": 1,
      "unit": "脚",
      "description": "",
      "stock": 26,
      "stock_flag": 0,
      "stock_parent": null,
      "stock_view_id": null,
      "stock_few": 0,
      "view_group_filter": "1,2",
      "visible_customer_id": "10000,5555",
      "hide_customer_id": "10010,10013",
      "customs": [
        {
          "field_id": 17,
          "value": "custom1"
        },
        {
          "field_id": 18,
          "value": "custom2"
        },
        {
          "field_id": 19,
          "value": "custom3"
        }
      ],
      "option_ids": [
        1,
        2
      ],
      "shipping_group_id": 3,
      "shipping_size": 0,
      "priority": 0,
      "set_flag": "表示",
      "tax_type_id": 1,
      "updated_at": "2022-01-26 14:29:29"
    },
    {
      "id": 2,
      "product_id": 1,
      "product_no": "DUMMY2",
      "jan_code": "xxx",
      "location_no": "",
      "jodai_type": "メーカー希望小売価格",
      "jodai": 25000,
      "name": "単品販売 カラー：ブラウン2",
      "unit_price": 22000,
      "min_order": null,
      "max_order": 10,
      "group_price": {
        "1": {
          "name": "リピート会員",
          "rate": "0.9000",
          "unit_price": 12800,
          "fixed_price": 12800,
          "volume_discount": {
            "2": 12000,
            "3": 11000
          }
        },
        "2": {
          "name": "特別会員",
          "rate": "0.7000",
          "unit_price": 4000,
          "fixed_price": 4000,
          "volume_discount": {
            "2": 3600
          }
        },
        "3": {
          "name": "グループ名は自由につけられます",
          "rate": "0.6000",
          "unit_price": 2000,
          "fixed_price": 2000,
          "volume_discount": {
            "5": 1800
          }
        },
        "4": {
          "name": "販売掛率もいつでも変更できます",
          "rate": "0.5500",
          "unit_price": 12100.000000000002,
          "fixed_price": null,
          "volume_discount": null
        },
        "n": {
          "name": "非会員のお客様",
          "rate": "1.0000",
          "unit_price": 21000,
          "fixed_price": 21000,
          "volume_discount": {
            "5": 18000
          }
        }
      },
      "special_price": {
        "9888": {
          "unit_price": 15000,
          "volume_discount": {
            "5": 14000
          }
        },
        "9999": {
          "unit_price": 17800,
          "volume_discount": {
            "5": 10000,
            "10": 9980
          }
        },
        "10000": {
          "unit_price": 16800,
          "volume_discount": null
        }
      },
      "volume_discount": {
        "2": 14200,
        "5": 13800
      },
      "quantity": 1,
      "unit": "脚",
      "description": "",
      "stock": 5,
      "stock_flag": 100,
      "stock_parent": {
        "1": 5,
        "4": 1
      },
      "stock_view_id": 1,
      "stock_few": 0,
      "view_group_filter": null,
      "visible_customer_id": "5555",
      "hide_customer_id": "10013",
      "customs": [
        {
          "field_id": 17,
          "value": "カスタム1"
        },
        {
          "field_id": 19,
          "value": "カスタム3"
        }
      ],
      "option_ids": [
        1,
        5
      ],
      "shipping_group_id": 3,
      "shipping_size": 0,
      "priority": 0,
      "set_flag": "表示",
      "tax_type_id": 1,
      "updated_at": "2022-01-26 14:29:29"
    }
  ]
}
```

## POST {{api_url}}/api/v1/product_sets

**リクエストBODY**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| product_sets\[{{i}}\]\[product_id\] | 商品ID | 整数 | 11 | 商品セットの基本情報となる商品ID 必須 |
| product_sets\[{{i}}\]\[product_no\] | 品番 | 文字列 | 255 |  |
| product_sets\[{{i}}\]\[jan_code\] | JANコード | 文字列 | 255 |  |
| product_sets\[{{i}}\]\[location_no\] | ローケーションNO | 文字列 | 255 |  |
| product_sets\[{{i}}\]\[jodai_type\] | 参考上代タイプ | 文字列 | 50 | 非表示/オープン/参考上代/メーカー希望希望小売価格/カタログ価格/カスタム/単価表示 |
| product_sets\[{{i}}\]\[jodai\] | 参考上代 | 整数 | 11 |  |
| product_sets\[{{i}}\]\[name\] | セット名 | 文字列 | 255 | 必須 |
| product_sets\[{{i}}\]\[unit_price\] | 単価 | 整数 | 11 | 必須 |
| product_sets\[{{i}}\]\[min_order\] | 最小注文可能数 | 整数 | 8 |  |
| product_sets\[{{i}}\]\[max_order\] | 最大注文可能数 | 整数 | 8 |  |
| product_sets\[{{i}}\]\[group_price\]\[{{v_id}}\]\[fixed_price\] | 個別価格 | 整数 | 11 | {:n}に価格グループIDを指定 |
| product_sets\[{{i}}\]\[group_price\]\[{{v_id}}\]\[volume_discount\]\[{{cnt}}\] | グループ数量割引価格 | 数値 | 11 | {:n}に価格グループID {:cnt}には数量を指定 |
| product_sets\[{{i}}\]\[special_price\]\[{{c_id}}\]\[unit_price\] | 会員特別価格 | 整数 | 11 | {:id}には会員IDを指定 |
| product_sets\[{{i}}\]\[special_price\]\[{{c_id}}\]\[volume_discount\]\[{{cnt}}\] | 会員特別価格 | 数値 | 11 | {:id}には会員ID {:cnt}には数量を指定 |
| product_sets\[{{i}}\]\[volume_discount\]\[{{cnt}}\] | 数量割引価格 | 数値 | 11 | {:cnt}には数量を指定 |
| product_sets\[{{i}}\]\[quantity\] | 入数 | 整数 | 25 | 必須 |
| product_sets\[{{i}}\]\[unit\] | 単位 | 文字列 | 255 | 個/箱など |
| product_sets\[{{i}}\]\[description\] | セット説明 | 文字列 | 65,535 |  |
| product_sets\[{{i}}\]\[stock\] | 在庫 | 整数 | 11 | 在庫フラグが0の場合に指定可能 |
| product_sets\[{{i}}\]\[stock_flag\] | 在庫フラグ | 整数 | 4 | 0=在庫管理 / 1=在庫無制限 / 100=別在庫参照 |
| product_sets\[{{i}}\]\[stock_parent\] | 在庫参照商品セット入数 | 整数 | 11 | {:id}に参照する商品セットID |
| product_sets\[{{i}}\]\[stock_view_id\] | 在庫表示パターン | 整数 | 1 |  |
| product_sets\[{{i}}\]\[stock_few\] 在庫僅かの閾値 | 整数 | 11 |  |  |
| product_sets\[{{i}}\]\[view_group_filter\] | 非表示フィルタ | 配列 | 255 | 非会員,通常会員又は非表示にする表示グループIDをカンマ区切りで指定 |
| product_sets\[{{i}}\]\[visible_customer_id\] | 例外表示会員ID | 文字列 | 65,535 | 会員IDをカンマ区切りで指定 |
| product_sets\[{{i}}\]\[hide_customer_id\] | 商品セットを非表示とする会員ID | 文字列 | 65,535 | 会員IDをカンマ区切りで指定 |
| product_sets\[{{i}}\]\[customs\]\[{field_id, value}\] | カスタム項目 | 配列 | 65,535 |  |
| product_sets\[{{i}}\]\[option_ids\] | 商品オプションID | 配列 | 255 | 紐付ける商品オプションのIDをカンマ区切りで指定 |
| product_sets\[{{i}}\]\[shipping_group_id\] | 配送グループID | 整数 | 255 | 所属する配送グループのIDを指定 |
| product_sets\[{{i}}\]\[shipping_size\] | 配送サイズ | 数値 | 11 |  |
| product_sets\[{{i}}\]\[priority\] | 並び順 | 整数 | 4 | \-127〜127 |
| product_sets\[{{i}}\]\[set_flag\] | フラグ | 文字列 | 3 |  |
| product_sets\[{{i}}\]\[tax_type_id\] | 税区分 | 整数 | 1 | 1=標準税率,2=軽減税率,3=非課税 |
| product_sets\[{{i}}\]\[allowed_payments\] | 決済制限 | 配列 |  |  |

**リクエストボディ例:**

```json
{
  "product_sets": [
    {
      "product_id": 1,
      "product_no": "XXX-1008-AA",
      "jan_code": "xxx",
      "location_no": "1",
      "jodai_type": "メーカー希望小売価格",
      "jodai": 25000,
      "name": "単品販売 カラー：ブラウン",
      "unit_price": 20000,
      "min_order": null,
      "max_order": 10,
      "group_price": {
        "1": {
          "fixed_price": 12400,
          "volume_discount": {
            "2": 12000,
            "3": 11000
          }
        },
        "2": {
          "fixed_price": 4000,
          "volume_discount": {
            "2": 3600
          }
        },
        "3": {
          "fixed_price": 2000,
          "volume_discount": {
            "5": 1800
          }
        },
        "n": {
          "fixed_price": 21000,
          "volume_discount": {
            "5": 18000
          }
        }
      },
      "special_price": {
        "9888": {
          "unit_price": 15000,
          "volume_discount": {
            "5": 14000
          }
        },
        "10000": {
          "unit_price": 16800
        },
        "9999": {
          "unit_price": 17800,
          "volume_discount": {
            "5": 10000,
            "10": 9980
          }
        }
      },
      "volume_discount": {
        "2": 14200,
        "5": 13800
      },
      "quantity": 1,
      "unit": "脚",
      "stock": null,
      "stock_flag": 1,
      "stock_view_id": 1,
      "stock_few": 0,
      "priority": 0,
      "set_flag": "表示",
      "view_group_filter": "1,2",
      "visible_customer_id": "10000,5555",
      "customs": [
        {
          "field_id": 17,
          "value": "custom1"
        },
        {
          "field_id": 18,
          "value": "custom2"
        },
        {
          "field_id": 19,
          "value": "custom3"
        }
      ],
      "option_ids": [
        1,
        2
      ],
      "shipping_group_id": 3,
      "shipping_size": 0
    },
    {
      "product_id": 1,
      "product_no": "XXX-1008-AA2",
      "jan_code": "xxx",
      "location_no": "1",
      "jodai_type": "メーカー希望小売価格",
      "jodai": 25000,
      "name": "単品販売 カラー：ブラウン2",
      "unit_price": 22000,
      "min_order": null,
      "max_order": 10,
      "group_price": {
        "1": {
          "fixed_price": 12800,
          "volume_discount": {
            "2": 12000,
            "3": 11000
          }
        },
        "2": {
          "fixed_price": 4000,
          "volume_discount": {
            "2": 3600
          }
        },
        "3": {
          "fixed_price": 2000,
          "volume_discount": {
            "5": 1800
          }
        },
        "n": {
          "fixed_price": 21000,
          "volume_discount": {
            "5": 18000
          }
        }
      },
      "special_price": {
        "9888": {
          "unit_price": 15000,
          "volume_discount": {
            "5": 14000
          }
        },
        "10000": {
          "unit_price": 16800
        },
        "9999": {
          "unit_price": 17800,
          "volume_discount": {
            "5": 10000,
            "10": 9980
          }
        }
      },
      "volume_discount": {
        "2": 14200,
        "5": 13800
      },
      "quantity": 1,
      "unit": "脚",
      "stock_parent": {
        "1": 5,
        "2": 1
      },
      "stock_flag": 100,
      "stock_view_id": 1,
      "stock_few": 0,
      "priority": 0,
      "set_flag": "表示",
      "stock": 0,
      "visible_customer_id": 5555,
      "shipping_group_id": 3,
      "shipping_size": 0
    }
  ]
}
```

**レスポンス例（201 Created）:**

```json
{
    "product_sets": [
        {
            "id": 1,
            "product_id": 1,
            "product_no": "XXX-1008-AA",
            "jan_code": "xxx",
            "location_no": "1",
            "jodai_type": "メーカー希望小売価格",
            "jodai": 25000,
            "name": "単品販売 カラー：ブラウン",
            "unit_price": 20000,
            "min_order": null,
            "max_order": 10,
            "group_price": {
                "1": {
                    "name": "リピート会員",
                    "rate": "0.9000",
                    "unit_price": 12400,
                    "fixed_price": 12400,
                    "volume_discount": {
                        "2": 12000,
                        "3": 11000
                    }
                },
                "2": {
                    "name": "特別会員",
                    "rate": "0.7000",
                    "unit_price": 4000,
                    "fixed_price": 4000,
                    "volume_discount": {
                        "2": 3600
                    }
                },
                "3": {
                    "name": "グループ名は自由につけられます",
                    "rate": "0.6000",
                    "unit_price": 2000,
                    "fixed_price": 2000,
                    "volume_discount": {
                        "5": 1800
                    }
                },
                "4": {
                    "name": "販売掛率もいつでも変更できます",
                    "rate": "0.5500",
                    "unit_price": 11000,
                    "fixed_price": null,
                    "volume_discount": null
                },
                "n": {
                    "name": "非会員のお客様",
                    "rate": "1.0000",
                    "unit_price": 21000,
                    "fixed_price": 21000,
                    "volume_discount": {
                        "5": 18000
                    }
                }
            },
            "special_price": {
                "9888": {
                    "unit_price": 15000,
                    "volume_discount": {
                        "5": 14000
                    }
                },
                "9999": {
                    "unit_price": 17800,
                    "volume_discount": {
                        "5": 10000,
                        "10": 9980
                    }
                },
                "10000": {
                    "unit_price": 16800,
                    "volume_discount": null
                }
            },
            "volume_discount": {
                "2": 14200,
                "5": 13800
            },
            "quantity": 1,
            "unit": "脚",
            "description": "",
            "stock": null,
            "stock_flag": 1,
            "stock_parent": null,
            "stock_view_id": 1,
            "stock_few": 0,
            "view_group_filter": "1,2",
            "visible_customer_id": "10000,5555",
            "hide_customer_id": "10010,10013",
            "customs": [
                {
                    "field_id": 17,
                    "value": "custom1"
                },
                {
                    "field_id": 18,
                    "value": "custom2"
                },
                {
                    "field_id": 19,
                    "value": "custom3"
                }
            ],
            "option_ids": [
                1,
                2
            ],
            "shipping_group_id": 3,
            "shipping_size": 0,
            "priority": 0,
            "set_flag": "表示",
            "tax_type_id": 1,
            // "updated_at": "2022-01-26 14:32:55"
        }
    ]
}
```
