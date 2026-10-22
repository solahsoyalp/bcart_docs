# 商品基本

商品の基本情報（商品名やカテゴリなど）

## GET {{api_url}}/api/v1/products/1

**レスポンス一覧**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| id | 商品ID | 整数 | 11 |  |
| main_no | 商品管理番号 | 文字列 | 255 |  |
| name | 商品名 | 文字列 | 255 |  |
| catch_copy | キャッチコピー | 文字列 | 65,535 |  |
| category_id | カテゴリID | 整数 | 11 |  |
| sub_category_id | サブカテゴリID | 文字列 | 255 | サブカテゴリをカンマ区切り |
| feature_id1 | 特集ID1 | 整数 | 11 |  |
| feature_id2 | 特集ID2 | 整数 | 11 |  |
| feature_id3 | 特集ID3 | 整数 | 11 |  |
| made_in | 生産地 | 文字列 | 255 |  |
| size | サイズ | 文字列 | 65,535 |  |
| sozai | 素材 | 文字列 | 65,535 |  |
| caution | 注意事項 | 文字列 | 65,535 |  |
| tag | 商品特徴 | 文字列 | 21 | new/recommend/limitedなど |
| description | 説明 | 文字列 | 65,535 |  |
| meta_title | META情報タイトル | 文字列 | 255 |  |
| meta_keywords | META情報キーワード | 文字列 | 255 |  |
| meta_description | META情報説明 | 文字列 | 255 |  |
| image | 商品画像パス | 文字列 | 255 |  |
| view_group_filter | 商品非表示グループ | 文字列 | 255 | 表示グループIDをカンマ区切り |
| visible_customer_id | 例外的に表示させる会員ID | 文字列 | 65,535 | 会員IDをカンマ区切り |
| hide_customer_id | 商品を非表示とする会員ID | 文字列 | 65,535 | 会員IDをカンマ区切り |
| prepend_text | 上部フリースペース（PC表示） | 文字列 | 65,535 |  |
| append_text | 下部フリースペース（PC表示） | 文字列 | 65,535 |  |
| middle_text | 中部フリースペース（PC表示） | 文字列 | 65,535 |  |
| rv_prepend_text | 上部フリースペース（レスポンシブ表示） | 文字列 | 65,535 |  |
| rv_append_text | 下部フリースペース（レスポンシブ表示） | 文字列 | 65,535 |  |
| rv_middle_text | 中部フリースペース（レスポンシブ表示） | 文字列 | 65,535 |  |
| file_download | ダウンロードファイルパス | 文字列 | 255 |  |
| customs | カスタム項目 | 配列 |  |  |
| hanbai_start | 販売期間開始 | 日付 | 19 | Y-m-d H:i:s |
| hanbai_end | 販売期間終了 | 日付 | 19 | Y-m-d H:i:s |
| recommend_product_id | レコメンドで表示させる商品ID | 文字列 | 65,535 | 商品IDをカンマ区切り |
| view_pattern | 商品一覧表示パターン | 整数 | 1 | 0〜5。標準は0 |
| priority | 表示順 | 数値 | 11 | \-32,768 ～ 32,767 |
| flag | 状態 | 文字列 | 3 | ‘表示’,’非表示’ |
| updated_at | 更新日 | 日付 | 19 | Y-m-d H:i:s |
| sub_images | サブ画像 | 配列 |  | image=画像パス、caption=キャプション |

**レスポンス例（200 OK）:**

```json
{
  "product": {
    "id": 1,
    "main_no": "XXX-1008",
    "name": "イームズ風クラシックソファー2人掛け",
    "catch_copy": "",
    "category_id": 10,
    "sub_category_id": null,
    "feature_id1": null,
    "feature_id2": null,
    "feature_id3": null,
    "made_in": "スウェーデン",
    "size": "100:10:100",
    "sozai": "プラスチック",
    "caution": "少し昔の型になります。インテリアとしてお使いいただけます。",
    "tag": "recommend",
    "description": "ここには任意の商品説明が入力できます。\nここには任意の商品説明が入力できます。\n\nここには任意の商品説明が入力できます。\nここには任意の商品説明が入力できます。\n\n<table><tr><th>表項目</th><td>表内容</td></tr><tr><th>表項目</th><td>表内容</td></tr></table>\n<strong style=\"color: #f00; font-size: 16px;\">HTMLも挿入できます。</strong>\n<P>\n<font size=\"5\">【デモ用テキスト】</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n</P>",
    "meta_title": "",
    "meta_keywords": "",
    "meta_description": "",
    "image": "/demo/products/3.jpg",
    "view_group_filter": "非会員",
    "visible_customer_id": null,
    "hide_customer_id": "10010",
    "prepend_text": "",
    "append_text": "",
    "middle_text": "",
    "rv_prepend_text": "",
    "rv_append_text": "",
    "rv_middle_text": "",
    "file_download": null,
    "customs": [
      {
        "field_id": 14,
        "value": "基本カスタム1"
      },
      {
        "field_id": 16,
        "value": "基本カスタム3"
      },
      {
        "field_id": 20,
        "value": "基本カスタム4"
      }
    ],
    "hanbai_start": null,
    "hanbai_end": null,
    "recommend_product_id": null,
    "view_pattern": 0,
    "priority": 0,
    "flag": "非表示",
    "updated_at": "2022-01-26 14:15:44",
    "sub_images": {
      "1": {
        "image": "",
        "caption": ""
      },
      "2": {
        "image": "/demo/products/3.jpg",
        "caption": ""
      }
    }
  }
}
```

## GET {{api_url}}/api/v1/products

**URIパラメータ**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| limit | limit | 整数 |  | 指定した件数分のデータを取得します。指定なしの場合は20件、最大100件 |
| offset | offset | 整数 |  | 指定した値+1件目のデータからlimit分を取得します。指定しない場合は0 |
| ids | ID複数 | 整数 |  | 複数の商品IDをカンマ区切りで指定 |
| fields | フィールド | 文字列 |  | 取得したいフィールドをカンマ区切りで指定 |
| category_id | カテゴリID | 整数 | 11 |  |
| sub_category_id | サブカテゴリID | 整数 | 255 |  |
| name | 商品名 | 文字列 | 255 |  |
| main_no | 商品管理番号 | 文字列 | 255 |  |
| feature_id1 | 特集ID1 | 整数 | 11 |  |
| feature_id2 | 特集ID2 | 整数 | 11 |  |
| feature_id3 | 特集ID3 | 整数 | 11 |  |
| tag | 商品特徴 | 文字列 | 21 | 識別文字列 new/recommend/limitedなど |
| customs | カスタム項目 | 配列 |  | 配列のキーにfield_id、値にvalue。例) customs\[14\]=検索する値 |
| hanbai_start | 販売期間開始 | 日付 | 19 | Y-m-d |
| hanbai_start_min | 販売期間開始〜 | 日付 | 19 | Y-m-d　指定日以降 |
| hanbai_start_max | 〜販売期間開始 | 日付 | 19 | Y-m-d　指定日以前 |
| hanbai_end | 販売期間終了 | 日付 | 19 | Y-m-d |
| hanbai_end_min | 販売期間開始〜 | 日付 | 19 | Y-m-d　指定日以降 |
| hanbai_end_max | 〜販売期間終了 | 日付 | 19 | Y-m-d　指定日以前 |
| updated_at | 更新日 | 日付 | 19 | Y-m-d |
| updated_at_min | 更新日〜 | 日付 | 19 | Y-m-d H:i:s　指定日時以降 |
| updated_at_max | 〜更新日 | 日付 | 19 | Y-m-d H:i:s　指定日時以前 |

## 拡張パラメータによる高度な絞り込み

拡張パラメータを使用することで、より高度な絞り込みが可能です。

詳しくは、[パラメータ](../docs/04-parameters.md)の「拡張パラメータ」欄をご参照ください。

**レスポンス例（200 OK）:**

