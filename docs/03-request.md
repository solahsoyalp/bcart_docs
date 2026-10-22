# リクエスト

### エンドポイント

BカートAPIはRESTの原則に基づき設計されています。エンドポイントと呼ばれる一意なURIに対してGET、PATCH、POSTといったHTTPメソッドでパラメータを送信することで、取得、更新、登録することが出来ます。  
エンドポイントのベースURIは下記になります。

```
{{api_url}}/api/v1/

 ```

- リクエストを行うエンドポイントはAPIを確認ください。
    
- GETリクエストではパラメータを指定することで絞り込みを行うことが出来ます。
    
- マルチバイト文字列を含む場合はURLエンコードする必要があります。
    

### リクエストヘッダ

#### GET (取得API)

{:access_token}には取得したアクセストークンを記述

```
Accept:application/json
Authorization:Bearer {:access_token}

 ```

#### PATCH (更新API)

{:access_token}には取得したアクセストークンを記述

```
Accept:application/json
Authorization:Bearer {:access_token}
Content-Type:application/json

 ```

※ Content-Typeはapplication/x-www-form-urlencodedでも指定可能です。

#### POST (登録API)

{:access_token}には取得したアクセストークンを記述

```
Accept:application/json
Authorization:Bearer {:access_token}
Content-Type:application/json

 ```

※ Content-Typeはapplication/x-www-form-urlencodedでも指定可能です。

### リクエストBODY

更新したい項目をリクエストBODYに指定して実行します。  
リクエストBODYに書かれたKEYの値のみ更新されます。

登録のリクエストではリクエストしなかったKEYはデフォルトの値で設定されます。

※KEYによっては必須になる場合があります。
