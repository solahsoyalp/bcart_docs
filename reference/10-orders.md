# 受注

受注情報

## GET {{api_url}}/api/v1/orders/128

**レスポンス一覧**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| id | 受注ID | 整数 | 11 |  |
| code | 受注番号 | 整数 | 255 |  |
| customer_id | 注文者 会員ID | 整数 | 11 |  |
| customer_ext_id | 注文者 貴社独自会員ID | 文字列 | 255 |  |
| customer_parent_id | 注文者 親代理店ID | 文字列 | 255 |  |
| customer_salesman_id | 注文者 営業担当者ID | 文字列 | 255 | 営業担当者IDをカンマ区切り |
| customer_comp_name | 注文者 会社名 | 文字列 | 128 |  |
| customer_department | 注文者 部署名 | 文字列 | 255 |  |
| customer_name | 注文者名 | 文字列 | 128 |  |
| customer_tel | 注文者 電話番号 | 文字列 | 255 |  |
| customer_mobile_phone | 注文者 携帯番号 | 文字列 | 255 |  |
| customer_email | 注文者 メールアドレス | 文字列 | 255 |  |
| customer_price_group_id | 注文者 価格グループ名 | 文字列 | 255 | 通常会員の場合null,以外は会員価格グループ名 |
| customer_zip | 注文者 郵便番号 | 文字列 | 32 |  |
| customer_pref | 注文者 都道府県 | 文字列 | 32 |  |
| customer_address1 | 注文者 市町区村 | 文字列 | 255 |  |
| customer_address2 | 注文者 町域・番地 | 文字列 | 255 |  |
| customer_address3 | 注文者 ビル・建物名 | 文字列 | 255 |  |
| customer_customs | 注文者 カスタム項目 | 配列 |  |  |
| payment | 決済方法 | 文字列 | 255 |  |
| payment_at | 決済確認日 | 日付 | 10 | Y-m-d |
| total_price | 商品合計金額 | 数値 | 255 |  |
| tax | 消費税 | 整数 | 8 |  |
| tax_rate | 税率 | 数値 | 255 |  |
| COD_cost | 決済手数料 | 整数 | 8 |  |
| shipping_cost | 送料 | 整数 | 8 |  |
| final_price | 受注総額 | 整数 | 11 |  |
| use_point | ポイント利用 | 整数 | 255 |  |
| get_point | ポイント取得 | 整数 | 255 |  |
| order_totals | 税率ごとの合計金額 | 配列 |  | tax_rate=税率,total=税抜合計金額,tax=消費税,total_incl_tax=税込合計金額 |
| customer_message | お客様からの連絡事項 | 文字列 | 65,535 |  |
| admin_message | お客様への連絡事項 | 文字列 | 65,535 |  |
| memo | 管理用メモ | 文字列 | 65,535 |  |
| customs | 受注カスタム項目 | 配列 |  |  |
| enquete1 | アンケート1 | 文字列 | 255 |  |
| enquete2 | アンケート2 | 文字列 | 255 |  |
| enquete3 | アンケート3 | 文字列 | 255 |  |
| enquete4 | アンケート4 | 文字列 | 255 |  |
| enquete5 | アンケート5 | 文字列 | 255 |  |
| ordered_at | 受注日 | 日付 | 19 | Y-m-d H:i:s |
| affiliate_id | 参照元ID | 文字列 | 255 |  |
| estimate_id | 見積ID | 整数 | 255 |  |
| status | 対応状況 | 文字列 | 255 |  |

**URIパラメータ**

| パラメータ名 | 名称 | 型 | 内容 |
| --- | --- | --- | --- |
| complete | 受注情報一式 | 整数 | 1 を指定すると受注に紐付いた受注商品と出荷情報も取得 |

**レスポンス例（200 OK）:**

```json
{
  "order": {
    "id": 128,
    "code": "13354411463",
    "customer_id": 1,
    "customer_ext_id": "Bcart",
    "customer_parent_id": null,
    "customer_salesman_id": null,
    "customer_comp_name": "Bカートサポートセンター",
    "customer_department": "お客様サポート",
    "customer_name": "Bカート",
    "customer_tel": "075-361-1171",
    "customer_mobile_phone": "",
    "customer_email": "support@bcart.jp",
    "customer_price_group_id": null,
    "customer_zip": "600-8412",
    "customer_pref": "京都府",
    "customer_address1": "京都市下京区",
    "customer_address2": "二帖半敷町646番地",
    "customer_address3": "ダイマルヤ四条烏丸ビル5F",
    "customer_customs": [
      {
        "field_id": 11,
        "value": "会員カスタム1"
      },
      {
        "field_id": 12,
        "value": "会員カスタム2"
      },
      {
        "field_id": 13,
        "value": "会員カスタム3"
      }
    ],
    "payment": "銀行振込",
    "payment_at": null,
    "total_price": 728000,
    "tax": 36400,
    "tax_rate": "0.08",
    "COD_cost": 0,
    "shipping_cost": 525,
    "final_price": 764925,
    "use_point": 0,
    "get_point": 0,
    "order_totals": [
      {
        "tax_rate": "0.05",
        "total": 728500,
        "tax": 36425,
        "total_incl_tax": 764925
      }
    ],
    "customer_message": "在庫引当後ご連絡ください。",
    "admin_message": "要連絡",
    "memo": "電話番号 075-000-0000",
    "customs": [
      {
        "field_id": 6,
        "value": "受注カスタム1"
      },
      {
        "field_id": 7,
        "value": "受注カスタム2"
      },
      {
        "field_id": 8,
        "value": "受注カスタム3"
      }
    ],
    "enquete1": "1",
    "enquete2": "2",
    "enquete3": "3",
    "enquete4": "",
    "enquete5": "",
    "ordered_at": "2014-04-08 10:46:41",
    "affiliate_id": "",
    "estimate_id": "",
    "status": "完了"
  }
}
```

## GET {{api_url}}/api/v1/orders

