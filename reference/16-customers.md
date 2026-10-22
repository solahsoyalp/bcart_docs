# 会員

Bカートで商品を購入する側のアカウント

## GET {{api_url}}/api/v1/customers/1

**レスポンス一覧**

| パラメータ名 | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| id | 会員ID | 整数 | 11 |  |
| ext_id | 貴社独自会員ID | 文字列 | 255 |  |
| agent_id | 代理店ID | 文字列 | 255 |  |
| agent_rate | 代理店レート | 数値 | 11 | 10%の場合、0.1 |
| parent_id | 親代理店ID | 文字列 | 255 |  |
| destination_code | 配送コード | 文字列 | 255 |  |
| comp_name | 会社名 | 文字列 | 255 |  |
| comp_name_kana | 会社名カナ | 文字列 | 255 |  |
| ceo_last_name | 代表者姓 | 文字列 | 50 |  |
| ceo_first_name | 代表者名 | 文字列 | 50 |  |
| ceo_last_name_kana | 代表者姓カナ | 文字列 | 50 |  |
| ceo_first_name_kana | 代表者名カナ | 文字列 | 50 |  |
| department | 部署名 | 文字列 | 255 |  |
| tanto_last_name | 担当者姓 | 文字列 | 50 |  |
| tanto_first_name | 担当者名 | 文字列 | 50 |  |
| tanto_last_name_kana | 担当者姓カナ | 文字列 | 50 |  |
| tanto_first_name_kana | 担当者名カナ | 文字列 | 50 |  |
| zip | 郵便番号 | 文字列 | 64 |  |
| pref | 都道府県 | 文字列 | 32 |  |
| address1 | 市区町村 | 文字列 | 255 |  |
| address2 | 町域・番地 | 文字列 | 255 |  |
| address3 | ビル・建物名 | 文字列 | 255 |  |
| email | メールアドレス | 文字列 | 255 |  |
| is_invalid_email | メールアドレス無効 | 整数 | 1 | 無効：1  <br>有効：0 |
| email_cc | メールアドレスCC | 文字列 | 255 | 複数ある場合はカンマ区切り |
| tel | 電話番号 | 文字列 | 255 |  |
| mobile_phone | 携帯番号 | 文字列 | 255 |  |
| fax | FAX番号 | 文字列 | 255 |  |
| url | URL | 文字列 | 255 |  |
| foundation | 設立年月 | 文字列 | 50 | 2021年1月の場合、2021-1 |
| sales | 年商 | 整数 | 255 |  |
| job | 業態 / 業種 | 文字列 | 255 |  |
| memo | メモ | 文字列 | 65,535 |  |
| payment | 決済方法 | 文字列 | 255 |  |
| special_shipping_cost | 特別送料 | 整数 | 255 | 無効：空文字列  <br>特別送料：半角整数  <br>別見積もり：NULL |
| special_shipping_service_price | 特別送料無料設定 | 整数 | 255 | 無効：空文字列  <br>配送グループ：'配送グループ'  <br>会員別：半角整数 |
| paid | paid申請状況 | 文字列 | 255 | 空文字列または下記いずれかの文字列。'申請待ち','申請済','審査中','利用可能-取引中','利用可能-取引不可','利用不可' |
| mm_flag | メール案内 | 整数 | 1 | 0,1 |
| point | 所持ポイント | 整数 | 255 |  |
| price_group_id | 価格グループID | 整数 | 255 |  |
| view_group_id | 表示グループID | 整数 | 255 |  |
| customs | カスタム項目 | 配列 |  |  |
| salesman_id | 営業担当者 | 文字列 | 255 | 営業担当者IDをカンマ区切り |
| af_id | 参照元ID | 文字列 | 255 |  |
| credit_limit | 月毎の注文限度額 | 整数 | 11 |  |
| cutoff_date | 締め日 | 文字列 | 2 |  |
| payment_month | 支払月 | 文字列 | 4 | 空文字列または下記いずれかの文字列。'当月','翌月','翌々月','翌々々月' |
| payment_date | 支払日 | 文字列 | 2 | 1\~30、または末 |
| default_other_shipping_id | いつもの配送先ID | 整数 | 10 | 別配送先ID |
| default_payment | いつもの決済方法 | 文字列 | 255 |  |
| hidden_price | 価格非表示 | 整数 | 4 | 非表示の場合1、表示の場合0 |
| email_verified_at | メールアドレス認証日時 | 日付 | 19 | 認証済み：Y-m-d H:i:s  <br>未認証：NULL |
| tsa_is_used | 二段階認証 | 整数 | 1 | 有効：1  <br>無効：0 |
| status | 会員認証 | 文字列 | 3 | 空文字列または下記いずれかの文字列。'未承認','無効' |
| created_at | 登録日 | 日付 | 19 | Y-m-d |
| updated_at | 更新日 | 日付 | 19 | Y-m-d |

**レスポンス例（200 OK）:**

```json
{
  "customer": {
    "id": 1,
    "ext_id": "B15487",
    "agent_id": null,
    "agent_rate": null,
    "parent_id": null,
    "destination_code": null,
    "comp_name": "有限会社サンプル",
    "comp_name_kana": "カブシキガイシャサンプル",
    "ceo_last_name": "山田",
    "ceo_first_name": "一郎",
    "ceo_last_name_kana": "ヤマダ",
    "ceo_first_name_kana": "イチロウ",
    "department": "制作部",
    "tanto_last_name": "通常価格",
    "tanto_first_name": "さとし",
    "tanto_last_name_kana": "ツウジョウ",
    "tanto_first_name_kana": "サトシ",
    "zip": "111-1111",
    "pref": "東京都",
    "address1": "○○区△町",
    "address2": "3-24",
    "address3": "〇〇ビル",
    "email": "guest@dai.co.jp",
    "is_invalid_email": 0,
    "email_cc": "",
    "tel": "222-222-3333",
    "mobile_phone": "090-555-5555",
    "fax": "222-222-3333",
    "url": "http://dai.co.jp/",
    "foundation": "2000-4",
    "sales": 10000,
    "job": "雑貨店、ネットショップ",
    "memo": "「有限会社サンプル」様\r\nEメール：guest@dai.co.jp\r\nパスワード：guest\r\n\r\n※ここには会員に関するメモ（管理画面のみで表示）が保存できます。",
    "payment": "銀行振込,代金引換,自社掛払い",
    "special_shipping_cost": null,
    "special_shipping_service_price": "配送グループ",
    "paid": "申請済",
    "special_view": 0,
    "mm_flag": 1,
    "point": 2600,
    "price_group_id": null,
    "view_group_id": null,
    "customs": [
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
    "salesman_id": null,
    "af_id": null,
    "credit_limit": null,
    "cutoff_date": null,
    "payment_month": null,
    "payment_date": null,
    "default_other_shipping_id": null,
    "default_payment": null,
    "hidden_price": 0,
    "email_verified_at": "2025-11-21 10:21:30",
    "tsa_is_used": 1,
    "status": null,
    "created_at": "2012-04-26 18:53:05",
    "updated_at": "2012-04-26 18:53:05"
  }
}
```

## GET {{api_url}}/api/v1/customers

**URLパラメータ**

| パラメータ名 | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| limit | limit | 整数 |  | 指定した件数分のデータを取得します。指定なしの場合は20件、最大100件 |
| offset | offset | 整数 |  | 指定した値+1件目のデータからlimit分を取得します。指定しない場合は0 |
| ids | ID複数 | 整数 |  | 複数の会員IDをカンマ区切りで指定 |
| fields | フィールド | 文字列 |  | 取得したいフィールドカンマ区切りで指定 |
| ext_id | 貴社独自会員ID | 文字列 | 255 |  |
| agent_id | 代理店ID | 文字列 | 255 |  |
| parent_id | 親代理店ID | 文字列 | 255 |  |
| salesman_id | 営業担当者 | 文字列 | 255 |  |
| destination_code | 配送コード | 文字列 | 255 |  |
| comp_name | 会社名 | 文字列 | 255 |  |
| comp_name_kana | 会社名カナ | 文字列 | 255 |  |
| ceo_last_name | 代表者姓 | 文字列 | 50 |  |
| ceo_first_name | 代表者名 | 文字列 | 50 |  |
| ceo_last_name_kana | 代表者姓カナ | 文字列 | 50 |  |
| ceo_first_name_kana | 代表者名カナ | 文字列 | 50 |  |
| tanto_last_name | 担当者姓 | 文字列 | 50 |  |
| tanto_first_name | 担当者名 | 文字列 | 50 |  |
| tanto_last_name_kana | 担当者姓カナ | 文字列 | 50 |  |
| tanto_first_name_kana | 担当者名カナ | 文字列 | 50 |  |
| zip | 郵便番号 | 文字列 | 64 | 000-0000 |
| pref | 都道府県 | 文字列 | 32 |  |
| address1 | 市区町村 | 文字列 | 255 |  |
| address2 | 町域・番地 | 文字列 | 255 |  |
| address3 | ビル・建物名 | 文字列 | 255 |  |
| email | メールアドレス | 文字列 | 255 | メールアドレスの形式 |
| is_invalid_email | メールアドレス無効 | 整数 | 1 | 無効：1  <br>有効：0 |
| email_cc | メールアドレスCC | 文字列 | 255 | メールアドレスをカンマ区切りで指定 |
| tel | 電話番号 | 文字列 | 255 |  |
| mobile_phone | 携帯番号 | 文字列 | 255 |  |
| fax | FAX番号 | 文字列 | 255 |  |
| url | URL | 文字列 | 255 |  |
| price_group_id | 価格グループID | 整数 | 255 |  |
| view_group_id | 表示グループID | 整数 | 255 |  |
| customs | カスタム項目 | 配列 |  | 配列のキーにfield_id、値にvalue。例) customs\[11\]=検索する値 |
| status | 会員認証 | 文字列 | 3 | 空文字列または下記いずれかの文字列。'未承認','無効' |
| payment | 決済方法 | 文字列 | 255 |  |
| special_shipping_cost | 特別送料 | 整数 | 255 | 無効：空文字列  <br>特別送料：半角整数  <br>別見積もり：NULL |
| special_shipping_service_price | 特別送料無料設定 | 整数 | 255 | 無効：空文字列  <br>配送グループ：'配送グループ'  <br>会員別：半角整数 |
| credit_limit | 月毎の注文限度額 | 整数 | 11 |  |
| email_verified_at | メールアドレス認証日時 | 日付 | 19 | 拡張パラメータによる日付（Y-m-d）範囲指定をご利用ください |
| tsa_is_used | 二段階認証 | 整数 | 1 | 有効：1  <br>無効：0 |
| created_at | 登録日 | 日付 | 19 | Y-m-d |
| updated_at | 更新日 | 日付 | 19 | Y-m-d |
| created_at_min | 登録日時〜 | 日時 | 19 | Y-m-d H:i:s　以降を絞込 |
| created_at_max | 〜登録日時 | 日時 | 19 | Y-m-d H:i:s　以前を絞込 |
| updated_at_min | 更新日時〜 | 日時 | 19 | Y-m-d H:i:s　以降を絞込 |
| updated_at_max | 〜更新日時 | 日時 | 19 | Y-m-d H:i:s　以前を絞込 |

