# Webhook

BカートのWebhookをAPIから取得・登録・変更・削除することができます。

Webhookの説明や活用事例は[こちら](https://bcart.jp/functions/detail/158/)をご確認ください。

## GET {{api_url}}/api/v1/webhooks/0b1f1fc2-e567-4ce4-ac44-6d1856049a1a

**レスポンス一覧**

| パラメータ名 | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| id | Webhook ID | UUID | 36 |  |
| name | Webhook名 | 文字列 | 255 |  |
| uri | Webhook URL | 文字列 | 255 | 通知先URL |
| secret | シークレット | 文字列 | 255 | Webhook署名検証用のシークレットキー |
| events | イベント | 配列 | \- | 通知対象のイベント名リスト（注文登録=order.created・注文変更=order.updated・会員登録=customer.created・会員変更=customer.updated・別配送先登録=other_address.created・別配送先変更=other_address.updated） |
| enabled | 状態 | 真偽値 | 1 | true=有効, false=無効 |
| created_at | 登録日時 | 日時 | 19 | Y-m-d H:i:s |
| updated_at | 更新日時 | 日時 | 19 | Y-m-d H:i:s |

**レスポンス例:**

```json
{
  "webhook": {
    "id": "0b1f1fc2-e567-4ce4-ac44-6d1856049a1a",
    "name": "webhook1234",
    "uri": "https://example.com/webhook/endpoint1",
    "secret": "!#$%\"&'()*+,-./:;<=>?@[\\]^_{|}~ 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
    "events": [
      "order.updated",
      "customer.updated"
    ],
    "enabled": true,
    "created_at": "2025-09-30T02:00:11.523687+00:00",
    "updated_at": "2025-09-30T02:00:12.504730+00:00"
  }
}
```

## GET {{api_url}}/api/v1/webhooks

**URLパラメータ**
なし

**レスポンス例:**

```json
{
    "webhooks": [
        {
            "id": "0b1f1fc2-e567-4ce4-ac44-6d1856049a1a",
            "name": "webhook1234",
            "uri": "https://example.com/webhook/endpoint1",
            "secret": "!#$%\"&'()*+,-./:;<=>?@[\\]^_{|}~ 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
            "events": [
                "order.updated",
                "customer.updated"
            ],
            "enabled": true,
            "created_at": "2025-09-30T02:00:11.523687+00:00",
            "updated_at": "2025-09-30T02:00:12.504730+00:00"
        },
        {
            "id": "14ff8fd0-c7b0-457e-8ab1-187323ff231e",
            "name": "webhook5678",
            "uri": ""https://example.com/webhook/endpoint2",
            "secret": "!#$%\"&'()*+,-./:;<=>?@[\\]^_{|}~ 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
            "events": [
                "order.updated",
                "customer.created",
                "customer.updated"
            ],
            "enabled": true,
            "created_at": "2025-09-16T05:58:51.681871+00:00",
            "updated_at": "2025-09-16T05:58:52.660984+00:00"
        },
        {
            "id": "2181b025-bfc7-4997-ab2a-74a4dd114181",
            "name": "webhookABCD",
            "uri": "https://example.com/webhook/endpoint3",
            "secret": "!#$%\"&'()*+,-./:;<=>?@[\\]^_{|}~ 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
            "events": [
                "order.updated"
            ],
            "enabled": true,
            "created_at": "2025-09-11T02:19:48.295079+00:00",
            "updated_at": "2025-09-11T02:19:48.414778+00:00"
        }
    ],
    "meta": {
        "total": 3
    }
}
```

## PATCH {{api_url}}/api/v1/webhooks/0b1f1fc2-e567-4ce4-ac44-6d1856049a1a

**リクエストBODY**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| name | Webhook名 | 文字列 | 255 | 項目存在時必須 |
| uri | Webhook URL | 文字列 | 255 | コールバック先のURL  <br>項目存在時必須 |
| secret | シークレット | 文字列 | 255 | Webhook署名検証用のシークレットキー  <br>項目存在時必須  <br>36文字以上  <br>半角英数記号 |
| events | イベント | 配列 | \- | 通知対象のイベント名リスト（注文登録=order.created・注文変更=order.updated・会員登録=customer.created・会員変更=customer.updated・別配送先登録=other_address.created・別配送先変更=other_address.updated）  <br>項目存在時必須 |
| enabled | 状態 | 真偽値 | 1 | true=有効, false=無効  <br>項目存在時必須 |

**リクエストボディ例:**

```json
{
  "secret": "!#$%\"&'()*+,-./:;<=>?@[\\]^_{|}~ 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzｦｧｨｩｪｫｬｭｮｯｰｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝﾞﾟ",
  "events": [
    "order.created",
    "order.updated",
    "customer.created",
    "customer.updated",
    "other_address.created",
    "other_address.updated"
  ]
}
```

**レスポンス例:**

```json
{
  "webhook": {
    "id": "0b1f1fc2-e567-4ce4-ac44-6d1856049a1a",
    "name": "webhook1234",
    "uri": "https://example.com/webhook/endpoint1",
    "secret": "!#$%\"&'()*+,-./:;<=>?@[\\]^_{|}~ 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
    "events": [
      "order.created",
      "order.updated",
      "customer.created",
      "customer.updated",
      "other_address.created",
      "other_address.updated"
    ],
    "enabled": true,
    "created_at": "2025-09-30T02:00:11.523687+00:00",
    "updated_at": "2025-09-30T02:00:12.504730+00:00"
  }
}
```

## POST {{api_url}}/api/v1/webhooks

**リクエストBODY**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| name | Webhook名 | 文字列 | 255 | 必須 |
| uri | Webhook URL | 文字列 | 255 | コールバック先のURL  <br>必須 |
| secret | シークレット | 文字列 | 255 | Webhook署名検証用のシークレットキー  <br>必須  <br>36文字以上  <br>半角英数記号 |
| events | イベント | 配列 | \- | 通知対象のイベント名リスト（注文登録=order.created・注文変更=order.updated・会員登録=customer.created・会員変更=customer.updated・別配送先登録=other_address.created・別配送先変更=other_address.updated）  <br>必須 |
| enabled | 状態 | 真偽値 | 1 | true=有効, false=無効  <br>必須 |

**リクエストボディ例:**

```json
{
  "name": "webhookEFGH",
  "uri": "https://example.com/webhook/endpoint4",
  "secret": "secret_secret_secret_secret_secret_secret",
  "events": [
    "order.updated",
    "customer.updated"
  ],
  "enabled": true
}
```

**レスポンス例:**

```json
{
  "webhook": {
    "id": "9dbf8a26-c0ee-42ca-a6c2-da7517148654",
    "name": "webhookEFGH",
    "uri": "https://example.com/webhook/endpoint4",
    "secret": "!#$%\"&'()*+,-./:;<=>?@[\\]^_{|}~ 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
    "events": [
      "order.updated",
      "customer.updated"
    ],
    "enabled": true,
    "created_at": "2025-10-09T01:42:29.364708+00:00",
    "updated_at": "2025-10-09T01:42:29.364716+00:00"
  }
}
```

## DELETE {{api_url}}/api/v1/webhooks/139104dd-b020-4cb5-80a2-3cc9205a1166

**レスポンス例:**

```json
{}
```