**URIパラメータ**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| limit | limit | 整数 |  | 指定した件数分のデータを取得します。指定なしの場合は20件、最大100件 |
| offset | offset | 整数 |  | 指定した値+1件目のデータからlimit分を取得します。指定しない場合は0 |
| ids | ID複数 | 整数 |  | 複数の受注IDをカンマ区切りで指定 |
| fields | フィールド | 文字列 |  | 取得したいフィールドカンマ区切りで指定 |
| code | 受注番号 | 整数 | 255 |  |
| customer_id | 会員ID | 整数 | 11 |  |
| customer_salesman_id | 営業担当者 | 文字列 | 255 |  |
| estimate_id | 見積ID | 整数 | 11 |  |
| payment | 決済方法 | 文字列 | 255 |  |
| customer_zip | 注文者郵便番号 | 文字列 | 32 |  |
| customer_pref | 注文者都道府県 | 文字列 | 32 |  |
| customer_address1 | 注文者 市区町村 | 文字列 | 255 |  |
| customer_address2 | 注文者 町域・番地 | 文字列 | 255 |  |
| customer_address3 | 注文者 ビル建物名 | 文字列 | 255 |  |
| customer_customs | 注文者 カスタム項目 | 配列 |  | 配列のキーにfield_id、値にvalue。例) customer_customs\[11\]=検索する値 |
| enquete1 | アンケート1 | 文字列 | 255 |  |
| enquete2 | アンケート2 | 文字列 | 255 |  |
| enquete3 | アンケート3 | 文字列 | 255 |  |
| enquete4 | アンケート4 | 文字列 | 255 |  |
| enquete5 | アンケート5 | 文字列 | 255 |  |
| customer_message | お客様からの連絡事項 | 文字列 | 65,535 |  |
| admin_message | お客様への連絡事項 | 文字列 | 65,535 |  |
| memo | 管理用メモ | 文字列 | 65,535 |  |
| customs | 受注カスタム項目 | 配列 |  | 配列のキーにfield_id、値にvalue。例) customs\[6\]=検索する値 |
| status | 対応状況 | 文字列 | 255 |  |
| qualified_invoice | インボイス設定 | 整数 | 1 | 0=無効,1=有効 |
| ordered_at | 注文日 | 文字列 | 19 | Y-m-d |
| ordered_at_min | 注文日時〜 | 文字列 | 19 | Y-m-d H:i:s指定日時以降 |
| ordered_at_max | 〜注文日時 | 文字列 | 19 | Y-m-d H:i:s指定日時以前 |
| complete | 受注情報一式 | 整数 | 1 | 1 を指定すると受注に紐付いた受注商品と出荷情報も取得 |

**受注商品/出荷情報から絞り込み**

| パラメータ名 | 名称 |
| --- | --- |
| order_products__{{key}} | 受注商品の{{key}}で絞り込み |
| logistics__{{key}} | 受注商品の{{key}}で絞り込み |

※ それぞれの利用可能な{{key}}はそれぞれのAPIを確認してください。

## 拡張パラメータによる高度な絞り込み

拡張パラメータを使用することで、より高度な絞り込みが可能です。

詳しくは、[パラメータ](../docs/04-parameters.md)の「拡張パラメータ」欄をご参照ください。

**レスポンス例（200 OK）:**

