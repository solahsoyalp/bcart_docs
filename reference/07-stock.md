# 在庫

商品セットの在庫

## GET {{api_url}}/api/v1/product_stock/XXX-1008-AA

**レスポンス例（200 OK）:**

```json
{
  "product_stock": [
    {
      "id": 1,
      "product_id": 2,
      "product_no": "XXX-1008-AA",
      "name": "アタッシュケース【Mサイズ】",
      "stock": 26,
      "stock_flag": 0,
      "stock_parent": null
    },
    {
      "id": 160,
      "product_id": 1,
      "product_no": "XXX-1008-AA",
      "name": "単品販売 カラー：ブラウン",
      "stock": null,
      "stock_flag": 1,
      "stock_parent": null
    }
  ]
}
```

## GET {{api_url}}/api/v1/product_stock

**URIパラメータ**

| パラメータ名 | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| stock_flag | 在庫フラグ | 数値 | 4 | 0 = 通常, 1 = 無制限, 100 = 別在庫参照 |
| stock | 在庫 | 整数 | 11 | ※数値の頭+にプラスを付けると加算/+-に付けると減算 |
| stock_parent\[{{product_no}}\] | 在庫参照数 | 整数 | 11 | 品番{{product_no}}の数 |

※ stock_flagが1の場合はstockもstock_parentも利用されません。100の場合はstock_parentから在庫を算出します。

## 拡張パラメータによる高度な絞り込み

拡張パラメータを使用することで、より高度な絞り込みが可能です。

詳しくは、[パラメータ](../docs/04-parameters.md)の「拡張パラメータ」欄をご参照ください。

**レスポンス例（200 OK）:**

```json
{
  "product_stock": [
    {
      "id": 1,
      "product_id": 2,
      "product_no": "XXX-1008-AA",
      "name": "アタッシュケース【Mサイズ】",
      "stock": 26,
      "stock_flag": 0,
      "stock_parent": null
    },
    {
      "id": 2,
      "product_id": 2,
      "product_no": "AK-L",
      "name": "アタッシュケース【Lサイズ】",
      "stock": 5,
      "stock_flag": 100,
      "stock_parent": {
        "XXX-1008-AA": 5,
        "B0001s0001": 1
      }
    },
    {
      "id": 3,
      "product_id": 2,
      "product_no": "AK-M",
      "name": "アタッシュケース【Mサイズ】",
      "stock": 0,
      "stock_flag": 0,
      "stock_parent": null
    },
    {
      "id": 4,
      "product_id": 3,
      "product_no": "B0001s0001",
      "name": "セット品番",
      "stock": 83,
      "stock_flag": 0,
      "stock_parent": null
    },
    {
      "id": 5,
      "product_id": 3,
      "product_no": "B0001s0002",
      "name": "青色",
      "stock": 101,
      "stock_flag": 0,
      "stock_parent": null
    },
    {
      "id": 6,
      "product_id": 3,
      "product_no": "B0001s0003",
      "name": "黄色",
      "stock": 1,
      "stock_flag": 1,
      "stock_parent": null
    },
    {
      "id": 7,
      "product_id": 3,
      "product_no": "B0001s0004",
      "name": "３色",
      "stock": 101,
      "stock_flag": 0,
      "stock_parent": null
    },
    {
      "id": 8,
      "product_id": 3,
      "product_no": "B0001s0005",
      "name": "赤色",
      "stock": 10,
      "stock_flag": 0,
      "stock_parent": null
    },
    {
      "id": 9,
      "product_id": 4,
      "product_no": "KB-A1",
      "name": "1個販売",
      "stock": 1200,
      "stock_flag": 0,
      "stock_parent": null
    },
    {
      "id": 10,
      "product_id": 4,
      "product_no": "KB-A50",
      "name": "50個販売",
      "stock": 24,
      "stock_flag": 100,
      "stock_parent": {
        "KB-A1": 50
      }
    },
    {
      "id": 11,
      "product_id": 5,
      "product_no": "MT12",
      "name": "マジック用　トランプ　1ダースセット",
      "stock": 1,
      "stock_flag": 1,
      "stock_parent": null
    },
    {
      "id": 12,
      "product_id": 6,
      "product_no": "KBT-1",
      "name": "単品",
      "stock": 50,
      "stock_flag": 1,
      "stock_parent": null
    },
    {
      "id": 13,
      "product_id": 6,
      "product_no": "KBT-12",
      "name": "1ダース",
      "stock": 49,
      "stock_flag": 1,
      "stock_parent": null
    },
    {
      "id": 14,
      "product_id": 6,
      "product_no": "KBT-50",
      "name": "50個セット",
      "stock": 3,
      "stock_flag": 0,
      "stock_parent": null
    },
    {
      "id": 15,
      "product_id": 7,
      "product_no": "XM-1",
      "name": "単品",
      "stock": 101,
      "stock_flag": 1,
      "stock_parent": null
    },
    {
      "id": 16,
      "product_id": 7,
      "product_no": "XM-5",
      "name": "5個セット",
      "stock": 101,
      "stock_flag": 1,
      "stock_parent": null
    },
    {
      "id": 17,
      "product_id": 7,
      "product_no": "XM-24",
      "name": "24個セット",
      "stock": 1,
      "stock_flag": 0,
      "stock_parent": null
    },
    {
      "id": 18,
      "product_id": 8,
      "product_no": "SSM-1",
      "name": "単品",
      "stock": 6,
      "stock_flag": 1,
      "stock_parent": null
    },
    {
      "id": 19,
      "product_id": 8,
      "product_no": "SSM-5",
      "name": "5個セット",
      "stock": 0,
      "stock_flag": 0,
      "stock_parent": null
    },
    {
      "id": 20,
      "product_id": 9,
      "product_no": "TB-6",
      "name": "6個セット",
      "stock": 0,
      "stock_flag": 0,
      "stock_parent": null
    }
  ],
  "meta": {
    "limit": 20,
    "offset": 0,
    "total": 146
  }
}
```