```json
{
  "products": [
    {
      "id": 1,
      "main_no": "XXX-1008",
      "name": "イームズ風クラシックソファー2人掛け",
      "catch_copy": "",
      "category_id": 10,
      "sub_category_id": null,
      "feature_id1": null,
      "feature_id2": null,
      "feature_id3": null,
      "made_in": "スウェーデン",
      "size": "100:10:100",
      "sozai": "プラスチック",
      "caution": "少し昔の型になります。インテリアとしてお使いいただけます。",
      "tag": "recommend",
      "description": "ここには任意の商品説明が入力できます。\nここには任意の商品説明が入力できます。\n\nここには任意の商品説明が入力できます。\nここには任意の商品説明が入力できます。\n\n<table><tr><th>表項目</th><td>表内容</td></tr><tr><th>表項目</th><td>表内容</td></tr></table>\n<strong style=\"color: #f00; font-size: 16px;\">HTMLも挿入できます。</strong>\n<P>\n<font size=\"5\">【デモ用テキスト】</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n</P>",
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "image": "/demo/products/3.jpg",
      "view_group_filter": "非会員",
      "visible_customer_id": null,
      "hide_customer_id": "10010,10012",
      "prepend_text": "",
      "append_text": "",
      "middle_text": "",
      "rv_prepend_text": "",
      "rv_append_text": "",
      "rv_middle_text": "",
      "file_download": null,
      "customs": [
        {
          "field_id": 14,
          "value": "基本カスタム1"
        },
        {
          "field_id": 16,
          "value": "基本カスタム3"
        },
        {
          "field_id": 20,
          "value": "基本カスタム4"
        }
      ],
      "hanbai_start": null,
      "hanbai_end": null,
      "recommend_product_id": null,
      "view_pattern": 0,
      "priority": 0,
      "flag": "非表示",
      "updated_at": "2022-01-26 14:15:44",
      "sub_images": {
        "1": {
          "image": "",
          "caption": ""
        },
        "2": {
          "image": "/demo/products/3.jpg",
          "caption": ""
        }
      }
    },
    {
      "id": 2,
      "main_no": "C0001",
      "name": "アタッシュケース",
      "catch_copy": "ここにはキャッチコピーがはいります。",
      "category_id": 22,
      "sub_category_id": "47",
      "feature_id1": null,
      "feature_id2": null,
      "feature_id3": null,
      "made_in": "itary",
      "size": "L:600mm・300mm・200mm\r\nM:400mm・200mm・100mm\r\nS:200mm・100mm・50mm",
      "sozai": "アルミ製",
      "caution": "Sサイズはあまり容量が大きくありません。",
      "tag": null,
      "description": "ここには商品説明が入ります。\r\n\r\nHTMLも挿入できます。ここには商品説明が入ります。HTMLも挿入できます。ここには商品説明が入ります。HTMLも挿入できます。ここには商品説明が入ります。HTMLも挿入できます。ここには商品説明が入ります。\r\nHTMLも挿入できます。ここには商品説明が入ります。HTMLも挿入できます。ここには商品説明が入ります。HTMLも挿入できます。ここには商品説明が入ります。HTMLも挿入できます。\r\n<P>\r\n<font size=\"5\">【デモ用テキスト】</font><br>\r\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\r\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\r\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\r\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\r\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\r\n</P>",
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "image": "/demo/products/17.jpg",
      "view_group_filter": "通常会員,1",
      "visible_customer_id": null,
      "hide_customer_id": "10010,10012",
      "prepend_text": "",
      "append_text": "",
      "middle_text": "",
      "rv_prepend_text": "",
      "rv_append_text": "",
      "rv_middle_text": "",
      "file_download": null,
      "customs": [
        {
          "field_id": 14,
          "value": "【カスタム項目1】自由項目を作れます（生産者と設定中）"
        },
        {
          "field_id": 15,
          "value": "【カスタム項目2】自由項目を作れます（ブランドと設定中）"
        },
        {
          "field_id": 16,
          "value": "【カスタム項目3】自由項目を作れます（カタログ頁と設定中）"
        }
      ],
      "hanbai_start": null,
      "hanbai_end": null,
      "recommend_product_id": null,
      "view_pattern": 0,
      "priority": 0,
      "flag": "表示",
      "updated_at": "2011-11-17 18:48:00",
      "sub_images": {
        "1": {
          "image": "/demo/sub_products/17_56.jpg",
          "caption": ""
        },
        "2": {
          "image": "/demo/products/17.jpg",
          "caption": ""
        },
        "3": {
          "image": "/demo/products/17.jpg",
          "caption": ""
        },
        "4": {
          "image": "/demo/products/17.jpg",
          "caption": ""
        },
        "5": {
          "image": "/demo/products/17.jpg",
          "caption": ""
        },
        "6": {
          "image": "/demo/products/17.jpg",
          "caption": ""
        }
      }
    },
    {
      "id": 3,
      "main_no": "B0001",
      "name": "【組合せ販売・登録例】絵の具",
      "catch_copy": "人気の三色詰め合わせ！",
      "category_id": 22,
      "sub_category_id": "47,50",
      "feature_id1": null,
      "feature_id2": null,
      "feature_id3": null,
      "made_in": "サンプルテキストです。",
      "size": "100ｍｍ：20ｍｍ：10ｍｍ",
      "sozai": "サンプルテキストです。",
      "caution": "サンプルテキストです。",
      "tag": null,
      "description": "サンプルテキストです。サンプルテキストです。サンプルテキストです。サンプルテキストです。サンプルテキストです。サンプルテキストです。サンプルテキストです。サンプルテキストです。サンプルテキストです。\r\n\r\nHTMLも入力できます。HTMLも入力できます。HTMLも入力できます。\r\nHTMLも入力できます。HTMLも入力できます。HTMLも入力できます。\r\n<P>\r\n<font size=\"5\">【デモ用テキスト】</font><br>\r\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\r\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\r\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\r\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\r\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\r\n</P>",
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "image": "/demo/products/19.jpg",
      "view_group_filter": "1",
      "visible_customer_id": null,
      "hide_customer_id": null,
      "prepend_text": "",
      "append_text": "",
      "middle_text": "",
      "rv_prepend_text": "",
      "rv_append_text": "",
      "rv_middle_text": "",
      "file_download": null,
      "customs": [
        {
          "field_id": 14,
          "value": "【カスタム項目1】自由項目を作れます（生産者と設定中）"
        },
        {
          "field_id": 15,
          "value": "【カスタム項目2】自由項目を作れます（ブランドと設定中）"
        },
        {
          "field_id": 16,
          "value": "【カスタム項目3】自由項目を作れます（カタログ頁と設定中）"
        }
      ],
      "hanbai_start": null,
      "hanbai_end": null,
      "recommend_product_id": null,
      "view_pattern": 0,
      "priority": 0,
      "flag": "表示",
      "updated_at": "2011-11-17 18:48:00",
      "sub_images": {
        "1": {
          "image": "/demo/products/19.jpg",
          "caption": ""
        },
        "2": {
          "image": "/demo/products/19.jpg",
          "caption": ""
        },
        "3": {
          "image": "/demo/products/19.jpg",
          "caption": ""
        },
        "4": {
          "image": "/demo/products/19.jpg",
          "caption": ""
        },
        "5": {
          "image": "/demo/products/19.jpg",
          "caption": ""
        },
        "6": {
          "image": "/demo/products/19.jpg",
          "caption": ""
        }
      }
    },
    {
      "id": 4,
      "main_no": "A00001",
      "name": "【ロット販売・登録例】　　観葉植物",
      "catch_copy": "",
      "category_id": 17,
      "sub_category_id": "47",
      "feature_id1": null,
      "feature_id2": null,
      "feature_id3": null,
      "made_in": "中国",
      "size": "",
      "sozai": "",
      "caution": "",
      "tag": "recommend",
      "description": "<P>\r\n<font size=\"3\">このページに登録してある商品は「<b>セット名：1個販売（在庫数1200個）品番：KB-A1</b>」の在庫数を参照するように登録してあります。</font><br>\r\n<br>\r\n【例1】<br>\r\n商品名：ポット<br>\r\nセット名：10個販売<br>\r\n品番：<b>KB-A10</b><br>\r\n<br>\r\nが売れたら「1個販売（在庫数1200）<b>KB-A1</b>」の在庫数が<b>マイナス10個</b>されます。<br>\r\n<br>\r\n【例2】<br>\r\n商品名：ポット<br>\r\nセット名：50個販売<br>\r\n品番：<b>KB-A50</b><br>\r\n<br>\r\nが売れたら「1個販売（在庫数1200）<b>KB-A1</b>」の在庫数が<b>マイナス50個</b>されます。<br>\r\n</P>",
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "image": "/demo/products/zakka/pot01.jpg",
      "view_group_filter": null,
      "visible_customer_id": null,
      "hide_customer_id": null,
      "prepend_text": "",
      "append_text": "",
      "middle_text": "",
      "rv_prepend_text": "",
      "rv_append_text": "",
      "rv_middle_text": "",
      "file_download": null,
      "customs": [
        {
          "field_id": 14,
          "value": "【カスタム項目1】自由項目を作れます（生産者と設定中）"
        },
        {
          "field_id": 15,
          "value": "【カスタム項目2】自由項目を作れます（ブランドと設定中）"
        },
        {
          "field_id": 16,
          "value": "【カスタム項目3】自由項目を作れます（カタログ頁と設定中）"
        }
      ],
      "hanbai_start": null,
      "hanbai_end": null,
      "recommend_product_id": "9,10,11,12,48",
      "view_pattern": 0,
      "priority": 0,
      "flag": "表示",
      "updated_at": "2016-05-06 13:55:17",
      "sub_images": {
        "1": {
          "image": "/demo/products/zakka/pot01.jpg",
          "caption": ""
        },
        "2": {
          "image": "/demo/products/zakka/pot01.jpg",
          "caption": ""
        },
        "3": {
          "image": "/demo/products/zakka/pot01.jpg",
          "caption": ""
        },
        "4": {
          "image": "/demo/products/zakka/pot01.jpg",
          "caption": ""
        },
        "5": {
          "image": "/demo/products/zakka/pot01.jpg",
          "caption": ""
        },
        "6": {
          "image": "/demo/products/zakka/pot01.jpg",
          "caption": ""
        }
      }
    },
    {
      "id": 5,
      "main_no": "O00001",
      "name": "マジック用トランプ※全ての会員に見えている商品です",
      "catch_copy": "誰でもマジシャン",
      "category_id": 37,
      "sub_category_id": "47,50",
      "feature_id1": 8,
      "feature_id2": null,
      "feature_id3": null,
      "made_in": "台湾",
      "size": "",
      "sozai": "プラスチック",
      "caution": "ネタバレ注意",
      "tag": null,
      "description": "手品専用のトランプと取扱説明者のセットです。\r\n取扱説明書には、15種類の手品のネタが解説してあります。\r\n<P>\r\n<font size=\"5\">【デモ用テキスト】</font><br>\r\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\r\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\r\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\r\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\r\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\r\n</P>",
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "image": "/demo/products/21.jpg",
      "view_group_filter": null,
      "visible_customer_id": null,
      "hide_customer_id": null,
      "prepend_text": "",
      "append_text": "",
      "middle_text": "",
      "rv_prepend_text": "",
      "rv_append_text": "",
      "rv_middle_text": "",
      "file_download": null,
      "customs": [
        {
          "field_id": 14,
          "value": "【カスタム項目1】自由項目を作れます（生産者と設定中）"
        },
        {
          "field_id": 15,
          "value": "【カスタム項目2】自由項目を作れます（ブランドと設定中）"
        },
        {
          "field_id": 16,
          "value": "【カスタム項目3】自由項目を作れます（カタログ頁と設定中）"
        }
      ],
      "hanbai_start": null,
      "hanbai_end": null,
      "recommend_product_id": null,
      "view_pattern": 0,
      "priority": 0,
      "flag": "表示",
      "updated_at": "2011-11-17 18:48:00",
      "sub_images": {
        "1": {
          "image": "/demo/products/21.jpg",
          "caption": ""
        },
        "2": {
          "image": "/demo/products/21.jpg",
          "caption": ""
        },
        "3": {
          "image": "/demo/products/21.jpg",
          "caption": ""
        },
        "4": {
          "image": "/demo/products/21.jpg",
          "caption": ""
        },
        "5": {
          "image": "/demo/products/21.jpg",
          "caption": ""
        },
        "6": {
          "image": "/demo/products/21.jpg",
          "caption": ""
        }
      }
    },
    {
      "id": 6,
      "main_no": "SS0003",
      "name": "蚊取り豚※複数カテゴリの例（この商品にはインテリア・生活雑貨カテゴリでも表示されます）",
      "catch_copy": "なつかしい豚です。",
      "category_id": 22,
      "sub_category_id": "47,50",
      "feature_id1": 5,
      "feature_id2": null,
      "feature_id3": null,
      "made_in": "日本",
      "size": "",
      "sozai": "陶器2",
      "caution": "割れやすいので取扱注意",
      "tag": null,
      "description": "有田焼き窯元「BUTA」の新作\r\n蚊取り線香セット付き\r\n<P>\r\n<font size=\"5\">【デモ用テキスト】</font><br>\r\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\r\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\r\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\r\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\r\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\r\n</P>",
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "image": "/demo/products/24.jpg",
      "view_group_filter": "1",
      "visible_customer_id": null,
      "hide_customer_id": null,
      "prepend_text": "",
      "append_text": "",
      "middle_text": "",
      "rv_prepend_text": "",
      "rv_append_text": "",
      "rv_middle_text": "",
      "file_download": null,
      "customs": [
        {
          "field_id": 14,
          "value": "【カスタム項目1】自由項目を作れます（生産者と設定中）"
        },
        {
          "field_id": 15,
          "value": "【カスタム項目2】自由項目を作れます（ブランドと設定中）"
        },
        {
          "field_id": 16,
          "value": "【カスタム項目3】自由項目を作れます（カタログ頁と設定中）"
        }
      ],
      "hanbai_start": null,
      "hanbai_end": null,
      "recommend_product_id": null,
      "view_pattern": 0,
      "priority": 0,
      "flag": "表示",
      "updated_at": "2011-11-17 18:48:00",
      "sub_images": {
        "1": {
          "image": "/demo/products/event3_6.jpg",
          "caption": "senko"
        },
        "2": {
          "image": "/demo/products/24.jpg",
          "caption": ""
        },
        "3": {
          "image": "/demo/products/24.jpg",
          "caption": ""
        },
        "4": {
          "image": "/demo/products/24.jpg",
          "caption": ""
        },
        "5": {
          "image": "/demo/products/24.jpg",
          "caption": ""
        },
        "6": {
          "image": "/demo/products/24.jpg",
          "caption": ""
        }
      }
    },
    {
      "id": 7,
      "main_no": "SS0002",
      "name": "クリスマスツリー",
      "catch_copy": "",
      "category_id": 12,
      "sub_category_id": null,
      "feature_id1": null,
      "feature_id2": null,
      "feature_id3": null,
      "made_in": "米国",
      "size": "全長140cm",
      "sozai": "プラスチック",
      "caution": "",
      "tag": null,
      "description": "アメリカXXX社製の本格的クリスマスツリー\n100Wのライトと頂上の星の飾りのセットです。\n<P>\n<font size=\"5\">【デモ用テキスト】</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n</P>",
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "image": "/demo/products/25.jpg",
      "view_group_filter": "1",
      "visible_customer_id": null,
      "hide_customer_id": null,
      "prepend_text": "",
      "append_text": "",
      "middle_text": "",
      "rv_prepend_text": "",
      "rv_append_text": "",
      "rv_middle_text": "",
      "file_download": null,
      "customs": [
        {
          "field_id": 14,
          "value": "【カスタム項目1】自由項目を作れます（生産者と設定中）"
        },
        {
          "field_id": 15,
          "value": "【カスタム項目2】自由項目を作れます（ブランドと設定中）"
        },
        {
          "field_id": 16,
          "value": "【カスタム項目3】自由項目を作れます（カタログ頁と設定中）"
        }
      ],
      "hanbai_start": null,
      "hanbai_end": null,
      "recommend_product_id": null,
      "view_pattern": 0,
      "priority": 0,
      "flag": "非表示",
      "updated_at": "2011-11-17 18:48:00",
      "sub_images": {
        "1": {
          "image": "/demo/products/25.jpg",
          "caption": ""
        },
        "2": {
          "image": "/demo/products/25.jpg",
          "caption": ""
        },
        "3": {
          "image": "/demo/products/25.jpg",
          "caption": ""
        },
        "4": {
          "image": "/demo/products/25.jpg",
          "caption": ""
        },
        "5": {
          "image": "/demo/products/25.jpg",
          "caption": ""
        },
        "6": {
          "image": "/demo/products/25.jpg",
          "caption": ""
        }
      }
    },
    {
      "id": 8,
      "main_no": "SS0001",
      "name": "【複数カテゴリ・登録例】電子タバコ（全てのカテゴリで表示させています）",
      "catch_copy": "人気電子タバコセット",
      "category_id": 37,
      "sub_category_id": "17,24,32,33,10,22,21,31,47,50",
      "feature_id1": null,
      "feature_id2": null,
      "feature_id3": null,
      "made_in": "",
      "size": "",
      "sozai": "",
      "caution": "",
      "tag": null,
      "description": "パーティで大人気の獅子舞コスプレセットです。\r\n<P>\r\n<font size=\"5\">【デモ用テキスト】</font><br>\r\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\r\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\r\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\r\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\r\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\r\n</P>",
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "image": "/demo/products/zakka/22391e6a2006448b14e38787ae8a075b_t.jpg",
      "view_group_filter": "1",
      "visible_customer_id": null,
      "hide_customer_id": null,
      "prepend_text": "",
      "append_text": "",
      "middle_text": "",
      "rv_prepend_text": "",
      "rv_append_text": "",
      "rv_middle_text": "",
      "file_download": null,
      "customs": [
        {
          "field_id": 14,
          "value": "【カスタム項目1】自由項目を作れます（生産者と設定中）"
        },
        {
          "field_id": 15,
          "value": "【カスタム項目2】自由項目を作れます（ブランドと設定中）"
        },
        {
          "field_id": 16,
          "value": "【カスタム項目3】自由項目を作れます（カタログ頁と設定中）"
        }
      ],
      "hanbai_start": null,
      "hanbai_end": null,
      "recommend_product_id": null,
      "view_pattern": 0,
      "priority": 0,
      "flag": "非表示",
      "updated_at": "2011-11-17 18:48:00",
      "sub_images": {
        "1": {
          "image": "/demo/products/event1_2.jpg",
          "caption": ""
        },
        "2": {
          "image": "/demo/products/26.jpg",
          "caption": ""
        },
        "3": {
          "image": "/demo/products/26.jpg",
          "caption": ""
        },
        "4": {
          "image": "/demo/products/26.jpg",
          "caption": ""
        },
        "5": {
          "image": "/demo/products/26.jpg",
          "caption": ""
        },
        "6": {
          "image": "/demo/products/26.jpg",
          "caption": ""
        }
      }
    },
    {
      "id": 9,
      "main_no": "C0002",
      "name": "PC用カバン",
      "catch_copy": "",
      "category_id": 10,
      "sub_category_id": null,
      "feature_id1": null,
      "feature_id2": null,
      "feature_id3": null,
      "made_in": "",
      "size": "",
      "sozai": "合皮",
      "caution": "",
      "tag": null,
      "description": "<P>\n<font size=\"5\">【デモ用テキスト】</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n</P>",
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "image": "/demo/products/27.jpg",
      "view_group_filter": "1",
      "visible_customer_id": null,
      "hide_customer_id": null,
      "prepend_text": "",
      "append_text": "",
      "middle_text": "",
      "rv_prepend_text": "",
      "rv_append_text": "",
      "rv_middle_text": "",
      "file_download": null,
      "customs": [
        {
          "field_id": 14,
          "value": "【カスタム項目1】自由項目を作れます（生産者と設定中）"
        },
        {
          "field_id": 15,
          "value": "【カスタム項目2】自由項目を作れます（ブランドと設定中）"
        },
        {
          "field_id": 16,
          "value": "【カスタム項目3】自由項目を作れます（カタログ頁と設定中）"
        }
      ],
      "hanbai_start": null,
      "hanbai_end": null,
      "recommend_product_id": "4,10,11,12",
      "view_pattern": 0,
      "priority": 0,
      "flag": "表示",
      "updated_at": "2011-11-17 18:48:00",
      "sub_images": {
        "1": {
          "image": "/demo/products/27.jpg",
          "caption": ""
        },
        "2": {
          "image": "/demo/products/27.jpg",
          "caption": ""
        },
        "3": {
          "image": "/demo/products/27.jpg",
          "caption": ""
        },
        "4": {
          "image": "/demo/products/27.jpg",
          "caption": ""
        },
        "5": {
          "image": "/demo/products/27.jpg",
          "caption": ""
        },
        "6": {
          "image": "/demo/products/27.jpg",
          "caption": ""
        }
      }
    },
    {
      "id": 10,
      "main_no": "A00002",
      "name": "激安マウス・アソート",
      "catch_copy": "激安アソートのマウス",
      "category_id": 10,
      "sub_category_id": null,
      "feature_id1": null,
      "feature_id2": null,
      "feature_id3": null,
      "made_in": "中国",
      "size": "50ｍｍ：30ｍｍ：80ｍｍ",
      "sozai": "プラスチック",
      "caution": "",
      "tag": null,
      "description": "中国製の激安PS/2のマウスです。\r\n<P>\r\n<font size=\"5\">【デモ用テキスト】</font><br>\r\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\r\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\r\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\r\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\r\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\r\n</P>",
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "image": "/demo/products/28.jpg",
      "view_group_filter": "通常会員",
      "visible_customer_id": null,
      "hide_customer_id": null,
      "prepend_text": "",
      "append_text": "",
      "middle_text": "",
      "rv_prepend_text": "",
      "rv_append_text": "",
      "rv_middle_text": "",
      "file_download": null,
      "customs": [
        {
          "field_id": 14,
          "value": "【カスタム項目1】自由項目を作れます（生産者と設定中）"
        },
        {
          "field_id": 15,
          "value": "【カスタム項目2】自由項目を作れます（ブランドと設定中）"
        },
        {
          "field_id": 16,
          "value": "【カスタム項目3】自由項目を作れます（カタログ頁と設定中）"
        }
      ],
      "hanbai_start": null,
      "hanbai_end": null,
      "recommend_product_id": "4,9,11,12",
      "view_pattern": 0,
      "priority": 0,
      "flag": "非表示",
      "updated_at": "2011-11-17 18:48:00",
      "sub_images": {
        "1": {
          "image": "/demo/sub_products/28_61.jpg",
          "caption": ""
        },
        "2": {
          "image": "/demo/products/28.jpg",
          "caption": ""
        },
        "3": {
          "image": "/demo/products/28.jpg",
          "caption": ""
        },
        "4": {
          "image": "/demo/products/28.jpg",
          "caption": ""
        },
        "5": {
          "image": "/demo/products/28.jpg",
          "caption": ""
        },
        "6": {
          "image": "/demo/products/28.jpg",
          "caption": ""
        }
      }
    },
    {
      "id": 11,
      "main_no": "A0003",
      "name": "【注文不可商品】観葉植物※セットを登録していない注文できない商品の例です",
      "catch_copy": "",
      "category_id": 22,
      "sub_category_id": "47,50",
      "feature_id1": null,
      "feature_id2": null,
      "feature_id3": null,
      "made_in": "",
      "size": "",
      "sozai": "",
      "caution": "",
      "tag": null,
      "description": "<P>\r\n<font size=\"5\">【デモ用テキスト】</font><br>\r\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\r\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\r\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\r\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\r\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\r\n</P>",
      "meta_title": "テストテストtitle",
      "meta_keywords": "テストテストキー",
      "meta_description": "テストテストです。",
      "image": "/demo/products/zakka/green05.jpg",
      "view_group_filter": null,
      "visible_customer_id": "10005",
      "hide_customer_id": null,
      "prepend_text": "",
      "append_text": "",
      "middle_text": "",
      "rv_prepend_text": "",
      "rv_append_text": "",
      "rv_middle_text": "",
      "file_download": null,
      "customs": [
        {
          "field_id": 14,
          "value": "【カスタム項目1】自由項目を作れます（生産者と設定中）"
        },
        {
          "field_id": 15,
          "value": "【カスタム項目2】自由項目を作れます（ブランドと設定中）"
        },
        {
          "field_id": 16,
          "value": "【カスタム項目3】自由項目を作れます（カタログ頁と設定中）"
        }
      ],
      "hanbai_start": null,
      "hanbai_end": null,
      "recommend_product_id": "4,9,10,12",
      "view_pattern": 0,
      "priority": 0,
      "flag": "表示",
      "updated_at": "2011-11-17 18:48:00",
      "sub_images": {
        "1": {
          "image": "/demo/products/zakka/green05.jpg",
          "caption": ""
        },
        "2": {
          "image": "/demo/products/zakka/green05.jpg",
          "caption": ""
        },
        "3": {
          "image": "/demo/products/zakka/green05.jpg",
          "caption": ""
        },
        "4": {
          "image": "/demo/products/zakka/green05.jpg",
          "caption": ""
        },
        "5": {
          "image": "/demo/products/zakka/green05.jpg",
          "caption": ""
        },
        "6": {
          "image": "/demo/products/zakka/green05.jpg",
          "caption": ""
        }
      }
    },
    {
      "id": 12,
      "main_no": "ABC123",
      "name": "ノートパソコン※この商品には個別でおすすめ商品を設定しています",
      "catch_copy": "ここにはキャッチコピーがはいります。",
      "category_id": 10,
      "sub_category_id": null,
      "feature_id1": null,
      "feature_id2": null,
      "feature_id3": null,
      "made_in": "中国",
      "size": "15インチ",
      "sozai": "アルミ製",
      "caution": "",
      "tag": null,
      "description": "CPU：Pentium4　1.8G\nメモリ：512MB\nHD：40G\n<P>\n<font size=\"5\">【デモ用テキスト】</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n</P>",
      "meta_title": "激安ノートパソコン",
      "meta_keywords": "",
      "meta_description": "",
      "image": "/demo/products/30.jpg",
      "view_group_filter": null,
      "visible_customer_id": null,
      "hide_customer_id": null,
      "prepend_text": "",
      "append_text": "",
      "middle_text": "",
      "rv_prepend_text": "",
      "rv_append_text": "",
      "rv_middle_text": "",
      "file_download": null,
      "customs": [
        {
          "field_id": 14,
          "value": "【カスタム項目1】自由項目を作れます（生産者と設定中）"
        },
        {
          "field_id": 15,
          "value": "【カスタム項目2】自由項目を作れます（ブランドと設定中）"
        },
        {
          "field_id": 16,
          "value": "【カスタム項目3】自由項目を作れます（カタログ頁と設定中）"
        }
      ],
      "hanbai_start": null,
      "hanbai_end": null,
      "recommend_product_id": "4,9,10,11,48",
      "view_pattern": 0,
      "priority": 0,
      "flag": "表示",
      "updated_at": "2011-11-17 18:48:00",
      "sub_images": {
        "1": {
          "image": "/demo/products/30.jpg",
          "caption": ""
        },
        "2": {
          "image": "/demo/products/30.jpg",
          "caption": ""
        },
        "3": {
          "image": "/demo/products/30.jpg",
          "caption": ""
        },
        "4": {
          "image": "/demo/products/30.jpg",
          "caption": ""
        },
        "5": {
          "image": "/demo/products/30.jpg",
          "caption": ""
        },
        "6": {
          "image": "/demo/products/30.jpg",
          "caption": ""
        }
      }
    },
    {
      "id": 13,
      "main_no": "L0001",
      "name": "1,000均一",
      "catch_copy": "夏の商品を1,000均一で！",
      "category_id": 22,
      "sub_category_id": null,
      "feature_id1": 1,
      "feature_id2": null,
      "feature_id3": null,
      "made_in": "日本",
      "size": "",
      "sozai": "",
      "caution": "",
      "tag": null,
      "description": "1セット内容\n・和風スタンド\n・扇子\n・日傘\n・虫かご\n・扇風機\n<P>\n<font size=\"5\">【デモ用テキスト】</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n</P>",
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "image": "/demo/products/23.jpg",
      "view_group_filter": "非会員,1",
      "visible_customer_id": "10013",
      "hide_customer_id": null,
      "prepend_text": "",
      "append_text": "",
      "middle_text": "",
      "rv_prepend_text": "",
      "rv_append_text": "",
      "rv_middle_text": "",
      "file_download": "/demo/products/23.jpg",
      "customs": [
        {
          "field_id": 14,
          "value": "【カスタム項目1】自由項目を作れます（生産者と設定中）"
        },
        {
          "field_id": 15,
          "value": "【カスタム項目2】自由項目を作れます（ブランドと設定中）"
        },
        {
          "field_id": 16,
          "value": "【カスタム項目3】自由項目を作れます（カタログ頁と設定中）"
        }
      ],
      "hanbai_start": null,
      "hanbai_end": null,
      "recommend_product_id": null,
      "view_pattern": 0,
      "priority": 0,
      "flag": "表示",
      "updated_at": "2012-03-23 11:33:00",
      "sub_images": {
        "1": {
          "image": "/demo/products/event3_10.jpg",
          "caption": "1000均一"
        },
        "2": {
          "image": "/demo/products/event3_11.jpg",
          "caption": "1000均一"
        },
        "3": {
          "image": "/demo/products/event3_9.jpg",
          "caption": "1000均一"
        },
        "4": {
          "image": "/demo/products/event3_8.jpg",
          "caption": "1000均一"
        },
        "5": {
          "image": "/demo/products/23.jpg",
          "caption": ""
        },
        "6": {
          "image": "/demo/products/23.jpg",
          "caption": ""
        }
      }
    },
    {
      "id": 14,
      "main_no": "B0002",
      "name": "本皮手帳",
      "catch_copy": "",
      "category_id": 22,
      "sub_category_id": null,
      "feature_id1": null,
      "feature_id2": null,
      "feature_id3": null,
      "made_in": "日本",
      "size": "150ｍｍ：80ｍｍ：15ｍｍ",
      "sozai": "",
      "caution": "",
      "tag": null,
      "description": "安心の定番手帳\nミニカレンダー付き\n<P>\n<font size=\"5\">【デモ用テキスト】</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n</P>",
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "image": "/demo/products/18.jpg",
      "view_group_filter": "1",
      "visible_customer_id": null,
      "hide_customer_id": null,
      "prepend_text": "",
      "append_text": "",
      "middle_text": "",
      "rv_prepend_text": "",
      "rv_append_text": "",
      "rv_middle_text": "",
      "file_download": null,
      "customs": [
        {
          "field_id": 14,
          "value": "【カスタム項目1】自由項目を作れます（生産者と設定中）"
        },
        {
          "field_id": 15,
          "value": "【カスタム項目2】自由項目を作れます（ブランドと設定中）"
        },
        {
          "field_id": 16,
          "value": "【カスタム項目3】自由項目を作れます（カタログ頁と設定中）"
        }
      ],
      "hanbai_start": null,
      "hanbai_end": null,
      "recommend_product_id": null,
      "view_pattern": 0,
      "priority": 0,
      "flag": "表示",
      "updated_at": "2012-03-26 09:45:00",
      "sub_images": {
        "1": {
          "image": "/demo/sub_products/18_57.jpg",
          "caption": ""
        },
        "2": {
          "image": "/demo/products/18.jpg",
          "caption": ""
        },
        "3": {
          "image": "/demo/products/18.jpg",
          "caption": ""
        },
        "4": {
          "image": "/demo/products/18.jpg",
          "caption": ""
        },
        "5": {
          "image": "/demo/products/18.jpg",
          "caption": ""
        },
        "6": {
          "image": "/demo/products/18.jpg",
          "caption": ""
        }
      }
    },
    {
      "id": 15,
      "main_no": "i0005",
      "name": "餅つきセット",
      "catch_copy": "",
      "category_id": 17,
      "sub_category_id": null,
      "feature_id1": null,
      "feature_id2": null,
      "feature_id3": null,
      "made_in": "カナダ",
      "size": "臼:直径700mm\r\n杵:長さ900mm",
      "sozai": "",
      "caution": "クッションは付属しておりません。",
      "tag": null,
      "description": "<P>\n<font size=\"5\">【デモ用テキスト】</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n</P>",
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "image": "/demo/products/event2_4.jpg",
      "view_group_filter": null,
      "visible_customer_id": null,
      "hide_customer_id": null,
      "prepend_text": "",
      "append_text": "",
      "middle_text": "",
      "rv_prepend_text": "",
      "rv_append_text": "",
      "rv_middle_text": "",
      "file_download": null,
      "customs": [
        {
          "field_id": 14,
          "value": "【カスタム項目1】自由項目を作れます（生産者と設定中）"
        },
        {
          "field_id": 15,
          "value": "【カスタム項目2】自由項目を作れます（ブランドと設定中）"
        },
        {
          "field_id": 16,
          "value": "【カスタム項目3】自由項目を作れます（カタログ頁と設定中）"
        }
      ],
      "hanbai_start": null,
      "hanbai_end": null,
      "recommend_product_id": null,
      "view_pattern": 0,
      "priority": 0,
      "flag": "非表示",
      "updated_at": "2012-03-26 11:38:00",
      "sub_images": {
        "1": {
          "image": "/demo/products/event2_4.jpg",
          "caption": ""
        },
        "2": {
          "image": "/demo/products/event2_4.jpg",
          "caption": ""
        },
        "3": {
          "image": "/demo/products/event2_4.jpg",
          "caption": ""
        },
        "4": {
          "image": "/demo/products/event2_4.jpg",
          "caption": ""
        },
        "5": {
          "image": "/demo/products/event2_4.jpg",
          "caption": ""
        },
        "6": {
          "image": "/demo/products/event2_4.jpg",
          "caption": ""
        }
      }
    },
    {
      "id": 16,
      "main_no": "SF-002",
      "name": "ソファー　ホワイト",
      "catch_copy": "予想以上のボリューム感！",
      "category_id": 17,
      "sub_category_id": null,
      "feature_id1": 1,
      "feature_id2": null,
      "feature_id3": null,
      "made_in": "",
      "size": "H800mm:W750mm:D750mm",
      "sozai": "合皮製：撥水加工",
      "caution": "",
      "tag": "recommend,limited",
      "description": "人気につき追加生産が決定致しました。お届けまでお待ちいただく事がありますので、ご了承ください。\nクッション・スリッパは付属しておりません。\n<P>\n<font size=\"5\">【デモ用テキスト】</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n</P>",
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "image": "/demo/products/interior1_2.jpg",
      "view_group_filter": "1",
      "visible_customer_id": null,
      "hide_customer_id": null,
      "prepend_text": "",
      "append_text": "",
      "middle_text": "",
      "rv_prepend_text": "",
      "rv_append_text": "",
      "rv_middle_text": "",
      "file_download": null,
      "customs": [
        {
          "field_id": 14,
          "value": "【カスタム項目1】自由項目を作れます（生産者と設定中）"
        },
        {
          "field_id": 15,
          "value": "【カスタム項目2】自由項目を作れます（ブランドと設定中）"
        },
        {
          "field_id": 16,
          "value": "【カスタム項目3】自由項目を作れます（カタログ頁と設定中）"
        }
      ],
      "hanbai_start": null,
      "hanbai_end": null,
      "recommend_product_id": null,
      "view_pattern": 0,
      "priority": 0,
      "flag": "非表示",
      "updated_at": "2012-03-26 11:45:00",
      "sub_images": {
        "1": {
          "image": "/demo/products/interior1_2_0.jpg",
          "caption": ""
        },
        "2": {
          "image": "/demo/products/interior1_2.jpg",
          "caption": ""
        },
        "3": {
          "image": "/demo/products/interior1_2.jpg",
          "caption": ""
        },
        "4": {
          "image": "/demo/products/interior1_2.jpg",
          "caption": ""
        },
        "5": {
          "image": "/demo/products/interior1_2.jpg",
          "caption": ""
        },
        "6": {
          "image": "/demo/products/interior1_2.jpg",
          "caption": ""
        }
      }
    },
    {
      "id": 17,
      "main_no": "SF-003",
      "name": "クラシックソファー（2人がけ）",
      "catch_copy": "シンプルイズベスト！",
      "category_id": 17,
      "sub_category_id": null,
      "feature_id1": null,
      "feature_id2": null,
      "feature_id3": null,
      "made_in": "ノルウェー",
      "size": "H700mm:W1600:D700mm",
      "sozai": "合皮製、撥水加工済",
      "caution": "足部が細めの為、床へのダメージにお気をつけください。",
      "tag": "new,recommend,limited",
      "description": "小物は付属していません。\n<P>\n<font size=\"5\">【デモ用テキスト】</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n</P>",
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "image": "/demo/products/interior1_3.jpg",
      "view_group_filter": "1",
      "visible_customer_id": null,
      "hide_customer_id": null,
      "prepend_text": "",
      "append_text": "<p>一人がけはこちらです。</p><a href=\"/bcart/html/product.php?id=37\"><img src=\"/bcart/html/uploads/demo/products/interior1_4.jpg\" width=\"150\" height=\"100\"></a>",
      "middle_text": "",
      "rv_prepend_text": "",
      "rv_append_text": "<p>一人がけはこちらです。</p><a href=\"/bcart/html/product.php?id=37\"><img src=\"/bcart/html/uploads/demo/products/interior1_4.jpg\" width=\"150\" height=\"100\"></a>",
      "rv_middle_text": "",
      "file_download": null,
      "customs": [
        {
          "field_id": 14,
          "value": "【カスタム項目1】自由項目を作れます（生産者と設定中）"
        },
        {
          "field_id": 15,
          "value": "【カスタム項目2】自由項目を作れます（ブランドと設定中）"
        },
        {
          "field_id": 16,
          "value": "【カスタム項目3】自由項目を作れます（カタログ頁と設定中）"
        }
      ],
      "hanbai_start": null,
      "hanbai_end": null,
      "recommend_product_id": null,
      "view_pattern": 0,
      "priority": 0,
      "flag": "非表示",
      "updated_at": "2012-03-26 11:50:00",
      "sub_images": {
        "1": {
          "image": "/demo/products/interior1_3.jpg",
          "caption": ""
        },
        "2": {
          "image": "/demo/products/interior1_3.jpg",
          "caption": ""
        },
        "3": {
          "image": "/demo/products/interior1_3.jpg",
          "caption": ""
        },
        "4": {
          "image": "/demo/products/interior1_3.jpg",
          "caption": ""
        },
        "5": {
          "image": "/demo/products/interior1_3.jpg",
          "caption": ""
        },
        "6": {
          "image": "/demo/products/interior1_3.jpg",
          "caption": ""
        }
      }
    },
    {
      "id": 18,
      "main_no": "SF-004",
      "name": "クラシックソファー（一人がけ）",
      "catch_copy": "シンプルに暮らそう",
      "category_id": 17,
      "sub_category_id": null,
      "feature_id1": null,
      "feature_id2": null,
      "feature_id3": null,
      "made_in": "ノルウェー",
      "size": "H700mm:W700mm:D700m",
      "sozai": "合皮製　撥水加工済",
      "caution": "",
      "tag": "new,recommend",
      "description": "小物は付属しておりません。\n<P>\n<font size=\"5\">【デモ用テキスト】</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n</P>",
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "image": "/demo/products/interior1_4.jpg",
      "view_group_filter": "1,3",
      "visible_customer_id": null,
      "hide_customer_id": "10010",
      "prepend_text": "",
      "append_text": "<p>二人がけはこちらです。</p><a href=\"/bcart/html/product.php?id=36\"><img src=\"/bcart/html/uploads/demo/products/interior1_3.jpg\" width=\"150\" height=\"100\"></a>",
      "middle_text": "",
      "rv_prepend_text": "",
      "rv_append_text": "<p>二人がけはこちらです。</p><a href=\"/bcart/html/product.php?id=36\"><img src=\"/bcart/html/uploads/demo/products/interior1_3.jpg\" width=\"150\" height=\"100\"></a>",
      "rv_middle_text": "",
      "file_download": null,
      "customs": [
        {
          "field_id": 14,
          "value": "【カスタム項目1】自由項目を作れます（生産者と設定中）"
        },
        {
          "field_id": 15,
          "value": "【カスタム項目2】自由項目を作れます（ブランドと設定中）"
        },
        {
          "field_id": 16,
          "value": "【カスタム項目3】自由項目を作れます（カタログ頁と設定中）"
        }
      ],
      "hanbai_start": null,
      "hanbai_end": null,
      "recommend_product_id": null,
      "view_pattern": 0,
      "priority": 0,
      "flag": "非表示",
      "updated_at": "2012-03-26 11:55:00",
      "sub_images": {
        "1": {
          "image": "/demo/products/interior1_4.jpg",
          "caption": ""
        },
        "2": {
          "image": "/demo/products/interior1_4.jpg",
          "caption": ""
        },
        "3": {
          "image": "/demo/products/interior1_4.jpg",
          "caption": ""
        },
        "4": {
          "image": "/demo/products/interior1_4.jpg",
          "caption": ""
        },
        "5": {
          "image": "/demo/products/interior1_4.jpg",
          "caption": ""
        },
        "6": {
          "image": "/demo/products/interior1_4.jpg",
          "caption": ""
        }
      }
    },
    {
      "id": 19,
      "main_no": "i0001",
      "name": "雛人形セット※在庫切れ商品例",
      "catch_copy": "訳ありにつき格安でご提供！",
      "category_id": 37,
      "sub_category_id": null,
      "feature_id1": 1,
      "feature_id2": null,
      "feature_id3": null,
      "made_in": "日本",
      "size": "ひな壇：H1800ｍｍ",
      "sozai": "",
      "caution": "訳ありの為、商品詳細画像をよくご確認ください。",
      "tag": "new,recommend",
      "description": "<P>\r\n<font size=\"5\">【デモ用テキスト】</font><br>\r\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\r\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\r\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\r\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\r\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\r\n</P>",
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "image": "/demo/products/event2_5.jpg",
      "view_group_filter": "1",
      "visible_customer_id": null,
      "hide_customer_id": null,
      "prepend_text": "",
      "append_text": "",
      "middle_text": "",
      "rv_prepend_text": "",
      "rv_append_text": "",
      "rv_middle_text": "",
      "file_download": null,
      "customs": [
        {
          "field_id": 14,
          "value": "【カスタム項目1】自由項目を作れます（生産者と設定中）"
        },
        {
          "field_id": 15,
          "value": "【カスタム項目2】自由項目を作れます（ブランドと設定中）"
        },
        {
          "field_id": 16,
          "value": "【カスタム項目3】自由項目を作れます（カタログ頁と設定中）"
        }
      ],
      "hanbai_start": null,
      "hanbai_end": null,
      "recommend_product_id": null,
      "view_pattern": 0,
      "priority": 0,
      "flag": "非表示",
      "updated_at": "2012-03-26 12:04:00",
      "sub_images": {
        "1": {
          "image": "/demo/products/event2_6.jpg",
          "caption": ""
        },
        "2": {
          "image": "/demo/products/event2_7.jpg",
          "caption": ""
        },
        "3": {
          "image": "/demo/products/event2_8.jpg",
          "caption": ""
        },
        "4": {
          "image": "/demo/products/event2_9.jpg",
          "caption": ""
        },
        "5": {
          "image": "/demo/products/event2_5.jpg",
          "caption": ""
        },
        "6": {
          "image": "/demo/products/event2_5.jpg",
          "caption": ""
        }
      }
    },
    {
      "id": 20,
      "main_no": "i0004",
      "name": "コマ※商品詳細の振りスペース活用例",
      "catch_copy": "",
      "category_id": 37,
      "sub_category_id": null,
      "feature_id1": 8,
      "feature_id2": null,
      "feature_id3": null,
      "made_in": "",
      "size": "直径80ｍｍ",
      "sozai": "北山杉",
      "caution": "",
      "tag": "new,recommend",
      "description": "ひとつひとつ職人の手作り。\n商品によって若干の模様の違いがあります。\n<P>\n<font size=\"5\">【デモ用テキスト】</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n</P>",
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "image": "/demo/products/event1_4.jpg",
      "view_group_filter": "1",
      "visible_customer_id": null,
      "hide_customer_id": null,
      "prepend_text": "<div class=\"free-space\">\r\n<div class=\"free-head\">（上部フリースペース※商品毎にご用意）</div>\r\n・文章やHTMLコンテンツを表示できます。<br>\r\n・商品は管理画面で表示、非表示を切り替えられるのはもちろん、販売期間等を設定して特定の期間だけ表示するような設定もできます。\r\n</div>",
      "append_text": "<div class=\"free-space\">\r\n<div class=\"free-head\">Bカート活用のポイント#30（下部フリースペース）</div>\r\n・文章やHTMLコンテンツを表示できます。<br><br>\r\n\r\n<div style=\"padding:10px;background:#FFF;\">\r\n<h3>例）商品詳細ページのフリースペース</h3>\r\n<img src=\"uploads/demo/products/event1_4.jpg\" style=\"width:100%;\">\r\n<p style=\"background:#FFF39D;padding:30px;font-size:16px;text-align:center\">↓色違いもございます。</p>\r\n<img src=\"uploads/demo/products/event1_5.jpg\" style=\"width:100%;\">\r\n<p style=\"background:#FFF39D;padding:30px;font-size:16px;\">商品サブ画像の上限を超える画像や、大きく見せたい画像、画像をたくさん使っての説明などはフリースペースを使って表現することもできます。</p>\r\n</div>\r\n\r\n</div>",
      "middle_text": "",
      "rv_prepend_text": "<div class=\"free-space\">\r\n<div class=\"free-head\">（上部フリースペース※商品毎にご用意）</div>\r\n・文章やHTMLコンテンツを表示できます。<br>\r\n・商品は管理画面で表示、非表示を切り替えられるのはもちろん、販売期間等を設定して特定の期間だけ表示するような設定もできます。\r\n</div>",
      "rv_append_text": "<div class=\"free-space\">\r\n<div class=\"free-head\">Bカート活用のポイント#30（下部フリースペース）</div>\r\n・文章やHTMLコンテンツを表示できます。<br><br>\r\n\r\n<div style=\"padding:10px;background:#FFF;\">\r\n<h3>例）商品詳細ページのフリースペース</h3>\r\n<img src=\"uploads/demo/products/event1_4.jpg\" style=\"width:100%;\">\r\n<p style=\"background:#FFF39D;padding:30px;font-size:16px;text-align:center\">↓色違いもございます。</p>\r\n<img src=\"uploads/demo/products/event1_5.jpg\" style=\"width:100%;\">\r\n<p style=\"background:#FFF39D;padding:30px;font-size:16px;\">商品サブ画像の上限を超える画像や、大きく見せたい画像、画像をたくさん使っての説明などはフリースペースを使って表現することもできます。</p>\r\n</div>\r\n\r\n</div>",
      "rv_middle_text": "",
      "file_download": null,
      "customs": [
        {
          "field_id": 14,
          "value": "【カスタム項目1】自由項目を作れます（生産者と設定中）"
        },
        {
          "field_id": 15,
          "value": "【カスタム項目2】自由項目を作れます（ブランドと設定中）"
        },
        {
          "field_id": 16,
          "value": "【カスタム項目3】自由項目を作れます（カタログ頁と設定中）"
        }
      ],
      "hanbai_start": null,
      "hanbai_end": null,
      "recommend_product_id": null,
      "view_pattern": 0,
      "priority": 0,
      "flag": "表示",
      "updated_at": "2012-03-26 12:21:00",
      "sub_images": {
        "1": {
          "image": "/demo/products/event1_5.jpg",
          "caption": ""
        },
        "2": {
          "image": "/demo/products/event1_4.jpg",
          "caption": ""
        },
        "3": {
          "image": "/demo/products/event1_4.jpg",
          "caption": ""
        },
        "4": {
          "image": "/demo/products/event1_4.jpg",
          "caption": ""
        },
        "5": {
          "image": "/demo/products/event1_4.jpg",
          "caption": ""
        },
        "6": {
          "image": "/demo/products/event1_4.jpg",
          "caption": ""
        }
      }
    }
  ],
  "meta": {
    "limit": 20,
    "offset": 0,
    "total": 60
  }
}
```

