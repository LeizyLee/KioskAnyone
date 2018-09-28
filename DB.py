import pymysql

def get_item(_list, _key):
    return [i[2:4] for i in _list if _key in i]


conn = pymysql.connect(host='right.jbnu.ac.kr', user='', password='',db='',charset='utf8')

curs = conn.cursor()
sql = "select * from menulist"
curs.execute(sql)

rows = list(curs.fetchall())
print(type(rows))

conn.close()

print(get_item(rows, "Coffee"))
