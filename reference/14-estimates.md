# 見積

見積情報

## GET {{api_url}}/api/v1/estimates/1

**レスポンス一覧**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| id | 見積ID | 整数 | 11 |  |
| code | 見積番号 | 整数 | 255 |  |
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
| destination_code | 配送先コード | 文字列 | 255 |  |
| shipping_group_id | 配送グループID | 文字列 | 255 |  |
| delivery_comp_name | 配送先 会社名 | 文字列 | 255 |  |
| delivery_department | 配送先 部署名 | 文字列 | 255 |  |
| delivery_name | 配送先 担当者名 | 文字列 | 255 |  |
| delivery_zip | 配送先郵便番号 | 文字列 | 16 |  |
| delivery_pref | 配送先都道府県 | 文字列 | 32 |  |
| delivery_address1 | 配送先 市町区村 | 文字列 | 255 |  |
| delivery_address2 | 配送先 町域・番地 | 文字列 | 255 |  |
| delivery_address3 | 配送先 ビル・建物名 | 文字列 | 255 |  |
| delivery_tel | 配送先電話番号 | 文字列 | 255 |  |
| due_date | 配送希望日 | 日付 | 10 | Y-m-d |
| due_time | 配送希望日 | 文字列 | 32 |  |
| customer_customs | 注文者 カスタム項目 | 配列 |  |  |
| payment | 決済方法 | 文字列 | 255 |  |
| total_price | 商品合計金額 | 数値 | 255 |  |
| tax | 消費税 | 整数 | 8 |  |
| tax_rate | 税率 | 数値 | 255 |  |
| COD_cost | 決済手数料 | 整数 | 8 |  |
| shipping_cost | 送料 | 整数 | 8 |  |
| final_price | 見積総額 | 整数 | 11 |  |
| estimate_totals | 税率ごとの合計金額 | 配列 |  | tax_rate=税率,total=税抜合計金額,tax=消費税,total_incl_tax=税込合計金額 |
| customer_message | お客様からの連絡事項 | 文字列 | 65,535 |  |
| admin_message | お客様への連絡事項 | 文字列 | 65,535 |  |
| memo | 管理用メモ | 文字列 | 65,535 |  |
| customs | 見積カスタム項目 | 配列 |  |  |
| enquete1 | アンケート1 | 文字列 | 255 |  |
| enquete2 | アンケート2 | 文字列 | 255 |  |
| enquete3 | アンケート3 | 文字列 | 255 |  |
| enquete4 | アンケート4 | 文字列 | 255 |  |
| enquete5 | アンケート5 | 文字列 | 255 |  |
| estimated_at | 見積日 | 日付 | 19 | Y-m-d H:i:s |
| affiliate_id | 参照元ID | 文字列 | 255 |  |
| related_order_id | 受注ID | 整数 | 11 |  |
| estimate_due | 見積期限 | 日付 | 19 | Y-m-d |
| status | 対応状況 | 文字列 | 255 |  |

**レスポンス例（200 OK）:**

```json
{
  "estimate": {
    "id": 1,
    "code": "13793979691",
    "customer_id": 1,
    "customer_ext_id": "B15487",
    "customer_parent_id": null,
    "customer_salesman_id": null,
    "customer_comp_name": "有限会社サンプル",
    "customer_department": "制作部",
    "customer_name": "通常価格さとし",
    "customer_tel": "222-222-3333",
    "customer_mobile_phone": "090-555-5555",
    "customer_email": "guest@dai.co.jp",
    "customer_price_group_id": null,
    "customer_zip": "111-1111",
    "customer_pref": "東京都",
    "customer_address1": "○○区△町",
    "customer_address2": "3-24",
    "customer_address3": "〇〇ビル",
    "customer_customs": null,
    "destination_code": null,
    "shipping_group_id": 1,
    "delivery_comp_name": "有限会社サンプル",
    "delivery_department": "制作部",
    "delivery_name": "通常価格さとし",
    "delivery_zip": "111-1111",
    "delivery_pref": "東京都",
    "delivery_address1": "○○区△町3-24 〇〇ビル",
    "delivery_address2": "",
    "delivery_address3": "",
    "delivery_tel": "222-222-3333",
    "due_date": null,
    "due_time": null,
    "payment": "銀行振込",
    "total_price": 2755000,
    "tax": 137750,
    "tax_rate": "",
    "COD_cost": 0,
    "shipping_cost": 0,
    "final_price": 2892750,
    "estimate_totals": [
      {
        "tax_rate": "",
        "total": 2892750,
        "tax": 0,
        "total_incl_tax": 2892750
      }
    ],
    "customer_message": "",
    "admin_message": "",
    "memo": "",
    "enquete1": "ああ",
    "enquete2": "yahoo",
    "enquete3": "dena,sd",
    "enquete4": "",
    "enquete5": "",
    "estimated_at": "2013-09-17 15:06:09",
    "affiliate_id": null,
    "related_order_id": null,
    "estimate_due": "2014-09-17",
    "status": "新規見積"
  }
}
```