## PATCH {{api_url}}/api/v1/products/1

**リクエストBODY**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| main_no | 商品管理番号 | 文字列 | 255 |  |
| name | 商品名 | 文字列 | 255 |  |
| catch_copy | キャッチコピー | 文字列 | 255 |  |
| category_id | カテゴリID | 整数 | 11 |  |
| sub_category_id | サブカテゴリID | 文字列 | 255 | category_idをカンマ区切りで指定 |
| feature_id1 | 特集ID1 | 整数/null | 11 |  |
| feature_id2 | 特集ID2 | 整数/null | 11 |  |
| feature_id3 | 特集ID3 | 整数/null | 11 |  |
| made_in | 生産地 | 文字列 | 255 |  |
| size | サイズ | 文字列 | 65,535 |  |
| sozai | 素材 | 文字列 | 65,535 |  |
| caution | 注意事項 | 文字列 | 65,535 |  |
| tag | 商品特徴 | 文字列 | 21 | 識別文字列 new/recommend/limitedなどをカンマ区切りで指定 |
| description | 説明 | 文字列 | 65,535 |  |
| meta_title | meta title | 文字列 | 255 |  |
| meta_keywords | meta keyword | 文字列 | 255 |  |
| meta_description | meta description | 文字列 | 255 |  |
| image | 商品画像パス | 文字列 | 255 |  |
| view_group_filter | 非表示のフループID | 文字列 | 255 | view_group_idをカンマ区切りで指定 |
| visible_customer_id | 例外表示会員ID | 文字列 | 65,535 | customer_idをカンマ区切りで指定 |
| hide_customer_id | 商品を非表示とする会員ID | 文字列 | 65,535 | customer_idをカンマ区切りで指定 |
| prepend_text | 上部フリースペース | 文字列 | 65,535 |  |
| middle_text | 中部フリースペース | 文字列 | 65,535 |  |
| append_text | 下部フリースペース | 文字列 | 65,535 |  |
| rv_prepend_text | レスポンシブ上部フリースペース | 文字列 | 65,535 |  |
| rv_middle_text | レスポンシブ中部フリースペース | 文字列 | 65,535 |  |
| rv_append_text | レスポンシブ下部フリースペース | 文字列 | 65,535 |  |
| file_download | ダウンロードファイルパス | 文字列 | 255 |  |
| customs\[{field_id, value}\] | カスタム項目 | 配列 | 65,535 |  |
| hanbai_start | 販売開始日時 | 日時/null | 19 | Y-m-d H:i:s |
| hanbai_end | 販売終了日時 | 日時/null | 19 | Y-m-d H:i:s |
| recommend_product_id | リコメンド商品ID | 文字列 | 255 | product_idをカンマ区切りで指定 |
| view_pattern | 商品一覧表示パターン | 整数 | 1 |  |
| priority | 表示優先度 | 文字列 | 5 |  |
| flag | 状態 | 文字列 | 3 | 表示/非表示 |
| updated_at | 更新日時 | 文字列 | 19 | Y-m-d H:i:s |
| sub_images\[{{i}}\]\[image\] | サブ画像{{i}}パス | 文字列 | 255 | {{i}}に配列のキー |
| sub_images\[{{i}}\]\[caption\] | サブ画像{{i}}キャプション | 文字列 | 255 | {{i}}に配列のキー |