## 拡張パラメータによる高度な絞り込み

拡張パラメータを使用することで、より高度な絞り込みが可能です。

詳しくは、[パラメータ](../docs/04-parameters.md)の「拡張パラメータ」欄をご参照ください。

**レスポンス例（200 OK）:**

```json
{
  "customers": [
    {
      "id": 1,
      "ext_id": "B15487",
      "agent_id": null,
      "agent_rate": null,
      "parent_id": null,
      "destination_code": null,
      "comp_name": "有限会社サンプル",
      "comp_name_kana": "カブシキガイシャサンプル",
      "ceo_last_name": "山田",
      "ceo_first_name": "一郎",
      "ceo_last_name_kana": "ヤマダ",
      "ceo_first_name_kana": "イチロウ",
      "department": "制作部",
      "tanto_last_name": "通常価格",
      "tanto_first_name": "さとし",
      "tanto_last_name_kana": "ツウジョウ",
      "tanto_first_name_kana": "サトシ",
      "zip": "111-1111",
      "pref": "東京都",
      "address1": "○○区△町",
      "address2": "3-24",
      "address3": "〇〇ビル",
      "email": "guest@dai.co.jp",
      "is_invalid_email": 0,
      "email_cc": "",
      "tel": "222-222-3333",
      "mobile_phone": "090-555-5555",
      "fax": "222-222-3333",
      "url": "http://dai.co.jp/",
      "foundation": "2000-4",
      "sales": 10000,
      "job": "雑貨店、ネットショップ",
      "memo": "「有限会社サンプル」様\r\nEメール：guest@dai.co.jp\r\nパスワード：guest\r\n\r\n※ここには会員に関するメモ（管理画面のみで表示）が保存できます。",
      "payment": "銀行振込,代金引換,自社掛払い",
      "special_shipping_cost": null,
      "special_shipping_service_price": "配送グループ",
      "paid": "申請済",
      "special_view": 0,
      "mm_flag": 1,
      "point": 2600,
      "price_group_id": null,
      "view_group_id": null,
      "customs": [
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
      "salesman_id": null,
      "af_id": null,
      "credit_limit": null,
      "cutoff_date": null,
      "payment_month": null,
      "payment_date": null,
      "default_other_shipping_id": null,
      "default_payment": null,
      "hidden_price": 0,
      "email_verified_at": null,
      "tsa_is_used": 0,
      "status": null,
      "created_at": "2012-04-26 18:53:05",
      "updated_at": "2012-04-26 18:53:05"
    },
    {
      "id": 10019,
      "ext_id": "A38930",
      "agent_id": null,
      "agent_rate": null,
      "parent_id": null,
      "destination_code": null,
      "comp_name": "販路規制株式会社",
      "comp_name_kana": "ハンロキセイ",
      "ceo_last_name": "販路",
      "ceo_first_name": "規制",
      "ceo_last_name_kana": "ハンロ",
      "ceo_first_name_kana": "キセイ",
      "department": "購買部",
      "tanto_last_name": "ブランド",
      "tanto_first_name": "Aです",
      "tanto_last_name_kana": "ブランド",
      "tanto_first_name_kana": "エデス",
      "zip": "162-0045",
      "pref": "東京都",
      "address1": "新宿区馬場下町",
      "address2": "11111111111111100000",
      "address3": "",
      "email": "brand_a@bcart.jp",
      "email_cc": "",
      "tel": "000000-00000-00000",
      "mobile_phone": "",
      "fax": "",
      "url": "",
      "foundation": "1980-4",
      "sales": 510,
      "job": "雑貨",
      "memo": "",
      "payment": "銀行振込,代金引換,クレジット,自社掛払い,Paid",
      "special_shipping_cost": null,
      "special_shipping_service_price": "配送グループ",
      "paid": "申請済",
      "special_view": 0,
      "mm_flag": 1,
      "point": 0,
      "price_group_id": null,
      "view_group_id": null,
      "customs": [
        {
          "field_id": 11,
          "value": "おおこい"
        },
        {
          "field_id": 12,
          "value": "カスタムオプション1"
        }
      ],
      "salesman_id": null,
      "af_id": null,
      "credit_limit": null,
      "cutoff_date": null,
      "payment_month": null,
      "payment_date": null,
      "default_other_shipping_id": null,
      "default_payment": null,
      "hidden_price": 0,
      "email_verified_at": "2025-11-21 10:21:30",
      "tsa_is_used": 0,
      "status": "未承認",
      "created_at": "2012-05-17 16:11:16",
      "updated_at": "2012-05-17 16:11:16"
    },
    {
      "id": 10021,
      "ext_id": "101235",
      "agent_id": null,
      "agent_rate": null,
      "parent_id": null,
      "destination_code": null,
      "comp_name": "株式会社ミニコンビニ",
      "comp_name_kana": "ミニコンビニ",
      "ceo_last_name": "加藤",
      "ceo_first_name": "たかし",
      "ceo_last_name_kana": "カトウ",
      "ceo_first_name_kana": "タカシ",
      "department": "",
      "tanto_last_name": "御得意価格",
      "tanto_first_name": "たろう",
      "tanto_last_name_kana": "オトクイ",
      "tanto_first_name_kana": "タロウ",
      "zip": "163-1310",
      "pref": "東京都",
      "address1": "新宿区",
      "address2": "西新宿新宿アイランドタワー",
      "address3": "",
      "email": "guest+2@dai.co.jp",
      "email_cc": "",
      "tel": "000-0000-0000",
      "mobile_phone": "",
      "fax": "",
      "url": "",
      "foundation": null,
      "sales": 0,
      "job": "",
      "memo": "会員のメモを残すことができます。",
      "payment": "銀行振込,代金引換,クレジット,自社掛払い,Paid",
      "special_shipping_cost": null,
      "special_shipping_service_price": "配送グループ",
      "paid": "申請済",
      "special_view": 0,
      "mm_flag": 0,
      "point": 0,
      "price_group_id": 2,
      "view_group_id": null,
      "customs": [
        {
          "field_id": 11,
          "value": "jp"
        },
        {
          "field_id": 12,
          "value": "カスタムオプション1"
        }
      ],
      "salesman_id": null,
      "af_id": null,
      "credit_limit": null,
      "cutoff_date": null,
      "payment_month": null,
      "payment_date": null,
      "default_other_shipping_id": null,
      "default_payment": null,
      "hidden_price": 1,
      "email_verified_at": "2025-11-21 10:21:30",
      "tsa_is_used": 1,
      "status": null,
      "created_at": "2012-05-31 19:06:27",
      "updated_at": "2012-05-31 19:06:27"
    },
    {
      "id": 10022,
      "ext_id": null,
      "agent_id": null,
      "agent_rate": null,
      "parent_id": null,
      "destination_code": null,
      "comp_name": "地元オークション株式会社",
      "comp_name_kana": "ジモトオークション",
      "ceo_last_name": "商野",
      "ceo_first_name": "繁彦",
      "ceo_last_name_kana": "ショウノ",
      "ceo_first_name_kana": "シゲヒコ",
      "department": "営業部",
      "tanto_last_name": "販売制限",
      "tanto_first_name": "まさみ",
      "tanto_last_name_kana": "ハンバイシボリ",
      "tanto_first_name_kana": "マサミ",
      "zip": "616-8093",
      "pref": "京都府",
      "address1": "京都市右京区御室竪町",
      "address2": "1−25",
      "address3": "妙心寺ビル10F",
      "email": "guest+3@dai.co.jp",
      "email_cc": "",
      "tel": "0000-00-0000",
      "mobile_phone": "",
      "fax": "",
      "url": "http://co.jp",
      "foundation": "2000-2",
      "sales": 3,
      "job": "卸売",
      "memo": "",
      "payment": "銀行振込,代金引換,クレジット,自社掛払い,Paid",
      "special_shipping_cost": null,
      "special_shipping_service_price": "配送グループ",
      "paid": "申請済",
      "special_view": 0,
      "mm_flag": 1,
      "point": 0,
      "price_group_id": null,
      "view_group_id": 1,
      "customs": [
        {
          "field_id": 11,
          "value": "三井住友銀行"
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
      "salesman_id": null,
      "af_id": null,
      "credit_limit": null,
      "cutoff_date": null,
      "payment_month": null,
      "payment_date": null,
      "default_other_shipping_id": null,
      "default_payment": null,
      "hidden_price": 0,
      "email_verified_at": "2025-11-21 10:21:30",
      "tsa_is_used": 1,
      "status": null,
      "created_at": "2012-07-12 15:58:41",
      "updated_at": "2012-07-12 15:58:41"
    },
    {
      "id": 10023,
      "ext_id": null,
      "agent_id": null,
      "agent_rate": null,
      "parent_id": null,
      "destination_code": null,
      "comp_name": "インポートオブユーロ株式会社",
      "comp_name_kana": "インポートオブユーロ株式会社",
      "ceo_last_name": "秋山",
      "ceo_first_name": "和雄",
      "ceo_last_name_kana": "アキヤマ",
      "ceo_first_name_kana": "カズオ",
      "department": "",
      "tanto_last_name": "垣内",
      "tanto_first_name": "博文",
      "tanto_last_name_kana": "垣内",
      "tanto_first_name_kana": "博文",
      "zip": "111-1111",
      "pref": "大阪府",
      "address1": "吹田市江坂町",
      "address2": "3−23",
      "address3": "江坂第1ビル",
      "email": "guest+4@dai.co.jp",
      "email_cc": "",
      "tel": "0000-00-0000",
      "mobile_phone": "",
      "fax": "",
      "url": "http://euro.co.jp",
      "foundation": "2000-3",
      "sales": 7,
      "job": "輸入、ヨーロッパ",
      "memo": "",
      "payment": "銀行振込,代金引換,クレジット,自社掛払い,Paid",
      "special_shipping_cost": null,
      "special_shipping_service_price": "配送グループ",
      "paid": "申請済",
      "special_view": 0,
      "mm_flag": 1,
      "point": 0,
      "price_group_id": null,
      "view_group_id": null,
      "customs": [
        {
          "field_id": 11,
          "value": "関西アーバン銀行"
        },
        {
          "field_id": 12,
          "value": "カスタムオプション1"
        }
      ],
      "salesman_id": null,
      "af_id": null,
      "credit_limit": null,
      "cutoff_date": null,
      "payment_month": null,
      "payment_date": null,
      "default_other_shipping_id": null,
      "default_payment": null,
      "hidden_price": 0,
      "email_verified_at": "2025-11-21 10:21:30",
      "tsa_is_used": 1,
      "status": null,
      "created_at": "2012-07-12 16:06:46",
      "updated_at": "2012-07-12 16:06:46"
    },
    {
      "id": 10028,
      "ext_id": "X999",
      "agent_id": null,
      "agent_rate": null,
      "parent_id": null,
      "destination_code": null,
      "comp_name": "大竹家具株式会社",
      "comp_name_kana": "オオタケカグカブシキガイシャ",
      "ceo_last_name": "田中",
      "ceo_first_name": "圭一",
      "ceo_last_name_kana": "タナカ",
      "ceo_first_name_kana": "ケイイチ",
      "department": "仕入れ課",
      "tanto_last_name": "中田",
      "tanto_first_name": "宗二",
      "tanto_last_name_kana": "ナカタ",
      "tanto_first_name_kana": "ソウジ",
      "zip": "150-0013",
      "pref": "東京都",
      "address1": "渋谷区恵比寿",
      "address2": "3-24",
      "address3": "",
      "email": "guest+6@dai.co.jp",
      "email_cc": "",
      "tel": "03-1111-1111",
      "mobile_phone": "",
      "fax": "",
      "url": "http://admintest.com",
      "foundation": "1999-1",
      "sales": 2000,
      "job": "家具",
      "memo": "",
      "payment": "銀行振込,代金引換,自社掛払い",
      "special_shipping_cost": null,
      "special_shipping_service_price": "配送グループ",
      "paid": "申請済",
      "special_view": 0,
      "mm_flag": 0,
      "point": 0,
      "price_group_id": null,
      "view_group_id": null,
      "customs": [
        {
          "field_id": 11,
          "value": "三井住友銀行"
        },
        {
          "field_id": 12,
          "value": "カスタムオプション1"
        }
      ],
      "salesman_id": null,
      "af_id": null,
      "credit_limit": null,
      "cutoff_date": null,
      "payment_month": null,
      "payment_date": null,
      "default_other_shipping_id": null,
      "default_payment": null,
      "hidden_price": 0,
      "email_verified_at": "2025-11-21 10:21:30",
      "tsa_is_used": 1,
      "status": null,
      "created_at": "2012-07-23 19:20:13",
      "updated_at": "2012-07-23 19:20:13"
    },
    {
      "id": 10029,
      "ext_id": null,
      "agent_id": null,
      "agent_rate": null,
      "parent_id": null,
      "destination_code": null,
      "comp_name": "酒井衣料有限会社",
      "comp_name_kana": "サカイイリョウユウゲンガイシャ",
      "ceo_last_name": "酒井",
      "ceo_first_name": "一生",
      "ceo_last_name_kana": "サカイ",
      "ceo_first_name_kana": "イチオ",
      "department": "EC事業部",
      "tanto_last_name": "丸藤",
      "tanto_first_name": "祥子",
      "tanto_last_name_kana": "ナルフジ",
      "tanto_first_name_kana": "ショウコ",
      "zip": "100-0001",
      "pref": "東京都",
      "address1": "千代田区千代田",
      "address2": "2-0",
      "address3": "",
      "email": "guest+7@dai.co.jp",
      "email_cc": "",
      "tel": "1111-1111-1111",
      "mobile_phone": "",
      "fax": "",
      "url": "http://admintest.com",
      "foundation": "1988-3",
      "sales": 1000,
      "job": "衣料品",
      "memo": "",
      "payment": "銀行振込,代金引換,自社掛払い,Paid",
      "special_shipping_cost": null,
      "special_shipping_service_price": "配送グループ",
      "paid": "申請済",
      "special_view": 0,
      "mm_flag": 0,
      "point": 0,
      "price_group_id": 2,
      "view_group_id": 3,
      "customs": [
        {
          "field_id": 11,
          "value": "三菱東京UFJ銀行"
        },
        {
          "field_id": 12,
          "value": "カスタムオプション1"
        },
        {
          "field_id": 13,
          "value": "あり"
        }
      ],
      "salesman_id": null,
      "af_id": null,
      "credit_limit": null,
      "cutoff_date": null,
      "payment_month": null,
      "payment_date": null,
      "default_other_shipping_id": null,
      "default_payment": null,
      "hidden_price": 0,
      "email_verified_at": "2025-11-21 10:21:30",
      "tsa_is_used": 1,
      "status": null,
      "created_at": "2012-07-23 19:23:18",
      "updated_at": "2012-07-23 19:23:18"
    },
    {
      "id": 10030,
      "ext_id": null,
      "agent_id": null,
      "agent_rate": null,
      "parent_id": null,
      "destination_code": null,
      "comp_name": "斉藤化粧品リテール株式会社",
      "comp_name_kana": "サイトウケショウヒンリテールカブシキガイシャ",
      "ceo_last_name": "斉藤",
      "ceo_first_name": "和義",
      "ceo_last_name_kana": "サイトウ",
      "ceo_first_name_kana": "カズヨシ",
      "department": "調達部門",
      "tanto_last_name": "三木本",
      "tanto_first_name": "優香",
      "tanto_last_name_kana": "ミキモト",
      "tanto_first_name_kana": "ユウカ",
      "zip": "100-0005",
      "pref": "東京都",
      "address1": "千代田区丸の内",
      "address2": "2-２　",
      "address3": "",
      "email": "guest+8@dai.co.jp",
      "email_cc": "",
      "tel": "0000-000-0000",
      "mobile_phone": "",
      "fax": "",
      "url": "http://admintest.com",
      "foundation": "1998-1",
      "sales": 90000,
      "job": "化粧品、小売、卸",
      "memo": "",
      "payment": "銀行振込,代金引換,クレジット,自社掛払い,Paid",
      "special_shipping_cost": null,
      "special_shipping_service_price": "配送グループ",
      "paid": "申請済",
      "special_view": 0,
      "mm_flag": 0,
      "point": 0,
      "price_group_id": null,
      "view_group_id": null,
      "customs": [
        {
          "field_id": 11,
          "value": "東京三菱UFJ銀行"
        },
        {
          "field_id": 12,
          "value": "カスタムオプション1"
        }
      ],
      "salesman_id": null,
      "af_id": null,
      "credit_limit": null,
      "cutoff_date": null,
      "payment_month": null,
      "payment_date": null,
      "default_other_shipping_id": null,
      "default_payment": null,
      "hidden_price": 0,
      "email_verified_at": "2025-11-21 10:21:30",
      "tsa_is_used": 1,
      "status": null,
      "created_at": "2012-07-23 19:26:43",
      "updated_at": "2012-07-23 19:26:43"
    },
    {
      "id": 10031,
      "ext_id": null,
      "agent_id": null,
      "agent_rate": null,
      "parent_id": null,
      "destination_code": null,
      "comp_name": "有限会社佐藤商店",
      "comp_name_kana": "ユウゲンガイシャサトウショウテン",
      "ceo_last_name": "佐藤",
      "ceo_first_name": "佑樹",
      "ceo_last_name_kana": "サトウ",
      "ceo_first_name_kana": "ユウキ",
      "department": "仕入れ担当",
      "tanto_last_name": "勝間",
      "tanto_first_name": "和子",
      "tanto_last_name_kana": "カツマ",
      "tanto_first_name_kana": "カズコ",
      "zip": "100-0000",
      "pref": "東京都",
      "address1": "千代田区",
      "address2": "111",
      "address3": "",
      "email": "guest+9@dai.co.jp",
      "email_cc": "",
      "tel": "0000-00-0000",
      "mobile_phone": "",
      "fax": "",
      "url": "http://admintest.com",
      "foundation": "1998-2",
      "sales": 10,
      "job": "小売",
      "memo": "",
      "payment": "銀行振込,代金引換,クレジット,自社掛払い,Paid",
      "special_shipping_cost": null,
      "special_shipping_service_price": "配送グループ",
      "paid": "申請済",
      "special_view": 0,
      "mm_flag": 0,
      "point": 0,
      "price_group_id": null,
      "view_group_id": null,
      "customs": [
        {
          "field_id": 11,
          "value": "三井住友銀行"
        },
        {
          "field_id": 12,
          "value": "カスタムオプション1"
        }
      ],
      "salesman_id": null,
      "af_id": null,
      "credit_limit": null,
      "cutoff_date": null,
      "payment_month": null,
      "payment_date": null,
      "default_other_shipping_id": null,
      "default_payment": null,
      "hidden_price": 0,
      "email_verified_at": "2025-11-21 10:21:30",
      "tsa_is_used": 1,
      "status": null,
      "created_at": "2012-07-23 19:37:06",
      "updated_at": "2012-07-23 19:37:06"
    },
    {
      "id": 10032,
      "ext_id": null,
      "agent_id": null,
      "agent_rate": null,
      "parent_id": null,
      "destination_code": null,
      "comp_name": "株式会社近藤商会",
      "comp_name_kana": "カブシキガイシャコンドウショウカイ",
      "ceo_last_name": "近藤",
      "ceo_first_name": "吉弘",
      "ceo_last_name_kana": "コンドウ",
      "ceo_first_name_kana": "ヨシヒロ",
      "department": "調達課",
      "tanto_last_name": "甲斐",
      "tanto_first_name": "雅美",
      "tanto_last_name_kana": "カイ",
      "tanto_first_name_kana": "マサミ",
      "zip": "100-0006",
      "pref": "東京都",
      "address1": "千代田区有楽町",
      "address2": "3-24",
      "address3": "",
      "email": "guest+10@dai.co.jp",
      "email_cc": "",
      "tel": "0000-00-0000",
      "mobile_phone": "",
      "fax": "",
      "url": "http://admintest.com",
      "foundation": "1988-2",
      "sales": 2000,
      "job": "実店舗",
      "memo": "",
      "payment": "銀行振込,代金引換,クレジット,自社掛払い,Paid",
      "special_shipping_cost": null,
      "special_shipping_service_price": "配送グループ",
      "paid": "申請済",
      "special_view": 0,
      "mm_flag": 0,
      "point": 0,
      "price_group_id": null,
      "view_group_id": null,
      "customs": [
        {
          "field_id": 11,
          "value": "東京三菱UFJ銀行"
        },
        {
          "field_id": 12,
          "value": "カスタムオプション1"
        }
      ],
      "salesman_id": null,
      "af_id": null,
      "credit_limit": null,
      "cutoff_date": null,
      "payment_month": null,
      "payment_date": null,
      "default_other_shipping_id": null,
      "default_payment": null,
      "hidden_price": 0,
      "email_verified_at": "2025-11-21 10:21:30",
      "tsa_is_used": 1,
      "status": null,
      "created_at": "2012-07-23 19:40:03",
      "updated_at": "2012-07-23 19:40:03"
    },
    {
      "id": 10033,
      "ext_id": null,
      "agent_id": null,
      "agent_rate": null,
      "parent_id": null,
      "destination_code": null,
      "comp_name": "株式会社カワサキ雑貨",
      "comp_name_kana": "カブシキガイシャカワサキザッカ",
      "ceo_last_name": "川崎",
      "ceo_first_name": "伸二",
      "ceo_last_name_kana": "カワサキ",
      "ceo_first_name_kana": "シンジ",
      "department": "小売部門",
      "tanto_last_name": "神崎",
      "tanto_first_name": "隼人",
      "tanto_last_name_kana": "カンザキ",
      "tanto_first_name_kana": "ハヤト",
      "zip": "100-0000",
      "pref": "東京都",
      "address1": "千代田区",
      "address2": "11",
      "address3": "",
      "email": "guest+11@dai.co.jp",
      "email_cc": "",
      "tel": "0000-00-1111",
      "mobile_phone": "",
      "fax": "",
      "url": "http://admintest.com",
      "foundation": "1999-1",
      "sales": 100000,
      "job": "小売",
      "memo": "",
      "payment": "銀行振込,代金引換,クレジット,自社掛払い,Paid",
      "special_shipping_cost": null,
      "special_shipping_service_price": "配送グループ",
      "paid": "申請済",
      "special_view": 0,
      "mm_flag": 0,
      "point": 0,
      "price_group_id": null,
      "view_group_id": null,
      "customs": [
        {
          "field_id": 11,
          "value": "東京三菱UFJ銀行"
        },
        {
          "field_id": 12,
          "value": "カスタムオプション1"
        }
      ],
      "salesman_id": null,
      "af_id": null,
      "credit_limit": null,
      "cutoff_date": null,
      "payment_month": null,
      "payment_date": null,
      "default_other_shipping_id": null,
      "default_payment": null,
      "hidden_price": 0,
      "email_verified_at": "2025-11-21 10:21:30",
      "tsa_is_used": 1,
      "status": null,
      "created_at": "2012-07-23 19:43:06",
      "updated_at": "2012-07-23 19:43:06"
    },
    {
      "id": 10034,
      "ext_id": null,
      "agent_id": null,
      "agent_rate": null,
      "parent_id": null,
      "destination_code": null,
      "comp_name": "株式会社カンサイ機械",
      "comp_name_kana": "カブシキガイシャカンサイキカイ",
      "ceo_last_name": "兼田",
      "ceo_first_name": "昌彦",
      "ceo_last_name_kana": "カネダ",
      "ceo_first_name_kana": "マサヒコ",
      "department": "購買部",
      "tanto_last_name": "新山",
      "tanto_first_name": "綱彦",
      "tanto_last_name_kana": "ニイヤマ",
      "tanto_first_name_kana": "ツナヒコ",
      "zip": "100-0000",
      "pref": "東京都",
      "address1": "千代田区",
      "address2": "1-１　",
      "address3": "",
      "email": "support+test@bcart.jp",
      "email_cc": "",
      "tel": "0000-1111-0000",
      "mobile_phone": "",
      "fax": "",
      "url": "http://admintest.com",
      "foundation": "2000-1",
      "sales": 1000,
      "job": "小売",
      "memo": "例）代引きでのみお取り引きしているお客様です。",
      "payment": "代金引換",
      "special_shipping_cost": null,
      "special_shipping_service_price": "配送グループ",
      "paid": "申請済",
      "special_view": 0,
      "mm_flag": 0,
      "point": 0,
      "price_group_id": 2,
      "view_group_id": null,
      "customs": [
        {
          "field_id": 11,
          "value": "関西アーバン銀行"
        },
        {
          "field_id": 12,
          "value": "カスタムオプション2"
        }
      ],
      "salesman_id": null,
      "af_id": null,
      "credit_limit": null,
      "cutoff_date": null,
      "payment_month": null,
      "payment_date": null,
      "default_other_shipping_id": null,
      "default_payment": null,
      "hidden_price": 0,
      "email_verified_at": "2025-11-21 10:21:30",
      "tsa_is_used": 1,
      "status": null,
      "created_at": "2012-07-23 19:46:24",
      "updated_at": "2018-10-12 13:21:22"
    },
    {
      "id": 10036,
      "ext_id": null,
      "agent_id": null,
      "agent_rate": null,
      "parent_id": null,
      "destination_code": null,
      "comp_name": "株式会社品川商事",
      "comp_name_kana": "カブシキガイシャシナガワショウジ",
      "ceo_last_name": "品川",
      "ceo_first_name": "一夫",
      "ceo_last_name_kana": "シナガワ",
      "ceo_first_name_kana": "カズオ",
      "department": "仕入れ部",
      "tanto_last_name": "金田",
      "tanto_first_name": "盛介",
      "tanto_last_name_kana": "カネダ",
      "tanto_first_name_kana": "モリスケ",
      "zip": "111-1111",
      "pref": "新潟県",
      "address1": "新潟市神田町",
      "address2": "111",
      "address3": "",
      "email": "guest+13@dai.co.jp",
      "email_cc": "",
      "tel": "0000-00-0000",
      "mobile_phone": "",
      "fax": "",
      "url": "http://admintest.com",
      "foundation": "2000-1",
      "sales": 10000,
      "job": "日用品商社、小売店舗運営",
      "memo": "",
      "payment": "銀行振込,代金引換,自社掛払い",
      "special_shipping_cost": null,
      "special_shipping_service_price": "配送グループ",
      "paid": "申請待ち",
      "special_view": 0,
      "mm_flag": 1,
      "point": 0,
      "price_group_id": null,
      "view_group_id": null,
      "customs": [
        {
          "field_id": 11,
          "value": "三井住友銀行"
        },
        {
          "field_id": 12,
          "value": "カスタムオプション1"
        }
      ],
      "salesman_id": "9,11",
      "af_id": null,
      "credit_limit": null,
      "cutoff_date": null,
      "payment_month": null,
      "payment_date": null,
      "default_other_shipping_id": null,
      "default_payment": null,
      "hidden_price": 0,
      "email_verified_at": "2025-11-21 10:21:30",
      "tsa_is_used": 1,
      "status": null,
      "created_at": "2012-08-10 19:02:49",
      "updated_at": "2018-11-30 09:26:08"
    },
    {
      "id": 10037,
      "ext_id": null,
      "agent_id": null,
      "agent_rate": null,
      "parent_id": null,
      "destination_code": null,
      "comp_name": "大塚寝具株式会社",
      "comp_name_kana": "オオツカシングカブシキガイシャ",
      "ceo_last_name": "大塚",
      "ceo_first_name": "武雄",
      "ceo_last_name_kana": "オオツカ",
      "ceo_first_name_kana": "タケオ",
      "department": "調達部",
      "tanto_last_name": "坂本",
      "tanto_first_name": "時郎",
      "tanto_last_name_kana": "サカモト",
      "tanto_first_name_kana": "トキオ",
      "zip": "111-1111",
      "pref": "青森県",
      "address1": "青森市",
      "address2": "111",
      "address3": "",
      "email": "guest+14@dai.co.jp",
      "email_cc": "",
      "tel": "0000-00-0000",
      "mobile_phone": "",
      "fax": "",
      "url": "http://admintest.com",
      "foundation": "2000-5",
      "sales": 100000,
      "job": "輸入家具の小売",
      "memo": "会員毎にメモを残せます\r\n会員一覧からの「参照」「更新」が可能です。",
      "payment": "銀行振込,代金引換,自社掛払い,Paid",
      "special_shipping_cost": null,
      "special_shipping_service_price": "配送グループ",
      "paid": "申請待ち",
      "special_view": 0,
      "mm_flag": 0,
      "point": 0,
      "price_group_id": null,
      "view_group_id": null,
      "customs": [
        {
          "field_id": 11,
          "value": "三井住友銀行"
        },
        {
          "field_id": 12,
          "value": "カスタムオプション1"
        },
        {
          "field_id": 13,
          "value": "あり"
        }
      ],
      "salesman_id": null,
      "af_id": null,
      "credit_limit": null,
      "cutoff_date": null,
      "payment_month": null,
      "payment_date": null,
      "default_other_shipping_id": null,
      "default_payment": null,
      "hidden_price": 0,
      "email_verified_at": "2025-11-21 10:21:30",
      "tsa_is_used": 1,
      "status": null,
      "created_at": "2012-08-10 19:05:40",
      "updated_at": "2012-08-10 19:05:40"
    },
    {
      "id": 10038,
      "ext_id": "X0001",
      "agent_id": null,
      "agent_rate": null,
      "parent_id": null,
      "destination_code": "1",
      "comp_name": "Dai",
      "comp_name_kana": "",
      "ceo_last_name": "",
      "ceo_first_name": "",
      "ceo_last_name_kana": "",
      "ceo_first_name_kana": "",
      "department": "営業",
      "tanto_last_name": "山田",
      "tanto_first_name": "太郎",
      "tanto_last_name_kana": "ヤマダ",
      "tanto_first_name_kana": "タロウ",
      "zip": "600-0000",
      "pref": "京都府",
      "address1": "京都市下京区",
      "address2": "二帖半敷町",
      "address3": "",
      "email": "tester+create@dai.co.jp",
      "email_cc": "",
      "tel": "075-000-0000",
      "mobile_phone": "",
      "fax": "",
      "url": "",
      "foundation": null,
      "sales": 0,
      "job": "",
      "memo": "",
      "payment": "銀行振込",
      "special_shipping_cost": null,
      "special_shipping_service_price": "配送グループ",
      "paid": null,
      "special_view": 0,
      "mm_flag": 1,
      "point": 0,
      "price_group_id": null,
      "view_group_id": null,
      "customs": [
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
      "salesman_id": null,
      "af_id": null,
      "credit_limit": 100,
      "cutoff_date": null,
      "payment_month": null,
      "payment_date": null,
      "default_other_shipping_id": null,
      "default_payment": null,
      "hidden_price": 0,
      "email_verified_at": "2025-11-21 10:21:30",
      "tsa_is_used": 1,
      "status": null,
      "created_at": "2022-10-28 16:31:18",
      "updated_at": "2022-10-28 16:31:18"
    },
    {
      "id": 10039,
      "ext_id": "X0002",
      "agent_id": null,
      "agent_rate": null,
      "parent_id": null,
      "destination_code": "2",
      "comp_name": "Dai",
      "comp_name_kana": "",
      "ceo_last_name": "",
      "ceo_first_name": "",
      "ceo_last_name_kana": "",
      "ceo_first_name_kana": "",
      "department": "営業",
      "tanto_last_name": "山田",
      "tanto_first_name": "太郎",
      "tanto_last_name_kana": "ヤマダ",
      "tanto_first_name_kana": "タロウ",
      "zip": "600-0001",
      "pref": "京都府",
      "address1": "京都市下京区",
      "address2": "悪王子町",
      "address3": "",
      "email": "tester+create2@dai.co.jp",
      "email_cc": "",
      "tel": "075-000-0000",
      "mobile_phone": "",
      "fax": "",
      "url": "",
      "foundation": null,
      "sales": 0,
      "job": "",
      "memo": "",
      "payment": null,
      "special_shipping_cost": null,
      "special_shipping_service_price": "配送グループ",
      "paid": null,
      "special_view": 0,
      "mm_flag": 1,
      "point": 0,
      "price_group_id": null,
      "view_group_id": null,
      "customs": [
        {
          "field_id": 11,
          "value": "Bカート銀行"
        },
        {
          "field_id": 13,
          "value": "あり"
        }
      ],
      "salesman_id": null,
      "af_id": null,
      "credit_limit": null,
      "cutoff_date": null,
      "payment_month": null,
      "payment_date": null,
      "default_other_shipping_id": null,
      "default_payment": null,
      "hidden_price": 0,
      "email_verified_at": "2025-11-21 10:21:30",
      "tsa_is_used": 1,
      "status": null,
      "created_at": "2022-10-28 16:31:18",
      "updated_at": "2022-10-28 16:31:18"
    },
    {
      "id": 10040,
      "ext_id": null,
      "agent_id": null,
      "agent_rate": null,
      "parent_id": null,
      "destination_code": null,
      "comp_name": "",
      "comp_name_kana": "",
      "ceo_last_name": "",
      "ceo_first_name": "",
      "ceo_last_name_kana": "",
      "ceo_first_name_kana": "",
      "department": "",
      "tanto_last_name": "山田",
      "tanto_first_name": "",
      "tanto_last_name_kana": "",
      "tanto_first_name_kana": "",
      "zip": "600-0000",
      "pref": "京都府",
      "address1": "京都市下京区",
      "address2": "二帖半敷町",
      "address3": "",
      "email": "tester+create_mini@dai.co.jp",
      "email_cc": "",
      "tel": "",
      "mobile_phone": "",
      "fax": "",
      "url": "",
      "foundation": null,
      "sales": 0,
      "job": "",
      "memo": "",
      "payment": null,
      "special_shipping_cost": null,
      "special_shipping_service_price": "配送グループ",
      "paid": null,
      "special_view": 0,
      "mm_flag": 1,
      "point": 0,
      "price_group_id": null,
      "view_group_id": null,
      "customs": null,
      "salesman_id": null,
      "af_id": null,
      "credit_limit": null,
      "cutoff_date": null,
      "payment_month": null,
      "payment_date": null,
      "default_other_shipping_id": null,
      "default_payment": null,
      "hidden_price": 0,
      "email_verified_at": "2025-11-21 10:21:30",
      "tsa_is_used": 1,
      "status": null,
      "created_at": "2022-10-28 16:31:19",
      "updated_at": "2022-10-28 16:31:19"
    }
  ],
  "meta": {
    "limit": 20,
    "offset": 0,
    "total": 17
  }
}
```

