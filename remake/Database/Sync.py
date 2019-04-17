class SyncCursor:
    def __init__(self, _host, _db, _user, _password):
        import pymysql
        import os

        # id_num(INT), image(LONG BLOB), image_name(VARCHAR 45), dir(VARCHAR 80)
        self.conn = pymysql.connect(host=_host, db=_db, charset='utf8', user=_user, password=_password)
        self.cur = self.conn.cursor()
        self.getDB = _db
        self.getHost = _host
        self.getUser = _user

    def ImageConvertToBinaryData(self, file_src):
        with open(file_src, 'rb') as file:
            binaryData = file.read()
        return binaryData

    def write_file(self, data, filename):
        # Convert binary data to proper format and write it on Hard Disk
        with open(filename, 'wb') as file:
            file.write(data)

    def insert_data(self, img_src):
        sql_insert_blob_query = "INSERT INTO menu.menulist VALUES (%s, %s, %s, %s, %s, %s, %s)"

        image = self.ImageConvertToBinaryData(img_src)

        insert_blob_tuple = (1, image, img_src.split('/')[-1], img_src)
        print(insert_blob_tuple)
        result = self.cur.execute(sql_insert_blob_query, insert_blob_tuple)
        self.conn.commit()

    def insert_PickImage(self, _flag, _name, _property, _price):
        dir = self.get_dir()

        self.cur.execute("SELECT * FROM menu.menulist WHERE local='korea'")
        id_num = self.cur.fetchall()
        print(id_num)
        country = 'korea' if _flag == 1 else ('china' if _flag == 2 else 'japan')
        #sql_insert_blob_query = "INSERT INTO menu.menulist VALUES (%s, %s, %s, %s, %s, %s, %s)"

        #image = self.ImageConvertToBinaryData(dir)

        insert_blob_tuple = ()

    def deploy_image(self):
        print("Checking res Directory exist\n")
        if not os.path.isdir("C:/res"):
            print("Can't find res Directory...\nprocessing make res")
            os.mkdir('C:/res')
            os.mkdir('C:/res/korea')
            os.mkdir('C:/res/china')
            os.mkdir('C:/res/japan')
        elif not os.path.isdir('C:/res/korea') or not os.path.isdir('C:/res/china') or not os.path.isdir('C:/res/japan'):
            os.mkdir('C:/res/korea')
            os.mkdir('C:/res/china')
            os.mkdir('C:/res/japan')
        else:
            print("already exist")
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

    def temp(self):
        self.cur.execute("SELECT * FROM menu.menulist")
        record = self.cur.fetchall()
        for i in record:
            print(i[-2])
        dic = {i[2]: i[-2] for i in record}
        print(dic)
    def __del__(self):
        self.cur.close()
        self.conn.close()

if __name__ == "__main__":
    import os

    src = 'C:/Users/User/Desktop/image'
    #dir = os.listdir('C:/Users/User/Desktop/image')
    #item = [src+'/'+i for i in dir if '.jpg' in i or '.png' in i] #'C:/Users/User/Desktop/image/doge.png'
    dbsync = SyncCursor('202.31.147.28', 'menu', 'admin', 'qwe123!!@@')
    #dbsync.insert_PickImage(1, '참치찌개', '밥, 기름, 국, 매운, 찌개', 4000)
    #dbsync.getting_image('C:/res/')
    #print(dbsync.get_dir())
    dbsync.deploy_image()
    """
    print(os.path.isdir(src+'/Kioskimg'))
    print(os.getcwd().replace('\\','/'))

    if not os.path.isdir(os.getcwd().replace('\\','/') + '/res'):
        print("없음")
        os.mkdir(os.getcwd().replace('\\','/') + '/res')
        print("글서 만듬")
    else:
        print("있음")
    dbsync.getting_image()
    """