※ {{i}}は配列のキー  
※ sub_imagesを指定した場合は商品ID紐付いた全てを置き換えますので全てのサブ画像をリクエストして下さい。

**リクエストボディ例:**

```json
{
  "main_no": "SS0000v2",
  "name": "デスクトップパソコン2",
  "catch_copy": "",
  "category_id": 10,
  "sub_category_id": "",
  "feature_id1": null,
  "feature_id2": null,
  "feature_id3": null,
  "made_in": "日本",
  "size": "100:10:100",
  "sozai": "プラスチック",
  "caution": "少し昔の型になります。インテリアとしてお使いいただけます。",
  "tag": "",
  "description": "ここには任意の商品説明が入力できます。\nここには任意の商品説明が入力できます。\n\nここには任意の商品説明が入力できます。\nここには任意の商品説明が入力できます。\n\n<table><tr><th>表項目</th><td>表内容</td></tr><tr><th>表項目</th><td>表内容</td></tr></table>\n<strong style=\"color: #f00; font-size: 16px;\">HTMLも挿入できます。</strong>\n<P>\n<font size=\"5\">【デモ用テキスト】</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n</P>",
  "meta_title": "",
  "meta_keywords": "",
  "meta_description": "",
  "image": "/demo/products/3.jpg",
  "view_group_filter": "非会員",
  "visible_customer_id": "",
  "prepend_text": "",
  "append_text": "",
  "middle_text": "",
  "rv_prepend_text": "",
  "rv_append_text": "＜font color=\"blue\"＞※ブラックは入荷待ちです。＜/font＞",
  "rv_middle_text": "",
  "file_download": "",
  "customs": [
    {
      "field_id": 14,
      "value": "基本カスタム1"
    },
    {
      "field_id": 16,
      "value": "基本カスタム3"
    },
    {
      "field_id": 20,
      "value": "基本カスタム4"
    }
  ],
  "hanbai_start": null,
  "hanbai_end": null,
  "recommend_product_id": "",
  "view_pattern": 0,
  "priority": 0,
  "flag": "非表示",
  "sub_images": {
    "1": {
      "image": "/demo/products/3.jpg",
      "caption": ""
    },
    "2": {
      "image": "/demo/products/3.jpg",
      "caption": ""
    },
    "3": {
      "image": "/demo/products/3.jpg",
      "caption": ""
    },
    "4": {
      "image": "/demo/products/3.jpg",
      "caption": ""
    },
    "5": {
      "image": "/demo/products/3.jpg",
      "caption": ""
    },
    "6": {
      "image": "/demo/products/3.jpg",
      "caption": ""
    }
  },
  "updated_at": "2011-11-17 18:48:00"
}
```