## PATCH {{api_url}}/api/v1/customers/10003

**リクエストBODY**

| KEY | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| ext_id | 貴社独自会員ID | 文字列 | 255 | Bカート管理画面のオプション設定で「貴社独自会員IDでログイン」の項目を「有効」にしている場合は項目存在時必須。「無効」の場合は任意。 |
| agent_id | 代理店ID | 文字列 | 255 |  |
| agent_rate | 代理店レート | 数値 | 11 |  |
| parent_id | 親代理店ID | 文字列 | 255 |  |
| destination_code | 配送コード | 文字列 | 255 |  |
| comp_name | 会社名 | 文字列 | 255 |  |
| comp_name_kana | 会社名カナ | 文字列 | 255 |  |
| ceo_last_name | 代表者姓 | 文字列 | 50 |  |
| ceo_first_name | 代表者名 | 文字列 | 50 |  |
| ceo_last_name_kana | 代表者姓カナ | 文字列 | 50 |  |
| ceo_first_name_kana | 代表者名カナ | 文字列 | 50 |  |
| department | 部署 | 文字列 | 255 |  |
| tanto_last_name | 担当者姓 | 文字列 | 50 | 項目存在時必須 |
| tanto_first_name | 担当者名 | 文字列 | 50 |  |
| tanto_last_name_kana | 担当者姓カナ | 文字列 | 50 |  |
| tanto_first_name_kana | 担当者名カナ | 文字列 | 50 |  |
| zip | 郵便番号 | 文字列 | 64 | 項目存在時必須  <br>000-0000 |
| pref | 都道府県 | 文字列 | 32 | 項目存在時必須 |
| address1 | 市区町村 | 文字列 | 255 | 項目存在時必須 |
| address2 | 町域・番地 | 文字列 | 255 | 項目存在時必須 |
| address3 | ビル・建物名 | 文字列 | 255 |  |
| email | メールアドレス | 文字列 | 255 | Bカート管理画面のオプション設定で「空のメールアドレスを許可」にチェックがある場合は任意。ない場合は項目存在時必須。  <br>メールアドレスの形式  <br>※1 |
| is_invalid_email | メールアドレス無効 | 整数 | 1 | 無効：1  <br>有効：0 |
| email_cc | メールアドレスCC | 文字列 | 255 | メールアドレスをカンマ区切りで指定 |
| tel | 電話番号 | 文字列 | 255 |  |
| mobile_phone | 携帯番号 | 文字列 | 255 |  |
| fax | FAX番号 | 文字列 | 255 |  |
| url | URL | 文字列 | 255 |  |
| foundation | 設立年月 | 文字列 | 50 |  |
| sales | 年商 | 整数 | 255 |  |
| job | 業態/業種 | 文字列 | 255 |  |
| memo | 管理者用メモ | 文字列 | 255 |  |
| payment | 決済方法 | 文字列 | 255 |  |
| special_shipping_cost | 特別送料 | 整数 | 255 | 無効：空文字列  <br>特別送料：半角整数  <br>別見積もり：NULL |
| special_shipping_service_price | 特別送料無料設定 | 整数 | 255 | 無効：空文字列  <br>配送グループ：'配送グループ'  <br>会員別：半角整数 |
| mm_flag | メルマガフラグ | 整数 | 1 |  |
| price_group_id | 価格グループID | 整数 | 255 |  |
| view_group_id | 表示グループID | 整数 | 255 |  |
| customs\[{field_id, value}\] | カスタム項目 | 配列 | 65,535 |  |
| salesman_id | 営業担当者 | 文字列 | 255 | 管理者IDをカンマ区切りで指定 |
| af_id | 参照元ID | 文字列 | 255 |  |
| credit_limit | 月毎の注文限度額 | 整数 | 11 |  |
| cutoff_date | 締め日 | 文字列 | 2 |  |
| payment_month | 支払い日（月） | 文字列 | 255 |  |
| payment_date | 支払い日（日） | 文字列 | 2 |  |
| default_other_shipping_id | いつもの配送先 | 整数 | 10 |  |
| default_payment | いつもの決済方法 | 文字列 | 255 |  |
| hidden_price | 価格表示設定 | 整数 | 4 |  |
| tsa_is_used | 二段階認証 | 整数 | 1 | 有効：1  <br>無効：0  <br>※メールアドレスが未認証の場合、二段階認証を有効にできません |
| password | パスワード | 文字列 | 255 | 項目存在時必須　パスワードは暗号化され取得不可 |
| status | 会員認証 | 文字列 | 3 | 未承認/無効、承認の場合は空文字列 |
| created_at | 登録日 | 日付 | 19 | Y-m-d |
| updated_at | 更新日 | 日付 | 19 | Y-m-d |