```json
{
  "orders": [
    {
      "id": 128,
      "code": "13354411463",
      "customer_id": 1,
      "customer_ext_id": "Bcart",
      "customer_parent_id": null,
      "customer_salesman_id": null,
      "customer_comp_name": "Bカートサポートセンター",
      "customer_department": "お客様サポート",
      "customer_name": "Bカート",
      "customer_tel": "075-361-1171",
      "customer_mobile_phone": "",
      "customer_email": "support@bcart.jp",
      "customer_price_group_id": null,
      "customer_zip": "600-8412",
      "customer_pref": "京都府",
      "customer_address1": "京都市下京区",
      "customer_address2": "二帖半敷町646番地",
      "customer_address3": "ダイマルヤ四条烏丸ビル5F",
      "customer_customs": [
        {
          "field_id": 11,
          "value": "会員カスタム1"
        },
        {
          "field_id": 12,
          "value": "会員カスタム2"
        },
        {
          "field_id": 13,
          "value": "会員カスタム3"
        }
      ],
      "payment": "銀行振込",
      "payment_at": null,
      "total_price": 728000,
      "tax": 36400,
      "tax_rate": "0.08",
      "COD_cost": 0,
      "shipping_cost": 525,
      "final_price": 764925,
      "use_point": 0,
      "get_point": 0,
      "order_totals": [
        {
          "tax_rate": "0.05",
          "total": 728500,
          "tax": 36425,
          "total_incl_tax": 764925
        }
      ],
      "customer_message": "在庫引当後ご連絡ください。",
      "admin_message": "要連絡",
      "memo": "電話番号 075-000-0000",
      "customs": [
        {
          "field_id": 6,
          "value": "受注カスタム1"
        },
        {
          "field_id": 7,
          "value": "受注カスタム2"
        },
        {
          "field_id": 8,
          "value": "受注カスタム3"
        }
      ],
      "enquete1": "1",
      "enquete2": "2",
      "enquete3": "3",
      "enquete4": "",
      "enquete5": "",
      "ordered_at": "2014-04-08 10:46:41",
      "affiliate_id": "",
      "estimate_id": "",
      "status": "完了"
    },
    {
      "id": 129,
      "code": "13402604907",
      "customer_id": 2,
      "customer_ext_id": "Bcart",
      "customer_parent_id": null,
      "customer_salesman_id": null,
      "customer_comp_name": "Bカートサポートセンター",
      "customer_department": "お客様サポート",
      "customer_name": "Bカート",
      "customer_tel": "075-361-1171",
      "customer_mobile_phone": "",
      "customer_email": "support@bcart.jp",
      "customer_price_group_id": null,
      "customer_zip": "600-8412",
      "customer_pref": "京都府",
      "customer_address1": "京都市下京区",
      "customer_address2": "二帖半敷町646番地",
      "customer_address3": "ダイマルヤ四条烏丸ビル5F",
      "customer_customs": [
        {
          "field_id": 11,
          "value": "Dai銀行"
        },
        {
          "field_id": 12,
          "value": "ソフトウェア"
        },
        {
          "field_id": 13,
          "value": "なし"
        }
      ],
      "payment": "銀行振込",
      "payment_at": null,
      "total_price": 50000,
      "tax": 2500,
      "tax_rate": "0.08",
      "COD_cost": 0,
      "shipping_cost": 0,
      "final_price": 52500,
      "use_point": 0,
      "get_point": 0,
      "order_totals": [
        {
          "tax_rate": "0.05",
          "total": 50000,
          "tax": 2500,
          "total_incl_tax": 52500
        }
      ],
      "customer_message": "",
      "admin_message": "",
      "memo": null,
      "customs": null,
      "enquete1": "1",
      "enquete2": "",
      "enquete3": "",
      "enquete4": "",
      "enquete5": "",
      "ordered_at": "2016-04-13 16:44:43",
      "affiliate_id": "",
      "estimate_id": "",
      "status": "新規注文"
    },
    {
      "id": 130,
      "code": "13402606204",
      "customer_id": 10018,
      "customer_ext_id": "B15487",
      "customer_parent_id": null,
      "customer_salesman_id": null,
      "customer_comp_name": "株式会社サンプル",
      "customer_department": "営業部",
      "customer_name": "鈴木太郎",
      "customer_tel": "222-222-2222",
      "customer_mobile_phone": "090-555-5555",
      "customer_email": "guest@dai.co.jp",
      "customer_price_group_id": null,
      "customer_zip": "111-1111",
      "customer_pref": "東京都",
      "customer_address1": "○○区△町3-24〇〇ビル",
      "customer_address2": "",
      "customer_address3": "",
      "customer_customs": null,
      "payment": "銀行振込",
      "payment_at": null,
      "total_price": 6000,
      "tax": 300,
      "tax_rate": "0.05",
      "COD_cost": 0,
      "shipping_cost": 525,
      "final_price": 6825,
      "use_point": 0,
      "get_point": 0,
      "order_totals": [
        {
          "tax_rate": "0.05",
          "total": 6500,
          "tax": 325,
          "total_incl_tax": 6825
        }
      ],
      "customer_message": "",
      "admin_message": "",
      "memo": null,
      "customs": null,
      "enquete1": "",
      "enquete2": "",
      "enquete3": "",
      "enquete4": "",
      "enquete5": "",
      "ordered_at": "2012-06-21 15:37:00",
      "affiliate_id": "",
      "estimate_id": "",
      "status": "完了"
    },
    {
      "id": 131,
      "code": "13417978910",
      "customer_id": 10018,
      "customer_ext_id": "B15487",
      "customer_parent_id": null,
      "customer_salesman_id": null,
      "customer_comp_name": "株式会社サンプル",
      "customer_department": "営業部",
      "customer_name": "鈴木太郎",
      "customer_tel": "222-222-2222",
      "customer_mobile_phone": "090-555-5555",
      "customer_email": "guest@dai.co.jp",
      "customer_price_group_id": null,
      "customer_zip": "111-1111",
      "customer_pref": "東京都",
      "customer_address1": "○○区△町3-24〇〇ビル",
      "customer_address2": "",
      "customer_address3": "",
      "customer_customs": null,
      "payment": "代金引換",
      "payment_at": null,
      "total_price": 6000,
      "tax": 300,
      "tax_rate": "0.05",
      "COD_cost": 0,
      "shipping_cost": 525,
      "final_price": 6825,
      "use_point": 0,
      "get_point": 0,
      "order_totals": [
        {
          "tax_rate": "0.05",
          "total": 6500,
          "tax": 325,
          "total_incl_tax": 6825
        }
      ],
      "customer_message": "",
      "admin_message": "",
      "memo": null,
      "customs": null,
      "enquete1": "",
      "enquete2": "",
      "enquete3": "",
      "enquete4": "",
      "enquete5": "",
      "ordered_at": "2012-07-09 10:38:11",
      "affiliate_id": "",
      "estimate_id": "",
      "status": "カスタム6"
    },
    {
      "id": 132,
      "code": "13417979368",
      "customer_id": 10018,
      "customer_ext_id": "B15487",
      "customer_parent_id": null,
      "customer_salesman_id": null,
      "customer_comp_name": "株式会社サンプル",
      "customer_department": "営業部",
      "customer_name": "鈴木太郎",
      "customer_tel": "222-222-2222",
      "customer_mobile_phone": "090-555-5555",
      "customer_email": "guest@dai.co.jp",
      "customer_price_group_id": null,
      "customer_zip": "111-1111",
      "customer_pref": "東京都",
      "customer_address1": "○○区△町3-24〇〇ビル",
      "customer_address2": "",
      "customer_address3": "",
      "customer_customs": null,
      "payment": "銀行振込",
      "payment_at": null,
      "total_price": 6000,
      "tax": 300,
      "tax_rate": "0.05",
      "COD_cost": 0,
      "shipping_cost": 525,
      "final_price": 6825,
      "use_point": 0,
      "get_point": 0,
      "order_totals": [
        {
          "tax_rate": "0.05",
          "total": 6500,
          "tax": 325,
          "total_incl_tax": 6825
        }
      ],
      "customer_message": "",
      "admin_message": "",
      "memo": null,
      "customs": null,
      "enquete1": "",
      "enquete2": "",
      "enquete3": "",
      "enquete4": "",
      "enquete5": "",
      "ordered_at": "2012-07-09 10:38:56",
      "affiliate_id": "",
      "estimate_id": "",
      "status": "カスタム1"
    },
    {
      "id": 133,
      "code": "13430991508",
      "customer_id": 1,
      "customer_ext_id": "B15487",
      "customer_parent_id": null,
      "customer_salesman_id": null,
      "customer_comp_name": "株式会社サンプル",
      "customer_department": "営業部",
      "customer_name": "鈴木太郎",
      "customer_tel": "222-222-2222",
      "customer_mobile_phone": "090-555-5555",
      "customer_email": "guest@dai.co.jp",
      "customer_price_group_id": null,
      "customer_zip": "111-1111",
      "customer_pref": "東京都",
      "customer_address1": "○○区△町",
      "customer_address2": "3-24",
      "customer_address3": "〇〇ビル",
      "customer_customs": null,
      "payment": "Paid",
      "payment_at": null,
      "total_price": 35800,
      "tax": 1790,
      "tax_rate": "0.05",
      "COD_cost": 0,
      "shipping_cost": 0,
      "final_price": 37590,
      "use_point": 0,
      "get_point": 0,
      "order_totals": [
        {
          "tax_rate": "0.05",
          "total": 35800,
          "tax": 1790,
          "total_incl_tax": 37590
        }
      ],
      "customer_message": "発送が遅れる場合は早めにご連絡頂ければ幸いです。",
      "admin_message": "",
      "memo": null,
      "customs": null,
      "enquete1": "",
      "enquete2": "",
      "enquete3": "",
      "enquete4": "",
      "enquete5": "",
      "ordered_at": "2012-07-24 12:05:50",
      "affiliate_id": "",
      "estimate_id": "",
      "status": "完了"
    },
    {
      "id": 135,
      "code": "13430995504",
      "customer_id": 1,
      "customer_ext_id": "B15487",
      "customer_parent_id": null,
      "customer_salesman_id": null,
      "customer_comp_name": "株式会社サンプル",
      "customer_department": "営業部",
      "customer_name": "鈴木太郎",
      "customer_tel": "222-222-2222",
      "customer_mobile_phone": "090-555-5555",
      "customer_email": "guest@dai.co.jp",
      "customer_price_group_id": null,
      "customer_zip": "111-1111",
      "customer_pref": "東京都",
      "customer_address1": "○○区△町",
      "customer_address2": "3-24",
      "customer_address3": "〇〇ビル",
      "customer_customs": null,
      "payment": "Paid",
      "payment_at": null,
      "total_price": 29800,
      "tax": 1490,
      "tax_rate": "0.05",
      "COD_cost": 0,
      "shipping_cost": 0,
      "final_price": 31290,
      "use_point": 0,
      "get_point": 0,
      "order_totals": [
        {
          "tax_rate": "0.05",
          "total": 29800,
          "tax": 1490,
          "total_incl_tax": 31290
        }
      ],
      "customer_message": "お盆前に発送・受取可能かどうかご連絡いただければ幸いです。",
      "admin_message": "",
      "memo": null,
      "customs": null,
      "enquete1": "",
      "enquete2": "",
      "enquete3": "",
      "enquete4": "",
      "enquete5": "",
      "ordered_at": "2012-07-24 12:12:30",
      "affiliate_id": "",
      "estimate_id": "",
      "status": "新規注文"
    },
    {
      "id": 137,
      "code": "13430995897",
      "customer_id": 1,
      "customer_ext_id": "B15487",
      "customer_parent_id": null,
      "customer_salesman_id": null,
      "customer_comp_name": "株式会社サンプル",
      "customer_department": "営業部",
      "customer_name": "鈴木太郎",
      "customer_tel": "222-222-2222",
      "customer_mobile_phone": "090-555-5555",
      "customer_email": "guest@dai.co.jp",
      "customer_price_group_id": null,
      "customer_zip": "111-1111",
      "customer_pref": "東京都",
      "customer_address1": "○○区△町",
      "customer_address2": "3-24",
      "customer_address3": "〇〇ビル",
      "customer_customs": null,
      "payment": "Paid",
      "payment_at": null,
      "total_price": 35800,
      "tax": 1790,
      "tax_rate": "0.05",
      "COD_cost": 0,
      "shipping_cost": 0,
      "final_price": 37590,
      "use_point": 0,
      "get_point": 0,
      "order_totals": [
        {
          "tax_rate": "0.05",
          "total": 35800,
          "tax": 1790,
          "total_incl_tax": 37590
        }
      ],
      "customer_message": "発送が遅れる場合は早めにご連絡頂ければ幸いです。",
      "admin_message": "",
      "memo": null,
      "customs": null,
      "enquete1": "",
      "enquete2": "",
      "enquete3": "",
      "enquete4": "",
      "enquete5": "",
      "ordered_at": "2012-07-24 12:13:09",
      "affiliate_id": "",
      "estimate_id": "",
      "status": "新規注文"
    },
    {
      "id": 138,
      "code": "13431041914",
      "customer_id": 1,
      "customer_ext_id": "B15487",
      "customer_parent_id": null,
      "customer_salesman_id": null,
      "customer_comp_name": "株式会社サンプル",
      "customer_department": "営業部",
      "customer_name": "鈴木太郎",
      "customer_tel": "222-222-2222",
      "customer_mobile_phone": "090-555-5555",
      "customer_email": "guest@dai.co.jp",
      "customer_price_group_id": null,
      "customer_zip": "111-1111",
      "customer_pref": "東京都",
      "customer_address1": "○○区△町",
      "customer_address2": "3-24",
      "customer_address3": "〇〇ビル",
      "customer_customs": null,
      "payment": "クレジット",
      "payment_at": null,
      "total_price": 20000,
      "tax": 1000,
      "tax_rate": "0.05",
      "COD_cost": 0,
      "shipping_cost": 525,
      "final_price": 21525,
      "use_point": 0,
      "get_point": 0,
      "order_totals": [
        {
          "tax_rate": "0.05",
          "total": 20500,
          "tax": 1025,
          "total_incl_tax": 21525
        }
      ],
      "customer_message": "",
      "admin_message": "",
      "memo": null,
      "customs": null,
      "enquete1": "",
      "enquete2": "",
      "enquete3": "",
      "enquete4": "",
      "enquete5": "",
      "ordered_at": "2012-07-24 13:29:51",
      "affiliate_id": "",
      "estimate_id": "",
      "status": "カスタム5"
    },
    {
      "id": 140,
      "code": "13431923006",
      "customer_id": 1,
      "customer_ext_id": "B15487",
      "customer_parent_id": null,
      "customer_salesman_id": null,
      "customer_comp_name": "株式会社サンプル",
      "customer_department": "営業部",
      "customer_name": "鈴木太郎",
      "customer_tel": "222-222-2222",
      "customer_mobile_phone": "090-555-5555",
      "customer_email": "guest@dai.co.jp",
      "customer_price_group_id": null,
      "customer_zip": "111-1111",
      "customer_pref": "東京都",
      "customer_address1": "○○区△町",
      "customer_address2": "3-24",
      "customer_address3": "〇〇ビル",
      "customer_customs": null,
      "payment": "代金引換",
      "payment_at": null,
      "total_price": 6000,
      "tax": 300,
      "tax_rate": "0.05",
      "COD_cost": 315,
      "shipping_cost": 525,
      "final_price": 7140,
      "use_point": 0,
      "get_point": 0,
      "order_totals": [
        {
          "tax_rate": "0.05",
          "total": 6800,
          "tax": 340,
          "total_incl_tax": 7140
        }
      ],
      "customer_message": "",
      "admin_message": "",
      "memo": null,
      "customs": null,
      "enquete1": "",
      "enquete2": "",
      "enquete3": "",
      "enquete4": "",
      "enquete5": "",
      "ordered_at": "2012-07-25 13:58:20",
      "affiliate_id": "",
      "estimate_id": "",
      "status": "カスタム5"
    },
    {
      "id": 141,
      "code": "13442370709",
      "customer_id": 10028,
      "customer_ext_id": "",
      "customer_parent_id": null,
      "customer_salesman_id": null,
      "customer_comp_name": "大竹家具株式会社",
      "customer_department": "仕入れ課",
      "customer_name": "山口宗二",
      "customer_tel": "03-1111-1111",
      "customer_mobile_phone": "",
      "customer_email": "guest+6@dai.co.jp",
      "customer_price_group_id": null,
      "customer_zip": "150-0013",
      "customer_pref": "東京都",
      "customer_address1": "渋谷区恵比寿",
      "customer_address2": "3-24",
      "customer_address3": "",
      "customer_customs": null,
      "payment": "代金引換",
      "payment_at": null,
      "total_price": 390000,
      "tax": 19500,
      "tax_rate": "0.05",
      "COD_cost": 2100,
      "shipping_cost": 0,
      "final_price": 411600,
      "use_point": 0,
      "get_point": 0,
      "order_totals": [
        {
          "tax_rate": "0.05",
          "total": 392000,
          "tax": 19600,
          "total_incl_tax": 411600
        }
      ],
      "customer_message": "",
      "admin_message": "",
      "memo": null,
      "customs": null,
      "enquete1": "",
      "enquete2": "",
      "enquete3": "",
      "enquete4": "",
      "enquete5": "",
      "ordered_at": "2012-08-06 16:11:10",
      "affiliate_id": "1",
      "estimate_id": "",
      "status": "カスタム5"
    },
    {
      "id": 143,
      "code": "13442372147",
      "customer_id": 10028,
      "customer_ext_id": "",
      "customer_parent_id": null,
      "customer_salesman_id": null,
      "customer_comp_name": "大竹家具株式会社",
      "customer_department": "仕入れ課",
      "customer_name": "山口宗二",
      "customer_tel": "03-1111-1111",
      "customer_mobile_phone": "",
      "customer_email": "guest+6@dai.co.jp",
      "customer_price_group_id": null,
      "customer_zip": "150-0013",
      "customer_pref": "東京都",
      "customer_address1": "渋谷区恵比寿",
      "customer_address2": "3-24",
      "customer_address3": "",
      "customer_customs": null,
      "payment": "自社掛払い",
      "payment_at": null,
      "total_price": 24000,
      "tax": 1200,
      "tax_rate": "0.05",
      "COD_cost": 0,
      "shipping_cost": 525,
      "final_price": 25725,
      "use_point": 0,
      "get_point": 0,
      "order_totals": [
        {
          "tax_rate": "0.05",
          "total": 24500,
          "tax": 1225,
          "total_incl_tax": 25725
        }
      ],
      "customer_message": "",
      "admin_message": "",
      "memo": null,
      "customs": null,
      "enquete1": "",
      "enquete2": "",
      "enquete3": "",
      "enquete4": "",
      "enquete5": "",
      "ordered_at": "2012-08-06 16:13:34",
      "affiliate_id": "",
      "estimate_id": "",
      "status": "カスタム5"
    },
    {
      "id": 144,
      "code": "13442373817",
      "customer_id": 10031,
      "customer_ext_id": "",
      "customer_parent_id": null,
      "customer_salesman_id": null,
      "customer_comp_name": "有限会社佐藤商店",
      "customer_department": "仕入れ担当",
      "customer_name": "勝間和子",
      "customer_tel": "0000-00-0000",
      "customer_mobile_phone": "",
      "customer_email": "guest+9@dai.co.jp",
      "customer_price_group_id": null,
      "customer_zip": "100-0000",
      "customer_pref": "東京都",
      "customer_address1": "千代田区",
      "customer_address2": "111",
      "customer_address3": "",
      "customer_customs": null,
      "payment": "代金引換",
      "payment_at": null,
      "total_price": 21000,
      "tax": 1050,
      "tax_rate": "0.05",
      "COD_cost": 420,
      "shipping_cost": 525,
      "final_price": 22995,
      "use_point": 0,
      "get_point": 0,
      "order_totals": [
        {
          "tax_rate": "0.05",
          "total": 21900,
          "tax": 1095,
          "total_incl_tax": 22995
        }
      ],
      "customer_message": "",
      "admin_message": "",
      "memo": null,
      "customs": null,
      "enquete1": "",
      "enquete2": "",
      "enquete3": "",
      "enquete4": "",
      "enquete5": "",
      "ordered_at": "2012-08-06 16:16:21",
      "affiliate_id": "1",
      "estimate_id": "",
      "status": "カスタム5"
    },
    {
      "id": 145,
      "code": "13442374204",
      "customer_id": 10031,
      "customer_ext_id": "",
      "customer_parent_id": null,
      "customer_salesman_id": null,
      "customer_comp_name": "有限会社佐藤商店",
      "customer_department": "仕入れ担当",
      "customer_name": "勝間和子",
      "customer_tel": "0000-00-0000",
      "customer_mobile_phone": "",
      "customer_email": "guest+9@dai.co.jp",
      "customer_price_group_id": null,
      "customer_zip": "100-0000",
      "customer_pref": "東京都",
      "customer_address1": "千代田区",
      "customer_address2": "111",
      "customer_address3": "",
      "customer_customs": null,
      "payment": "銀行振込",
      "payment_at": null,
      "total_price": 141600,
      "tax": 7080,
      "tax_rate": "0.05",
      "COD_cost": 0,
      "shipping_cost": 0,
      "final_price": 148680,
      "use_point": 0,
      "get_point": 0,
      "order_totals": [
        {
          "tax_rate": "0.05",
          "total": 141600,
          "tax": 7080,
          "total_incl_tax": 148680
        }
      ],
      "customer_message": "",
      "admin_message": "",
      "memo": null,
      "customs": null,
      "enquete1": "",
      "enquete2": "",
      "enquete3": "",
      "enquete4": "",
      "enquete5": "",
      "ordered_at": "2012-08-06 16:17:00",
      "affiliate_id": "",
      "estimate_id": "",
      "status": "カスタム5"
    },
    {
      "id": 146,
      "code": "13442376067",
      "customer_id": 10031,
      "customer_ext_id": "",
      "customer_parent_id": null,
      "customer_salesman_id": null,
      "customer_comp_name": "有限会社佐藤商店",
      "customer_department": "仕入れ担当",
      "customer_name": "勝間和子",
      "customer_tel": "0000-00-0000",
      "customer_mobile_phone": "",
      "customer_email": "guest+9@dai.co.jp",
      "customer_price_group_id": null,
      "customer_zip": "100-0000",
      "customer_pref": "東京都",
      "customer_address1": "千代田区",
      "customer_address2": "111",
      "customer_address3": "",
      "customer_customs": null,
      "payment": "代金引換",
      "payment_at": null,
      "total_price": 76800,
      "tax": 3840,
      "tax_rate": "0.05",
      "COD_cost": 630,
      "shipping_cost": 0,
      "final_price": 81270,
      "use_point": 0,
      "get_point": 0,
      "order_totals": [
        {
          "tax_rate": "0.05",
          "total": 77400,
          "tax": 3870,
          "total_incl_tax": 81270
        }
      ],
      "customer_message": "",
      "admin_message": "",
      "memo": null,
      "customs": null,
      "enquete1": "",
      "enquete2": "",
      "enquete3": "",
      "enquete4": "",
      "enquete5": "",
      "ordered_at": "2012-08-06 16:20:06",
      "affiliate_id": "",
      "estimate_id": "",
      "status": "カスタム6"
    },
    {
      "id": 147,
      "code": "13442376862",
      "customer_id": 10023,
      "customer_ext_id": "",
      "customer_parent_id": null,
      "customer_salesman_id": null,
      "customer_comp_name": "インポートオブユーロ株式会社",
      "customer_department": "",
      "customer_name": "垣内博文",
      "customer_tel": "0000-00-0000",
      "customer_mobile_phone": "",
      "customer_email": "guest+4@dai.co.jp",
      "customer_price_group_id": null,
      "customer_zip": "111-1111",
      "customer_pref": "大阪府",
      "customer_address1": "吹田市江坂町3－23江坂第1ビル",
      "customer_address2": "",
      "customer_address3": "",
      "customer_customs": null,
      "payment": "代金引換",
      "payment_at": null,
      "total_price": 117000,
      "tax": 5850,
      "tax_rate": "0.05",
      "COD_cost": 1050,
      "shipping_cost": 0,
      "final_price": 123900,
      "use_point": 0,
      "get_point": 0,
      "order_totals": [
        {
          "tax_rate": "0.05",
          "total": 118000,
          "tax": 5900,
          "total_incl_tax": 123900
        }
      ],
      "customer_message": "",
      "admin_message": "",
      "memo": null,
      "customs": null,
      "enquete1": "",
      "enquete2": "",
      "enquete3": "",
      "enquete4": "",
      "enquete5": "",
      "ordered_at": "2012-08-06 16:21:26",
      "affiliate_id": "",
      "estimate_id": "",
      "status": "カスタム5"
    },
    {
      "id": 148,
      "code": "13442377128",
      "customer_id": 10023,
      "customer_ext_id": "",
      "customer_parent_id": null,
      "customer_salesman_id": null,
      "customer_comp_name": "インポートオブユーロ株式会社",
      "customer_department": "",
      "customer_name": "垣内博文",
      "customer_tel": "0000-00-0000",
      "customer_mobile_phone": "",
      "customer_email": "guest+4@dai.co.jp",
      "customer_price_group_id": null,
      "customer_zip": "111-1111",
      "customer_pref": "大阪府",
      "customer_address1": "吹田市江坂町3－23江坂第1ビル",
      "customer_address2": "",
      "customer_address3": "",
      "customer_customs": null,
      "payment": "銀行振込",
      "payment_at": null,
      "total_price": 57000,
      "tax": 2850,
      "tax_rate": "0.05",
      "COD_cost": 0,
      "shipping_cost": 0,
      "final_price": 59850,
      "use_point": 0,
      "get_point": 0,
      "order_totals": [
        {
          "tax_rate": "0.05",
          "total": 57000,
          "tax": 2850,
          "total_incl_tax": 59850
        }
      ],
      "customer_message": "",
      "admin_message": "",
      "memo": null,
      "customs": null,
      "enquete1": "",
      "enquete2": "",
      "enquete3": "",
      "enquete4": "",
      "enquete5": "",
      "ordered_at": "2012-08-06 16:21:52",
      "affiliate_id": "",
      "estimate_id": "",
      "status": "カスタム5"
    },
    {
      "id": 149,
      "code": "13442378512",
      "customer_id": 10034,
      "customer_ext_id": "",
      "customer_parent_id": null,
      "customer_salesman_id": null,
      "customer_comp_name": "株式会社カンサイ機械",
      "customer_department": "購買部",
      "customer_name": "新山綱彦",
      "customer_tel": "0000-1111-0000",
      "customer_mobile_phone": "",
      "customer_email": "guest+12@dai.co.jp",
      "customer_price_group_id": null,
      "customer_zip": "100-0000",
      "customer_pref": "東京都",
      "customer_address1": "千代田区",
      "customer_address2": "1-１　",
      "customer_address3": "",
      "customer_customs": null,
      "payment": "銀行振込",
      "payment_at": null,
      "total_price": 8000,
      "tax": 400,
      "tax_rate": "0.05",
      "COD_cost": 0,
      "shipping_cost": 525,
      "final_price": 8925,
      "use_point": 0,
      "get_point": 0,
      "order_totals": [
        {
          "tax_rate": "0.05",
          "total": 8500,
          "tax": 425,
          "total_incl_tax": 8925
        }
      ],
      "customer_message": "",
      "admin_message": "",
      "memo": null,
      "customs": null,
      "enquete1": "",
      "enquete2": "",
      "enquete3": "",
      "enquete4": "",
      "enquete5": "",
      "ordered_at": "2012-08-06 16:24:11",
      "affiliate_id": "2",
      "estimate_id": "",
      "status": "カスタム5"
    },
    {
      "id": 150,
      "code": "13442378927",
      "customer_id": 10034,
      "customer_ext_id": "",
      "customer_parent_id": null,
      "customer_salesman_id": null,
      "customer_comp_name": "株式会社カンサイ機械",
      "customer_department": "購買部",
      "customer_name": "新山綱彦",
      "customer_tel": "0000-1111-0000",
      "customer_mobile_phone": "",
      "customer_email": "guest+12@dai.co.jp",
      "customer_price_group_id": null,
      "customer_zip": "100-0000",
      "customer_pref": "東京都",
      "customer_address1": "千代田区",
      "customer_address2": "1-１　",
      "customer_address3": "",
      "customer_customs": null,
      "payment": "カスタム",
      "payment_at": null,
      "total_price": 88000,
      "tax": 0,
      "tax_rate": "0",
      "COD_cost": 630,
      "shipping_cost": 0,
      "final_price": 88630,
      "use_point": 0,
      "get_point": 0,
      "order_totals": [
        {
          "tax_rate": "0",
          "total": 88630,
          "tax": 0,
          "total_incl_tax": 88630
        }
      ],
      "customer_message": "",
      "admin_message": "",
      "memo": null,
      "customs": null,
      "enquete1": "",
      "enquete2": "",
      "enquete3": "",
      "enquete4": "",
      "enquete5": "",
      "ordered_at": "2012-08-06 16:24:52",
      "affiliate_id": "",
      "estimate_id": "",
      "status": "カスタム5"
    },
    {
      "id": 151,
      "code": "13442379262",
      "customer_id": 10034,
      "customer_ext_id": "",
      "customer_parent_id": null,
      "customer_salesman_id": null,
      "customer_comp_name": "株式会社カンサイ機械",
      "customer_department": "購買部",
      "customer_name": "新山綱彦",
      "customer_tel": "0000-1111-0000",
      "customer_mobile_phone": "",
      "customer_email": "guest+12@dai.co.jp",
      "customer_price_group_id": null,
      "customer_zip": "100-0000",
      "customer_pref": "東京都",
      "customer_address1": "千代田区",
      "customer_address2": "1-１　",
      "customer_address3": "",
      "customer_customs": null,
      "payment": "代金引換",
      "payment_at": null,
      "total_price": 16000,
      "tax": 800,
      "tax_rate": "0.05",
      "COD_cost": 420,
      "shipping_cost": 525,
      "final_price": 17745,
      "use_point": 0,
      "get_point": 0,
      "order_totals": [
        {
          "tax_rate": "0.05",
          "total": 16900,
          "tax": 845,
          "total_incl_tax": 17745
        }
      ],
      "customer_message": "",
      "admin_message": "",
      "memo": null,
      "customs": null,
      "enquete1": "",
      "enquete2": "",
      "enquete3": "",
      "enquete4": "",
      "enquete5": "",
      "ordered_at": "2012-08-06 16:25:26",
      "affiliate_id": "",
      "estimate_id": "",
      "status": "キャンセル"
    }
  ],
  "meta": {
    "limit": 20,
    "offset": 0,
    "total": 65
  }
}
```