**レスポンス例（200 OK）:**

```json
{
  "product": {
    "id": 1,
    "main_no": "SS0000v2",
    "name": "デスクトップパソコン2",
    "catch_copy": "",
    "category_id": 10,
    "sub_category_id": null,
    "feature_id1": null,
    "feature_id2": null,
    "feature_id3": null,
    "made_in": "日本",
    "size": "100:10:100",
    "sozai": "プラスチック",
    "caution": "少し昔の型になります。インテリアとしてお使いいただけます。",
    "tag": null,
    "description": "ここには任意の商品説明が入力できます。\nここには任意の商品説明が入力できます。\n\nここには任意の商品説明が入力できます。\nここには任意の商品説明が入力できます。\n\n<table><tr><th>表項目</th><td>表内容</td></tr><tr><th>表項目</th><td>表内容</td></tr></table>\n<strong style=\"color: #f00; font-size: 16px;\">HTMLも挿入できます。</strong>\n<P>\n<font size=\"5\">【デモ用テキスト】</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n</P>",
    "meta_title": "",
    "meta_keywords": "",
    "meta_description": "",
    "image": "/demo/products/3.jpg",
    "view_group_filter": "非会員",
    "visible_customer_id": null,
    "hide_customer_id": "10010",
    "prepend_text": "",
    "append_text": "",
    "middle_text": "",
    "rv_prepend_text": "",
    "rv_append_text": "＜font color=\"blue\"＞※ブラックは入荷待ちです。＜/font＞",
    "rv_middle_text": "",
    "file_download": null,
    "customs": [
      {
        "field_id": 14,
        "value": "基本カスタム1"
      },
      {
        "field_id": 16,
        "value": "基本カスタム3"
      },
      {
        "field_id": 20,
        "value": "基本カスタム4"
      }
    ],
    "hanbai_start": null,
    "hanbai_end": null,
    "recommend_product_id": null,
    "view_pattern": 0,
    "priority": 0,
    "flag": "非表示",
    "sub_images": {
      "1": {
        "image": "",
        "caption": ""
      },
      "2": {
        "image": "/demo/products/3.jpg",
        "caption": ""
      },
      "3": {
        "image": "/demo/products/3.jpg",
        "caption": ""
      },
      "4": {
        "image": "/demo/products/3.jpg",
        "caption": ""
      },
      "5": {
        "image": "/demo/products/3.jpg",
        "caption": ""
      },
      "6": {
        "image": "/demo/products/3.jpg",
        "caption": ""
      },
      "7": {
        "image": "/demo/products/3.jpg",
        "caption": ""
      }
    },
    "updated_at": "2011-11-17 18:48:00"
  }
}
```

