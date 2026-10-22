# 商品カテゴリ

商品のカテゴリ

## GET {{api_url}}/api/v1/categories/9

**レスポンス例（200 OK）:**

```json
{
  "category": {
    "id": 9,
    "name": "コンタクトレンズ",
    "description": "<div class=\"free-space\">\r\n<p><a href=\"https://bcart.jp/example/category/10/\" target=\"_blank\"><img style=\"width: 100%;\" src=\"uploads/sample/banner/category_top.jpg\" alt=\"導入事例\" /></a></p>\r\nここにはカテゴリの説明が表示できます（<strong style=\"#f00\">HTML可</strong>）。</div>",
    "rv_description": "<div class=\"free-space\">\r\n<p><a href=\"https://bcart.jp/example/category/10/\" target=\"_blank\"><img style=\"width: 100%;\" src=\"uploads/sample/banner/category_top.jpg\" alt=\"導入事例\" /></a></p>\r\nここにはカテゴリの説明が表示できます（<strong style=\"#f00\">HTML可</strong>）。</div>",
    "parent_category_id": null,
    "header_image": null,
    "banner_image": null,
    "menu_image": null,
    "meta_title": "",
    "meta_keywords": "",
    "meta_description": "",
    "priority": -9,
    "flag": 1
  }
}
```

## GET {{api_url}}/api/v1/categories

**URIパラメータ**

| パラメータ名 | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| limit | limit | 整数 |  | 指定した件数分のデータを取得します。指定なしの場合は20件、最大100件 |
| offset | offset | 整数 |  | 指定した値+1件目のデータからlimit分を取得します。指定しない場合は0 |
| ids | ID複数 | 整数 |  | 複数の商品カテゴリIDをカンマ区切りで指定 |
| fields | フィールド | 文字列 |  | 取得したいフィールドカンマ区切りで指定 |
| name | カテゴリ名 | 文字列 | 255 |  |
| parent_category_id | 親カテゴリID | 整数 | 11 |  |
| flag | 表示フラグ | 整数 | 1 | 0（非表示）/1（表示） |

## 拡張パラメータによる高度な絞り込み

拡張パラメータを使用することで、より高度な絞り込みが可能です。

詳しくは、[パラメータ](../docs/04-parameters.md)の「拡張パラメータ」欄をご参照ください。

**レスポンス例（200 OK）:**

