# AIWorkShop202304

個人のM1 MacではChatGPTのモジュールがうまく動かなかったのでコンテナにして動作を確認した

## コンテナの内容

- Chat GPT API接続するRESTAPIを作成
- 金融に関するデータを取得するためのRESTAPIを作成

## 初期設定

ChatGPT API接続　
.envファイルをDataSourceAPI直下に作成してAPI_KEYを登録する

``` .env
#open api key
OPENAI_API_KEY=xxxxxxxxxxxxxx
```

金融に関するデータを取得
データソースによってはAPI_KEYの取得が必要なものがあるので適宜追加する

## 使い方

コンテナの起動方法

```
# コンテナの起動
$cd DataSourceAPI
$docker-compose build
$docker-compose up -d 

# sample request
$ curl -X POST localhost:8002/chatGPT -H "Content-Type: application/json" -d '{"role": "user", "content": "Hello!"}'

```

Dockerが起動していることが前提条件

APIにリクエストを投げる

- ChatGTPに質問を行う
`localhost:8002/chatGPT`

- FITraderのロールを設定したChatGTPに質問を行う
`localhost:8002/fitrader`

- FXTraderのロールを設定したChatGTPに質問を行う
`localhost:8002/fxtrader`

- 分類のモデルを設定したChatGTPに質問を行う
`localhost:8002/sentiment`


# test 用のコード
`chatGPT_test.py`