## GET {{api_url}}/api/v1/estimates

**URIパラメータ**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| limit | limit | 整数 |  | 指定した件数分のデータを取得します。指定なしの場合は20件、最大100件 |
| offset | offset | 整数 |  | 指定した値+1件目のデータからlimit分を取得します。指定しない場合は0 |
| ids | ID複数 | 整数 |  | 複数の見積IDをカンマ区切りで指定 |
| fields | フィールド | 文字列 |  | 取得したいフィールドカンマ区切りで指定 |
| code | 見積番号 | 整数 | 255 |  |
| customer_id | 会員ID | 整数 | 11 |  |
| customer_salesman_id | 営業担当者 | 文字列 | 255 |  |
| payment | 決済方法 | 文字列 | 255 |  |
| customer_zip | 注文者 郵便番号 | 文字列 | 32 |  |
| customer_pref | 注文者 都道府県 | 文字列 | 32 |  |
| customer_address1 | 注文者 市区町村 | 文字列 | 255 |  |
| customer_address2 | 注文者 町域・番地 | 文字列 | 255 |  |
| customer_address3 | 注文者 ビル建物名 | 文字列 | 255 |  |
| destination_code | 配送先コード | 文字列 | 255 |  |
| shipping_group_id | 配送グループID | 文字列 | 255 |  |
| delivery_zip | 配送先郵便番号 | 文字列 | 16 |  |
| delivery_pref | 配送先都道府県 | 文字列 | 32 |  |
| delivery_tel | 配送先電話番号 | 文字列 | 255 |  |
| due_date | 配送希望日 | 文字列 | 19 | Y-m-d |
| customer_customs | 注文者 カスタム項目 | 配列 |  | 配列のキーにfield_id、値にvalue。例) customer_customs\[11\]=検索する値 |
| enquete1 | アンケート1 | 文字列 | 255 |  |
| enquete2 | アンケート2 | 文字列 | 255 |  |
| enquete3 | アンケート3 | 文字列 | 255 |  |
| enquete4 | アンケート4 | 文字列 | 255 |  |
| enquete5 | アンケート5 | 文字列 | 255 |  |
| customer_message | お客様からの連絡事項 | 文字列 | 65,535 |  |
| admin_message | お客様への連絡事項 | 文字列 | 65,535 |  |
| memo | 管理用メモ | 文字列 | 65,535 |  |
| customs | 見積カスタム項目 | 配列 |  | 配列のキーにfield_id、値にvalue。例) customs\[6\]=検索する値 |
| status | 対応状況 | 文字列 | 255 |  |
| estimated_at | 見積日 | 文字列 | 19 | Y-m-d |
| estimate_due | 見積期限 | 日付 | 19 | Y-m-d |
| related_order_id | 受注ID | 整数 | 11 |  |
| complete | 見積情報一式 | 整数 |  | 1 指定すると見積に紐付いた見積商品を取得 |

**見積商品から絞り込み**

| パラメータ名 | 名称 |
| --- | --- |
| estimate_products__{{key}} | 見積商品の{{key}}で絞り込み |

※ それぞれの利用可能な{{key}}はそれぞれのAPIを確認してください。

## 拡張パラメータによる高度な絞り込み

