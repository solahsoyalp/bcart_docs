# レスポンス

### レスポンスヘッダ

| ヘッダー名 | 説明 |
| --- | --- |
| HTTPステータス | 成功時には200、それ以外はエラーコード |
| Date | 日付が返却される |
| X-RateLimit-Limit | 一定時間にアクセス可能な回数 |
| X-RateLimit-Remaining | 一定時間のアクセス回数 |
| Content-Length | レスポンスボディのバイト数 |
| Content-Type | レスポンスのメディアタイプ |

例

```
HTTP/1 200 OK
Date: Fri, 10 Feb 2017 09:23:28 GMT
X-RateLimit-Limit: 300
X-RateLimit-Remaining: 299
Strict-Transport-Security: max-age=315360000;
Content-Length: 899
Content-Type: application/json

 ```

### レスポンスボディ

レスポンスはJSON形式になります。

### エラーレスポンス

APIで正常に処理が行われなかった場合は下記のレスポンスが返ります。  
※事前告知の上、よりエラーを明確にする把握できるように仕様を変更する場合がございます。

#### パラメータの値が不正な場合

errorsのレスポンスが返り、不正なパラメータの結果を返します。

```
{
    "errors": [
        {
            "param1": [
                "param1には〇〇を指定してください。"
            ]
        }
    ]
}

 ```

#### APIの権限、API Keyが不正な場合

```
{
    "error": "Unauthenticated."
}

 ```

#### 存在しないAPIのURLを叩いた場合

```
{
    "error": "Authorization not exist."
}

 ```