## PATCH {{api_url}}/api/v1/products/

**リクエストBODY**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| products\[{{i}}\]\[main_no\] | 商品管理番号 | 文字列 | 255 |  |
| products\[{{i}}\]\[name\] | 商品名 | 文字列 | 255 |  |
| products\[{{i}}\]\[catch_copy\] | キャッチコピー | 文字列 | 255 |  |
| products\[{{i}}\]\[category_id\] | カテゴリID | 整数 | 11 |  |
| products\[{{i}}\]\[sub_category_id\] | サブカテゴリID | 文字列 | 255 | category_idをカンマ区切りで指定 |
| products\[{{i}}\]\[feature_id1\] | 特集ID1 | 整数/null | 11 |  |
| products\[{{i}}\]\[feature_id2\] | 特集ID2 | 整数/null | 11 |  |
| products\[{{i}}\]\[feature_id3\] | 特集ID3 | 整数/null | 11 |  |
| products\[{{i}}\]\[made_in\] | 生産地 | 文字列 | 255 |  |
| products\[{{i}}\]\[size\] | サイズ | 文字列 | 65,535 |  |
| products\[{{i}}\]\[sozai\] | 素材 | 文字列 | 65,535 |  |
| products\[{{i}}\]\[caution\] | 注意事項 | 文字列 | 65,535 |  |
| products\[{{i}}\]\[tag\] | 商品特徴 | 文字列 | 21 | 識別文字列 new/recommend/limitedなどをカンマ区切りで指定 |
| products\[{{i}}\]\[description\] | 説明 | 文字列 | 65,535 |  |
| products\[{{i}}\]\[meta_title\] | meta title | 文字列 | 255 |  |
| products\[{{i}}\]\[meta_keywords\] | meta keyword | 文字列 | 255 |  |
| products\[{{i}}\]\[meta_description\] | meta description | 文字列 | 255 |  |
| products\[{{i}}\]\[image\] | 商品画像パス | 文字列 | 255 |  |
| products\[{{i}}\]\[view_group_filter\] | 非表示のフループID | 文字列 | 255 | view_group_idをカンマ区切りで指定 |
| products\[{{i}}\]\[visible_customer_id\] | 例外表示会員ID | 文字列 | 65,535 | customer_idをカンマ区切りで指定 |
| products\[{{i}}\]\[hide_customer_id\] | 商品を非表示とする会員ID | 文字列 | 65,535 | customer_idをカンマ区切りで指定 |
| products\[{{i}}\]\[prepend_text\] | 上部フリースペース | 文字列 | 65,535 |  |
| products\[{{i}}\]\[middle_text\] | 中部フリースペース | 文字列 | 65,535 |  |
| products\[{{i}}\]\[append_text\] | 下部フリースペース | 文字列 | 65,535 |  |
| products\[{{i}}\]\[file_download\] | ダウンロードファイルパス | 文字列 | 255 |  |
| products\[{{i}}\]\[rv_prepend_text\] | レスポンシブ上部フリースペース | 文字列 | 65,535 |  |
| products\[{{i}}\]\[rv_middle_text\] | レスポンシブ中部フリースペース | 文字列 | 65,535 |  |
| products\[{{i}}\]\[rv_append_text\] | レスポンシブ下部フリースペース | 文字列 | 65,535 |  |
| products\[{{i}}\]\[customs\]\[{field_id, value}\] | カスタム項目 | 配列 | 65,535 |  |
| products\[{{i}}\]\[hanbai_start\] | 販売開始日時 | 日時/null | 19 | Y-m-d H:i:s |
| products\[{{i}}\]\[hanbai_end\] | 販売終了日時 | 日時/null | 19 | Y-m-d H:i:s |
| products\[{{i}}\]\[recommend_product_id\] | リコメンド商品ID | 文字列 | 255 | product_idをカンマ区切りで指定 |
| products\[{{i}}\]\[view_pattern\] | 商品一覧表示パターン | 整数 | 1 |  |
| products\[{{i}}\]\[priority\] | 表示優先度 | 文字列 | 5 |  |
| products\[{{i}}\]\[flag\] | 状態 | 文字列 | 3 | 表示/非表示 |
| products\[{{i}}\]\[updated_at\] | 更新日時 | 文字列 | 19 | Y-m-d H:i:s |
| products\[{{i}}\]\[sub_images\]\[{{j}}\]\[image\] | サブ画像{{j}}パス\[^1\] | 文字列 | 255 | {{j}}に配列のキー |
| products\[{{i}}\]\[sub_images\]\[{{j}}\]\[caption\] | サブ画像{{j}}キャプション | 文字列 | 255 | {{j}}に配列のキー |

