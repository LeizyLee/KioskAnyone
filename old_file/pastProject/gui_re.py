# -*- coding: utf-8 -*-
import tkinter
from tkinter import ttk
from tkinter import font
from tkinter import scrolledtext
from PIL import Image, ImageTk
import os

def resized_img(src):
    tmp = Image.open(src)
    tmp = tmp.convert("RGB")
    tmp2 = tmp.resize((200, 200))
    return tmp2

#===============================================================================
# GUI 객체 생성
#===============================================================================

root = tkinter.Tk()
self = ttk.Frame(root)
root.title("Lazy Lee")
root.geometry("700x300")
root.resizable(True, True)
self.pack(fill=None, expand=True)

#===============================================================================
# 변수 선언
#===============================================================================

label_num = 0
src = "C:/Users/User/Desktop/image/Kioskimg"
dir = [src + '/' + i for i in os.listdir(src)]
menu = []
maxN = 3
Lnum, Mnum, Rnum = 0, 0, 1
status = 0
#===============================================================================
# 프레임 생성
#===============================================================================
UpFrame = ttk.Frame(self)
UpFrame.grid(column=0, row=0)

DownFrame = ttk.Frame(self)
DownFrame.grid(column=0, row=1)

MidFrame = ttk.Frame(self)
MidFrame.grid(column=0, row=2)

#===============================================================================
# 버튼 이벤트
#===============================================================================
def set_title():
    Lbtn.config(text="<----")
    Rbtn.config(text="---->")
    button.config(text="  선택  ")

def press_Lbtn():
    global maxN, status, menu, Lnum, Mnum, Rnum, Limg, img, Rimg

    if status == 0:
        menu = [dir[0] + '/' + i for i in os.listdir(dir[0])]
        maxN = len(menu) - 1
        Lnum = maxN
        status = 1
        Limg = ImageTk.PhotoImage(resized_img(menu[Lnum]))
        Llabel.config(image=Limg)
        img = ImageTk.PhotoImage(resized_img(menu[Mnum]))
        label.config(image=img)
        Rimg = ImageTk.PhotoImage(resized_img(menu[Rnum]))
        Rlabel.config(image=Rimg)
        set_title()
    elif status == 1:
        if Lnum == 0:
            Lnum = maxN
            Mnum = Mnum - 1
            Rnum = Rnum - 1
        elif Mnum == 0:
            Lnum = Lnum - 1
            Rnum = Rnum - 1
            Mnum = maxN
        elif Rnum == 0:
            Lnum = Lnum - 1
            Rnum = maxN
            Mnum = Mnum - 1
        else:
            Lnum = Lnum - 1
            Mnum = Mnum - 1
            Rnum = Rnum - 1
        print(Lnum, Mnum, Rnum)
        Limg = ImageTk.PhotoImage(resized_img(menu[Lnum]))
        Llabel.config(image=Limg)
        img = ImageTk.PhotoImage(resized_img(menu[Mnum]))
        label.config(image=img)
        Rimg = ImageTk.PhotoImage(resized_img(menu[Rnum]))
        Rlabel.config(image=Rimg)


def press_Rbtn():
    global maxN, status, menu, Lnum, Mnum, Rnum, Limg, img, Rimg
    if status == 0:
        menu = [dir[2] + '/' + i for i in os.listdir(dir[2])]
        maxN = len(menu) - 1
        Lnum = maxN
        status = 1
        Limg = ImageTk.PhotoImage(resized_img(menu[Lnum]))
        Llabel.config(image=Limg)
        img = ImageTk.PhotoImage(resized_img(menu[Mnum]))
        label.config(image=img)
        Rimg = ImageTk.PhotoImage(resized_img(menu[Rnum]))
        Rlabel.config(image=Rimg)
        set_title()
    elif status == 1:
        if Lnum == maxN:
            Lnum = 0
            Mnum = Mnum + 1
            Rnum = Rnum + 1
        elif Mnum == maxN:
            Lnum = Lnum + 1
            Rnum = Rnum + 1
            Mnum = 0
        elif Rnum == maxN:
            Lnum = Lnum + 1
            Rnum = 0
            Mnum = Mnum + 1
        else:
            Lnum = Lnum + 1
            Mnum = Mnum + 1
            Rnum = Rnum + 1
        print(Lnum, Mnum, Rnum)
        Limg = ImageTk.PhotoImage(resized_img(menu[Lnum]))
        Llabel.config(image=Limg)
        img = ImageTk.PhotoImage(resized_img(menu[Mnum]))
        label.config(image=img)
        Rimg = ImageTk.PhotoImage(resized_img(menu[Rnum]))
        Rlabel.config(image=Rimg)

def press_button():
    global maxN, status, menu, Lnum, Mnum, Rnum, Limg, img, Rimg
    if status == 0:
        menu = [dir[4] + '/' + i for i in os.listdir(dir[4])]
        maxN = len(menu) - 1
        Lnum = maxN
        status = 1
        Limg = ImageTk.PhotoImage(resized_img(menu[Lnum]))
        Llabel.config(image=Limg)
        img = ImageTk.PhotoImage(resized_img(menu[Mnum]))
        label.config(image=img)
        Rimg = ImageTk.PhotoImage(resized_img(menu[Rnum]))
        Rlabel.config(image=Rimg)
        set_title()
    elif status == 1:
        pass


#===============================================================================
# 상단 이미지 라벨 생성
#===============================================================================
Limg = ImageTk.PhotoImage(resized_img(dir[1]))
Llabel = tkinter.Label(UpFrame, image=Limg)
Llabel.grid(column=0, row=0)

img = ImageTk.PhotoImage(resized_img(dir[5]))
label = tkinter.Label(UpFrame, image=img)
label.grid(column=1, row=0)

Rimg = ImageTk.PhotoImage(resized_img(dir[3]))
Rlabel = tkinter.Label(UpFrame, image=Rimg)
Rlabel.grid(column=2, row=0)

#===============================================================================
#  버튼 생성
#===============================================================================
Lbtn = tkinter.Button(DownFrame, command=press_Lbtn)
Lbtn.config(text="  중식  ", font=('',15))
Lbtn.grid(column=0, row=0)
Lbtn.grid_configure(padx=0, pady=4)

Rbtn = tkinter.Button(DownFrame, command=press_Rbtn)
Rbtn.config(text="  일식  ", font=('',15))
Rbtn.grid(column=2, row=0)
Rbtn.grid_configure(padx=0, pady=4)

button = tkinter.Button(DownFrame, command=press_button)
button.config(text="  한식  ", font=('',15))
button.grid(column=1, row=0)
button.grid_configure(padx=125, pady=4)



#===============================================================================
# GUI 실행
#===============================================================================
root.mainloop()

