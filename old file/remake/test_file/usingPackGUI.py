# Use Tkinter for python 2, tkinter for python 3
from remake import DB
import tkinter
from tkinter import ttk
from tkinter import scrolledtext
from PIL import Image, ImageTk
import threading



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

class MainApplication(tkinter.Frame, threading.Thread):
    def __init__(self, parent, *args, **kwargs):
        threading.Thread.__init__(self)
        self.daemon = True
        self.start()
        tkinter.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.modeNum = 0
        self.listNum = 0
        self.Lnum, self.Mnum, self.Rnum = 0, 0, 1
        self.menu_control = []
        self.result_menu = []

        # ===============================================================================
        # 프레임 생성
        # ===============================================================================
        self.leftFrame = ttk.Frame(self)
        self.leftFrame.pack(side='left')

        self.RightFrame = ttk.Frame(self)
        self.RightFrame.pack(side='right')

        self.UpFrame = ttk.Frame(self.leftFrame)
        self.UpFrame.pack(side='top')

        self.DownFrame = ttk.Frame(self.leftFrame)
        self.DownFrame.pack(side='bottom')

        # ===============================================================================
        #   위젯 프레임
        # ===============================================================================
        self.left_widget = ttk.Frame(self.UpFrame)
        self.left_widget.pack(side='left')

        self.middle_widget = ttk.Frame(self.UpFrame)
        self.middle_widget.pack(side='left')

        self.right_widget = ttk.Frame(self.UpFrame)
        self.right_widget.pack(side='left')

        # ===============================================================================
        #   리스트 박스 생성
        # ===============================================================================
        """
        self.scr_w = 28
        self.scr_h = 24
        self.scr = scrolledtext.ScrolledText(self.RightFrame, width=self.scr_w, height=self.scr_h, wrap=tkinter.WORD)
        self.scr.grid(column=3,row=3)
        # scrolledtext.scrolledText(self.mighty, width=self.scr_w, height=self.scr_h, wrap=tk.WORD)
        """
        self.listbox = tkinter.Listbox(self.RightFrame, width=28, height=18, relief='solid')
        self.listbox.pack(side='right')


        # ===============================================================================
        # 상단 이미지 라벨 생성
        # ===============================================================================
        src = 'C:\\Users\\User\\Desktop\\image\\Kioskimg'.replace('\\', '/')
        self.images = {}
        self.images['china'] = ImageTk.PhotoImage(resized_img('C:/Users/User/Desktop/image/Kioskimg/china.png'))
        self.images['korea'] = ImageTk.PhotoImage(resized_img('C:/Users/User/Desktop/image/Kioskimg/korea.png'))
        self.images['japan'] = ImageTk.PhotoImage(resized_img('C:/Users/User/Desktop/image/Kioskimg/japan.png'))
        self.KorData = [[i[0], i[2], i[3], i[4], ImageTk.PhotoImage(resized_img(i[5]))] for i in data if i[1] == 'korea']
        self.JapData = [[i[0], i[2], i[3], i[4], ImageTk.PhotoImage(resized_img(i[5]))] for i in data if i[1] == 'japan']
        self.ChiData = [[i[0], i[2], i[3], i[4], ImageTk.PhotoImage(resized_img(i[5]))] for i in data if i[1] == 'china']
        # Data = 번호, 이름, 속성, 가격, 이미지 객체

        print(self.KorData[-1])
        # list(list[0].values) = 경로, list(list[0].keys()) = 이름
        # 그럼 list = [ImageTk.PhotoImage(resized_img(list(i.values())[0])) for i in KorImages]
        # ====> 레퍼런스를 유지한 이미지 객체 생성 완료료

        self.left_label = tkinter.Label(self.left_widget, image=self.images['china'])
        self.left_label.pack(side='top')

        self.center_label = tkinter.Label(self.middle_widget, image=self.images['korea'])
        self.center_label.pack(side='top')

        self.right_label = tkinter.Label(self.right_widget, image=self.images['japan'])
        self.right_label.pack(side='top')

        # ===============================================================================
        #   메뉴 정보 라벨
        # ===============================================================================
        self.left_info = tkinter.Label(self.left_widget)
        self.left_info.pack(side='bottom', fill='x')

        self.mid_info = tkinter.Label(self.middle_widget)
        self.mid_info.pack(side='bottom', fill='x')

        self.right_info = tkinter.Label(self.right_widget)
        self.right_info.pack(side='bottom', fill='x')

        # ===============================================================================
        #  버튼 생성
        # ===============================================================================
        self.Lbtn = tkinter.Button(self.DownFrame, command=self.left_action)
        self.Lbtn.config(text="  중식  ", font=('', 15))

        self.Rbtn = tkinter.Button(self.DownFrame, command=self.right_action)
        self.Rbtn.config(text="  일식  ", font=('', 15))

        self.button = tkinter.Button(self.DownFrame, command=self.center_action)
        self.button.config(text="  한식  ", font=('', 15))

        self.User_button = tkinter.Button(self.DownFrame, text="카테고리 입력", command=lambda: self.make_subMain())

        self.BackBtn = tkinter.Button(self.DownFrame, text="  뒤로  ", command=lambda: self.back_event(), font=('', 12))

        self.left_info.config(text="나는 오늘 살찌고싶다\n기름진 최강중식")
        self.mid_info.config(text="정갈한 한식\n고향맛 한식")
        self.right_info.config(text="난 비린맛따윈 모른다\n바다향 일식")

        self.button.pack(side='top', anchor='n', fill='both')
        self.Lbtn.pack(side='left', anchor='nw', fill='both')
        self.BackBtn.pack(side='top', anchor='w', fill='both')
        self.Rbtn.pack(side='right', anchor='ne', fill='both')

        self.User_button.pack(side='top', anchor='s', fill='both')




    # ===============================================================================
    #  버튼 이벤트
    # ===============================================================================
    def move_left(self):
        if self.Lnum == 0:
            self.Lnum = len(self.menu_control) - 1
            self.Rnum = 1
            self.Mnum = 0
        else:
            self.Rnum = self.Mnum
            self.Mnum = self.Lnum
            self.Lnum = self.Lnum - 1

    def move_right(self):
        if self.Rnum == len(self.menu_control) - 1:
            self.Rnum = 0
            self.Mnum = len(self.menu_control) - 1
            self.Lnum = len(self.menu_control) - 2
        else:
            self.Lnum = self.Mnum
            self.Mnum = self.Rnum
            self.Rnum = self.Rnum + 1

    def back_event(self):
        if self.modeNum == 0:
            pass
        elif self.modeNum == 1:
            self.modeNum = 0
            self.Lnum, self.Mnum, self.Rnum = 0, 0, 1
            self.menu_control.clear()
            self.left_label.config(image=self.images['china'])
            self.center_label.config(image=self.images['korea'])
            self.right_label.config(image=self.images['japan'])
            self.button.config(text="  한식  ", font=('', 15))
            self.Lbtn.config(text="  중식  ", font=('', 15))
            self.Rbtn.config(text="  일식  ", font=('', 15))
            self.left_info.config(text="나는 오늘 살찌고싶다\n기름진 최강중식")
            self.mid_info.config(text="정갈한 한식\n고향맛 한식")
            self.right_info.config(text="난 비린맛따윈 모른다\n바다향 일식")
        pass

    def set_image(self):
        self.left_label.config(image=self.menu_control[self.Lnum][-1])
        self.right_label.config(image=self.menu_control[self.Rnum][-1])
        self.center_label.config(image=self.menu_control[self.Mnum][-1])

        self.left_info.config(text=str(self.menu_control[self.Lnum][1] + '\n' + str(self.menu_control[self.Lnum][3])))
        self.mid_info.config(text=str(self.menu_control[self.Mnum][1] + '\n' + str(self.menu_control[self.Mnum][3])))
        self.right_info.config(text=str(self.menu_control[self.Rnum][1] + '\n' + str(self.menu_control[self.Rnum][3])))

    def btnTextSet(self):
        self.Lbtn.config(text=" <---  ")
        self.button.config(text="  선택  ")
        self.Rbtn.config(text="  ---> ")

    def left_action(self):
        if self.modeNum == 0:
            self.menu_control = self.ChiData.copy()
            self.Lnum = len(self.menu_control) - 1
            self.btnTextSet()
            self.set_image()
            self.modeNum = 1
        elif self.modeNum == 1:
            self.move_left()
            self.set_image()
        pass

    def right_action(self):
        if self.modeNum == 0:
            self.menu_control = self.JapData.copy()
            self.Lnum = len(self.menu_control) - 1
            self.btnTextSet()
            self.set_image()
            self.modeNum = 1
        elif self.modeNum == 1:
            self.move_right()
            self.set_image()
        pass

    def center_action(self):
        if self.modeNum == 0:
            self.menu_control = self.KorData.copy()
            self.Lnum = len(self.menu_control) - 1
            self.btnTextSet()
            self.set_image()
            self.modeNum = 1
        elif self.modeNum == 1:
            self.result_menu[self.listNum] = self.menu_control[self.Mnum]
            self.listbox.insert(self.listNum, )
            self.listNum = self.listNum + 1
        pass

    # 유저 카테고리 윈도우
    def make_subMain(self):
        self.new_window = tkinter.Toplevel(self.parent)
        self.sub_win = UserCat(self.new_window)