※ {{i}}/{{j}}は配列のキー  
※ sub_imagesを指定した場合は商品ID紐付いた全てを置き換えますので全てのサブ画像をリクエストして下さい。

**リクエストボディ例:**

```json
{
  "products": [
    {
      "id": 1,
      "main_no": "COL-1008",
      "name": "コルビジェ風クラシックソファー2人掛け",
      "made_in": "フランス",
      "sub_images": [
        {
          "image": "/test/testXXX.jpg"
        }
      ]
    }
  ]
}
```

**レスポンス例（200 OK）:**

```json
{
  "products": [
    {
      "id": 1,
      "main_no": "COL-1008",
      "name": "コルビジェ風クラシックソファー2人掛け",
      "catch_copy": "",
      "category_id": 10,
      "sub_category_id": null,
      "feature_id1": null,
      "feature_id2": null,
      "feature_id3": null,
      "made_in": "フランス",
      "size": "100:10:100",
      "sozai": "プラスチック",
      "caution": "少し昔の型になります。インテリアとしてお使いいただけます。",
      "tag": null,
      "description": "ここには任意の商品説明が入力できます。\nここには任意の商品説明が入力できます。\n\nここには任意の商品説明が入力できます。\nここには任意の商品説明が入力できます。\n\n<table><tr><th>表項目</th><td>表内容</td></tr><tr><th>表項目</th><td>表内容</td></tr></table>\n<strong style=\"color: #f00; font-size: 16px;\">HTMLも挿入できます。</strong>\n<P>\n<font size=\"5\">【デモ用テキスト】</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n<font size=\"2\">ここに説明が入ります。HTMLの記入も可能。</font><br>\n</P>",
      "meta_title": "",
      "meta_keywords": "",
      "meta_description": "",
      "image": "/demo/products/3.jpg",
      "view_group_filter": "非会員",
      "visible_customer_id": null,
      "hide_customer_id": "10010",
      "prepend_text": "",
      "append_text": "",
      "middle_text": "",
      "rv_prepend_text": "",
      "rv_append_text": "＜font color=\"blue\"＞※ブラックは入荷待ちです。＜/font＞",
      "rv_middle_text": "",
      "file_download": null,
      "customs": [
        {
          "field_id": 14,
          "value": "基本カスタム1"
        },
        {
          "field_id": 16,
          "value": "基本カスタム3"
        },
        {
          "field_id": 20,
          "value": "基本カスタム4"
        }
      ],
      "hanbai_start": null,
      "hanbai_end": null,
      "recommend_product_id": null,
      "view_pattern": 0,
      "priority": 0,
      "flag": "非表示",
      "sub_images": {
        "1": {
          "image": "/test/testXXX.jpg",
          "caption": ""
        }
      },
      "updated_at": "2022-01-26 14:36:43"
    }
  ]
}
```