拡張パラメータを使用することで、より高度な絞り込みが可能です。

詳しくは、[パラメータ](../docs/04-parameters.md)の「拡張パラメータ」欄をご参照ください。

**レスポンス例（200 OK）:**

```json
{
  "estimates": [
    {
      "id": 1,
      "code": "13793979691",
      "customer_id": 1,
      "customer_ext_id": "B15487",
      "customer_parent_id": null,
      "customer_salesman_id": null,
      "customer_comp_name": "有限会社サンプル",
      "customer_department": "制作部",
      "customer_name": "通常価格さとし",
      "customer_tel": "222-222-3333",
      "customer_mobile_phone": "090-555-5555",
      "customer_email": "guest@dai.co.jp",
      "customer_price_group_id": null,
      "customer_zip": "111-1111",
      "customer_pref": "東京都",
      "customer_address1": "○○区△町",
      "customer_address2": "3-24",
      "customer_address3": "〇〇ビル",
      "customer_customs": null,
      "destination_code": null,
      "shipping_group_id": 1,
      "delivery_comp_name": "有限会社サンプル",
      "delivery_department": "制作部",
      "delivery_name": "通常価格さとし",
      "delivery_zip": "111-1111",
      "delivery_pref": "東京都",
      "delivery_address1": "○○区△町3-24 〇〇ビル",
      "delivery_address2": "",
      "delivery_address3": "",
      "delivery_tel": "222-222-3333",
      "due_date": null,
      "due_time": null,
      "payment": "銀行振込",
      "total_price": 2755000,
      "tax": 137750,
      "tax_rate": "",
      "COD_cost": 0,
      "shipping_cost": 0,
      "final_price": 2892750,
      "estimate_totals": [
        {
          "tax_rate": "",
          "total": 2892750,
          "tax": 0,
          "total_incl_tax": 2892750
        }
      ],
      "customer_message": "",
      "admin_message": "",
      "memo": "",
      "enquete1": "ああ",
      "enquete2": "yahoo",
      "enquete3": "dena,sd",
      "enquete4": "",
      "enquete5": "",
      "estimated_at": "2013-09-17 15:06:09",
      "affiliate_id": null,
      "related_order_id": null,
      "estimate_due": "2014-09-17",
      "status": "新規見積"
    },
    {
      "id": 2,
      "code": "13964062594",
      "customer_id": 1,
      "customer_ext_id": "B15487",
      "customer_parent_id": null,
      "customer_salesman_id": null,
      "customer_comp_name": "有限会社サンプル",
      "customer_department": "制作部",
      "customer_name": "通常価格さとし",
      "customer_tel": "222-222-3333",
      "customer_mobile_phone": "090-555-5555",
      "customer_email": "guest@dai.co.jp",
      "customer_price_group_id": null,
      "customer_zip": "111-1111",
      "customer_pref": "東京都",
      "customer_address1": "○○区△町",
      "customer_address2": "3-24",
      "customer_address3": "〇〇ビル",
      "customer_customs": null,
      "destination_code": null,
      "shipping_group_id": 1,
      "delivery_comp_name": "有限会社サンプル",
      "delivery_department": "制作部",
      "delivery_name": "通常価格さとし",
      "delivery_zip": "111-1111",
      "delivery_pref": "東京都",
      "delivery_address1": "○○区△町3-24 〇〇ビル",
      "delivery_address2": "",
      "delivery_address3": "",
      "delivery_tel": "222-222-3333",
      "due_date": null,
      "due_time": null,
      "payment": "自社掛払い",
      "total_price": 13600,
      "tax": 680,
      "tax_rate": "0.05",
      "COD_cost": 0,
      "shipping_cost": 525,
      "final_price": 14805,
      "estimate_totals": [
        {
          "tax_rate": "0.05",
          "total": 14100,
          "tax": 705,
          "total_incl_tax": 14805
        }
      ],
      "customer_message": "",
      "admin_message": "",
      "memo": "",
      "enquete1": "",
      "enquete2": "google",
      "enquete3": "",
      "enquete4": "",
      "enquete5": "",
      "estimated_at": "2014-04-02 11:37:39",
      "affiliate_id": null,
      "related_order_id": null,
      "estimate_due": "2015-04-02",
      "status": "新規見積"
    },
    {
      "id": 3,
      "code": "13964063317",
      "customer_id": 10021,
      "customer_ext_id": "101235",
      "customer_parent_id": null,
      "customer_salesman_id": null,
      "customer_comp_name": "株式会社ミニコンビニ",
      "customer_department": "",
      "customer_name": "御得意価格たろう",
      "customer_tel": "000-0000-0000",
      "customer_mobile_phone": "",
      "customer_email": "guest+2@dai.co.jp",
      "customer_price_group_id": "特別会員様",
      "customer_zip": "163-1310",
      "customer_pref": "東京都",
      "customer_address1": "新宿区",
      "customer_address2": "西新宿新宿アイランドタワー",
      "customer_address3": "",
      "customer_customs": null,
      "destination_code": null,
      "shipping_group_id": 1,
      "delivery_comp_name": "株式会社ミニコンビニ",
      "delivery_department": "",
      "delivery_name": "御得意価格たろう",
      "delivery_zip": "163-1310",
      "delivery_pref": "東京都",
      "delivery_address1": "新宿区",
      "delivery_address2": "西新宿新宿アイランドタワー",
      "delivery_address3": "",
      "delivery_tel": "000-0000-0000",
      "due_date": null,
      "due_time": null,
      "payment": "銀行振込",
      "total_price": 72000,
      "tax": 3600,
      "tax_rate": "0.05",
      "COD_cost": 0,
      "shipping_cost": 0,
      "final_price": 75600,
      "estimate_totals": [
        {
          "tax_rate": "0.05",
          "total": 72000,
          "tax": 3600,
          "total_incl_tax": 75600
        }
      ],
      "customer_message": "",
      "admin_message": "",
      "memo": "",
      "enquete1": "",
      "enquete2": "etc",
      "enquete3": "",
      "enquete4": "",
      "enquete5": "",
      "estimated_at": "2014-04-02 11:38:51",
      "affiliate_id": null,
      "related_order_id": null,
      "estimate_due": "2015-04-02",
      "status": "新規見積"
    },
    {
      "id": 4,
      "code": "13964064017",
      "customer_id": 10021,
      "customer_ext_id": "101235",
      "customer_parent_id": null,
      "customer_salesman_id": null,
      "customer_comp_name": "株式会社ミニコンビニ",
      "customer_department": "",
      "customer_name": "御得意価格たろう",
      "customer_tel": "000-0000-0000",
      "customer_mobile_phone": "",
      "customer_email": "guest+2@dai.co.jp",
      "customer_price_group_id": "特別会員様",
      "customer_zip": "163-1310",
      "customer_pref": "東京都",
      "customer_address1": "新宿区",
      "customer_address2": "西新宿新宿アイランドタワー",
      "customer_address3": "",
      "customer_customs": null,
      "destination_code": null,
      "shipping_group_id": 1,
      "delivery_comp_name": "株式会社ミニコンビニ",
      "delivery_department": "",
      "delivery_name": "御得意価格たろう",
      "delivery_zip": "163-1310",
      "delivery_pref": "東京都",
      "delivery_address1": "新宿区",
      "delivery_address2": "西新宿新宿アイランドタワー",
      "delivery_address3": "",
      "delivery_tel": "000-0000-0000",
      "due_date": null,
      "due_time": null,
      "payment": "銀行振込",
      "total_price": 1600000,
      "tax": 80000,
      "tax_rate": "0.05",
      "COD_cost": 0,
      "shipping_cost": 0,
      "final_price": 1680000,
      "estimate_totals": [
        {
          "tax_rate": "0.05",
          "total": 1600000,
          "tax": 80000,
          "total_incl_tax": 1680000
        }
      ],
      "customer_message": "",
      "admin_message": "",
      "memo": "",
      "enquete1": "",
      "enquete2": "hp",
      "enquete3": "",
      "enquete4": "",
      "enquete5": "",
      "estimated_at": "2014-04-02 11:40:01",
      "affiliate_id": null,
      "related_order_id": null,
      "estimate_due": "2015-04-02",
      "status": "新規見積"
    },
    {
      "id": 5,
      "code": "13964064738",
      "customer_id": 10022,
      "customer_ext_id": "",
      "customer_parent_id": null,
      "customer_salesman_id": null,
      "customer_comp_name": "地元オークション株式会社",
      "customer_department": "営業部",
      "customer_name": "販売制限まさみ",
      "customer_tel": "0000-00-0000",
      "customer_mobile_phone": "",
      "customer_email": "guest+3@dai.co.jp",
      "customer_price_group_id": null,
      "customer_zip": "616-8093",
      "customer_pref": "京都府",
      "customer_address1": "京都市右京区御室竪町",
      "customer_address2": "1−25",
      "customer_address3": "妙心寺ビル10F",
      "customer_customs": null,
      "destination_code": null,
      "shipping_group_id": 1,
      "delivery_comp_name": "地元オークション株式会社",
      "delivery_department": "営業部",
      "delivery_name": "販売制限まさみ",
      "delivery_zip": "616-8093",
      "delivery_pref": "京都府",
      "delivery_address1": "京都市右京区",
      "delivery_address2": "御室竪町1−25 ",
      "delivery_address3": "妙心寺ビル10F",
      "delivery_tel": "0000-00-0000",
      "due_date": null,
      "due_time": null,
      "payment": "クレジット",
      "total_price": 6000,
      "tax": 300,
      "tax_rate": "0.05",
      "COD_cost": 0,
      "shipping_cost": 525,
      "final_price": 6825,
      "estimate_totals": [
        {
          "tax_rate": "0.05",
          "total": 6500,
          "tax": 325,
          "total_incl_tax": 6825
        }
      ],
      "customer_message": "",
      "admin_message": "",
      "memo": "",
      "enquete1": "",
      "enquete2": "yahoo",
      "enquete3": "",
      "enquete4": "",
      "enquete5": "",
      "estimated_at": "2014-04-02 11:41:13",
      "affiliate_id": null,
      "related_order_id": null,
      "estimate_due": "2015-04-02",
      "status": "新規見積"
    },
    {
      "id": 6,
      "code": "14358923004",
      "customer_id": 10037,
      "customer_ext_id": "",
      "customer_parent_id": null,
      "customer_salesman_id": null,
      "customer_comp_name": "大塚寝具株式会社",
      "customer_department": "調達部",
      "customer_name": "坂本時郎",
      "customer_tel": "0000-00-0000",
      "customer_mobile_phone": "",
      "customer_email": "guest+14@dai.co.jp",
      "customer_price_group_id": null,
      "customer_zip": "111-1111",
      "customer_pref": "青森県",
      "customer_address1": "青森市",
      "customer_address2": "111",
      "customer_address3": "",
      "customer_customs": null,
      "destination_code": null,
      "shipping_group_id": 1,
      "delivery_comp_name": "大塚寝具株式会社",
      "delivery_department": "調達部",
      "delivery_name": "坂本時郎",
      "delivery_zip": "111-1111",
      "delivery_pref": "青森県",
      "delivery_address1": "青森市111 ",
      "delivery_address2": "",
      "delivery_address3": "",
      "delivery_tel": "0000-00-0000",
      "due_date": null,
      "due_time": null,
      "payment": "銀行振込",
      "total_price": 500000,
      "tax": 40000,
      "tax_rate": "0.08",
      "COD_cost": 0,
      "shipping_cost": 0,
      "final_price": 540000,
      "estimate_totals": [
        {
          "tax_rate": "0.08",
          "total": 500000,
          "tax": 40000,
          "total_incl_tax": 540000
        }
      ],
      "customer_message": "大量購入するので見積りお願いします",
      "admin_message": "",
      "memo": "",
      "enquete1": "",
      "enquete2": "",
      "enquete3": "",
      "enquete4": "",
      "enquete5": "",
      "estimated_at": "2015-07-03 11:58:20",
      "affiliate_id": null,
      "related_order_id": null,
      "estimate_due": "2016-07-02",
      "status": "新規見積"
    },
    {
      "id": 7,
      "code": "14358972320",
      "customer_id": 1,
      "customer_ext_id": "B15487",
      "customer_parent_id": null,
      "customer_salesman_id": null,
      "customer_comp_name": "有限会社サンプル",
      "customer_department": "制作部",
      "customer_name": "通常価格さとし",
      "customer_tel": "222-222-3333",
      "customer_mobile_phone": "090-555-5555",
      "customer_email": "guest@dai.co.jp",
      "customer_price_group_id": null,
      "customer_zip": "111-1111",
      "customer_pref": "東京都",
      "customer_address1": "○○区△町",
      "customer_address2": "3-24",
      "customer_address3": "〇〇ビル",
      "customer_customs": null,
      "destination_code": null,
      "shipping_group_id": 1,
      "delivery_comp_name": "有限会社サンプル",
      "delivery_department": "制作部",
      "delivery_name": "通常価格さとし",
      "delivery_zip": "111-1111",
      "delivery_pref": "東京都",
      "delivery_address1": "○○区△町3-24 〇〇ビル",
      "delivery_address2": "",
      "delivery_address3": "",
      "delivery_tel": "222-222-3333",
      "due_date": null,
      "due_time": null,
      "payment": "銀行振込",
      "total_price": 6000000,
      "tax": 480000,
      "tax_rate": "0.08",
      "COD_cost": 0,
      "shipping_cost": 0,
      "final_price": 6480000,
      "estimate_totals": [
        {
          "tax_rate": "0.08",
          "total": 6000000,
          "tax": 480000,
          "total_incl_tax": 6480000
        }
      ],
      "customer_message": "先入金、大量購入なのでお見積りお願いします",
      "admin_message": "",
      "memo": "",
      "enquete1": "",
      "enquete2": "",
      "enquete3": "",
      "enquete4": "",
      "enquete5": "",
      "estimated_at": "2015-07-03 13:20:32",
      "affiliate_id": null,
      "related_order_id": null,
      "estimate_due": "2016-07-02",
      "status": "新規見積"
    },
    {
      "id": 8,
      "code": "14768770706",
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
      "customer_price_group_id": "特別会員",
      "customer_zip": "100-0000",
      "customer_pref": "東京都",
      "customer_address1": "千代田区",
      "customer_address2": "1-１　",
      "customer_address3": "",
      "customer_customs": [
        {
          "field_id": 11,
          "value": "関西アーバン銀行"
        },
        {
          "field_id": 12,
          "value": "カスタムオプション2"
        }
      ],
      "destination_code": null,
      "shipping_group_id": 3,
      "delivery_comp_name": "株式会社カンサイ機械",
      "delivery_department": "購買部",
      "delivery_name": "新山綱彦",
      "delivery_zip": "100-0000",
      "delivery_pref": "東京都",
      "delivery_address1": "千代田区",
      "delivery_address2": "1-１　",
      "delivery_address3": "",
      "delivery_tel": "0000-1111-0000",
      "due_date": null,
      "due_time": null,
      "payment": null,
      "total_price": 47600,
      "tax": 3808,
      "tax_rate": "0.08",
      "COD_cost": 0,
      "shipping_cost": 1000,
      "final_price": 52408,
      "estimate_totals": [
        {
          "tax_rate": "0.08",
          "total": 48526,
          "tax": 3882,
          "total_incl_tax": 52408
        }
      ],
      "customer_message": "",
      "admin_message": "",
      "memo": "",
      "enquete1": "",
      "enquete2": "",
      "enquete3": "",
      "enquete4": "",
      "enquete5": "",
      "estimated_at": "2016-10-19 20:37:50",
      "affiliate_id": null,
      "related_order_id": null,
      "estimate_due": "2017-10-19",
      "status": "新規見積"
    },
    {
      "id": 9,
      "code": "16786977735",
      "customer_id": 1,
      "customer_ext_id": "B15487safsdfsa",
      "customer_parent_id": null,
      "customer_salesman_id": null,
      "customer_comp_name": "有限会社サンプル",
      "customer_department": "制作部",
      "customer_name": "通常価格さとし",
      "customer_tel": "222-222-3333",
      "customer_mobile_phone": "090-555-5555",
      "customer_email": "guest@dai.co.jp",
      "customer_price_group_id": null,
      "customer_zip": "111-1111",
      "customer_pref": "東京都",
      "customer_address1": "○○区△町",
      "customer_address2": "3-24",
      "customer_address3": "〇〇ビル",
      "customer_customs": [
        {
          "field_id": 11,
          "value": "カスタム1"
        },
        {
          "field_id": 12,
          "value": "カスタムオプション1"
        },
        {
          "field_id": 13,
          "value": "なし"
        }
      ],
      "destination_code": null,
      "shipping_group_id": 1,
      "delivery_comp_name": "有限会社サンプル",
      "delivery_department": "制作部",
      "delivery_name": "通常価格さとし",
      "delivery_zip": "111-1111",
      "delivery_pref": "東京都",
      "delivery_address1": "○○区△町",
      "delivery_address2": "3-24",
      "delivery_address3": "〇〇ビル",
      "delivery_tel": "222-222-3333",
      "due_date": null,
      "due_time": null,
      "payment": "銀行振込",
      "total_price": 4000,
      "tax": 450,
      "tax_rate": "0.1",
      "COD_cost": 0,
      "shipping_cost": 500,
      "final_price": 4950,
      "estimate_totals": [
        {
          "tax_rate": "0.1",
          "total": 4500,
          "tax": 450,
          "total_incl_tax": 4950
        }
      ],
      "customer_message": "",
      "admin_message": "",
      "memo": null,
      "enquete1": "",
      "enquete2": "",
      "enquete3": "",
      "enquete4": "",
      "enquete5": "",
      "estimated_at": "2023-03-13 17:56:13",
      "affiliate_id": null,
      "related_order_id": null,
      "estimate_due": "2024-03-12",
      "status": "新規見積"
    },
    {
      "id": 10,
      "code": "16799795816",
      "customer_id": 1,
      "customer_ext_id": "B15487safsdfsa",
      "customer_parent_id": null,
      "customer_salesman_id": null,
      "customer_comp_name": "有限会社サンプル",
      "customer_department": "制作部",
      "customer_name": "通常価格さとし",
      "customer_tel": "222-222-3333",
      "customer_mobile_phone": "090-555-5555",
      "customer_email": "guest@dai.co.jp",
      "customer_price_group_id": null,
      "customer_zip": "111-1111",
      "customer_pref": "東京都",
      "customer_address1": "○○区△町",
      "customer_address2": "3-24",
      "customer_address3": "〇〇ビル",
      "customer_customs": [
        {
          "field_id": 11,
          "value": "カスタム1"
        },
        {
          "field_id": 12,
          "value": "カスタムオプション1"
        },
        {
          "field_id": 13,
          "value": "なし"
        }
      ],
      "destination_code": null,
      "shipping_group_id": 1,
      "delivery_comp_name": "有限会社サンプル",
      "delivery_department": "制作部",
      "delivery_name": "通常価格さとし",
      "delivery_zip": "111-1111",
      "delivery_pref": "東京都",
      "delivery_address1": "○○区△町",
      "delivery_address2": "3-24",
      "delivery_address3": "〇〇ビル",
      "delivery_tel": "222-222-3333",
      "due_date": null,
      "due_time": null,
      "payment": "銀行振込",
      "total_price": 10200,
      "tax": 1070,
      "tax_rate": "0.1",
      "COD_cost": 0,
      "shipping_cost": 500,
      "final_price": 11770,
      "estimate_totals": [
        {
          "tax_rate": "0.1",
          "total": 10700,
          "tax": 1070,
          "total_incl_tax": 11770
        }
      ],
      "customer_message": "",
      "admin_message": "",
      "memo": null,
      "enquete1": "111",
      "enquete2": "google",
      "enquete3": "dena",
      "enquete4": "",
      "enquete5": "",
      "estimated_at": "2023-03-28 13:59:41",
      "affiliate_id": null,
      "related_order_id": null,
      "estimate_due": "2024-03-27",
      "status": "新規見積"
    }
  ],
  "meta": {
    "limit": 20,
    "offset": 0,
    "total": 10
  }
}
```