## PATCH {{api_url}}/api/v1/orders/128

**リクエストBODY**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| estimate_id | 見積番号 | 整数 | 255 |  |
| customer_id | 会員ID | 整数 | 11 |  |
| customer_salesman_id | 営業担当者 | 文字列 | 255 | 管理者IDをカンマ区切りで指定 |
| customer_ext_id | 貴社独自ID | 文字列 | 255 |  |
| customer_parent_id | 親代理店ID | 文字列 | 255 |  |
| customer_comp_name | 注文者会社名 | 文字列 | 255 |  |
| customer_department | 注文者部署 | 文字列 | 255 |  |
| customer_name | 注文者名前 | 文字列 | 50 | 項目存在時必須 |
| customer_tel | 注文者電話番号 | 文字列 | 255 |  |
| customer_email | 注文者メールアドレス | 文字列 | 255 |  |
| customer_mobile_phone | 注文者携帯番号 | 文字列 | 255 |  |
| customer_price_group_id | 価格グループID | 文字列 | 255 |  |
| customer_zip | 注文者郵便番号 | 文字列 | 32 |  |
| customer_pref | 注文者都道府県 | 文字列 | 32 |  |
| customer_address1 | 注文者市区町村 | 文字列 | 255 |  |
| customer_address2 | 注文者町域・番地 | 文字列 | 255 |  |
| customer_address3 | 注文者ビル・建物名 | 文字列 | 255 |  |
| customer_customs\[{field_id, value}\] | 注文者カスタム項目 | 配列 | 65,535 |  |
| payment | 決済方法 | 文字列 | 255 |  |
| payment_at | 決済確認日 | 年月日 | 19 | Y-m-d |
| customs\[{field_id, value}\] | カスタム項目 | 配列 | 65,535 |  |
| enquete1 | アンケート1 | 文字列 | 255 |  |
| enquete2 | アンケート2 | 文字列 | 255 |  |
| enquete3 | アンケート3 | 文字列 | 255 |  |
| enquete4 | アンケート4 | 文字列 | 255 |  |
| enquete5 | アンケート5 | 文字列 | 255 |  |
| customer_message | お客様からの連絡事項 | 文字列 | 65,535 |  |
| admin_message | お客様への連絡事項 | 文字列 | 65,535 |  |
| memo | 管理用メモ | 文字列 | 65,535 |  |
| status | 対応状況 | 文字列 | 255 |  |

