# アクセストークンの取得

## パーソナルアクセストークン

詳細は[プライベートアプリ開発](https://api.bcart.jp/start/private_app)をご確認ください。

## OAuth2.0

先に[アプリストア アプリ開発](https://api.bcart.jp/start/app)をご確認ください。

#### 1 認可コード取得

まずはアプリ利用者に、アプリがBカートAPIを通して取得するデータのアクセス権について、確認と許可を得るための画面を表示する必要があります。下記のURLにパラメータを設定しリクエストしてください。

許可されることで、アクセストークンをリクエストする際に必要な認可コードが発行されます。

```
https://app.bcart.jp/oauth/authorize

 ```

| **パラメータ** | **説明** | **例** |
| --- | --- | --- |
| client_id | アプリの登録時に発行された「クライアントID」 | 95941eef-e310-4a9c-9b56-8bdf26ef8bdf |
| response_type | 固定値「code」を指定 | code |
| redirect_uri | アプリの登録時に設定した「リダイレクトURI」 | [https://example.app/callback](https://example.app/callback) |
| scope | アプリで使用するAPIへのアクセス権（スコープ一覧参照） | products-read products-write customers-read |
| state （任意） | ユーザー同一性検証用の任意の文字列。セットした内容をそのままレスポンスパラメータに含めて返却します。アプリ側で検証を行う場合はセットしてください（推奨） | 6202367c31f31 |

リクエスト例

```
https://app.bcart.jp/oauth/authorize?client_id=95941eef-e310-4a9c-9b56-8bdf26ef8bdf&response_type=code&redirect_uri=https://example.app/callback&scope=products-read%20products-write%20customers-read&state=6202367c31f31

 ```

リクエスト後、アプリ利用者に「許可」された場合は、「code」というクエリパラメータに認可コードが付与されたアプリの「リダイレクトURI」にリダイレクトされます。

※ 認可コードの有効期限は発行から10分間です。

```
https://example.app/callback?code=def50200ad47270…&state=6202367c31f31

 ```

認可ページで「キャンセル」された、または何かしらのエラーが起きた場合は、「error」というクエリパラメータにエラーの内容を表す文字列が付与されます。

```
https://example.app/callback?error=access_denied&state=6202367c31f31

 ```

#### 2 アクセストークン発行

次に、取得した認可コードを含むパラメータをセットして、以下のURLにアクセストークンをリクエストしてください。

```
https://app.bcart.jp/oauth/token

 ```

| パラメータ | 説明 | **例** |
| --- | --- | --- |
| grant_type | 固定値「authorization_code」を指定 | authorization_code |
| client_id | アプリの登録時に発行された「クライアントID | 95941eef-e310-4a9c-9b56-8bdf26ef8bdf |
| client_secret | アプリの登録時に発行された「クライアントシークレット」 | p2goTCrIoxdwfTAobFMwnQbQb0NCNFx1DKCPqSom |
| redirect_uri | アプリの登録時に設定した「リダイレクトURI」 | [https://example.app/callback](https://example.app/callback) |
| code | 先ほど取得した認可コード | 15aa7711e434c24d399d4766d76873fc40162ebf6d29e5b90933a27ff5deee19bb80fa5b68255dfa |

リクエストが成功すると、以下のようなJSONデータが返却されます。

```
{
    "token_type": "Bearer",
    "expires_in": 1209600,
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbG…（以降省略）",
    "refresh_token": "def502006bbe5a47fcf453…（以降省略）"
}

 ```

「access_token」には、アクセストークン、「refresh_token」には、アクセストークンを更新するためのリフレッシュトークンが含まれます。

「expires_in」には、アクセストークンが無効になるまでの秒数を含んでいます。アクセストークンの有効期限は14日間です。

リクエストが失敗した場合は下記のようなパラメータを持つエラー内容のJSONデータが返却されます。

```
{
    "error": "invalid_request",
    "error_description": "The request is missing a …",
    "hint": "Cannot decrypt the …",
    "message": "The request is missing a …"
}

 ```

#### 3 リフレッシュトークンによるアクセストークンの更新

取得したアクセストークンは有効期限があるため、有効期限が切れそう（切れた）場合は、アクセストークンと合わせて取得したリフレッシュトークン（refresh_token）を使って、新しいアクセストークンを再取得してください。リフレッシュトークンには有効期限はありません。

下記のURLにパラメータを設定しリクエストしてください。

```
https://app.bcart.jp/oauth/token

 ```

| パラメータ | 説明 | **例** |
| --- | --- | --- |
| grant_type | 固定値「refresh_token」を指定 | refresh_token |
| refresh_token | リフレッシュトークン | def502006bbe5… |
| client_id | アプリの登録時に発行された「クライアントID」 | 95941eef-e310-4a9c-9b56-8bdf26ef8bdf |
| client_secret | アプリの登録時に発行された「クライアントシークレット」 | p2goTCrIoxdwfTAobFMwnQbQb0NCNFx1DKCPqSom |

リクエストが成功すると、認可コードとの交換時と同じように以下のようなJSONデータが返却されます。

```
{
    "token_type": "Bearer",
    "expires_in": 1209600,
    "access_token": "eyJ0eXAiYasieQiLHIde…（以降省略）",
    "refresh_token": "def5020sde47fcf4dsad…（以降省略）"
}

 ```

リフレッシュトークンを使用したアクセストークン再発行時にも、新たなリフレッシュトークンが発行されますので、都度最新のリフレッシュトークンを使用して再発行を行ってください。

使用済みのリフレッシュトークンと、古いアクセストークンは再取得と同時に無効になります。

リクエストが失敗した場合は下記のようなパラメータを持つエラー内容のJSONデータが返却されます。

```
{
    "error": "invalid_request",
    "error_description": "The refresh token is invalid.",
    "hint": "Token …",
    "message": "The refresh token is invalid."
}

 ```
