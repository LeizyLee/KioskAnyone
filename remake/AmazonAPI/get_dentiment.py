def sentiment(_text):
    import boto3
    import json
    from remake.NaverAPI.papago import GetTranslatedText as tt

    comprehend = boto3.client(service_name='comprehend', region_name='us-east-2')
    text = tt(_text)
    # 언어 감지
    """
    print('Calling DetectDominantLanguage')
    print(json.dumps(comprehend.detect_dominant_language(Text=text), sort_keys=True, indent=4))
    print("End of DetectDominantLanguage\n")
    """

    # 언어 성향 분석석
    # print('Calling DetectSentiment')
    sentiment = json.dumps(comprehend.detect_sentiment(Text=text, LanguageCode='en'), sort_keys=True, indent=4)
    temp = json.loads(sentiment)
    # print(sentiment)
    # print('End of DetectSentiment\n')

    # 문장 분석(주로 사용된 성분)
    # print('Calling DetectKeyPhrases')
    # key_phrases = json.dumps(comprehend.detect_key_phrases(Text=text, LanguageCode='en'), sort_keys=True, indent=4)
    # print(key_phrases)
    # print('End of DetectKeyPhrases\n')

    return temp['Sentiment'], '%0.2f' % temp['SentimentScore'][temp['Sentiment'].title()]

if __name__=='__main__':
    sentiment("치킨을 먹었는데 치즈양념이랑 포테이토랑 파랑 양파랑 하나씩 먹어봤는데 맛있다. 얻어먹"
              "은 거라 가격은 모르겠지만 매콤한 거 좋아하면 치즈양념 먹고 달콤한거는 포테이토 "
              "먹는게 맛있다")