**リクエストボディ例:**

```json
{
  "code": "13969216012",
  "customer_id": 1,
  "customer_ext_id": "Bcart",
  "customer_parent_id": null,
  "customer_salesman_id": null,
  "customer_comp_name": "Bカートサポートセンター",
  "customer_department": "お客様サポート",
  "customer_name": "Bカート",
  "customer_tel": "075-361-1171",
  "customer_mobile_phone": null,
  "customer_email": "support@bcart.jp",
  "customer_price_group_id": null,
  "customer_zip": "600-8412",
  "customer_pref": "京都府",
  "customer_address1": "京都市下京区",
  "customer_address2": "二帖半敷町646番地",
  "customer_address3": "ダイマルヤ四条烏丸ビル5F",
  "customer_customs": [
    {
      "field_id": 11,
      "value": "会員カスタム1"
    },
    {
      "field_id": 12,
      "value": "会員カスタム2"
    },
    {
      "field_id": 13,
      "value": "会員カスタム3"
    }
  ],
  "payment": "銀行振込",
  "payment_at": null,
  "tax_rate": 0.08,
  "get_point": 0,
  "customer_message": "在庫引当後ご連絡ください。",
  "admin_message": "要連絡",
  "memo": "電話番号 075-000-0000",
  "customs": [
    {
      "field_id": 6,
      "value": "受注カスタム1"
    },
    {
      "field_id": 7,
      "value": "受注カスタム2"
    },
    {
      "field_id": 8,
      "value": "受注カスタム3"
    }
  ],
  "enquete1": "1",
  "enquete2": "2",
  "enquete3": "3",
  "enquete4": null,
  "enquete5": null,
  "ordered_at": "2014-04-08 10:46:41",
  "affiliate_id": null,
  "estimate_id": null,
  "status": "完了"
}
```

