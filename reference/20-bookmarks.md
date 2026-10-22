# お気に入り

Bカートでは商品を「お気に入り」に登録できます

## GET {{api_url}}/api/v1/bookmarks/1

**レスポンス例（200 OK）:**

```json
{
  "bookmark": {
    "id": 1,
    "customer_id": 1,
    "product_id": 17,
    "updated_at": "2012-11-06 15:32:28"
  }
}
```

## GET {{api_url}}/api/v1/bookmarks

**URLパラメータ**

| パラメータ名 | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| limit | limit | 整数 |  | 指定した件数分のデータを取得します。指定なしの場合は20件、最大100件 |
| offset | offset | 整数 |  | 指定した値+1件目のデータからlimit分を取得します。指定しない場合は0 |
| ids | ID複数 | 整数 |  | 複数のお気に入りIDをカンマ区切りで指定 |
| fields | フィールド | 文字列 |  | 取得したいフィールドカンマ区切りで指定 |
| customer_id | 会員ID | 整数 | 8 |  |
| product_id | 商品ID | 整数 | 255 |  |
| updated_at | 追加日 | 日付 | 19 | Y-m-d H:i:s |

## 拡張パラメータによる高度な絞り込み

拡張パラメータを使用することで、より高度な絞り込みが可能です。

詳しくは、[パラメータ](../docs/04-parameters.md)の「拡張パラメータ」欄をご参照ください。

**レスポンス例（200 OK）:**

```json
{
  "bookmarks": [
    {
      "id": 1,
      "customer_id": 1,
      "product_id": 17,
      "updated_at": "2012-11-06 15:32:28"
    },
    {
      "id": 2,
      "customer_id": 1,
      "product_id": 30,
      "updated_at": "2012-10-11 15:12:46"
    },
    {
      "id": 3,
      "customer_id": 1,
      "product_id": 31,
      "updated_at": "2012-11-16 10:49:38"
    },
    {
      "id": 4,
      "customer_id": 1,
      "product_id": 37,
      "updated_at": "2012-11-03 15:56:56"
    },
    {
      "id": 5,
      "customer_id": 1,
      "product_id": 38,
      "updated_at": "2012-10-15 20:00:34"
    },
    {
      "id": 6,
      "customer_id": 1,
      "product_id": 41,
      "updated_at": "2012-11-05 17:13:23"
    },
    {
      "id": 7,
      "customer_id": 10018,
      "product_id": 12,
      "updated_at": "2012-04-26 20:59:11"
    },
    {
      "id": 8,
      "customer_id": 10018,
      "product_id": 16,
      "updated_at": "2012-06-01 18:20:34"
    },
    {
      "id": 9,
      "customer_id": 10021,
      "product_id": 5,
      "updated_at": "2014-04-02 11:46:18"
    },
    {
      "id": 10,
      "customer_id": 10021,
      "product_id": 13,
      "updated_at": "2014-04-02 11:46:09"
    },
    {
      "id": 11,
      "customer_id": 10022,
      "product_id": 4,
      "updated_at": "2014-04-02 11:52:59"
    },
    {
      "id": 12,
      "customer_id": 10022,
      "product_id": 12,
      "updated_at": "2014-04-02 11:52:54"
    },
    {
      "id": 13,
      "customer_id": 10022,
      "product_id": 21,
      "updated_at": "2014-04-02 11:52:51"
    },
    {
      "id": 14,
      "customer_id": 10022,
      "product_id": 24,
      "updated_at": "2014-04-02 11:52:49"
    },
    {
      "id": 15,
      "customer_id": 10022,
      "product_id": 25,
      "updated_at": "2014-04-02 11:52:45"
    },
    {
      "id": 16,
      "customer_id": 10032,
      "product_id": 42,
      "updated_at": "2016-11-10 12:11:35"
    },
    {
      "id": 17,
      "customer_id": 10037,
      "product_id": 21,
      "updated_at": "2015-07-03 11:57:12"
    },
    {
      "id": 18,
      "customer_id": 10037,
      "product_id": 23,
      "updated_at": "2015-07-03 11:57:18"
    },
    {
      "id": 19,
      "customer_id": 10037,
      "product_id": 55,
      "updated_at": "2017-07-11 10:17:43"
    }
  ],
  "meta": {
    "limit": 20,
    "offset": 0,
    "total": 19
  }
}
```

## PATCH {{api_url}}/api/v1/bookmarks/1

**リクエストBODY**

| KEY | 名称 | 型 | 最大桁数 | 内容 | 
| --- | --- | --- | --- | --- |
| customer_id | 会員ID | 整数 | 8 |  |
| product_id | 商品ID | 整数 | 255 |  |

**リクエストボディ例:**

```json
{
  "product_id": 6
}
```

**レスポンス例（200 OK）:**

```json
{
  "bookmark": {
    "id": 1,
    "customer_id": 1,
    "product_id": 6,
    "updated_at": "2019-09-26 09:19:56"
  }
}
```

## PATCH {{api_url}}/api/v1/bookmarks/

**リクエストBODY**

| KEY | 名称 | 型 | 最大桁数 | 内容 | 
| --- | --- | --- | --- | --- |
| bookmarks[{:i}][id] | ID | 整数 | 255 | 必須 |
| bookmarks[{:i}][customer_id] | 会員ID | 整数 | 8 | 必須 |
| bookmarks[{:i}][product_id] | 商品ID | 整数 | 255 | 必須 |

**リクエストボディ例:**

```json
{
  "bookmarks": [
    {
      "id": 3,
      "product_id": 9
    },
    {
      "id": 4,
      "product_id": 8
    }
  ]
}
```

**レスポンス例（200 OK）:**

```json
{
  "bookmarks": [
    {
      "id": 3,
      "customer_id": 1,
      "product_id": 9,
      "updated_at": "2019-09-26 09:20:45"
    },
    {
      "id": 4,
      "customer_id": 1,
      "product_id": 8,
      "updated_at": "2019-09-26 09:20:45"
    }
  ]
}
```

## POST {{api_url}}/api/v1/bookmarks/

**リクエストBODY**

| KEY | 名称 | 型 | 最大桁数 | 内容 | 
| --- | --- | --- | --- | --- |
| bookmarks[{:i}][id] | ID | 整数 | 255 | 必須 |
| bookmarks[{:i}][customer_id] | 会員ID | 整数 | 8 | 必須 |
| bookmarks[{:i}][product_id] | 商品ID | 整数 | 255 | 必須 |

**リクエストボディ例:**

```json
{
  "bookmarks": [
    {
      "customer_id": 10,
      "product_id": 9
    },
    {
      "customer_id": 10,
      "product_id": 8
    }
  ]
}
```

**レスポンス例（201 Created）:**

```json
{
  "bookmarks": [
    {
      "id": 20,
      "customer_id": 10,
      "product_id": 9,
      "updated_at": "2019-09-26 09:21:00"
    },
    {
      "id": 21,
      "customer_id": 10,
      "product_id": 8,
      "updated_at": "2019-09-26 09:21:00"
    }
  ]
}
```