※1 email_verified_at≠null（メールアドレス認証済み）のレコードのメールアドレスを変更した場合、リクエスト内容に関わらず、自動的にemail_verified_at=null、tsa_is_used=0が設定されます。

**リクエストボディ例:**

```json
{
  "ext_id": "B15487safsdfsa",
  "agent_id": "",
  "agent_rate": "",
  "parent_id": "",
  "destination_code": "",
  "comp_name": "有限会社サンプル",
  "comp_name_kana": "カブシキガイシャサンプル",
  "ceo_last_name": "山田",
  "ceo_first_name": "一郎",
  "ceo_last_name_kana": "ヤマダ",
  "ceo_first_name_kana": "イチロウ",
  "department": "制作部",
  "tanto_last_name": "通常価格",
  "tanto_first_name": "さとし",
  "tanto_last_name_kana": "ツウジョウ",
  "tanto_first_name_kana": "サトシ",
  "credit_limit": 100,
  "password": "1111aaaaa",
  "payment": "銀行振込,代金引換",
  "tsa_is_used": "0"
}
```

**レスポンス例（200 OK）:**

```json
{
  "customer": {
    "id": 1,
    "ext_id": "B15487safsdfsa",
    "agent_id": null,
    "agent_rate": null,
    "parent_id": null,
    "destination_code": null,
    "comp_name": "有限会社サンプル",
    "comp_name_kana": "カブシキガイシャサンプル",
    "ceo_last_name": "山田",
    "ceo_first_name": "一郎",
    "ceo_last_name_kana": "ヤマダ",
    "ceo_first_name_kana": "イチロウ",
    "department": "制作部",
    "tanto_last_name": "通常価格",
    "tanto_first_name": "さとし",
    "tanto_last_name_kana": "ツウジョウ",
    "tanto_first_name_kana": "サトシ",
    "zip": "111-1111",
    "pref": "東京都",
    "address1": "○○区△町",
    "address2": "3-24",
    "address3": "〇〇ビル",
    "email": "guest@dai.co.jp",
    "is_invalid_email": 0,
    "email_cc": "",
    "tel": "222-222-3333",
    "mobile_phone": "090-555-5555",
    "fax": "222-222-3333",
    "url": "http://dai.co.jp/",
    "foundation": "2000-4",
    "sales": 10000,
    "job": "雑貨店、ネットショップ",
    "memo": "「有限会社サンプル」様\r\nEメール：guest@dai.co.jp\r\nパスワード：guest\r\n\r\n※ここには会員に関するメモ（管理画面のみで表示）が保存できます。",
    "payment": "銀行振込,代金引換",
    "special_shipping_cost": null,
    "special_shipping_service_price": "配送グループ",
    "paid": "申請済",
    "special_view": 0,
    "mm_flag": 1,
    "point": 2600,
    "price_group_id": null,
    "view_group_id": null,
    "customs": [
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
    "salesman_id": null,
    "af_id": null,
    "credit_limit": 100,
    "cutoff_date": null,
    "payment_month": null,
    "payment_date": null,
    "default_other_shipping_id": null,
    "default_payment": null,
    "hidden_price": 0,
    "status": null,
    "email_verified_at": "2025-11-21 10:21:30",
    "tsa_is_used": 0,
    "created_at": "2012-04-26 18:53:05",
    "updated_at": "2022-01-26 15:31:26"
  }
}
```

