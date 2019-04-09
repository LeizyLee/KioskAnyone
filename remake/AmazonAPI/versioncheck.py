import boto3
import json

if __name__ == '__main__':
    comprehend = boto3.client(service_name='comprehend', region_name='us-east-2')
    text = 'Thirteen wealthy parents, including actress Felicity Huffman, and one coach will plead guilty to using bribery and other forms of fraud as part of the college admissions scandal, federal prosecutors in Boston said on Monday.'

    # 언어 감지
    print('Calling DetectDominantLanguage')
    print(json.dumps(comprehend.detect_dominant_language(Text=text), sort_keys=True, indent=4))
    print("End of DetectDominantLanguage\n")

    # 언어 성향 분석석
    print('Calling DetectSentiment')
    print(json.dumps(comprehend.detect_sentiment(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
    print('End of DetectSentiment\n')

    # 문장 분석(주로 사용된 성분)
    print('Calling DetectKeyPhrases')
    print(json.dumps(comprehend.detect_key_phrases(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
    print('End of DetectKeyPhrases\n')

    """

    """