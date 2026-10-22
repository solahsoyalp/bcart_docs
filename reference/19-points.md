# ポイント

Bカート内で利用できるポイント

## GET {{api_url}}/api/v1/points/1

**URIパラメータ**

| パラメータ名 | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| id | ポイントID | 整数 | 10 |  |
| customer_id | 会員ID | 整数 | 11 |  |
| order_id | 受注ID | 整数 | 11 |  |
| subject_id | 件名ID | 整数 | 11 |  |
| point | ポイント | 整数 | 11 |  |
| status | 状態 | 文字列 | 3 | 未処理,完了 |
| activated_at | ポイント付与日 | 文字列 | 19 | Y-m-d H:i:s |
| updated_at | 更新日 | 文字列 | 19 | Y-m-d H:i:s |
| created_at | 作成日 | 文字列 | 19 | Y-m-d H:i:s |

**レスポンス例（200 OK）:**

```json
{
  "point": {
    "id": 1,
    "customer_id": 1,
    "order_id": null,
    "subject_id": 4,
    "point": 300,
    "status": "完了",
    "activated_at": "2019-05-17 13:06:55",
    "updated_at": null,
    "created_at": "2019-05-17 13:06:55"
  }
}
```

## GET {{api_url}}/api/v1/points

**URIパラメータ**

| パラメータ名 | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| limit | limit | 整数 |  | 指定した件数分のデータを取得します。指定なしの場合は20件、最大100件 |
| offset | offset | 整数 |  | 指定した値+1件目のデータからlimit分を取得します。指定しない場合は0 |
| ids | ID複数 | 整数 |  | 複数のポイントIDをカンマ区切りで指定 |
| fields | フィールド | 文字列 |  | 取得したいフィールドカンマ区切りで指定 |
| customer_id | 会員ID | 整数 | 11 |  |
| order_id | 受注ID | 整数 | 11 |  |
| subject_id | 件名ID | 整数 | 11 |  |
| point | ポイント | 整数 | 11 |  |
| status | 状態 | 文字列 | 3 | 未処理,完了 |

## 拡張パラメータによる高度な絞り込み

拡張パラメータを使用することで、より高度な絞り込みが可能です。

詳しくは、[パラメータ](../docs/04-parameters.md)の「拡張パラメータ」欄をご参照ください。

**レスポンス例（200 OK）:**

```json
{
  "points": [
    {
      "id": 1,
      "customer_id": 1,
      "order_id": null,
      "subject_id": 4,
      "point": 300,
      "status": "完了",
      "activated_at": "2019-05-17 13:06:55",
      "updated_at": null,
      "created_at": "2019-05-17 13:06:55"
    },
    {
      "id": 2,
      "customer_id": 10034,
      "order_id": null,
      "subject_id": 4,
      "point": 300,
      "status": "未処理",
      "activated_at": null,
      "updated_at": null,
      "created_at": "2019-05-17 13:07:13"
    }
  ],
  "meta": {
    "limit": 20,
    "offset": 0,
    "total": 2
  }
}
```

## PATCH {{api_url}}/api/v1/points/1

**リクエストBODY**

| KEY | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| customer_id | 会員ID | 整数 | 11 | 項目存在時必須 |
| order_id | 受注ID | 整数 | 11 |  |
| subject_id | 件名ID | 整数 | 11 |  |
| point | ポイント | 整数 | 11 | 項目存在時必須 |
| status | 状態 | 文字列 | 3 | 項目存在時必須 未処理,完了 |
| updated_at | 更新日 | 文字列 | 19 | Y-m-d H:i:s |
| created_at | 作成日 | 文字列 | 19 | Y-m-d H:i:s |

**リクエストボディ例:**

```json
{
  "point": 1200
}
```

**レスポンス例（200 OK）:**

```json
{
  "point": {
    "id": 1,
    "customer_id": 1,
    "order_id": null,
    "subject_id": 4,
    "point": 1200,
    "status": "完了",
    "activated_at": "2019-05-17 13:06:55",
    "updated_at": "2019-09-26 09:18:47",
    "created_at": "2019-05-17 13:06:55"
  }
}
```

## PATCH {{api_url}}/api/v1/points/

**リクエストBODY**

