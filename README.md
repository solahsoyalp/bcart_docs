# BカートAPI リファレンス（V1）

出典: https://docs.api.bcart.jp/ （公式のAI参照向け正規化Markdown `bcart-api_document_v1_normalized.md` を取得日 2026-10-22 時点で分割・整理）

仕様の正本は公式ドキュメント。本リポジトリは参照しやすいようにトピック単位へ分割したもの。

## 共通仕様

| ファイル | 内容 |
| --- | --- |
| [docs/01-basics.md](docs/01-basics.md) | 基本仕様・利用制限・スコープ |
| [docs/02-authentication.md](docs/02-authentication.md) | 認証（アクセストークン取得） |
| [docs/03-request.md](docs/03-request.md) | リクエスト |
| [docs/04-parameters.md](docs/04-parameters.md) | URI・拡張パラメータ |
| [docs/05-response.md](docs/05-response.md) | レスポンス・エラー |

## リファレンス（エンドポイント別）

共通事項（変数・認証）: [reference/00-overview.md](reference/00-overview.md)

| ファイル | リソース | エンドポイント |
| --- | --- | --- |
| [reference/01-user.md](reference/01-user.md) | アカウント情報 | `GET /api/v1/user` |
| [reference/02-product_sets.md](reference/02-product_sets.md) | 商品セット | `GET /api/v1/product_sets/1`<br>`GET /api/v1/product_sets`<br>`PATCH /api/v1/product_sets/1`<br>`PATCH /api/v1/product_sets/2`<br>`PATCH /api/v1/product_sets/`<br>`POST /api/v1/product_sets` |
| [reference/03-product_set_customs.md](reference/03-product_set_customs.md) | 商品セットカスタム項目 | `GET /api/v1/product_set_customs/17`<br>`GET /api/v1/product_set_customs`<br>`PATCH /api/v1/product_set_customs/21`<br>`PATCH /api/v1/product_set_customs/`<br>`POST /api/v1/product_set_customs/` |
| [reference/04-product_set_options.md](reference/04-product_set_options.md) | 商品オプション | `GET /api/v1/product_set_options/1`<br>`GET /api/v1/product_set_options/`<br>`PATCH /api/v1/product_set_options/1`<br>`PATCH /api/v1/product_set_options/`<br>`POST /api/v1/product_set_options/` |
| [reference/05-products.md](reference/05-products.md) | 商品基本 | `GET /api/v1/products/1`<br>`GET /api/v1/products`<br>`PATCH /api/v1/products/1`<br>`PATCH /api/v1/products/`<br>`POST /api/v1/products` |
| [reference/06-product_customs.md](reference/06-product_customs.md) | 商品基本カスタム項目 | `GET /api/v1/product_customs/14`<br>`GET /api/v1/product_customs`<br>`PATCH /api/v1/product_customs/20`<br>`PATCH /api/v1/product_customs/`<br>`POST /api/v1/product_customs/` |
| [reference/07-stock.md](reference/07-stock.md) | 在庫 | `GET /api/v1/product_stock/XXX-1008-AA`<br>`GET /api/v1/product_stock`<br>`PATCH /api/v1/product_stock/AK-M`<br>`PATCH /api/v1/product_stock/` |
| [reference/08-categories.md](reference/08-categories.md) | 商品カテゴリ | `GET /api/v1/categories/9`<br>`GET /api/v1/categories`<br>`PATCH /api/v1/categories/30`<br>`PATCH /api/v1/categories/`<br>`POST /api/v1/categories/` |
| [reference/09-product_features.md](reference/09-product_features.md) | 商品特集 | `GET /api/v1/product_features/1`<br>`GET /api/v1/product_features`<br>`PATCH /api/v1/product_features/1`<br>`PATCH /api/v1/product_features/`<br>`POST /api/v1/product_features/` |
| [reference/10-orders.md](reference/10-orders.md) | 受注 | `GET /api/v1/orders/128`<br>`GET /api/v1/orders`<br>`PATCH /api/v1/orders/128`<br>`PATCH /api/v1/orders` |
| [reference/11-order_products.md](reference/11-order_products.md) | 受注商品 | `GET /api/v1/order_products/2`<br>`GET /api/v1/order_products`<br>`PATCH /api/v1/order_products/2`<br>`PATCH /api/v1/order_products` |
| [reference/12-order_customs.md](reference/12-order_customs.md) | 受注カスタム項目 | `GET /api/v1/order_customs`<br>`GET /api/v1/order_customs/6`<br>`PATCH /api/v1/order_customs/6`<br>`PATCH /api/v1/order_customs/`<br>`POST /api/v1/order_customs/` |
| [reference/13-logistics.md](reference/13-logistics.md) | 出荷 | `GET /api/v1/logistics/20000000`<br>`GET /api/v1/logistics`<br>`PATCH /api/v1/logistics/20000000`<br>`PATCH /api/v1/logistics` |
| [reference/14-estimates.md](reference/14-estimates.md) | 見積 | `GET /api/v1/estimates/1`<br>`GET /api/v1/estimates` |
| [reference/15-estimate_products.md](reference/15-estimate_products.md) | 見積商品 | `GET /api/v1/estimate_products/2`<br>`GET /api/v1/estimate_products` |
| [reference/16-customers.md](reference/16-customers.md) | 会員 | `GET /api/v1/customers/1`<br>`GET /api/v1/customers`<br>`PATCH /api/v1/customers/10003`<br>`PATCH /api/v1/customers/`<br>`POST /api/v1/customers/` |
| [reference/17-other_addresses.md](reference/17-other_addresses.md) | 会員別配送先 | `GET /api/v1/other_addresses/1`<br>`GET /api/v1/other_addresses`<br>`PATCH /api/v1/other_addresses/1`<br>`PATCH /api/v1/other_addresses/`<br>`POST /api/v1/other_addresses/` |
| [reference/18-customer_customs.md](reference/18-customer_customs.md) | 会員カスタム項目 | `GET /api/v1/customer_customs/11`<br>`GET /api/v1/customer_customs`<br>`PATCH /api/v1/customer_customs/22`<br>`PATCH /api/v1/customer_customs/`<br>`POST /api/v1/customer_customs/` |
| [reference/19-points.md](reference/19-points.md) | ポイント | `GET /api/v1/points/1`<br>`GET /api/v1/points`<br>`PATCH /api/v1/points/1`<br>`PATCH /api/v1/points/`<br>`POST /api/v1/points/` |
| [reference/20-bookmarks.md](reference/20-bookmarks.md) | お気に入り | `GET /api/v1/bookmarks/1`<br>`GET /api/v1/bookmarks`<br>`PATCH /api/v1/bookmarks/1`<br>`PATCH /api/v1/bookmarks/`<br>`POST /api/v1/bookmarks/` |
| [reference/21-order_statuses.md](reference/21-order_statuses.md) | 受注ステータス | `GET /api/v1/order_statuses/%E3%82%AB%E3%82%B9%E3%82%BF%E3%83%A01`<br>`GET /api/v1/order_statuses`<br>`PATCH /api/v1/order_statuses/%E3%82%AB%E3%82%B9%E3%82%BF%E3%83%A01`<br>`PATCH /api/v1/order_statuses/`<br>`POST /api/v1/order_statuses/` |
| [reference/22-price_groups.md](reference/22-price_groups.md) | 価格グループ | `GET /api/v1/price_groups/1`<br>`GET /api/v1/price_groups` |
| [reference/23-view_groups.md](reference/23-view_groups.md) | 表示グループ | `GET /api/v1/view_groups/1`<br>`GET /api/v1/view_groups` |
| [reference/24-shipping_groups.md](reference/24-shipping_groups.md) | 配送グループ | `GET /api/v1/shipping_groups/1`<br>`GET /api/v1/shipping_groups` |
| [reference/25-script_tags.md](reference/25-script_tags.md) | スクリプトタグ | `GET /api/v1/script_tags/1`<br>`GET /api/v1/script_tags`<br>`PATCH /api/v1/script_tags/1`<br>`PATCH /api/v1/script_tags`<br>`POST /api/v1/script_tags`<br>`DELETE /api/v1/script_tags/1` |
| [reference/26-webhooks.md](reference/26-webhooks.md) | Webhook | `GET /api/v1/webhooks/0b1f1fc2-e567-4ce4-ac44-6d1856049a1a`<br>`GET /api/v1/webhooks`<br>`PATCH /api/v1/webhooks/0b1f1fc2-e567-4ce4-ac44-6d1856049a1a`<br>`POST /api/v1/webhooks`<br>`DELETE /api/v1/webhooks/139104dd-b020-4cb5-80a2-3cc9205a1166` |

## OpenAPI

[openapi/bcart-v1.yaml](openapi/bcart-v1.yaml) — OpenAPI 3.1。全リソース・全エンドポイント（公式の109件＋OAuthトークン発行）を収録。

- 生成元は公式の Postman コレクション（`https://docs.api.bcart.jp/api/collections/8793158/T1Dwbtbh?versionTag=latest`）。生成スクリプトは [tools/gen_openapi.py](tools/gen_openapi.py)。
- 認証は `bearerAuth` と `oauth2`（スコープ44種）。操作ごとに `<リソース>-read/write` を割り当て済み。
- `required` は付けていない（公式の「項目存在時必須」等の条件付き必須は各項目の description に記載）。
- レスポンススキーマはサンプルJSONからの推論を、公式の「レスポンス一覧」表で補ったもの。
- 検証: `openapi-spec-validator openapi/bcart-v1.yaml`
- 一括更新・登録の表（`product_sets[{{i}}][name]` 形式）は要素のキーに正規化している。
- 公式表の欠陥（`product_sets` POST の `stock_few` 行でKeyと名称のセルが結合）は生成時に補正している。