```json
{
  "categories": [
    {
      "id": 9,
      "name": "コンタクトレンズ",
      "description": "<div class=\"free-space\">\r\n<p><a href=\"https://bcart.jp/example/category/10/\" target=\"_blank\"><img style=\"width: 100%;\" src=\"uploads/sample/banner/category_top.jpg\" alt=\"導入事例\" /></a></p>\r\nここにはカテゴリの説明が表示できます（<strong style=\"#f00\">HTML可</strong>）。</div>",
      "rv_description": "<div class=\"free-space\">\r\n<p><a href=\"https://bcart.jp/example/category/10/\" target=\"_blank\"><img style=\"width: 100%;\" src=\"uploads/sample/banner/category_top.jpg\" alt=\"導入事例\" /></a></p>\r\nここにはカテゴリの説明が表示できます（<strong style=\"#f00\">HTML可</strong>）。</div>",
      "parent_category_id": null,
      "header_image": null,
      "banner_image": null,
      "menu_image": null,
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "priority": -9,
      "flag": 1
    },
    {
      "id": 10,
      "name": "家電・AV・コンピューター",
      "description": "<div class=\"free-space\">\r\n<p><a href=\"https://bcart.jp/example/category/7/\" target=\"_blank\"><img style=\"width: 100%;\" src=\"uploads/sample/banner/category_top.jpg\" alt=\"導入事例\" /></a></p>\r\nここにはカテゴリの説明が表示できます（<strong style=\"#f00\">HTML可</strong>）。</div>",
      "rv_description": "<div class=\"free-space\">\r\n<p><a href=\"https://bcart.jp/example/category/7/\" target=\"_blank\"><img style=\"width: 100%;\" src=\"uploads/sample/banner/category_top.jpg\" alt=\"導入事例\" /></a></p>\r\nここにはカテゴリの説明が表示できます（<strong style=\"#f00\">HTML可</strong>）。</div>",
      "parent_category_id": null,
      "header_image": null,
      "banner_image": null,
      "menu_image": null,
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "priority": -60,
      "flag": 0
    },
    {
      "id": 11,
      "name": "建築建材・工業用品",
      "description": "<div class=\"free-space\">\r\n<p><a href=\"https://bcart.jp/example/category/9/\" target=\"_blank\"><img style=\"width: 100%;\" src=\"uploads/sample/banner/category_top.jpg\" alt=\"導入事例\" /></a></p>\r\nここにはカテゴリの説明が表示できます（<strong style=\"#f00\">HTML可</strong>）。</div>",
      "rv_description": "<div class=\"free-space\">\r\n<p><a href=\"https://bcart.jp/example/category/9/\" target=\"_blank\"><img style=\"width: 100%;\" src=\"uploads/sample/banner/category_top.jpg\" alt=\"導入事例\" /></a></p>\r\nここにはカテゴリの説明が表示できます（<strong style=\"#f00\">HTML可</strong>）。</div>",
      "parent_category_id": null,
      "header_image": null,
      "banner_image": null,
      "menu_image": null,
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "priority": -8,
      "flag": 1
    },
    {
      "id": 12,
      "name": "自転車・サイクルパーツ",
      "description": "<div class=\"free-space\">\r\n<p><a href=\"https://bcart.jp/example/category/12/\" target=\"_blank\"><img style=\"width: 100%;\" src=\"uploads/sample/banner/category_top.jpg\" alt=\"導入事例\" /></a></p>\r\nここにはカテゴリの説明が表示できます（<strong style=\"#f00\">HTML可</strong>）。</div>",
      "rv_description": "<div class=\"free-space\">\r\n<p><a href=\"https://bcart.jp/example/category/12/\" target=\"_blank\"><img style=\"width: 100%;\" src=\"uploads/sample/banner/category_top.jpg\" alt=\"導入事例\" /></a></p>\r\nここにはカテゴリの説明が表示できます（<strong style=\"#f00\">HTML可</strong>）。</div>",
      "parent_category_id": null,
      "header_image": null,
      "banner_image": null,
      "menu_image": null,
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "priority": -11,
      "flag": 0
    },
    {
      "id": 17,
      "name": "インテリア",
      "description": "<div class=\"free-space\">\r\n<p><a href=\"https://bcart.jp/example/category/5/\" target=\"_blank\"><img style=\"width: 100%;\" src=\"uploads/sample/banner/category_top.jpg\" alt=\"導入事例\" /></a></p>\r\nここにはカテゴリの説明が表示できます（<strong style=\"#f00\">HTML可</strong>）。</div>",
      "rv_description": "<div class=\"free-space\">\r\n<p><a href=\"https://bcart.jp/example/category/5/\" target=\"_blank\"><img style=\"width: 100%;\" src=\"uploads/sample/banner/category_top.jpg\" alt=\"導入事例\" /></a></p>\r\nここにはカテゴリの説明が表示できます（<strong style=\"#f00\">HTML可</strong>）。</div>",
      "parent_category_id": null,
      "header_image": null,
      "banner_image": null,
      "menu_image": null,
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "priority": -4,
      "flag": 1
    },
    {
      "id": 18,
      "name": "ペット用品",
      "description": "<div class=\"free-space\">\r\n<p><a href=\"https://bcart.jp/example/category/11/\" target=\"_blank\"><img style=\"width: 100%;\" src=\"uploads/sample/banner/category_top.jpg\" alt=\"導入事例\" /></a></p>\r\nここにはカテゴリの説明が表示できます（<strong style=\"#f00\">HTML可</strong>）。</div>",
      "rv_description": "<div class=\"free-space\">\r\n<p><a href=\"https://bcart.jp/example/category/11/\" target=\"_blank\"><img style=\"width: 100%;\" src=\"uploads/sample/banner/category_top.jpg\" alt=\"導入事例\" /></a></p>\r\nここにはカテゴリの説明が表示できます（<strong style=\"#f00\">HTML可</strong>）。</div>",
      "parent_category_id": null,
      "header_image": null,
      "banner_image": null,
      "menu_image": null,
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "priority": -10,
      "flag": 0
    },
    {
      "id": 19,
      "name": "デスク※商品未登録カテゴリ例",
      "description": "",
      "rv_description": "",
      "parent_category_id": null,
      "header_image": null,
      "banner_image": null,
      "menu_image": null,
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "priority": -100,
      "flag": 0
    },
    {
      "id": 22,
      "name": "雑貨（生活・ファッション）",
      "description": "<div class=\"free-space\">\r\n<p><a href=\"https://bcart.jp/example/category/2/\" target=\"_blank\"><img style=\"width: 100%;\" src=\"uploads/sample/banner/category_top.jpg\" alt=\"導入事例\" /></a></p>\r\nここにはカテゴリの説明が表示できます（<strong style=\"#f00\">HTML可</strong>）。</div>",
      "rv_description": "<div class=\"free-space\">\r\n<p><a href=\"https://bcart.jp/example/category/2/\" target=\"_blank\"><img style=\"width: 100%;\" src=\"uploads/sample/banner/category_top.jpg\" alt=\"導入事例\" /></a></p>\r\nここにはカテゴリの説明が表示できます（<strong style=\"#f00\">HTML可</strong>）。</div>",
      "parent_category_id": null,
      "header_image": null,
      "banner_image": null,
      "menu_image": null,
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "priority": -20,
      "flag": 1
    },
    {
      "id": 23,
      "name": "食品・飲料",
      "description": "<div class=\"free-space\">\r\n<p><a href=\"https://bcart.jp/example/category/8/\" target=\"_blank\"><img style=\"width: 100%;\" src=\"uploads/sample/banner/category_top.jpg\" alt=\"導入事例\" /></a></p>\r\nここにはカテゴリの説明が表示できます（<strong style=\"#f00\">HTML可</strong>）。</div>",
      "rv_description": "<div class=\"free-space\">\r\n<p><a href=\"https://bcart.jp/example/category/8/\" target=\"_blank\"><img style=\"width: 100%;\" src=\"uploads/sample/banner/category_top.jpg\" alt=\"導入事例\" /></a></p>\r\nここにはカテゴリの説明が表示できます（<strong style=\"#f00\">HTML可</strong>）。</div>",
      "parent_category_id": null,
      "header_image": null,
      "banner_image": null,
      "menu_image": null,
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "priority": -7,
      "flag": 1
    },
    {
      "id": 24,
      "name": "ガラステーブル",
      "description": "",
      "rv_description": "",
      "parent_category_id": 17,
      "header_image": null,
      "banner_image": null,
      "menu_image": null,
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "priority": 0,
      "flag": 1
    },
    {
      "id": 30,
      "name": "青",
      "description": "",
      "rv_description": "",
      "parent_category_id": 24,
      "header_image": null,
      "banner_image": null,
      "menu_image": null,
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "priority": 0,
      "flag": 0
    },
    {
      "id": 31,
      "name": "店舗用品・オフィス用品",
      "description": "<div class=\"free-space\">\r\n<p><a href=\"https://bcart.jp/example/category/6/\" target=\"_blank\"><img style=\"width: 100%;\" src=\"uploads/sample/banner/category_top.jpg\" alt=\"導入事例\" /></a></p>\r\nここにはカテゴリの説明が表示できます（<strong style=\"#f00\">HTML可</strong>）。</div>",
      "rv_description": "<div class=\"free-space\">\r\n<p><a href=\"https://bcart.jp/example/category/6/\" target=\"_blank\"><img style=\"width: 100%;\" src=\"uploads/sample/banner/category_top.jpg\" alt=\"導入事例\" /></a></p>\r\nここにはカテゴリの説明が表示できます（<strong style=\"#f00\">HTML可</strong>）。</div>",
      "parent_category_id": null,
      "header_image": null,
      "banner_image": null,
      "menu_image": null,
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "priority": -10,
      "flag": 1
    },
    {
      "id": 32,
      "name": "ウッドテーブル",
      "description": "",
      "rv_description": "",
      "parent_category_id": 17,
      "header_image": null,
      "banner_image": null,
      "menu_image": null,
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "priority": 0,
      "flag": 0
    },
    {
      "id": 33,
      "name": "ステンレステーブル",
      "description": "",
      "rv_description": "",
      "parent_category_id": 17,
      "header_image": null,
      "banner_image": null,
      "menu_image": null,
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "priority": 0,
      "flag": 0
    },
    {
      "id": 35,
      "name": "アパレル",
      "description": "<div class=\"free-space\">\r\n<p><a href=\"https://bcart.jp/example/category/1/\" target=\"_blank\"><img style=\"width: 100%;\" src=\"uploads/sample/banner/category_top.jpg\" alt=\"導入事例\" /></a></p>\r\nここにはカテゴリの説明が表示できます（<strong style=\"#f00\">HTML可</strong>）。</div>",
      "rv_description": "<div class=\"free-space\">\r\n<p><a href=\"https://bcart.jp/example/category/1/\" target=\"_blank\"><img style=\"width: 100%;\" src=\"uploads/sample/banner/category_top.jpg\" alt=\"導入事例\" /></a></p>\r\nここにはカテゴリの説明が表示できます（<strong style=\"#f00\">HTML可</strong>）。</div>",
      "parent_category_id": null,
      "header_image": null,
      "banner_image": null,
      "menu_image": null,
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "priority": 0,
      "flag": 1
    },
    {
      "id": 36,
      "name": "サプリメント・健康食品",
      "description": "<div class=\"free-space\">\r\n<p><a href=\"https://bcart.jp/example/category/4/\" target=\"_blank\"><img style=\"width: 100%;\" src=\"uploads/sample/banner/category_top.jpg\" alt=\"導入事例\" /></a></p>\r\nここにはカテゴリの説明が表示できます（<strong style=\"#f00\">HTML可</strong>）。</div>",
      "rv_description": "<div class=\"free-space\">\r\n<p><a href=\"https://bcart.jp/example/category/4/\" target=\"_blank\"><img style=\"width: 100%;\" src=\"uploads/sample/banner/category_top.jpg\" alt=\"導入事例\" /></a></p>\r\nここにはカテゴリの説明が表示できます（<strong style=\"#f00\">HTML可</strong>）。</div>",
      "parent_category_id": null,
      "header_image": null,
      "banner_image": null,
      "menu_image": null,
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "priority": -9,
      "flag": 1
    },
    {
      "id": 37,
      "name": "玩具",
      "description": "<div class=\"free-space\">\r\n<p><a href=\"https://bcart.jp/example/category/14/\" target=\"_blank\"><img style=\"width: 100%;\" src=\"uploads/sample/banner/category_top.jpg\" alt=\"導入事例\" /></a></p>\r\nここにはカテゴリの説明が表示できます（<strong style=\"#f00\">HTML可</strong>）。</div>",
      "rv_description": "<div class=\"free-space\">\r\n<p><a href=\"https://bcart.jp/example/category/14/\" target=\"_blank\"><img style=\"width: 100%;\" src=\"uploads/sample/banner/category_top.jpg\" alt=\"導入事例\" /></a></p>\r\nここにはカテゴリの説明が表示できます（<strong style=\"#f00\">HTML可</strong>）。</div>",
      "parent_category_id": null,
      "header_image": null,
      "banner_image": null,
      "menu_image": null,
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "priority": -12,
      "flag": 0
    },
    {
      "id": 38,
      "name": "カラーコンタクト",
      "description": "",
      "rv_description": "",
      "parent_category_id": 9,
      "header_image": null,
      "banner_image": null,
      "menu_image": null,
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "priority": 0,
      "flag": 1
    },
    {
      "id": 39,
      "name": "医療用コンタクト",
      "description": "",
      "rv_description": "",
      "parent_category_id": 9,
      "header_image": null,
      "banner_image": null,
      "menu_image": null,
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "priority": 0,
      "flag": 1
    },
    {
      "id": 40,
      "name": "1day(1日使い捨て用)",
      "description": "",
      "rv_description": "",
      "parent_category_id": 39,
      "header_image": null,
      "banner_image": null,
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
    "total": 44
  }
}
```