**レスポンス例（200 OK）:**

```json
{
  "order": {
    "id": 128,
    "code": "13354411463",
    "customer_id": 1,
    "customer_ext_id": "Bcart",
    "customer_parent_id": null,
    "customer_salesman_id": null,
    "customer_comp_name": "Bカートサポートセンター",
    "customer_department": "お客様サポート",
    "customer_name": "Bカート",
    "customer_tel": "075-361-1171",
    "customer_mobile_phone": "",
    "customer_email": "support@bcart.jp",
    "customer_price_group_id": null,
    "customer_zip": "600-8412",
    "customer_pref": "京都府",
    "customer_address1": "京都市下京区",
    "customer_address2": "二帖半敷町646番地",
    "customer_address3": "ダイマルヤ四条烏丸ビル5F",
    "customer_customs": [
      {
        "field_id": 11,
        "value": "会員カスタム1"
      },
      {
        "field_id": 12,
        "value": "会員カスタム2"
      },
      {
        "field_id": 13,
        "value": "会員カスタム3"
      }
    ],
    "payment": "銀行振込",
    "payment_at": null,
    "total_price": 728000,
    "tax": 36400,
    "tax_rate": "0.08",
    "COD_cost": 0,
    "shipping_cost": 525,
    "final_price": 764925,
    "use_point": 0,
    "get_point": 0,
    "order_totals": [
      {
        "tax_rate": "0.05",
        "total": 728500,
        "tax": 36425,
        "total_incl_tax": 764925
      }
    ],
    "customer_message": "在庫引当後ご連絡ください。",
    "admin_message": "要連絡",
    "memo": "電話番号 075-000-0000",
    "customs": [
      {
        "field_id": 6,
        "value": "受注カスタム1"
      },
      {
        "field_id": 7,
        "value": "受注カスタム2"
      },
      {
        "field_id": 8,
        "value": "受注カスタム3"
      }
    ],
    "enquete1": "1",
    "enquete2": "2",
    "enquete3": "3",
    "enquete4": "",
    "enquete5": "",
    "ordered_at": "2014-04-08 10:46:41",
    "affiliate_id": "",
    "estimate_id": "",
    "status": "完了"
  }
}
```

