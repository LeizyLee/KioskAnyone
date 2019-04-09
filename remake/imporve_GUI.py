# Use Tkinter for python 2, tkinter for python 3
import DB
import tkinter
from tkinter import ttk
from PIL import Image, ImageTk

class MainApplication(tkinter.Frame):
    def __init__(self, parent, *args, **kwargs):
        tkinter.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

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

        # ===============================================================================
        # GUI 생성 시작
        # ===============================================================================
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

        img = [ImageTk.PhotoImage(self.resized_img('C:/Users/User/Desktop/image/userCat/' + str(i + 1) + '.jpg')) for i in
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
                                      command=lambda: self.button_press(checkboxVar, checklist, menuData, label_list)).grid(
            column=0, row=0)

    def button_press(self, checkboxVar, checklist, menuData, label_list):
        userData = [i[2:3] for i in menuData]
        sData = [i[0] for i in userData]
        tmp = [i.get() for i in checkboxVar]
        text = []
        textNum = 0
        result = []

        for i in range(0, 6):
            if tmp[i] == 1:
                text.append(checklist[i])
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
        self.show_result(result, label_list)

    def show_result(self, result, label_list):
        list_num = len(result)
        src = [i[-1].replace('\\', '/') for i in result]
        print(src[0])
        Imgsrc = [ImageTk.PhotoImage(self.resized_img(src[i])) for i in range(0, list_num)]
        for i in range(0, list_num):
            label_list[i].config(image=Imgsrc[i])

    def resized_img(self, src):
        tmp = Image.open(src)
        tmp = tmp.convert("RGB")
        tmp2 = tmp.resize((200, 200))
        return (tmp2)


if __name__ == "__main__":
    root = tkinter.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()