## PATCH {{api_url}}/api/v1/product_stock/AK-M

**リクエストBODY**

| パラメータ名 | 名称 | 型 | 最大桁数 | 内容 | 
| --- | --- | --- | --- | --- |
| stock_flag | 在庫フラグ | 数値 | 4 | 0 = 通常, 1 = 無制限, 100 = 別在庫参照 |
| stock | 在庫 | 整数 | 11 | ※数値の頭+にプラスを付けると加算/+-に付けると減算 |
| stock_parent[{{product_no}}] | 在庫参照数 | 整数 | 11 | 品番{{product_no}}の数 |

※ stock_flagが1の場合はstockもstock_parentも利用されません。100の場合はstock_parentから在庫を算出します。

**リクエストボディ例:**

```json
{
  "stock_flag": 0,
  "stock": 50
}
```

**レスポンス例（200 OK）:**

```json
{
  "product_stock": [
    {
      "id": 3,
      "product_id": 2,
      "product_no": "AK-M",
      "name": "アタッシュケース【Mサイズ】",
      "stock": 50,
      "stock_flag": 0,
      "stock_parent": null
    }
  ]
}
```

## PATCH {{api_url}}/api/v1/product_stock/

**リクエストBODY**

| KEY | 名称 | 型 | 最大桁数 | 内容 | 
| --- | --- | --- | --- | --- |
| product_stock[{{i}}][product_no] | 品番 | 文字列 | 255 | 必須 |
| product_stock[{{i}}][stock_flag] | 在庫フラグ | 数値 | 4 | 0 = 通常, 1 = 無制限, 100 = 別在庫参照 |
| product_stock[{{i}}][stock] | 在庫 | 整数 | 11 | ※数値の頭+にプラスを付けると加算/+-に付けると減算 |
| product_stock[{{i}}][stock_parent][{{product_no}}] | 在庫参照数 | 整数 | 11 | 品番{{product_no}}の数 |

※ stock_flagが1の場合はstockもstock_parentも利用されません。100の場合はstock_parentから在庫を算出します。

**リクエストボディ例:**

```json
{
  "product_stock": [
    {
      "product_no": "XM-5",
      "stock_flag": 0,
      "stock": 50
    },
    {
      "product_no": "SSM-1",
      "stock_flag": 0,
      "stock": 50
    },
    {
      "product_no": "AK-M",
      "stock": "+-2"
    }
  ]
}
```

**レスポンス例（200 OK）:**

```json
{
  "product_stock": [
    {
      "id": 16,
      "product_id": 7,
      "product_no": "XM-5",
      "name": "5個セット",
      "stock": 50,
      "stock_flag": 0,
      "stock_parent": null
    },
    {
      "id": 18,
      "product_id": 8,
      "product_no": "SSM-1",
      "name": "単品",
      "stock": 50,
      "stock_flag": 0,
      "stock_parent": null
    },
    {
      "id": 3,
      "product_id": 2,
      "product_no": "AK-M",
      "name": "アタッシュケース【Mサイズ】",
      "stock": 48,
      "stock_flag": 0,
      "stock_parent": null
    }
  ]
}
```