## PATCH {{api_url}}/api/v1/categories/30

**リクエストBODY**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| name | カテゴリ名 | 文字列 | 255 | 項目存在時必須 |
| description | カテゴリ説明（PC） | 文字列 | 65,535 |  |
| rv_description | カテゴリ説明（レスポンシブ） | 文字列 | 65,535 |  |
| parent_category_id | 親カテゴリID | 整数 | 11 |  |
| header_image | ヘッダー画像パス | 文字列 | 255 |  |
| banner_image | バナー画像パス | 文字列 |255 |  |
| menu_image | メニュー画像パス | 文字列 |255 |  |
| meta_title | meta title | 文字列 | 255 |  |
| meta_keywords | meta keywords | 文字列 | 255 |  |
| meta_description | meta description | 文字列 | 255 |  |
| priority | 表示優先度 | 整数 | 4 |  |
| flag | 表示フラグ | 整数 | 1 | 0（非表示）/1（表示） |

**リクエストボディ例:**

```json
{
  "name": "Cat 1 updated",
  "description": "Cat 1 Desc updated",
  "rv_description": "Cat 1 RV Desc updated",
  "header_image": "cat1_header_updated.png",
  "banner_image": "cat1_banner_updated.png",
  "menu_image": "cat1_menu_updated.png",
  "priority": 120,
  "flag": 0,
  "parent_category_id": 24
}
```