## PATCH {{api_url}}/api/v1/orders

**リクエストBODY**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| orders\[{{i}}\]\[id\] | 受注ID | 整数 | 11 | 必須 |
| orders\[{{i}}\]\[estimate_id\] | 見積番号 | 整数 | 255 |  |
| orders\[{{i}}\]\[customer_id\] | 会員ID | 整数 | 11 |  |
| orders\[{{i}}\]\[customer_salesman_id\] | 営業担当者 | 文字列 | 255 | 管理者IDをカンマ区切りで指定 |
| orders\[{{i}}\]\[customer_ext_id\] | 貴社独自ID | 文字列 | 255 |  |
| orders\[{{i}}\]\[customer_parent_id\] | 親代理店ID | 文字列 | 255 |  |
| orders\[{{i}}\]\[customer_comp_name\] | 注文者会社名 | 文字列 | 255 |  |
| orders\[{{i}}\]\[customer_department\] | 注文者部署 | 文字列 | 255 |  |
| orders\[{{i}}\]\[customer_name\] | 注文者名前 | 文字列 | 50 | 項目存在時必須 |
| orders\[{{i}}\]\[customer_tel\] | 注文者電話番号 | 文字列 | 255 |  |
| orders\[{{i}}\]\[customer_email\] | 注文者メールアドレス | 文字列 | 255 |  |
| orders\[{{i}}\]\[customer_mobile_phone\] | 注文者携帯番号 | 文字列 | 255 |  |
| orders\[{{i}}\]\[customer_price_group_id\] | 価格グループID | 文字列 | 255 |  |
| orders\[{{i}}\]\[customer_zip\] | 注文者郵便番号 | 文字列 | 32 |  |
| orders\[{{i}}\]\[customer_pref\] | 注文者都道府県 | 文字列 | 32 |  |
| orders\[{{i}}\]\[customer_address1\] | 注文者市区町村 | 文字列 | 255 |  |
| orders\[{{i}}\]\[customer_address2\] | 注文者町域・番地 | 文字列 | 255 |  |
| orders\[{{i}}\]\[customer_address3\] | 注文者ビル・建物名 | 文字列 | 255 |  |
| orders\[{{i}}\]\[customer_customs\]\[{field_id, value}\] | 注文者カスタム項目 | 配列 | 65,535 |  |
| orders\[{{i}}\]\[payment\] | 決済方法 | 文字列 | 255 |  |
| orders\[{{i}}\]\[payment_at\] | 決済確認日 | 年月日 | 19 | Y-m-d |
| orders\[{{i}}\]\[customs\]\[{field_id, value}\] | カスタム項目 | 配列 | 65,535 |  |
| orders\[{{i}}\]\[enquete1\] | アンケート1 | 文字列 | 255 |  |
| orders\[{{i}}\]\[enquete2\] | アンケート2 | 文字列 | 255 |  |
| orders\[{{i}}\]\[enquete3\] | アンケート3 | 文字列 | 255 |  |
| orders\[{{i}}\]\[enquete4\] | アンケート4 | 文字列 | 255 |  |
| orders\[{{i}}\]\[enquete5\] | アンケート5 | 文字列 | 255 |  |
| orders\[{{i}}\]\[customer_message\] | お客様からの連絡事項 | 文字列 | 65,535 |  |
| orders\[{{i}}\]\[admin_message\] | お客様への連絡事項 | 文字列 | 65,535 |  |
| orders\[{{i}}\]\[memo\] | 管理用メモ | 文字列 | 65,535 |  |
| orders\[{{i}}\]\[status\] | 対応状況 | 文字列 | 255 |  |