## POST {{api_url}}/api/v1/products

**リクエストBODY**

| Key | 名称 | 型 | 最大桁数 | 内容 |
| --- | --- | --- | --- | --- |
| products\[{{i}}\]\[main_no\] | 商品管理番号 | 文字列 | 255 |  |
| products\[{{i}}\]\[name\] | 商品名 | 文字列 | 255 |  |
| products\[{{i}}\]\[catch_copy\] | キャッチコピー | 文字列 | 255 |  |
| products\[{{i}}\]\[category_id\] | カテゴリID | 整数 | 11 |  |
| products\[{{i}}\]\[sub_category_id\] | サブカテゴリID | 文字列 | 255 | category_idをカンマ区切りで指定 |
| products\[{{i}}\]\[feature_id1\] | 特集ID1 | 整数/null | 11 |  |
| products\[{{i}}\]\[feature_id2\] | 特集ID2 | 整数/null | 11 |  |
| products\[{{i}}\]\[feature_id3\] | 特集ID3 | 整数/null | 11 |  |
| products\[{{i}}\]\[made_in\] | 生産地 | 文字列 | 255 |  |
| products\[{{i}}\]\[size\] | サイズ | 文字列 | 65,535 |  |
| products\[{{i}}\]\[sozai\] | 素材 | 文字列 | 65,535 |  |
| products\[{{i}}\]\[caution\] | 注意事項 | 文字列 | 65,535 |  |
| products\[{{i}}\]\[tag\] | 商品特徴 | 文字列 | 21 | 識別文字列 new/recommend/limited などをカンマ区切りで指定 |
| products\[{{i}}\]\[description\] | 説明 | 文字列 | 65,535 |  |
| products\[{{i}}\]\[meta_title\] | meta title | 文字列 | 255 |  |
| products\[{{i}}\]\[meta_keywords\] | meta keyword | 文字列 | 255 |  |
| products\[{{i}}\]\[meta_description\] | meta description | 文字列 | 255 |  |
| products\[{{i}}\]\[image\] | 商品画像パス | 文字列 | 255 |  |
| products\[{{i}}\]\[view_group_filter\] | 非表示のフループID | 文字列 | 255 | view_group_idをカンマ区切りで指定 |
| products\[{{i}}\]\[visible_customer_id\] | 例外表示会員ID | 文字列 | 65,535 | customer_idをカンマ区切りで指定 |
| products\[{{i}}\]\[hide_customer_id\] | 商品を非表示とする会員ID | 文字列 | 65,535 | customer_idをカンマ区切りで指定 |
| products\[{{i}}\]\[prepend_text\] | 上部フリースペース | 文字列 | 65,535 |  |
| products\[{{i}}\]\[middle_text\] | 中部フリースペース | 文字列 | 65,535 |  |
| products\[{{i}}\]\[append_text\] | 下部フリースペース | 文字列 | 65,535 |  |
| products\[{{i}}\]\[file_download\] | ダウンロードファイルパス | 文字列 | 255 |  |
| products\[{{i}}\]\[rv_prepend_text\] | レスポンシブ上部フリースペース | 文字列 | 65,535 |  |
| products\[{{i}}\]\[rv_middle_text\] | レスポンシブ中部フリースペース | 文字列 | 65,535 |  |
| products\[{{i}}\]\[rv_append_text\] | レスポンシブ下部フリースペース | 文字列 | 65,535 |  |
| products\[{{i}}\]\[customs\]\[{field_id, value}\] | カスタム項目 | 配列 | 65,535 |  |
| products\[{{i}}\]\[hanbai_start\] | 販売開始日時 | 日時/null | 19 | Y-m-d H:i:s |
| products\[{{i}}\]\[hanbai_end\] | 販売終了日時 | 日時/null | 19 | Y-m-d H:i:s |
| products\[{{i}}\]\[recommend_product_id\] | リコメンド商品ID | 文字列 | 255 | product_idをカンマ区切りで指定 |
| products\[{{i}}\]\[view_pattern\] | 商品一覧表示パターン | 整数 | 1 |  |
| products\[{{i}}\]\[priority\] | 表示優先度 | 文字列 | 5 |  |
| products\[{{i}}\]\[flag\] | 状態 | 文字列 | 3 | 表示/非表示 |
| products\[{{i}}\]\[updated_at\] | 更新日時 | 文字列 | 19 | Y-m-d H:i:s |
| products\[{{i}}\]\[sub_images\]\[{{j}}\]\[image\] | サブ画像{{j}}パス\[^1\] | 文字列 | 255 | {{j}}に配列のキー |
| products\[{{i}}\]\[sub_images\]\[{{j}}\]\[caption\] | サブ画像{{j}}キャプション | 文字列 | 255 | {{j}}に配列のキー |

※ {{i}}/{{j}}は配列のキー

**リクエストボディ例:**

```json
{
  "products": [
    {
      "main_no": "XXX-1008",
      "name": "イームズ風クラシックソファー2人掛け",
      "catch_copy": "高級欧州インテリア",
      "category_id": 17,
      "sub_category_id": "11",
      "feature_id1": 2,
      "feature_id2": 3,
      "feature_id3": 1,
      "made_in": "スウェーデン",
      "size": "H900mm:W1600:D900mm",
      "sozai": "本皮製",
      "caution": "革製品の為、メンテナンスをしてください。",
      "tag": "new,limited",
      "description": "イームズ風です。",
      "meta_title": "イームズ風ソファー",
      "meta_keywords": "ソファー,革製品,皮",
      "meta_description": "イームズ風の北欧革製ソファーです。",
      "image": "/sample/products/interior1_3.jpg",
      "view_group_filter": "1",
      "visible_customer_id": "5555",
      "prepend_text": "<p>こちらの商品はサンプル。<br>上が「商品基本情報」、下が「商品セット情報」になります。</p>",
      "append_text": "<p>一人がけはこちらです。</p><a href=\"/product.php?id=2\"><img src=\"/uploads/sample/products/interior1_4.jpg\" width=\"150\" height=\"100\"></a>",
      "middle_text": "お買い得",
      "file_download": null,
      "customs": [
        {
          "field_id": 14,
          "value": "32.0kg"
        },
        {
          "field_id": 15,
          "value": "XXXX"
        },
        {
          "field_id": 16,
          "value": "X3"
        }
      ],
      "hanbai_start": "2016-10-01 00:00:00",
      "hanbai_end": "2017-05-01 00:00:00",
      "recommend_product_id": "4,15",
      "view_pattern": 2,
      "priority": 0,
      "flag": "表示",
      "sub_images": [
        {
          "image": "/test/XXXXX.jpg"
        }
      ],
      "updated_at": "2015-09-26 18:09:01"
    }
  ]
}
```

**レスポンス例（200 OK）:**

```json
{
  "products": [
    {
      "id": 65,
      "main_no": "XXX-1008",
      "name": "イームズ風クラシックソファー2人掛け",
      "catch_copy": "高級欧州インテリア",
      "category_id": 17,
      "sub_category_id": "11",
      "feature_id1": 2,
      "feature_id2": 3,
      "feature_id3": 1,
      "made_in": "スウェーデン",
      "size": "H900mm:W1600:D900mm",
      "sozai": "本皮製",
      "caution": "革製品の為、メンテナンスをしてください。",
      "tag": "new,limited",
      "description": "イームズ風です。",
      "meta_title": "イームズ風ソファー",
      "meta_keywords": "ソファー,革製品,皮",
      "meta_description": "イームズ風の北欧革製ソファーです。",
      "image": "/sample/products/interior1_3.jpg",
      "view_group_filter": "1",
      "visible_customer_id": "5555",
      "hide_customer_id": null,
      "prepend_text": "<p>こちらの商品はサンプル。<br>上が「商品基本情報」、下が「商品セット情報」になります。</p>",
      "append_text": "<p>一人がけはこちらです。</p><a href=\"/product.php?id=2\"><img src=\"/uploads/sample/products/interior1_4.jpg\" width=\"150\" height=\"100\"></a>",
      "middle_text": "お買い得",
      "rv_prepend_text": "",
      "rv_append_text": "",
      "rv_middle_text": "",
      "file_download": null,
      "customs": [
        {
          "field_id": 14,
          "value": "32.0kg"
        },
        {
          "field_id": 15,
          "value": "XXXX"
        },
        {
          "field_id": 16,
          "value": "X3"
        }
      ],
      "hanbai_start": "2016-10-01 00:00:00",
      "hanbai_end": "2017-05-01 00:00:00",
      "recommend_product_id": "4,15",
      "view_pattern": 2,
      "priority": 0,
      "flag": "表示",
      "sub_images": {
        "1": {
          "image": "/test/XXXXX.jpg",
          "caption": ""
        }
      },
      "updated_at": "2015-09-26 18:09:01"
    }
  ]
}
```
