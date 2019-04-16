def GetTranslatedText(text):
    import os
    import sys
    import json
    import urllib.request
    client_id = "g6s84wi18i"
    client_secret = "HyoA7eFbKvFe6VvW0pzlb2FVkyxPTvezxGg7dQjH"

    encText = urllib.request.quote(text)

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