**レスポンス例（200 OK）:**

```json
{
  "category": {
    "id": 30,
    "name": "Cat 1 updated",
    "description": "Cat 1 Desc updated",
    "rv_description": "Cat 1 RV Desc updated",
    "parent_category_id": 24,
    "header_image": "cat1_header_updated.png",
    "banner_image": "cat1_banner_updated.png",
    "menu_image": "cat1_menu_updated.png",
    "meta_title": "",
    "meta_keywords": "",
    "meta_description": "",
    "priority": 120,
    "flag": 0
  }
}
```

## PATCH {{api_url}}/api/v1/categories/

**リクエストBODY**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| categories[{{id}}][name] | カテゴリ名 | 文字列 | 255 | 項目存在時必須 |
| categories[{{id}}][description] | カテゴリ説明（PC） | 文字列 | 65,535 |  |
| categories[{{id}}][rv_description] | カテゴリ説明（レスポンシブ） | 文字列 | 65,535 |  |
| categories[{{id}}][parent_category_id] | 親カテゴリID | 整数 | 11 |  |
| categories[{{id}}][header_image] | ヘッダー画像パス | 文字列 | 255 |  |
| categories[{{id}}][banner_image] | バナー画像パス | 文字列 |255 |  |
| categories[{{id}}][menu_image] | メニュー画像パス | 文字列 |255 |  |
| categories[{{id}}][meta_title] | meta title | 文字列 | 255 |  |
| categories[{{id}}][meta_keywords] | meta keywords | 文字列 | 255 |  |
| categories[{{id}}][meta_description] | meta description | 文字列 | 255 |  |
| categories[{{id}}][priority] | 表示優先度 | 整数 | 4 |  |
| categories[{{id}}][flag] | 表示フラグ | 整数 | 1 | 0（非表示）/1（表示） |

