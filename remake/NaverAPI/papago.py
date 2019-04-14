def GetTranslatedText():
    import os
    import sys
    import json
    import urllib.request
    client_id = "g6s84wi18i"
    client_secret = "HyoA7eFbKvFe6VvW0pzlb2FVkyxPTvezxGg7dQjH"

    encText = urllib.request.quote("치킨을 먹었는데 치즈양념이랑 포테이토랑 파랑 양파랑 하나씩 먹어봤는데 맛있다. 얻어먹"
                                   "은 거라 가격은 모르겠지만 매콤한 거 좋아하면 치즈양념 먹고 달콤한거는 포테이토 "
                                   "먹는게 맛있다")

    data = "source=ko&target=en&text=" + encText
    url = "https://naveropenapi.apigw.ntruss.com/nmt/v1/translation"
    request = urllib.request.Request(url)
    request.add_header("X-NCP-APIGW-API-KEY-ID",client_id)
    request.add_header("X-NCP-APIGW-API-KEY",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()

    if(rescode==200):
        response_body = response.read()
        JSON_object = json.loads(response_body.decode("utf-8"))
        return JSON_object['message']['result']['translatedText']
    else:
        print("Error Code:" + rescode)
        return False