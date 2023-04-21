import requests
import json


base_url = "http://127.0.0.1:8002"

fred_url =  base_url + "/fred"
quote_url = base_url + "/avquote"
timeserise_url = base_url + "/avtimeseries"

#POST先URL
chatGPT_url = base_url + "/chatGPT"

chatGPTfitrader_url = base_url + "/fitrader"
chatGPTfxtrader_url = base_url + "/fxtrader"
chatGPTsentiment_url= base_url + "/sentiment"

def get_dict_data(url, symbol) :
    result = ""

    try :
        payload = {
            "symbol": symbol
        }

        #GET送信
        response = requests.get(
            url,
            params = payload    #dataを指定する
            )

        res_data = response.json()
        print(type(res_data))
        result = json.dumps(res_data)
        #print(result)
    except Exception as e:
        print(e)

    return result

def get_str_data(url, symbol) :

    result = ""

    try :
        payload = {
            "symbol": symbol
        }

        #GET送信
        response = requests.get(
            url,
            params = payload    #dataを指定する
            )

        res_data = response.json()
        print(type(res_data))
        result = res_data
        #print(result)
    except Exception as e:
        print(e)

    return result

def get_historical_data(url, symbol, start, end) :
    result = ""

    try :
        payload = {
            "symbol": symbol,
            "start": start,
            "end": end
        }

        #GET送信
        response = requests.get(
            url,
            params = payload    #dataを指定する
            )

        res_data = response.json()
        print(type(res_data))
        result = json.dumps(res_data)
        print(result)
    except Exception as e:
        print(e)

    return result

def ask_chatGPT(question) :

    answer = ""
    try :

        #JSON形式のデータ
        json_data = {
            "role": "user",
            "content": question
        }

        #POST送信
        response = requests.post(
            chatGPT_url,
            data = json.dumps(json_data)    #dataを指定する
            )

        res_data = response.json()

        choices = res_data.get('choices')
        answer = choices[0].get('message').get('content')

    except Exception as e:
        print(e)
    return answer

def ask_chatGPTFITrader(question) :

    try :
        #JSON形式のデータ
        json_data = {
            "role": "user",
            "content": question
        }

        #POST送信
        response = requests.post(
            chatGPTfitrader_url,
            data =  json.dumps(json_data)    #dataを指定する
            )

        res_data = response.json()

        choices = res_data.get('choices')
        answer = choices[0].get('message').get('content')

    except Exception as e:
        print(e)

    return answer

def ask_chatGPTFXtrader(question) :

    try :

        #JSON形式のデータ
        json_data = {
            "role": "user",
            "content": question
        }

        #POST送信
        response = requests.post(
            chatGPTfxtrader_url,
            data =  json.dumps(json_data)    #dataを指定する
            )

        res_data = response.json()

        choices = res_data.get('choices')
        answer = choices[0].get('message').get('content')

    except Exception as e:
        print(e)

    return answer

def ask_chatGPTSentiment(question) :

    try :
        #JSON形式のデータ
        json_data = {
            "role": "user",
            "content": question
        }
        #POST送信
        response = requests.post(
            chatGPTsentiment_url,
            data =json.dumps(json_data)   #dataを指定する
            )

        res_data = response.json()

        choices = res_data.get('choices')
        answer = choices[0].get('text')

    except Exception as e:
        print(e)

    return answer

