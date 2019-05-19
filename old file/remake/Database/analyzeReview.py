from remake.AmazonAPI import get_dentiment
import pymysql

conn = pymysql.connect(host='localhost', db='menu', charset='utf8', user='root', password='0000')
cur = conn.cursor()

cur.execute("SELECT * FROM review")
#data = cur.fetchall()
row = 1
data = [('MIXED', '0.99'),('MIXED', '0.79'),('POSITIVE', '1.00'),('POSITIVE', '0.93'),('NEGATIVE', '0.58')
        ,('POSITIVE', '0.95'),('MIXED', '0.76'),('NEUTRAL', '0.47'),('NEGATIVE', '0.86'),('NEUTRAL', '0.88')]
#result_tuple = []

for i in data:
    if i[0] == "MIXED":
        result_tuple = ("복합", str('%1.f'%(float(i[1])*100))+'%', row)
    elif i[0] == "POSITIVE":
        result_tuple = ("긍정", str('%1.f'%(float(i[1])*100))+'%', row)
    elif i[0] == "NEGATIVE":
        result_tuple = ("부정", str('%1.f'%(float(i[1])*100))+'%', row)
    else:
        result_tuple = ("중립", str('%1.f'%(float(i[1])*100))+'%', row)

    print(result_tuple)
    #UPDATE menu.review SET 성향='복합', 수치='87%' WHERE id_num=1
    cur.execute("UPDATE menu.review SET 성향=%s, 수치=%s WHERE id_num=%s", (result_tuple))
    row = row + 1

conn.commit()