## PATCH {{api_url}}/api/v1/customers/

**リクエストBODY**

| KEY | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| customers\[{{i}}\]\[id\] | 会員ID | 整数 | 11 | 必須 |
| customers\[{{i}}\]\[ext_id\] | 貴社独自会員ID | 文字列 | 255 | Bカート管理画面のオプション設定で「貴社独自会員IDでログイン」の項目を「有効」にしている場合は項目存在時必須。「無効」の場合は任意。 |
| customers\[{{i}}\]\[agent_id\] | 代理店ID | 文字列 | 255 |  |
| customers\[{{i}}\]\[agent_rate\] | 代理店レート | 数値 | 11 |  |
| customers\[{{i}}\]\[parent_id\] | 親代理店ID | 文字列 | 255 |  |
| customers\[{{i}}\]\[destination_code\] | 配送コード | 文字列 | 255 |  |
| customers\[{{i}}\]\[comp_name\] | 会社名 | 文字列 | 255 |  |
| customers\[{{i}}\]\[comp_name_kana\] | 会社名カナ | 文字列 | 255 |  |
| customers\[{{i}}\]\[ceo_last_name\] | 代表者姓 | 文字列 | 50 |  |
| customers\[{{i}}\]\[ceo_first_name\] | 代表者名 | 文字列 | 50 |  |
| customers\[{{i}}\]\[ceo_last_name_kana\] | 代表者姓カナ | 文字列 | 50 |  |
| customers\[{{i}}\]\[ceo_first_name_kana\] | 代表者名カナ | 文字列 | 50 |  |
| customers\[{{i}}\]\[department\] | 部署 | 文字列 | 255 |  |
| customers\[{{i}}\]\[tanto_last_name\] | 担当者姓 | 文字列 | 50 | 項目存在時必須 |
| customers\[{{i}}\]\[tanto_first_name\] | 担当者名 | 文字列 | 50 |  |
| customers\[{{i}}\]\[tanto_last_name_kana\] | 担当者姓カナ | 文字列 | 50 |  |
| customers\[{{i}}\]\[tanto_first_name_kana\] | 担当者名カナ | 文字列 | 50 |  |
| customers\[{{i}}\]\[zip\] | 郵便番号 | 文字列 | 64 | 項目存在時必須  <br>000-0000 |
| customers\[{{i}}\]\[pref\] | 都道府県 | 文字列 | 32 | 項目存在時必須 |
| customers\[{{i}}\]\[address1\] | 市区町村 | 文字列 | 255 | 項目存在時必須 |
| customers\[{{i}}\]\[address2\] | 町域・番地 | 文字列 | 255 | 項目存在時必須 |
| customers\[{{i}}\]\[address3\] | ビル・建物名 | 文字列 | 255 |  |
| customers\[{{i}}\]\[email\] | メールアドレス | 文字列 | 255 | Bカート管理画面のオプション設定で「空のメールアドレスを許可」にチェックがある場合は任意。ない場合は項目存在時必須。  <br>メールアドレスの形式  <br>※1 |
| customers\[{{i}}\]\[is_invalid_email\] | メールアドレス無効 | 整数 | 1 | 無効：1  <br>有効：0 |
| customers\[{{i}}\]\[email_cc\] | メールアドレスCC | 文字列 | 255 | メールアドレスをカンマ区切りで指定 |
| customers\[{{i}}\]\[tel\] | 電話番号 | 文字列 | 255 |  |
| customers\[{{i}}\]\[mobile_phone\] | 携帯番号 | 文字列 | 255 |  |
| customers\[{{i}}\]\[fax\] | FAX番号 | 文字列 | 255 |  |
| customers\[{{i}}\]\[url\] | URL | 文字列 | 255 |  |
| customers\[{{i}}\]\[foundation\] | 設立年月 | 文字列 | 50 |  |
| customers\[{{i}}\]\[sales\] | 年商 | 整数 | 255 |  |
| customers\[{{i}}\]\[job\] | 業態/業種 | 文字列 | 255 |  |
| customers\[{{i}}\]\[memo\] | 管理者用メモ | 文字列 | 255 |  |
| customers\[{{i}}\]\[payment\] | 決済方法 | 文字列 | 255 |  |
| customers\[{{i}}\]\[special_shipping_cost\] | 特別送料 | 整数 | 255 | 無効：空文字列  <br>特別送料：半角整数  <br>別見積もり：NULL |
| customers\[{{i}}\]\[special_shipping_service_price\] | 特別送料無料設定 | 整数 | 255 | 無効：空文字列  <br>配送グループ：'配送グループ'  <br>会員別：半角整数 |
| customers\[{{i}}\]\[mm_flag\] | メルマガフラグ | 整数 | 1 |  |
| customers\[{{i}}\]\[point\] | ポイント | 整数 | 255 |  |
| customers\[{{i}}\]\[price_group_id\] | 価格グループID | 整数 | 255 |  |
| customers\[{{i}}\]\[view_group_id\] | 表示グループID | 整数 | 255 |  |
| customers\[{{i}}\]\[customs\]\[{field_id, value}\] | カスタム項目 | 配列 | 65,535 |  |
| customers\[{{i}}\]\[salesman_id\] | 営業担当者 | 文字列 | 255 | 管理者IDをカンマ区切りで指定 |
| customers\[{{i}}\]\[af_id\] | 参照元ID | 文字列 | 255 |  |
| customers\[{{i}}\]\[credit_limit\] | 月毎の注文限度額 | 整数 | 11 |  |
| customers\[{{i}}\]\[cutoff_date\] | 締め日 | 文字列 | 2 |  |
| customers\[{{i}}\]\[payment_month\] | 支払い日（月） | 文字列 | 255 |  |
| customers\[{{i}}\]\[payment_date\] | 支払い日（日） | 文字列 | 2 |  |
| customers\[{{i}}\]\[default_other_shipping_id\] | いつもの配送先 | 整数 | 10 |  |
| customers\[{{i}}\]\[default_payment\] | いつもの決済方法 | 文字列 | 255 |  |
| customers\[{{i}}\]\[hidden_price\] | 価格表示設定 | 整数 | 4 |  |
| customers\[{{i}}\]\[tsa_is_used\] | 二段階認証 | 整数 | 1 | 有効：1  <br>無効：0  <br>※メールアドレスが未認証の場合、二段階認証を有効にできません |
| customers\[{{i}}\]\[password\] | パスワード | 文字列 | 255 | 項目存在時必須  <br>パスワードは暗号化され取得不可 |
| customers\[{{i}}\]\[status\] | 会員認証 | 文字列 | 3 | 未承認/無効、承認の場合は空文字列 |
| customers\[{{i}}\]\[created_at\] | 登録日 | 日付 | 19 | Y-m-d |
| customers\[{{i}}\]\[updated_at\] | 更新日 | 日付 | 19 | Y-m-d |