| KEY | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| points\[{{i}}\]\[id\] | ポイントID | 整数 | 10 | 必須 |
| points\[{{i}}\]\[customer_id\] | 会員ID | 整数 | 11 | 項目存在時必須 |
| points\[{{i}}\]\[order_id\] | 受注ID | 整数 | 11 |  |
| points\[{{i}}\]\[subject_id\] | 件名ID | 整数 | 11 |  |
| points\[{{i}}\]\[point\] | ポイント | 整数 | 11 | 項目存在時必須 |
| points\[{{i}}\]\[status\] | 状態 | 文字列 | 3 | 項目存在時必須 未処理,完了 |
| points\[{{i}}\]\[updated_at\] | 更新日 | 文字列 | 19 | Y-m-d H:i:s |
| points\[{{i}}\]\[created_at\] | 作成日 | 文字列 | 19 | Y-m-d H:i:s |

※ {{i}}は配列のキー

**リクエストボディ例:**

```json
{
  "points": [
    {
      "id": 1,
      "point": 1600,
      "status": "未処理"
    },
    {
      "id": 2,
      "point": -200
    }
  ]
}
```

**レスポンス例（200 OK）:**

```json
{
  "points": [
    {
      "id": 1,
      "customer_id": 1,
      "order_id": null,
      "subject_id": 4,
      "point": 1600,
      "status": "未処理",
      "activated_at": null,
      "updated_at": "2019-09-26 09:18:58",
      "created_at": "2019-05-17 13:06:55"
    },
    {
      "id": 2,
      "customer_id": 10034,
      "order_id": null,
      "subject_id": 4,
      "point": -200,
      "status": "未処理",
      "activated_at": null,
      "updated_at": "2019-09-26 09:18:58",
      "created_at": "2019-05-17 13:07:13"
    }
  ]
}
```

## POST {{api_url}}/api/v1/points/

**リクエストBODY**

| KEY | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| points\[{{i}}\]\[customer_id\] | 会員ID | 整数 | 11 | 必須 |
| points\[{{i}}\]\[order_id\] | 受注ID | 整数 | 11 |  |
| points\[{{i}}\]\[subject_id\] | 件名ID | 整数 | 11 |  |
| points\[{{i}}\]\[point\] | ポイント | 整数 | 11 | 必須 |
| points\[{{i}}\]\[status\] | 状態 | 文字列 | 3 | 必須 未処理,完了 |
| points\[{{i}}\]\[updated_at\] | 更新日 | 文字列 | 19 | Y-m-d H:i:s |
| points\[{{i}}\]\[created_at\] | 作成日 | 文字列 | 19 | Y-m-d H:i:s |

※ {{i}}は配列のキー

**リクエストボディ例:**

```json
{
  "points": [
    {
      "point": 2600,
      "customer_id": 1,
      "order_id": null,
      "status": "未処理",
      "subject_id": 4
    },
    {
      "id": 2,
      "customer_id": 2,
      "order_id": 131,
      "point": 4600,
      "status": "未処理",
      "subject_id": 2
    },
    {
      "customer_id": 2,
      "order_id": 131,
      "point": 200,
      "status": "完了",
      "subject_id": 2
    },
    {
      "customer_id": 2,
      "order_id": 131,
      "point": 200,
      "status": "完了",
      "subject_id": 2
    }
  ]
}
```

**レスポンス例（201 Created）:**

```json
{
  "points": [
    {
      "id": 3,
      "customer_id": 1,
      "order_id": null,
      "subject_id": 4,
      "point": 2600,
      "status": "未処理",
      "activated_at": null,
      "updated_at": "2019-09-26 09:19:16",
      "created_at": "2019-09-26 09:19:16"
    },
    {
      "id": 4,
      "customer_id": 2,
      "order_id": 131,
      "subject_id": 2,
      "point": 4600,
      "status": "未処理",
      "activated_at": null,
      "updated_at": "2019-09-26 09:19:16",
      "created_at": "2019-09-26 09:19:16"
    },
    {
      "id": 5,
      "customer_id": 2,
      "order_id": 131,
      "subject_id": 2,
      "point": 200,
      "status": "完了",
      "activated_at": "2019-09-26 09:19:16",
      "updated_at": "2019-09-26 09:19:16",
      "created_at": "2019-09-26 09:19:16"
    },
    {
      "id": 6,
      "customer_id": 2,
      "order_id": 131,
      "subject_id": 2,
      "point": 200,
      "status": "完了",
      "activated_at": "2019-09-26 09:19:16",
      "updated_at": "2019-09-26 09:19:16",
      "created_at": "2019-09-26 09:19:16"
    }
  ]
}
```
