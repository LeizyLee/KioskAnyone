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
src = [i[-1] for i in menuData]
src = [i.replace('\\', '/') for i in src]
print(src)
temp = [i.replace('\\', '/') for i in [j[-1] for j in [k[1:] for k in data]]]
print(temp)

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

        User_button = tkinter.Button(DownFrame, text="카테고리 입력", command=lambda: self.set_userInterface())
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
    def UserCategory():
        global root
        root = tkinter.Tk()
        mighty = ttk.Frame(root)
        root.title("취향 조사")
        root.geometry("450x720")
        root.resizable(True, True)
        mighty.pack(fill=None, expand=True)

        UpFrame = ttk.Frame(mighty)
        DownFrame = ttk.Frame(mighty)
        UpFrame.grid(row=0)
        DownFrame.grid(row=1)

        checkboxVar = [tkinter.IntVar() for i in range(0, 6)]
        checklist = ['밥', '면', '국', '튀김', '매운', '고기']
        CheckBox_list = [ttk.Checkbutton(UpFrame, text="menu" + str(i), variable=checkboxVar[i]) for i in range(0, 6)]
        label_list = [ttk.Label(UpFrame, text="label__" + str(i)) for i in range(0, 6)]

        CheckBox_list[0].grid(column=0, row=1)
        CheckBox_list[0].config(text="밥")
        CheckBox_list[1].grid(column=1, row=1)
        CheckBox_list[1].config(text="면")
        CheckBox_list[2].grid(column=0, row=3)
        CheckBox_list[2].config(text="국")
        CheckBox_list[3].grid(column=1, row=3)
        CheckBox_list[3].config(text="튀김")
        CheckBox_list[4].grid(column=0, row=5)
        CheckBox_list[4].config(text="매운")
        CheckBox_list[5].grid(column=1, row=5)
        CheckBox_list[5].config(text="고기")

        img = [ImageTk.PhotoImage(resized_img('C:/Users/User/Desktop/image/userCat/' + str(i + 1) + '.jpg')) for i in
               range(0, 6)]
        for i in range(0, 6):
            label_list[i].config(image=img[i])

        label_list[0].grid(column=0, row=0)
        label_list[1].grid(column=1, row=0)
        label_list[2].grid(column=0, row=2)
        label_list[3].grid(column=1, row=2)
        label_list[4].grid(column=0, row=4)
        label_list[5].grid(column=1, row=4)

        SelectButton = tkinter.Button(DownFrame, text="다 골랐다면 눌러주세요!",
                                      command=lambda: button_press(checkboxVar, checklist, menuData)).grid(column=0,
                                                                                                           row=0)

        MicBtn = tkinter.Button(DownFrame, text="취향 조사",
                                command=lambda: UsingGCS(checklist, menuData)).grid(column=0, row=1)

        root.mainloop()

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("취향 조사")
    root.geometry("450x720")
    root.resizable(True, True)
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()