※ {{i}}は配列のキー

※1 email_verified_at≠null（メールアドレス認証済み）のレコードのメールアドレスを変更した場合、リクエスト内容に関わらず、自動的にemail_verified_at=null、tsa_is_used=0が設定されます。

**リクエストボディ例:**

```json
{
  "customers": [
    {
      "id": 1,
      "agent_id": "",
      "agent_rate": "",
      "parent_id": "",
      "destination_code": "1",
      "comp_name": "Dai",
      "department": "営業",
      "tanto_last_name": "山田",
      "tanto_first_name": "太郎",
      "tanto_last_name_kana": "ヤマダ",
      "tanto_first_name_kana": "タロウ"
    },
    {
      "id": 10028,
      "tanto_last_name": "中田",
      "tanto_last_name_kana": "ナカタ"
    }
  ]
}
```

**レスポンス例（200 OK）:**

```json
{
  "customers": [
    {
      "id": 1,
      "ext_id": "B15487safsdfsa",
      "agent_id": null,
      "agent_rate": null,
      "parent_id": null,
      "destination_code": "1",
      "comp_name": "Dai",
      "comp_name_kana": "カブシキガイシャサンプル",
      "ceo_last_name": "山田",
      "ceo_first_name": "一郎",
      "ceo_last_name_kana": "ヤマダ",
      "ceo_first_name_kana": "イチロウ",
      "department": "営業",
      "tanto_last_name": "山田",
      "tanto_first_name": "太郎",
      "tanto_last_name_kana": "ヤマダ",
      "tanto_first_name_kana": "タロウ",
      "zip": "111-1111",
      "pref": "東京都",
      "address1": "○○区△町",
      "address2": "3-24",
      "address3": "〇〇ビル",
      "email": "guest@dai.co.jp",
      "is_invalid_email": 0,
      "email_cc": "",
      "tel": "222-222-3333",
      "mobile_phone": "090-555-5555",
      "fax": "222-222-3333",
      "url": "http://dai.co.jp/",
      "foundation": "2000-4",
      "sales": 10000,
      "job": "雑貨店、ネットショップ",
      "memo": "「有限会社サンプル」様\r\nEメール：guest@dai.co.jp\r\nパスワード：guest\r\n\r\n※ここには会員に関するメモ（管理画面のみで表示）が保存できます。",
      "payment": "銀行振込,代金引換",
      "special_shipping_cost": null,
      "special_shipping_service_price": "配送グループ",
      "paid": "申請済",
      "special_view": 0,
      "mm_flag": 1,
      "point": 2600,
      "price_group_id": null,
      "view_group_id": null,
      "customs": [
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
      "salesman_id": null,
      "af_id": null,
      "credit_limit": 100,
      "cutoff_date": null,
      "payment_month": null,
      "payment_date": null,
      "default_other_shipping_id": null,
      "default_payment": null,
      "hidden_price": 0,
      "email_verified_at": null,
      "tsa_is_used": 0,
      "status": null,
      "created_at": "2012-04-26 18:53:05",
      "updated_at": "2022-10-28 18:23:56"
    },
    {
      "id": 10028,
      "ext_id": "X999",
      "agent_id": null,
      "agent_rate": null,
      "parent_id": null,
      "destination_code": null,
      "comp_name": "大竹家具株式会社",
      "comp_name_kana": "オオタケカグカブシキガイシャ",
      "ceo_last_name": "田中",
      "ceo_first_name": "圭一",
      "ceo_last_name_kana": "タナカ",
      "ceo_first_name_kana": "ケイイチ",
      "department": "仕入れ課",
      "tanto_last_name": "中田",
      "tanto_first_name": "宗二",
      "tanto_last_name_kana": "ナカタ",
      "tanto_first_name_kana": "ソウジ",
      "zip": "150-0013",
      "pref": "東京都",
      "address1": "渋谷区恵比寿",
      "address2": "3-24",
      "address3": "",
      "email": "guest+6@dai.co.jp",
      "email_cc": "",
      "tel": "03-1111-1111",
      "mobile_phone": "",
      "fax": "",
      "url": "http://admintest.com",
      "foundation": "1999-1",
      "sales": 2000,
      "job": "家具",
      "memo": "",
      "payment": "銀行振込,代金引換,自社掛払い",
      "special_shipping_cost": null,
      "special_shipping_service_price": "配送グループ",
      "paid": "申請済",
      "special_view": 0,
      "mm_flag": 0,
      "point": 0,
      "price_group_id": null,
      "view_group_id": null,
      "customs": [
        {
          "field_id": 11,
          "value": "三井住友銀行"
        },
        {
          "field_id": 12,
          "value": "カスタムオプション1"
        }
      ],
      "salesman_id": null,
      "af_id": null,
      "credit_limit": null,
      "cutoff_date": null,
      "payment_month": null,
      "payment_date": null,
      "default_other_shipping_id": null,
      "default_payment": null,
      "hidden_price": 0,
      "status": null,
      "email_verified_at": "2025-11-21 10:21:30",
      "tsa_is_used": 1,
      "created_at": "2012-07-23 19:20:13",
      "updated_at": "2022-10-28 18:23:56"
    }
  ]
}
```