**リクエストボディ例:**

```json
{
  "orders": [
    {
      "id": 128,
      "status": "完了"
    },
    {
      "id": 129,
      "memo": "お客様から電話があり、在庫確認後連絡が欲しいとのこと。",
      "status": "カスタム1"
    }
  ]
}
```

**レスポンス例（200 OK）:**

```json
{
  "orders": [
    {
      "id": 128,
      "code": "13354411463",
      "customer_id": 1,
      "customer_ext_id": "Bcart",
      "customer_parent_id": null,
      "customer_salesman_id": null,
      "customer_comp_name": "Bカートサポートセンター",
      "customer_department": "お客様サポート",
      "customer_name": "Bカート",
      "customer_tel": "075-361-1171",
      "customer_mobile_phone": "",
      "customer_email": "support@bcart.jp",
      "customer_price_group_id": null,
      "customer_zip": "600-8412",
      "customer_pref": "京都府",
      "customer_address1": "京都市下京区",
      "customer_address2": "二帖半敷町646番地",
      "customer_address3": "ダイマルヤ四条烏丸ビル5F",
      "customer_customs": [
        {
          "field_id": 11,
          "value": "会員カスタム1"
        },
        {
          "field_id": 12,
          "value": "会員カスタム2"
        },
        {
          "field_id": 13,
          "value": "会員カスタム3"
        }
      ],
      "payment": "銀行振込",
      "payment_at": null,
      "total_price": 728000,
      "tax": 36400,
      "tax_rate": "0.08",
      "COD_cost": 0,
      "shipping_cost": 525,
      "final_price": 764925,
      "use_point": 0,
      "get_point": 0,
      "order_totals": [
        {
          "tax_rate": "0.05",
          "total": 728500,
          "tax": 36425,
          "total_incl_tax": 764925
        }
      ],
      "customer_message": "在庫引当後ご連絡ください。",
      "admin_message": "要連絡",
      "memo": "電話番号 075-000-0000",
      "customs": [
        {
          "field_id": 6,
          "value": "受注カスタム1"
        },
        {
          "field_id": 7,
          "value": "受注カスタム2"
        },
        {
          "field_id": 8,
          "value": "受注カスタム3"
        }
      ],
      "enquete1": "1",
      "enquete2": "2",
      "enquete3": "3",
      "enquete4": "",
      "enquete5": "",
      "ordered_at": "2014-04-08 10:46:41",
      "affiliate_id": "",
      "estimate_id": "",
      "status": "完了"
    },
    {
      "id": 129,
      "code": "13402604907",
      "customer_id": 2,
      "customer_ext_id": "Bcart",
      "customer_parent_id": null,
      "customer_salesman_id": null,
      "customer_comp_name": "Bカートサポートセンター",
      "customer_department": "お客様サポート",
      "customer_name": "Bカート",
      "customer_tel": "075-361-1171",
      "customer_mobile_phone": "",
      "customer_email": "support@bcart.jp",
      "customer_price_group_id": null,
      "customer_zip": "600-8412",
      "customer_pref": "京都府",
      "customer_address1": "京都市下京区",
      "customer_address2": "二帖半敷町646番地",
      "customer_address3": "ダイマルヤ四条烏丸ビル5F",
      "customer_customs": [
        {
          "field_id": 11,
          "value": "Dai銀行"
        },
        {
          "field_id": 12,
          "value": "ソフトウェア"
        },
        {
          "field_id": 13,
          "value": "なし"
        }
      ],
      "payment": "銀行振込",
      "payment_at": null,
      "total_price": 50000,
      "tax": 2500,
      "tax_rate": "0.08",
      "COD_cost": 0,
      "shipping_cost": 0,
      "final_price": 52500,
      "use_point": 0,
      "get_point": 0,
      "order_totals": [
        {
          "tax_rate": "0.05",
          "total": 50000,
          "tax": 2500,
          "total_incl_tax": 52500
        }
      ],
      "customer_message": "",
      "admin_message": "",
      "memo": "お客様から電話があり、在庫確認後連絡が欲しいとのこと。",
      "customs": null,
      "enquete1": "1",
      "enquete2": "",
      "enquete3": "",
      "enquete4": "",
      "enquete5": "",
      "ordered_at": "2016-04-13 16:44:43",
      "affiliate_id": "",
      "estimate_id": "",
      "status": "カスタム1"
    }
  ]
}
```
