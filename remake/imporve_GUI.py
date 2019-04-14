# Use Tkinter for python 2, tkinter for python 3
from remake import DB
import tkinter
from tkinter import ttk
from PIL import Image, ImageTk

# ===============================================================================
# DB 접속
# ===============================================================================
db = DB.DBlist()
data = db.table_list
menuData = [i[1:] for i in data]
src = [i[-2] for i in menuData]
src = [i.replace('\\', '/') for i in src]
print(src)
#temp = [i.replace('\\', '/') for i in [j[-1] for j in [k[1:] for k in data]]]
#print(temp)

# 이미지 리사이징 함수
#===============================================================================
def resized_img(src):
    tmp = Image.open(src)
    tmp = tmp.convert("RGB")
    tmp2 = tmp.resize((200, 200))
    return (tmp2)

class MainApplication(tkinter.Frame):
    def __init__(self, parent, *args, **kwargs):
        tkinter.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # ===============================================================================
        # 프레임 생성
        # ===============================================================================
        UpFrame = ttk.Frame(self)
        UpFrame.grid(column=0, row=0)

        DownFrame = ttk.Frame(self)
        DownFrame.grid(column=0, row=1)

        MidFrame = ttk.Frame(self)
        MidFrame.grid(column=0, row=2)

        # 위젯 컨테이너
        Up_left = ttk.Frame(UpFrame)
        Up_right = ttk.Frame(UpFrame)
        Up_center = ttk.Frame(UpFrame)
        Up_left.grid(column=0, row=0)
        Up_center.grid(column=1, row=0)
        Up_right.grid(column=2, row=0)

        # ===============================================================================
        # 상단 이미지 라벨 생성
        # ===============================================================================
        src = 'C:\\Users\\User\\Desktop\\image\\Kioskimg'.replace('\\', '/')
        china_img = ImageTk.PhotoImage(Image.open(src + '/china.png'))
        left_label = tkinter.Label(Up_left, image=china_img)
        left_label.grid(column=0, row=0)

        korea_img = ImageTk.PhotoImage(Image.open(src + '/korea.png'))
        center_label = tkinter.Label(Up_center, image=korea_img)
        center_label.grid(column=1, row=0)

        japan_img = ImageTk.PhotoImage(Image.open(src + '/japan.png'))
        right_label = tkinter.Label(Up_right, image=japan_img)
        right_label.grid(column=2, row=0)

        # ===============================================================================
        #  버튼 생성
        # ===============================================================================
        Lbtn = tkinter.Button(DownFrame, command=self.left_action)
        Lbtn.config(text="  중식  ", font=('', 15))
        Lbtn.grid(column=0, row=0)
        Lbtn.grid_configure(padx=0, pady=4)


        Rbtn = tkinter.Button(DownFrame, command=self.right_action)
        Rbtn.config(text="  일식  ", font=('', 15))
        Rbtn.grid(column=2, row=0)
        Rbtn.grid_configure(padx=0, pady=4)



        button = tkinter.Button(DownFrame, command=self.center_action)
        button.config(text="  한식  ", font=('', 15))
        button.grid(column=1, row=0)
        button.grid_configure(padx=125, pady=4)

        User_button = tkinter.Button(DownFrame, text="카테고리 입력", command=lambda: self.UserCategory())
        User_button.grid(column=1, row=1)

    # ===============================================================================
    #  버튼 이벤트
    # ===============================================================================
    def left_action(self):
        pass

    def right_action(self):
        pass

    def center_action(self):
        pass

    # 유저 카테고리 윈도우
    def make_subMain(self):
        root = tkinter.Toplevel(self.parent)
        app = UserCat(root)

    def __del__(self):
        return