## POST {{api_url}}/api/v1/customers/

**リクエストBODY**

| KEY | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| customers\[{{i}}\]\[ext_id\] | 貴社独自会員ID | 文字列 | 255 |  |
| customers\[{{i}}\]\[agent_id\] | 代理店ID | 文字列 | 255 |  |
| customers\[{{i}}\]\[agent_rate\] | 代理店レート | 数値 | 11 |  |
| customers\[{{i}}\]\[parent_id\] | 親代理店ID | 文字列 | 255 |  |
| customers\[{{i}}\]\[destination_code\] | 配送コード | 文字列 | 255 |  |
| customers\[{{i}}\]\[comp_name\] | 会社名 | 文字列 | 255 |  |
| customers\[{{i}}\]\[comp_name_kana\] | 会社名カナ | 文字列 | 255 |  |
| customers\[{{i}}\]\[ceo_last_name\] | 代表者姓 | 文字列 | 50 |  |
| customers\[{{i}}\]\[ceo_first_name\] | 代表者名 | 文字列 | 50 |  |
| customers\[{{i}}\]\[ceo_last_name_kana\] | 代表者姓カナ | 文字列 | 50 |  |
| customers\[{{i}}\]\[ceo_first_name_kana\] | 代表者名カナ | 文字列 | 50 |  |
| customers\[{{i}}\]\[department\] | 部署 | 文字列 | 255 |  |
| customers\[{{i}}\]\[tanto_last_name\] | 担当者姓 | 文字列 | 50 | 必須 |
| customers\[{{i}}\]\[tanto_first_name\] | 担当者名 | 文字列 | 50 |  |
| customers\[{{i}}\]\[tanto_last_name_kana\] | 担当者姓カナ | 文字列 | 50 |  |
| customers\[{{i}}\]\[tanto_first_name_kana\] | 担当者名カナ | 文字列 | 50 |  |
| customers\[{{i}}\]\[zip\] | 郵便番号 | 文字列 | 64 | 必須  <br>000-0000 |
| customers\[{{i}}\]\[pref\] | 都道府県 | 文字列 | 32 | 必須 |
| customers\[{{i}}\]\[address1\] | 市区町村 | 文字列 | 255 | 必須 |
| customers\[{{i}}\]\[address2\] | 町域・番地 | 文字列 | 255 | 必須 |
| customers\[{{i}}\]\[address3\] | ビル・建物名 | 文字列 | 255 |  |
| customers\[{{i}}\]\[email\] | メールアドレス | 文字列 | 255 | Bカート管理画面のオプション設定で「空のメールアドレスを許可」にチェックがある場合は任意。ない場合は必須。  <br>メールアドレスの形式 |
| customers\[{{i}}\]\[is_invalid_email\] | メールアドレス無効 | 整数 | 1 | 無効：1  <br>有効：0 |
| customers\[{{i}}\]\[email_cc\] | メールアドレスCC | 文字列 | 255 | メールアドレスをカンマ区切りで指定 |
| customers\[{{i}}\]\[tel\] | 電話番号 | 文字列 | 255 |  |
| customers\[{{i}}\]\[mobile_phone\] | 携帯番号 | 文字列 | 255 |  |
| customers\[{{i}}\]\[fax\] | FAX番号 | 文字列 | 255 |  |
| customers\[{{i}}\]\[url\] | URL | 文字列 | 255 |  |
| customers\[{{i}}\]\[foundation\] | 設立年月 | 文字列 | 50 |  |
| customers\[{{i}}\]\[sales\] | 年商 | 整数 | 255 |  |
| customers\[{{i}}\]\[job\] | 業態/業種 | 文字列 | 255 |  |
| customers\[{{i}}\]\[memo\] | 管理者用メモ | 文字列 | 255 |  |
| customers\[{{i}}\]\[payment\] | 決済方法 | 文字列 | 255 |  |
| customers\[{{i}}\]\[special_shipping_cost\] | 特別送料 | 整数 | 255 | 無効：空文字列  <br>特別送料：半角整数  <br>別見積もり：NULL |
| customers\[{{i}}\]\[special_shipping_service_price\] | 特別送料無料設定 | 整数 | 255 | 無効：空文字列  <br>配送グループ：'配送グループ'  <br>会員別：半角整数 |
| customers\[{{i}}\]\[mm_flag\] | メルマガフラグ | 整数 | 1 |  |
| customers\[{{i}}\]\[point\] | ポイント | 整数 | 255 |  |
| customers\[{{i}}\]\[price_group_id\] | 価格グループID | 整数 | 255 |  |
| customers\[{{i}}\]\[view_group_id\] | 表示グループID | 整数 | 255 |  |
| customers\[{{i}}\]\[customs\]\[{field_id, value}\] | カスタム項目 | 配列 | 65,535 |  |
| customers\[{{i}}\]\[salesman_id\] | 営業担当者 | 文字列 | 255 | 管理者IDをカンマ区切りで指定 |
| customers\[{{i}}\]\[af_id\] | 参照元ID | 文字列 | 255 |  |
| customers\[{{i}}\]\[credit_limit\] | 月毎の注文限度額 | 整数 | 11 |  |
| customers\[{{i}}\]\[cutoff_date\] | 締め日 | 文字列 | 2 |  |
| customers\[{{i}}\]\[payment_month\] | 支払い日（月） | 文字列 | 255 |  |
| customers\[{{i}}\]\[payment_date\] | 支払い日（日） | 文字列 | 2 |  |
| customers\[{{i}}\]\[default_other_shipping_id\] | いつもの配送先 | 整数 | 10 |  |
| customers\[{{i}}\]\[default_payment\] | いつもの決済方法 | 文字列 | 255 |  |
| customers\[{{i}}\]\[hidden_price\] | 価格表示設定 | 整数 | 4 |  |
| customers\[{{i}}\]\[password\] | パスワード | 文字列 | 255 | 必須  <br>パスワードは暗号化され取得不可 |
| customers\[{{i}}\]\[status\] | 会員認証 | 文字列 | 3 | 未承認/無効、承認の場合は空文字列 |
| customers\[{{i}}\]\[created_at\] | 登録日 | 日付 | 19 | Y-m-d |
| customers\[{{i}}\]\[updated_at\] | 更新日 | 日付 | 19 | Y-m-d |

