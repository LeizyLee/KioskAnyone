
def tts(string="반갑습니다 네이버"):
    import urllib.request
    client_id = "7u94xasjth"
    client_secret = "bHIvf1d9QbS8IBrUN9c6l0ImHN96f4zrQ0spNVYb"
    encText = urllib.request.quote(string)
    data = "speaker=mijin&speed=0&text=" + encText
    url = "https://naveropenapi.apigw.ntruss.com/voice/v1/tts"
    request = urllib.request.Request(url)
    request.add_header("X-NCP-APIGW-API-KEY-ID", client_id)
    request.add_header("X-NCP-APIGW-API-KEY", client_secret)
    response = urllib.request.urlopen(request, data=data.encode('utf-8'))
    rescode = response.getcode()
    if (rescode == 200):
        print("TTS mp3 저장")
        response_body = response.read()
        with open('tts.mp3', 'wb') as f:
            f.write(response_body)
    else:
        print("Error Code:" + rescode)
