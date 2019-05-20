from old_file.remake.AmazonAPI import get_dentiment
import pymysql

conn = pymysql.connect(host='localhost', db='menu', charset='utf8', user='root', password='0000')
cur = conn.cursor()

cur.execute("SELECT * FROM review")
#data = cur.fetchall()
row = cur.rowcount + 1
data = ['군산에서 초밥드시려면 여기만한 곳이 없는 것 같습니다. 가격은 싸지 않지만 여러 초밥을 맛 볼 수 있습니다',
        '맛으로는 왠만한 초밥집을 따라올수가 없다. 기본 초밥류가 굉장히 훌륭하며 특수 초밥류는 그저그렇지만 다양하여'
        ' 취향에 맞춰서 먹기좋음. 다만 대기가 일상적으로 있으니 기다리기 싫다면 고려해보시길.',
        '가격은 비싸다고 느껴지지만 후회없는 집, 횟감이 신선해서 진짜맛있습니다. 개인적으로는 타코와사비초밥이 시작과'
        ' 끝을 하면 입가심해서 좋습니다',
        '비싸고 맛있어요. 먹는동안 가격 생각 안납니다. 한번도 안 온 사람은 있어도 한번만 온 사람은 없을 것 같네요.',
        '음식 완벽함! 런치코스 8코스 먹었는데 비싸다는 생각 안들게함. 아뮤즈부쉬로 나온 굴튀김, 캐비어,전복,문어,'
        '트러플비빔밥,은대구,갈비,수정과,대추블랑까지 플레이팅 너무 예쁘고 종업원분이 설명 자세하 해 주심,',
        '깔끔한 인테리어, 식기,음식, 디저트까지 만족입니다',
        '별로입니다.. 어떻게 미슐랭 2스타인지 모르겠네요.... ',
        '완성도 높은 퓨전 한식을 먹을 수 있다.',
        '현대적 한식이지만 전통의 맛을 지키는 힘이 있다. 비싼 가격 받을만한 곳',
        '임금님 수라상에 오를 듯한 정성 가득한 고급 음식들 대접받고 온 기분이예요',
        '전체적으로 서비스 좋고 음식 맛도 좋았지만 떡갈비는 그냥 늘 먹던 떡갈비맛 별로 특별할게 없었습니다',
        '가격에 비해 맛은 뻔한맛이네요. 한번정도 가볼만합니다.',
        '맛있네요!  음식도 빨리 나오고. 다만 짬뽕이 불맛이 좀 심해서 제취향은 아닌듯.',
        '홀 여직원분들 서비스 마인드가 참 좋음.',
        '짬뽕 매우 맛있음 별한개는 한번 더 가보고 다른매뉴먹고 만족하면 더 채울것',
        '주차장 진입로가 어려웠습니다  음식은 매우 좋았습니다',
        '볶음밥이 지나치게 기대 이하인 중국집이라... 밥은 설익은 것 같고, 파기름을 베이스로 한 것이 아니라 파볶음밥을'
        ' 먹는 듯한 풍미에 간도 전혀 안 되어 있는 듯한 느낌. 중국집 최악의 볶음밥',
        ]
#result_tuple = []

for i in data:
    tmp = get_dentiment.sentiment(i)
    if tmp[0] == "MIXED":
        result_tuple = (row, i, "복합", str('%1.f'%(float(tmp[1])*100))+'%')
    elif tmp[0] == "POSITIVE":
        result_tuple = (row, i, "긍정", str('%1.f'%(float(tmp[1])*100))+'%')
    elif tmp[0] == "NEGATIVE":
        result_tuple = (row, i, "부정", str('%1.f'%(float(tmp[1])*100))+'%')
    else:
        result_tuple = (row, i, "중립", str('%1.f'%(float(tmp[1])*100))+'%')
    print(result_tuple)
    #UPDATE menu.review SET 성향='복합', 수치='87%' WHERE id_num=1
    #INSERT INTO menu.menulist VALUES (%s, %s, %s, %s, %s, %s, %s)
    cur.execute("INSERT INTO menu.review VALUES (%s, %s, %s, %s)", (result_tuple))
    row = row + 1
conn.commit()

