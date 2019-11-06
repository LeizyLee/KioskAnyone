class SyncCursor:
    def __init__(self, _host='localhost', _user='root', _password='qwe123!!@@', _db='menu', _charset='utf8'):
        try:
            import pymysql

            self.conn = pymysql.connect(host=_host, user=_user, password=_password, db=_db, charset=_charset)
            self.cur = self.conn.cursor()
            sql = "select * from menu.menulist"
            self.cur.execute(sql)
            self.table_list = list(self.cur.fetchall())
        except ImportError as e:
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

    def ImageConvertToBinaryData(self, file_src):
        with open(file_src, 'rb') as file:
            binaryData = file.read()
        return binaryData

    def write_file(self, data, filename):
        # Convert binary data to proper format and write it on Hard Disk
        with open(filename, 'wb') as file:
            file.write(data)

    def deploy_image(self):
        print("Checking res Directory exist\n")
        import os

        if not os.path.isdir("./res"):
            print("Can't find res Directory...\nprocessing make res")
            os.mkdir('./res')
            os.mkdir('./res/korea')
            os.mkdir('./res/china')
            os.mkdir('./res/japan')
            os.mkdir('./res/userCat')
        elif not os.path.isdir('./res/korea') or not os.path.isdir('./res/china') or not os.path.isdir('./res/japan'):
            os.mkdir('./res/UserCat')
            os.mkdir('./res/korea')
            os.mkdir('./res/china')
            os.mkdir('./res/japan')
        else:
            print("Exist")
            return True
        print("Next step....\n")
        self.cur.execute("SELECT * FROM menu.menulist")

        #write_file(data, 저장 경로):
        print("Getting Image...")
        data = self.cur.fetchall()
        count = self.cur.rowcount
        num = 1
        for i in data:
            print(i[:-1])
            print(str("%0.1f"%float(num/count*100)) + '%...')
            num = num + 1
            dir_list = i[-2].split("\\")
            src = dir_list[-1]
            self.write_file(i[-1], src)
        print("Getting Image... Complete!")


    def getting_image(self, _loadingURL):
        self.cur.execute("SELECT * FROM menu.menulist")
        rc = self.cur.rowcount
        record = self.cur.fetchall()
        for i in record:
            #wirte_file(바이너리 데이터, 파일저장경로)
            print(_loadingURL+i[5].split('\\')[-1])
            self.write_file(i[6], _loadingURL+i[5].split('\\')[-1])

    def get_dir(self):
        import tkinter as tk
        import tkinter.filedialog as tf
        root = tk.Tk()
        root.withdraw()
        file_path = tf.askopenfilename()
        root.destroy()

        return file_path

    def sendSalesData(self, result):
        import datetime

        self.cur.execute("SELECT * FROM menu.salesstatics")
        row = self.cur.rowcount
        sql_insert_qurey = "INSERT INTO menu.salesstatics VALUES (%s, %s, %s, %s, %s)"
        for i in result:
            self.cur.execute(sql_insert_qurey, (str(row), str(i[0]), str(i[1]), str(i[2]), str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))))
            row = row + 1
        self.conn.commit()
