# 基本的な仕様について

## _現在クロスドメインでの接続を許可していないため、JavaScriptでAPIをご利用いただけませんのでご注意ください。（サンプルのjQueryも利用いただけません。）_

## 利用制限について

BカートAPIは300秒につき300回までリクエストすることが可能です。  
300秒に300回を越えると300秒間のロックがかかりアクセスできなくなります。  
なお、サイトID（Bカート環境のID）とクライアントID（トークンのID）の組み合わせに対してレート制限が適用されます。  
またリクエスト上限を超えた場合のみ、レスポンスヘッダーに「Retry-After」というカスタムヘッダーが追加され、解除までの時間を取得することも可能です。

## 仕様変更について

BカートAPIでは基本的に後方互換性を保ちつつ変更を行います。  
例えば廃止予定の項目がある場合、既存の項目は残しつつ新しい項目を追加します。  
その後一定期間を設けて廃止予定の項目を削除するような流れとなります。

また、下記のような後方互換性を保った変更は事前の予告なく実施する場合がありますので、これらの変更（例: プロパティの増減や順番）に影響を受けないようにアプリケーションの実装を行ってください。

- 新しいエンドポイントの追加
    
- 既存のエンドポイントに新しいプロパティの追加
    
- 必須ではないURIパラメータの追加
    

## 本ドキュメントのAI参照向けMarkdown版について

本ドキュメントは動的にHTMLが構築されるので、URLをAIに読ませてもAIが正常な形でHTMLを取得できずにBカートAPIの仕様を把握させることは難しいです。また、ドキュメントとしての可読性を向上させるためにエンドポイントごとにHeaderの情報を記載するなど、ヒトが読みやすい形を目指して作成していますが、AIが参照する場合には冗長な構成は不要です。

そこで、AIが参照することを前提として冗長な表現を無くしてMarkdown形式に変換した静的なファイルを[こちら](https://bcart-documents.s3.ap-northeast-1.amazonaws.com/api/bcart-api_document_v1_normalized.md)に設置しています。書かれているBカートAPIの仕様は本ドキュメントと同じです。

## APIを使用した構築例について

BカートAPIを使用しての、販売管理システムや倉庫管理システム等の連携について、構築事例をご紹介しております。

APIの使用をご検討されている方、現在使用中で運用方法をご検討されている方などは[こちら](https://bcart.jp/post/detail/184/)をご参照ください。

## 権限について

APIの利用できる許可を管理することが出来ます。 パーソナルアクセストークンの場合は発行する際にスコープを設定することが出来ます。  
Oauthクライアントの場合はクライアント側で許可コードリクエスト時にパラメータを送りログイン時に許可します。

### スコープ一覧

| スコープ名 | 説明 |
| --- | --- |
| user-read | アカウント情報参照 |
| products-read | 商品情報参照 |
| products-write | 商品情報書込み |
| product_customs-read | 商品カスタム情報参照 |
| product_customs-write | 商品カスタム情報書込み |
| product_sets-read | 商品セット情報参照 |
| product_sets-write | 商品セット情報書込み |
| product_set_options-read | 商品セットオプション情報参照 |
| product_set_options-write | 商品セットオプション情報書込み |
| product_set_customs-read | 商品セットカスタム情報参照 |
| product_set_customs-write | 商品セットカスタム情報書込み |
| product_stock-read | 在庫情報参照 |
| product_stock-write | 在庫情報書込み |
| categories-read | 商品カテゴリ参照 |
| categories-write | 商品カテゴリ書込み |
| customers-read | 会員情報参照 |
| customers-write | 会員情報書込み |
| customer_customs-read | 会員カスタム情報参照 |
| customer_customs-write | 会員カスタム情報書込み |
| other_addresses-read | 別配送先情報参照 |
| other_addresses-write | 別配送先情報書込み |
| orders-read | 受注情報参照 |
| orders-write | 受注情報書込み |
| order_customs-read | 受注カスタム情報参照 |
| order_customs-write | 受注カスタム情報書込み |
| order_products-read | 受注商品情報参照 |
| order_products-write | 受注商品情報書込み |
| logistics-read | 出荷情報参照 |
| logistics-write | 出荷情報書込み |
| estimates-read | 見積情報参照 |
| estimate_products-read | 見積商品情報参照 |
| price_groups-read | 価格グループ情報参照 |
| view_groups-read | 表示グループ情報参照 |
| shipping_groups-read | 配送グループ情報参照 |
| bookmarks-read | お気に入り参照 |
| bookmarks-write | お気に入り書込み |
| product_features-read | 特集参照 |
| product_features-write | 特集書込み |
| points-read | ポイント参照 |
| points-write | ポイント書込み |
| script_tags-read | スクリプトタグ参照 |
| script_tags-write | スクリプトタグ書込み |
| webhooks-read | webhook参照 |
| webhooks-write | webhook書込み |