**リクエストボディ例:**

```json
{
  "categories": [
    {
      "id": 30,
      "name": "Cat 2 updated",
      "description": "Cat 2 Desc updated",
      "rv_description": "Cat 2 RV Desc updated",
      "header_image": "cat2_header_updated.png",
      "banner_image": "cat2_banner_updated.png",
      "menu_image": "cat2_menu_updated.png",
      "priority": -10,
      "flag": 0,
      "parent_category_id": 24
    },
    {
      "id": 47,
      "name": "Cat 1 updated again",
      "description": "Cat 1 Desc",
      "menu_image": "cat1_menu.png",
      "priority": 10,
      "flag": 1
    }
  ]
}
```

**レスポンス例（200 OK）:**

```json
{
  "categories": [
    {
      "id": 30,
      "name": "Cat 2 updated",
      "description": "Cat 2 Desc updated",
      "rv_description": "Cat 2 RV Desc updated",
      "parent_category_id": 24,
      "header_image": "cat2_header_updated.png",
      "banner_image": "cat2_banner_updated.png",
      "menu_image": "cat2_menu_updated.png",
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "priority": -10,
      "flag": 0
    },
    {
      "id": 47,
      "name": "Cat 1 updated again",
      "description": "Cat 1 Desc",
      "rv_description": "",
      "parent_category_id": null,
      "header_image": null,
      "banner_image": null,
      "menu_image": "cat1_menu.png",
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "priority": 10,
      "flag": 1
    }
  ]
}
```

