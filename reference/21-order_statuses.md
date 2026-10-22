# 受注ステータス

受注のステータス

## GET {{api_url}}/api/v1/order_statuses/%E3%82%AB%E3%82%B9%E3%82%BF%E3%83%A01

**レスポンス例（200 OK）:**

```json
{
  "order_status": [
    {
      "id": "カスタム1",
      "label": "カスタム項目1",
      "system_defined": 0
    }
  ]
}
```

## GET {{api_url}}/api/v1/order_statuses

**レスポンス例（200 OK）:**

```json
{
  "order_statuses": [
    {
      "id": "新規注文",
      "label": "新規注文",
      "system_defined": 1
    },
    {
      "id": "キャンセル",
      "label": "キャンセル",
      "system_defined": 1
    },
    {
      "id": "完了",
      "label": "完了",
      "system_defined": 1
    },
    {
      "id": "送信未完",
      "label": "送信未完",
      "system_defined": 1
    },
    {
      "id": "決済未完了（クレジット）",
      "label": "決済未完了（クレジット）",
      "system_defined": 1
    },
    {
      "id": "カスタム1",
      "label": "カスタム項目1",
      "system_defined": 0
    },
    {
      "id": "カスタム2",
      "label": "(カスタム)見積中",
      "system_defined": 0
    },
    {
      "id": "カスタム3",
      "label": "(カスタム)入荷待ち",
      "system_defined": 0
    },
    {
      "id": "カスタム4",
      "label": "(カスタム)保留",
      "system_defined": 0
    },
    {
      "id": "カスタム5",
      "label": "任意のステータスを作成できます",
      "system_defined": 0
    }
  ],
  "meta": {
    "limit": 20,
    "offset": 0,
    "total": 10
  }
}
```

## PATCH {{api_url}}/api/v1/order_statuses/%E3%82%AB%E3%82%B9%E3%82%BF%E3%83%A01

**リクエストボディ例:**

```json
{
  "label": "updated 1"
}
```

**レスポンス例（200 OK）:**

```json
{
  "order_status": {
    "id": "カスタム1",
    "label": "updated 1",
    "system_defined": 0
  }
}
```

## PATCH {{api_url}}/api/v1/order_statuses/

**リクエストボディ例:**

```json
{
  "order_statuses": [
    {
      "id": "カスタム2",
      "label": "updated"
    },
    {
      "id": "カスタム3",
      "label": "updated"
    }
  ]
}
```

**レスポンス例（200 OK）:**

```json
{
  "order_statuses": [
    {
      "id": "カスタム2",
      "label": "updated",
      "system_defined": 0
    },
    {
      "id": "カスタム3",
      "label": "updated",
      "system_defined": 0
    }
  ]
}
```

## POST {{api_url}}/api/v1/order_statuses/

**リクエストボディ例:**

```json
{
  "order_statuses": [
    {
      "label": "foo"
    },
    {
      "label": "bar"
    }
  ]
}
```

**レスポンス例（201 Created）:**

```json
{
  "order_statuses": [
    {
      "id": "カスタム6",
      "label": "foo",
      "system_defined": 0
    },
    {
      "id": "カスタム7",
      "label": "bar",
      "system_defined": 0
    }
  ]
}
```
