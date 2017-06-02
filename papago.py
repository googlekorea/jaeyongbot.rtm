# -*- encoding: utf-8 -*-
import os
import sys
import json
import urllib.request

client_id = "dzeHmOOPgE7wGCxc29c3"
client_secret = "DeE630DkAJ"

encText = urllib.parse.quote("나 너 좋아하냐")

data = "source=ko&target=en&text=" + encText
url = "https://openapi.naver.com/v1/language/translate"

request = urllib.request.Request(url)

request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)

response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    json_dic = json.loads(response_body.decode('utf-8'))
    message_value = json_dic.get('message')
    result_value = message_value.get('result')
    translatedText = result_value.get('translatedText')
    print(translatedText)
else:
    print("Error Code:" + rescode)
