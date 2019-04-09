class DBlist:
    def __init__(self, _host='localhost', _user='root', _password='0000', _db='menu', _charset='utf8'):
        try:
            import pymysql
        except ImportError:
            print("Please install pymysql\n"
                  "pip install pymysql\n")
            exit()

        try:
            self.conn = pymysql.connect(host=_host, user=_user, password=_password, db=_db, charset=_charset)
            self.curs = self.conn.cursor()
            sql = "select * from menu.menulist"
            self.curs.execute(sql)
            self.table_list = list(self.curs.fetchall())
        except pymysql.err.OperationalError as e:
            print(e)
            exit()

    def show_table(self):
        print(self.table_list)

    def get_item(self, _key):
        tmp_list = []
        for i in self.table_list:
            if _key in i[1]:
                tmp_list.append(i[2:])
        return tmp_list

    def get_cat(self):
        tmp = []
        for i in self.table_list:
            if not i[1][3:] in tmp:
                tmp.append(i[1][3:])
        return tmp