def main() :

    question = "Hello"
    historical = ""

    print("--------------------------------------------")
    # # 「株式」
    # #historical += get_dict_data(fred_url, "DJIA")
    # #historical += get_dict_data(fred_url, "SP500")
    # #historical += get_dict_data(fred_url, "NASDAQ100")
    # #historical += get_dict_data(fred_url, "NIKKEI225")

    # # 「金利」
    # #historical += get_dict_data(fred_url, "DGS10")
    # #historical += get_dict_data(fred_url, "GS10")
    # #historical += get_dict_data(fred_url, "T10Y3M")
    # #historical += get_dict_data(fred_url, "T10Y2Y")
    # #historical += get_dict_data(fred_url, "DFEDTARU")
    # #historical += get_dict_data(fred_url, "DFEDTARL")
    # #historical += get_dict_data(fred_url, "DFF")
    # #historical += get_dict_data(fred_url, "IRLTLT01JPM156N")
    # historical += get_dict_data(fred_url, "IRLTLT01JPM156N")
    # # 「経済指標」
    # historical += get_dict_data(fred_url, "PAYEMS")
    # #historical += get_dict_data(fred_url, "UNRATE")
    # #historical += get_dict_data(fred_url, "A191RL1Q225SBEA")
    # #historical += get_dict_data(fred_url, "GDP")
    # #historical += get_dict_data(fred_url, "GDPC1")
    # #historical += get_dict_data(fred_url, "CPALTT01USM659N")
    # #historical += get_dict_data(fred_url, "ICSA")
    # historical += get_dict_data(fred_url, "JPNNGDP")
    # # 「貿易」
    # historical += get_dict_data(fred_url, "EXPJP")
    # historical += get_dict_data(fred_url, "IMPJP")
    # #historical += get_dict_data(fred_url, "XTEXVA01JPM667S")
    # #historical += get_dict_data(fred_url, "XTIMVA01JPM667S")
    # # 「その他」
    # #historical += get_dict_data(fred_url, "M2REAL")

    # question = historical + " の相関はありますか？"
    # print("question:" + question)
    # answer =  ask_chatGPT(question)
    # print("answer:" + answer)

    print("--------------------------------------------")
    print("sentiment")
    question = "以下の言葉を肯定か否定か評価してください:\n\n1. \"円が強い\"\n2. \"円が足踏み\"\n3. \"回復基調\"\n4. \"底堅い\"\n5. \"緩やかな\"\n6. \"弱含み\"\n7. \"継続して注視\"\n\n言葉の評価:"
    #question = "Classify the sentiment in these tweets:\n\n1. \"I can't stand homework\"\n2. \"This sucks. I'm bored 😠\"\n3. \"I can't wait for Halloween!!!\"\n4. \"My cat is adorable ❤️❤️\"\n5. \"I hate chocolate\"\n\nTweet sentiment ratings:"
    print("question:" + question)
    answer =  ask_chatGPTSentiment(question)
    print("answer:" + answer)

    # print("--------------------------------------------")
    # quote1 = get_str_data(quote_url, "ETH/USD")
    # quote2 = get_str_data(quote_url, "ETH/JPY")
    # quote3 = get_str_data(quote_url, "USD/JPY")

    # print("--------------------------------------------")
    # question = quote1 +  " " + quote2 + " " + quote3 + " いつ円高になりますか?"
    # print("question:" + question)
    # print("--------------------------------------------")
    # print("ask chatGPT")
    # answer =  ask_chatGPT(question)
    # print("answer:" + answer)
    # print("--------------------------------------------")
    # print("ask chatGPTFITrader")
    # answer =  ask_chatGPTFITrader(question )
    # print("answer:" + answer)
    # print("--------------------------------------------")
    # print("ask chatGPTFXtrader")
    # answer =  ask_chatGPTFXtrader(question )
    # print("answer:" + answer)
    # print("===========================================")

    print("===========================================")
    question = "100ドルををできるだけたくさん増やすにはどうしたらいいですか？"
    print("question:" + question)
    print("--------------------------------------------")
    print("ask chatGPT")
    answer =  ask_chatGPT(question)
    print("answer:" + answer)
    print("--------------------------------------------")
    print("ask chatGPTFITrader")
    answer =  ask_chatGPTFITrader(question)
    print("answer:" + answer)
    print("--------------------------------------------")
    print("ask chatGPTFXtrader")
    answer =  ask_chatGPTFXtrader(question)
    copy_answer = answer
    print("answer:" + answer)
    print("===========================================")

    # print("===========================================")
    # question = "日本国債の金利が上昇した場合の相場感をポジティブかネガティブで教えてください"
    # print("question:" + question)
    # print("--------------------------------------------")
    # print("ask chatGPT")
    # answer =  ask_chatGPT(question)
    # print("answer:" + answer)
    # print("--------------------------------------------")
    # print("ask chatGPTFITrader")
    # answer =  ask_chatGPTFITrader(question)
    # print("answer:" + answer)
    # print("--------------------------------------------")
    # print("ask chatGPTFXtrader")
    # answer =  ask_chatGPTFXtrader(question)
    # copy_answer = answer
    # print("answer:" + answer)
    # print("===========================================")

    # print("--------------------------------------------")
    # print("sentiment")
    # question = "以下の言葉を肯定か否定か評価してください:\n\n" + answer.replace("。", "\n").replace("、","\n") + "\n\n言葉の評価:"
    # print("question:" + question)
    # answer =  ask_chatGPTSentiment(question)
    # print("answer:" + answer)
    # print("--------------------------------------------")
    # print("sentiment")
    # question = "以下の言葉を肯定か否定か評価してください:\n\n"
    # i = 1
    # for line in copy_answer.split("。") :
    #     question = question + str(i) + ". " + line + "\n"
    #     i = i + 1
    # question = question + "\n\n言葉の評価:"
    # print("question:" + question)
    # answer =  ask_chatGPTSentiment(question)
    # print("answer:" + answer)


if __name__ == '__main__':

    blue= '\033[34m'
    green= '\033[32m'
    red = '\033[31m'
    bold = '\033[1m'
    reset = '\033[0m'

    while True:
        question = input(bold+blue+"Enter a prompt (or 'q'): "+reset+'\n')

        if question.lower() == 'q':
            break

        answer =  ask_chatGPT(question)
        print(bold+green+answer+reset, end = "\n")


    main()