※ {{i}}は配列のキー

**リクエストボディ例:**

```json
{
  "customers": [
    {
      "ext_id": "",
      "agent_id": "",
      "agent_rate": "",
      "parent_id": "",
      "destination_code": "1",
      "comp_name": "Dai",
      "zip": "600-0000",
      "pref": "京都府",
      "address1": "京都市下京区",
      "address2": "二帖半敷町",
      "email": "tester+create@dai.co.jp",
      "tel": "075-000-0000",
      "department": "営業",
      "tanto_last_name": "山田",
      "tanto_first_name": "太郎",
      "tanto_last_name_kana": "ヤマダ",
      "tanto_first_name_kana": "タロウ",
      "payment": "銀行振込",
      "customs": [
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
      "password": "test1234!ABC"
    },
    {
      "ext_id": "",
      "agent_id": "",
      "agent_rate": "",
      "parent_id": "",
      "destination_code": "2",
      "comp_name": "Dai",
      "department": "営業",
      "tanto_last_name": "山田",
      "tanto_first_name": "太郎",
      "tanto_last_name_kana": "ヤマダ",
      "tanto_first_name_kana": "タロウ",
      "zip": "600-0001",
      "pref": "京都府",
      "address1": "京都市下京区",
      "address2": "悪王子町",
      "email": "tester+create2@dai.co.jp",
      "tel": "075-000-0000",
      "credit_limit": null,
      "password": "test1234!ABC"
    }
  ]
}
```

**レスポンス例（201 Created）:**

```json
{
  "customers": [
    {
      "id": 10041,
      "ext_id": null,
      "agent_id": null,
      "agent_rate": null,
      "parent_id": null,
      "destination_code": "1",
      "comp_name": "Dai",
      "comp_name_kana": "",
      "ceo_last_name": "",
      "ceo_first_name": "",
      "ceo_last_name_kana": "",
      "ceo_first_name_kana": "",
      "department": "営業",
      "tanto_last_name": "山田",
      "tanto_first_name": "太郎",
      "tanto_last_name_kana": "ヤマダ",
      "tanto_first_name_kana": "タロウ",
      "zip": "600-0000",
      "pref": "京都府",
      "address1": "京都市下京区",
      "address2": "二帖半敷町",
      "address3": "",
      "email": "tester+create@dai.co.jp",
      "is_invalid_email": 0,
      "email_cc": "",
      "tel": "075-000-0000",
      "mobile_phone": "",
      "fax": "",
      "url": "",
      "foundation": null,
      "sales": 0,
      "job": "",
      "memo": "",
      "payment": "銀行振込",
      "special_shipping_cost": null,
      "special_shipping_service_price": "配送グループ",
      "paid": null,
      "special_view": 0,
      "mm_flag": 1,
      "point": 0,
      "price_group_id": null,
      "view_group_id": null,
      "customs": [
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
      "salesman_id": null,
      "af_id": null,
      "credit_limit": null,
      "cutoff_date": null,
      "payment_month": null,
      "payment_date": null,
      "default_other_shipping_id": null,
      "default_payment": null,
      "hidden_price": 0,
      "email_verified_at": null,
      "tsa_is_used": 0,
      "status": null,
      "created_at": "2022-01-26 15:33:38",
      "updated_at": "2022-01-26 15:33:38"
    },
    {
      "id": 10042,
      "ext_id": null,
      "agent_id": null,
      "agent_rate": null,
      "parent_id": null,
      "destination_code": "2",
      "comp_name": "Dai",
      "comp_name_kana": "",
      "ceo_last_name": "",
      "ceo_first_name": "",
      "ceo_last_name_kana": "",
      "ceo_first_name_kana": "",
      "department": "営業",
      "tanto_last_name": "山田",
      "tanto_first_name": "太郎",
      "tanto_last_name_kana": "ヤマダ",
      "tanto_first_name_kana": "タロウ",
      "zip": "600-0001",
      "pref": "京都府",
      "address1": "京都市下京区",
      "address2": "悪王子町",
      "address3": "",
      "email": "tester+create2@dai.co.jp",
      "email_cc": "",
      "tel": "075-000-0000",
      "mobile_phone": "",
      "fax": "",
      "url": "",
      "foundation": null,
      "sales": 0,
      "job": "",
      "memo": "",
      "payment": null,
      "special_shipping_cost": null,
      "special_shipping_service_price": "配送グループ",
      "paid": null,
      "special_view": 0,
      "mm_flag": 1,
      "point": 0,
      "price_group_id": null,
      "view_group_id": null,
      "customs": null,
      "salesman_id": null,
      "af_id": null,
      "credit_limit": null,
      "cutoff_date": null,
      "payment_month": null,
      "payment_date": null,
      "default_other_shipping_id": null,
      "default_payment": null,
      "hidden_price": 0,
      "email_verified_at": null,
      "tsa_is_used": 0,
      "status": null,
      "created_at": "2022-01-26 15:33:38",
      "updated_at": "2022-01-26 15:33:38"
    }
  ]
}
```