class UserCat:
    def __init__(self, root):
        self.root = root
        self.root = tkinter.Tk()
        self.mighty = ttk.Frame(self.root)
        self.root.title("취향 조사")
        self.root.geometry("450x720")
        self.root.resizable(True, True)
        self.mighty.pack(fill=None, expand=True)

        self.UpFrame = ttk.Frame(self.mighty)
        self.DownFrame = ttk.Frame(self.mighty)
        self.UpFrame.grid(row=0)
        self.DownFrame.grid(row=1)

        self.checkboxVar = [tkinter.IntVar() for i in range(0, 6)]
        self.checklist = ['밥', '면', '국', '튀김', '매운', '고기']
        self.CheckBox_list = [ttk.Checkbutton(self.UpFrame, text="menu" + str(i), variable=self.checkboxVar[i]) for i in range(0, 6)]
        self.label_list = [ttk.Label(self.UpFrame, text="label__" + str(i)) for i in range(0, 6)]

        self.CheckBox_list[0].grid(column=0, row=1)
        self.CheckBox_list[0].config(text="밥")
        self.CheckBox_list[1].config(text="면")
        self.CheckBox_list[1].grid(column=1, row=1)
        self.CheckBox_list[2].config(text="국")
        self.CheckBox_list[2].grid(column=0, row=3)
        self.CheckBox_list[3].grid(column=1, row=3)
        self.CheckBox_list[3].config(text="튀김")
        self.CheckBox_list[4].grid(column=0, row=5)
        self.CheckBox_list[4].config(text="매운")
        self.CheckBox_list[5].grid(column=1, row=5)
        self.CheckBox_list[5].config(text="고기")

        self.img = [ImageTk.PhotoImage(resized_img('C:/Users/User/Desktop/image/userCat/' + str(i + 1) + '.jpg')) for i
                    in range(0, 6)]
        for i in range(0, 6):
            self.label_list[i].config(image=self.img[i])

        self.label_list[0].grid(column=0, row=0)
        self.label_list[1].grid(column=1, row=0)
        self.label_list[2].grid(column=0, row=2)
        self.label_list[3].grid(column=1, row=2)
        self.label_list[4].grid(column=0, row=4)
        self.label_list[5].grid(column=1, row=4)

        self.SelectButton = tkinter.Button(self.DownFrame, text="다 골랐다면 눌러주세요!",
                                           command=lambda: self.button_press(menuData)).grid(column=0, row=0)

        self.MicBtn = tkinter.Button(self.DownFrame, text="취향 조사",
                                     command=lambda: self.UsingGCS(menuData)).grid(column=0, row=1)

    def button_press(self, menuData):
        userData = [i[2:3] for i in menuData]
        sData = [i[0] for i in userData]
        tmp = [i.get() for i in self.checkboxVar]
        text = []
        textNum = 0
        result = []

        for i in range(0,6):
            if tmp[i] == 1:
                text.append(self.checklist[i])
        print(text)
        for i in range(0, len(menuData)):
            check = 0
            for j in text:
                if j in sData[i]:
                    check = check + 1
            if check == len(text):
                result.append(menuData[i])
        print("====================== 결과 =========================")
        print(result)
        self.show_result(result)

    def find_tag(self, text):
        checklist = ['밥', '면', '국', '튀김', '매운', '고기']
        result = []
        if '밥' in text:
            result.append('밥')
        if '면' in text:
            result.append('면')
        if '국' in text:
            result.append('국')
        if '튀김' in text:
            result.append('튀김')
        if '고기' in text:
            result.append('고기')
        if '매운' in text or '맵고' in text:
            result.append('매운')
        return result

    def UsingGCS(self, menuData):
        userData = [i[2:3] for i in menuData]
        sData = [i[0] for i in userData]
        textNum = 0
        result = []
        tmp = []

        from remake.GoogleCloud import googleCloudSpeech, sound_recorder

        getUserOpinion = sound_recorder.getWaveFile()
        getUserOpinion.run()
        tmp = googleCloudSpeech.run_quickstart()
        text = self.find_tag(tmp)
        if text == []:
            print("원하는 결과가 없습니다.")
        else:
            print(text)
            for i in range(0, len(menuData)):
                check = 0
                for j in text:
                    if j in sData[i]:
                        check = check + 1
                if check == len(text):
                    result.append(menuData[i])
            print("====================== 결과 =========================")
            print(result)
            try:
                self.show_result(result)
            except IndexError as e:
                print("일치하는 결과가 없습니다~")

    def show_result(self, result):
        sub_main = tkinter.Toplevel(self.root)
        sub_app = Demo3(sub_main, result)

    def __del__(self, master):
        self.root.destroy()

class Demo3:
    def __init__(self, sub_main, result):
        self.root = sub_main

        mighty = ttk.Frame(self.root)
        root.title("결과 화면")
        root.resizable(True, True)
        mighty.pack(fill=None, expand=True)

        list_num = len(result)
        src = [i[-2].replace('\\','/') for i in result]
        print(src[0])
        Imgsrc = [ImageTk.PhotoImage(resized_img(src[i])) for i in range(0,list_num)]
        label_list = [tkinter.Label(mighty, image=Imgsrc[i]) for i in range(0, list_num)]
        row = 0
        for i in range(0, list_num):
            if i%2 == 0:
                row = row + 1
            label_list[i].grid(column=i%2, row=row)
        print(row)
        root.geometry(str(450)+'x'+str(row*200+50))
        result = ''

    def __del__(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("취향 조사")
    root.geometry("450x720")
    root.resizable(True, True)
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
