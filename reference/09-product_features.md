# 商品特集

Bカートの一般画面のトップページや、サイドメニューに表示される特集

## GET {{api_url}}/api/v1/product_features/1

**レスポンス例（200 OK）:**

```json
{
  "product_feature": {
    "id": 1,
    "name": "在庫処分セール",
    "rv_description": "<p style=\"background:red\">商品入れ替えの為大放出！</p>",
    "description": "",
    "header_image": null,
    "banner_image": "/sample/category/bbanner001.png",
    "menu_image": null,
    "meta_title": "",
    "meta_keywords": "",
    "meta_description": "",
    "priority": 0,
    "flag": 1
  }
}
```

## GET {{api_url}}/api/v1/product_features

**URIパラメータ**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| limit | limit | 整数 |  | 指定した件数分のデータを取得します。指定なしの場合は20件、最大100件 |
| offset | offset | 整数 |  | 指定した値+1件目のデータからlimit分を取得します。指定しない場合は0 |
| ids | ID複数 | 整数 |  | 複数の商品特集IDをカンマ区切りで指定 |
| fields | フィールド | 文字列 |  | 取得したいフィールドカンマ区切りで指定 |
| name | 特集名 | 文字列 | 255 |  |
| header_image | ヘッダ画像パス | 文字列 | 255 |  |
| top_image | トップ画像パス | 文字列 | 255 |  |
| menu_image | メニュー画像パス | 文字列 | 255 |  |

## 拡張パラメータによる高度な絞り込み

拡張パラメータを使用することで、より高度な絞り込みが可能です。

詳しくは、[パラメータ](../docs/04-parameters.md)の「拡張パラメータ」欄をご参照ください。

**レスポンス例（200 OK）:**

```json
{
  "product_features": [
    {
      "id": 1,
      "name": "在庫処分セール",
      "rv_description": "<p style=\"background:red\">商品入れ替えの為大放出！</p>",
      "description": "",
      "header_image": null,
      "banner_image": "/sample/category/bbanner001.png",
      "menu_image": null,
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "priority": 0,
      "flag": 1
    },
    {
      "id": 5,
      "name": "アンティーク家具特価SALE",
      "rv_description": "",
      "description": "",
      "header_image": null,
      "banner_image": "/demo/category/banner40.jpg",
      "menu_image": null,
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "priority": 0,
      "flag": 1
    },
    {
      "id": 7,
      "name": "F&Q",
      "rv_description": "",
      "description": "",
      "header_image": null,
      "banner_image": "/demo/banner/side0",
      "menu_image": null,
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "priority": 0,
      "flag": 0
    },
    {
      "id": 8,
      "name": "おもちゃ特集",
      "rv_description": "",
      "description": "",
      "header_image": null,
      "banner_image": "/demo/category/banner41.jpg",
      "menu_image": null,
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "priority": 0,
      "flag": 1
    }
  ],
  "meta": {
    "limit": 20,
    "offset": 0,
    "total": 4
  }
}
```

## PATCH {{api_url}}/api/v1/product_features/1

**リクエストBODY**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| name | 特集名 | 文字列 | 255 | 項目存在時必須 | 
| rv_description | 特集説明（レスポンシブ） | 文字列 | 65,535 |  |
| description | 特集説明（PC） | 文字列 | 65,535 | 
| header_image | ヘッダ画像パス | 文字列 | 255 |  | 
| top_image | トップ画像パス | 文字列 | 255 |  | 
| menu_image | メニュー画像パス | 文字列 | 255 |  | 
| meta_title | meta title | 文字列 | 255 |  | 
| meta_keywords | meta keywords | 文字列 | 255 |  | 
| meta_description | meta description | 文字列 | 255 |  |

**リクエストボディ例:**

```json
{
  "name": "Test #4",
  "priority": 6,
  "flag": 0
}
```

## PATCH {{api_url}}/api/v1/product_features/

**リクエストBODY**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| product_features[{{i}}]name | 特集名 | 文字列 | 255 | 項目存在時必須 | 
| product_features[{{i}}]rv_description | 特集説明（レスポンシブ） | 文字列 | 65,535 |  |
| product_features[{{i}}]description | 特集説明（PC） | 文字列 | 65,535 | 
| product_features[{{i}}]header_image  | ヘッダ画像パス | 文字列 | 255 |  | 
| product_features[{{i}}]top_image | トップ画像パス | 文字列 | 255 |  | 
| product_features[{{i}}]menu_image | メニュー画像パス | 文字列 | 255 |  | 
| product_features[{{i}}]meta_title | meta title | 文字列 | 255 |  | 
| product_features[{{i}}]meta_keywords | meta keywords | 文字列 | 255 |  | 
| product_features[{{i}}]meta_description | meta description | 文字列 | 255 |  |

**リクエストボディ例:**

```json
{
  "product_features": [
    {
      "id": 1,
      "name": "Test #4",
      "priority": 6,
      "flag": 0
    },
    {
      "id": 5,
      "name": "Test #5",
      "priority": 8,
      "flag": 1
    }
  ]
}
```

## POST {{api_url}}/api/v1/product_features/

**リクエストBODY**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| product_features[{{i}}]name | 特集名 | 文字列 | 255 | 項目存在時必須 | 
| product_features[{{i}}]rv_description | 特集説明（レスポンシブ） | 文字列 | 65,535 |  |
| product_features[{{i}}]description | 特集説明（PC） | 文字列 | 65,535 | 
| product_features[{{i}}]header_image  | ヘッダ画像パス | 文字列 | 255 |  | 
| product_features[{{i}}]top_image | トップ画像パス | 文字列 | 255 |  | 
| product_features[{{i}}]menu_image | メニュー画像パス | 文字列 | 255 |  | 
| product_features[{{i}}]meta_title | meta title | 文字列 | 255 |  | 
| product_features[{{i}}]meta_keywords | meta keywords | 文字列 | 255 |  | 
| product_features[{{i}}]meta_description | meta description | 文字列 | 255 |  |

**リクエストボディ例:**

```json
{
  "product_features": [
    {
      "name": "Test #4",
      "priority": 6,
      "flag": 0
    },
    {
      "id": 2,
      "name": "Test #5",
      "priority": 8,
      "flag": 1
    }
  ]
}
```

**レスポンス例（201 Created）:**

```json
{
  "product_features": [
    {
      "id": 9,
      "name": "Test #4",
      "rv_description": "",
      "description": "",
      "header_image": null,
      "banner_image": null,
      "menu_image": null,
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "priority": 6,
      "flag": 0
    },
    {
      "id": 10,
      "name": "Test #5",
      "rv_description": "",
      "description": "",
      "header_image": null,
      "banner_image": null,
      "menu_image": null,
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "priority": 8,
      "flag": 1
    }
  ]
}
```