## POST {{api_url}}/api/v1/categories/

**リクエストBODY**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| categories[{{id}}][name] | カテゴリ名 | 文字列 | 255 | 項目存在時必須 |
| categories[{{id}}][description] | カテゴリ説明（PC） | 文字列 | 65,535 |  |
| categories[{{id}}][rv_description] | カテゴリ説明（レスポンシブ） | 文字列 | 65,535 |  |
| categories[{{id}}][parent_category_id] | 親カテゴリID | 整数 | 11 |  |
| categories[{{id}}][header_image] | ヘッダー画像パス | 文字列 | 255 |  |
| categories[{{id}}][banner_image] | バナー画像パス | 文字列 |255 |  |
| categories[{{id}}][menu_image] | メニュー画像パス | 文字列 |255 |  |
| categories[{{id}}][meta_title] | meta title | 文字列 | 255 |  |
| categories[{{id}}][meta_keywords] | meta keywords | 文字列 | 255 |  |
| categories[{{id}}][meta_description] | meta description | 文字列 | 255 |  |
| categories[{{id}}][priority] | 表示優先度 | 整数 | 4 |  |
| categories[{{id}}][flag] | 表示フラグ | 整数 | 1 | 0（非表示）/1（表示） |

**リクエストボディ例:**

```json
{
  "categories": [
    {
      "name": "Cat 1",
      "description": "Cat 1 Desc",
      "rv_description": "Cat 1 RV Desc",
      "header_image": "cat1_header.png",
      "banner_image": "cat1_banner.png",
      "menu_image": "cat1_menu.png",
      "priority": 10,
      "flag": 1
    },
    {
      "name": "Cat 2",
      "description": "Cat 2 Desc",
      "rv_description": "Cat 2 RV Desc",
      "header_image": "cat2_header.png",
      "banner_image": "cat2_banner.png",
      "menu_image": "cat2_menu.png",
      "priority": -10,
      "flag": 0,
      "parent_category_id": 9
    }
  ]
}
```

**レスポンス例（201 Created）:**

```json
{
  "categories": [
    {
      "id": 68,
      "name": "Cat 1",
      "description": "Cat 1 Desc",
      "rv_description": "Cat 1 RV Desc",
      "parent_category_id": null,
      "header_image": "cat1_header.png",
      "banner_image": "cat1_banner.png",
      "menu_image": "cat1_menu.png",
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "priority": 10,
      "flag": 1
    },
    {
      "id": 69,
      "name": "Cat 2",
      "description": "Cat 2 Desc",
      "rv_description": "Cat 2 RV Desc",
      "parent_category_id": 9,
      "header_image": "cat2_header.png",
      "banner_image": "cat2_banner.png",
      "menu_image": "cat2_menu.png",
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "priority": -10,
      "flag": 0
    }
  ]
}
```