class UserCat:
    def __init__(self, sub_win):
        self.root = sub_win
        self.mighty = ttk.Frame(self.root)
        self.root.title("취향 조사")
        self.root.geometry("450x730")
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
        self.new_window = tkinter.Toplevel(self.root)
        self.sub_app = Demo3(self.new_window, result)
        pass


class Demo3:
    def __init__(self, sub_main, result):
        self.root = sub_main

        self.mighty = ttk.Frame(self.root)
        self.root.title("결과 화면")
        self.root.resizable(True, True)
        self.mighty.pack(fill=None, expand=True)

        self.list_num = len(result)
        self.src = [i[-2].replace('\\','/') for i in result]
        print(src[0])
        self.Imgsrc = [ImageTk.PhotoImage(resized_img(src[i])) for i in range(0,self.list_num)]
        self.label_list = [tkinter.Label(self.mighty, image=self.Imgsrc[i]) for i in range(0, self.list_num)]
        self.row = 0
        for i in range(0, self.list_num):
            if i%2 == 0:
                self.row = self.row + 1
            self.label_list[i].grid(column=i%2, row=self.row)
        print(self.row)
        self.root.geometry(str(450)+'x'+str(self.row*200+50))

    def __del__(self):
        return

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("OpenKiosk")
    root.geometry("1024x600")
    root.resizable(False, False)
    MainApplication(root).pack()
    root.mainloop()
