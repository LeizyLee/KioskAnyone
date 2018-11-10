import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#======================================================================
#출력창 한글을 위한 모듈__ 본 프로젝트와는 관련 없음

import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import *
from tkinter import scrolledtext
import DB
#이것은 테스트다

#==============================================================================
# 메뉴 데이터 불러오기
#==============================================================================
db_tmp = DB.DBlist(_host="202.31.147.29",_db="kioskmenu", _user="guest", _password='0000')
flag = 0
i, j, k = 0, 0, 0
catlist = db_tmp.get_cat()
result = {}

#==============================================================================
# Create GUI instance
#==============================================================================
win = tk.Tk()
mighty = ttk.Frame(win)
mighty.pack(fill=NONE, expand=TRUE)

#==============================================================================
# 프레임 형성하기
#==============================================================================
UpFrame = ttk.Frame(mighty)
UpFrame.grid(column=0, row=0)

up1 = ttk.LabelFrame(UpFrame)
up1.grid(column=0, row=0, padx=15, pady='5m')
up2 = ttk.LabelFrame(UpFrame)
up2.grid(column=1, row=0, padx=15, pady='5m')
up3 = ttk.LabelFrame(UpFrame)
up3.grid(column=2, row=0, padx=15, pady='5m')

MidFrame = ttk.Frame(mighty)
MidFrame.grid(column=0, row=1)

#==============================================================================
# 메뉴를 보여줄 라벨 형성
#==============================================================================
sideFont = font.Font(size=20)
middleFont = font.Font(size=24)

left_label = ttk.Label(up1, text="첫번째 항목", anchor="center", font=sideFont, width=15,  justify=LEFT)
left_label.grid(column=0, row=0, pady = '5m')
middle_label = ttk.Label(up2, text="두번째 항목", anchor="center", font=middleFont, width=20, justify=CENTER)
middle_label.grid(column=1, row=0,pady = '5m')
right_label = ttk.Label(up3, text="세번째 항목", anchor="center", font=sideFont, width=15, justify=RIGHT)
right_label.grid(column=2, row=0,pady = '5m')

#==============================================================================
# 버튼 이벤트
#==============================================================================
def CenterClick():
    global db_tmp, catlist, flag, i, j, k
    if flag == 0:
        scr.insert(tk.INSERT, "안녕하세요!\n")
        scr.insert(tk.INSERT, "===============\n카테고리 항목 출력\n")
        for i in catlist:
            scr.insert(tk.INSERT, str(i) + "\n")
        scr.insert(tk.INSERT,"===============\n")
        left_label.config(text=str(catlist[-1]))
        middle_label.config(text=str(catlist[0]))
        right_label.config(text=str(catlist[1]))
        flag = 1
    elif flag == 1:
        scr.insert(tk.INSERT, str(catlist[j])+" 선택 완료!\n해당 메뉴 목록을 불러옵니다.")
        scr.insert(tk.INSERT, "===============\n아이템 항목 출력\n")
        itemlist = db_tmp.get_item(catlist[j])
        for i in itemlist:
            scr.insert(tk.INSERT, str(i) + "\n")
        catlist = itemlist
        left_label.config(text=str(catlist[-1][0]))
        middle_label.config(text=str(catlist[0][0]))
        right_label.config(text=str(catlist[1][0]))
        flag = 2

    elif flag == 2:
        scr.insert(tk.INSERT, "===================================================\n")
        scr.insert(tk.INSERT,"해당 메뉴가 선택 되었씁니다! 더 고르실려면 왼쪽 그렇지 않다면 오른쪽을 눌러주세요!\n")

        if not catlist[j] in result:
            result[catlist[j]] = 1
        else:
            result[catlist[j]] = result[catlist[j]].pop(catlist[j]) + 1
        print(result)
        print("\n")
        left_label.config(text="추가!")
        right_label.config(text="종료! 및 계산!")
        middle_label.config(text="--------")
        flag = 3
    elif flag == 4:
        scr.insert(tk.INSERT, "\n\n")
        num = 0
        k_list = result.keys()
        for i in k_list:
            scr.insert(tk.INSERT, str(i[0]) + " " + str(i[1] * result.get(i)) + "원\n")
            num = num + i[1] * result.get(i)
        scr.insert(tk.INSERT, "======================\n총 금액 " + str(num) + "원\n")
        flag = 5
        left_label.config(text="left")
        middle_label.config(text="종료")
        right_label.config(text="right")
    elif flag == 5:
        exit()
    i = -1
    j = 0
    k = 1

def rightClick():
    global db_tmp, catlist, flag, i, j, k, result
    if flag == 1 or flag == 2:
        i = i + 1
        j = j + 1
        k = k + 1
        if i == len(catlist):
            i = 0
        elif j == len(catlist):
            j = 0
        elif k == len(catlist):
            k = 0
        if flag == 1:
            left_label.config(text=str(catlist[i]))
            middle_label.config(text=str(catlist[j]))
            right_label.config(text=str(catlist[k]))
        else:
            left_label.config(text=str(catlist[i][0])+" "+str(catlist[i][1])+"원")
            middle_label.config(text=str(catlist[j][0]+" "+str(catlist[j][1])+"원"))
            right_label.config(text=str(catlist[k][0]+" "+str(catlist[k][1])+"원"))
    elif flag == 3:
            scr.insert(tk.INSERT, "\n\n")
            num = 0
            k_list = result.keys()
            for i in k_list:
                scr.insert(tk.INSERT, str(i[0]) + " " + str(i[1] * result.get(i)) + "원\n")
                num = num + i[1] * result.get(i)
            scr.insert(tk.INSERT, "======================\n총 금액 " + str(num) + "원\n")
            flag = 5
            left_label.config(text="left")
            middle_label.config(text="종료")
            right_label.config(text="right")
    elif flag == 4:
        catlist = db_tmp.get_cat()
        left_label.config(text=str(catlist[i]))
        middle_label.config(text=str(catlist[j]))
        right_label.config(text=str(catlist[k]))
        flag = 1
    else:
        pass

def leftClick():
    global db_tmp, catlist, flag, i, j, k, result
    if flag == 1 or flag == 2:
        if i < 0:
            i = len(catlist) - 1
        elif j < 0:
            j = len(catlist) - 1
        elif k < 0:
            k = len(catlist) - 1
        i = i - 1
        j = j - 1
        k = k - 1
        if flag == 1:
            left_label.config(text=str(catlist[i]))
            middle_label.config(text=str(catlist[j]))
            right_label.config(text=str(catlist[k]))
        else:
            left_label.config(text=str(catlist[i][0])+" "+str(catlist[i][1])+"원")
            middle_label.config(text=str(catlist[j][0]+" "+str(catlist[j][1])+"원"))
            right_label.config(text=str(catlist[k][0]+" "+str(catlist[k][1])+"원"))
    elif flag == 3:
        scr.insert(tk.INSERT, "기존의 카테고리에서 선택하시기를 원하시면 왼쪽\n새로운 카테고리를 원하시면 오른쪽을 눌러주세요.\n")
        left_label.config(text="현 카테고리")
        right_label.config(text="새로 선택")
        middle_label.config(text="귀찮아 결제해")
        flag = 4
    elif flag == 4:
        left_label.config(text=str(catlist[i][0]))
        middle_label.config(text=str(catlist[j][0]))
        right_label.config(text=str(catlist[k][0]))
        flag = 2
    else:
        pass

#==============================================================================
# 버튼 생성
#==============================================================================
left_button = ttk.Button(MidFrame, text="Left", command=leftClick)
left_button.grid(column=0, row=0, ipady='3m')
left_button.grid_configure(padx=8, pady=4)
mid_button = ttk.Button(MidFrame, text="Center", command=CenterClick)
mid_button.grid(column=1, row=0, ipady='3m')
mid_button.grid_configure(padx=8, pady=4)
right_button = ttk.Button(MidFrame, text="Right", command=rightClick)
right_button.grid(column=2, row=0, ipady='3m')
right_button.grid_configure(padx=8, pady=4)

#==============================================================================
# 스크롤 텍스트 생성
#==============================================================================
scr_w = 80
scr_h = 10
scr = scrolledtext.ScrolledText(mighty, width=scr_w, height=scr_h, wrap=tk.WORD)
scr.grid(column=0, row=2, sticky="S")

#==============================================================================
#GUI 창 크기 조절 메소드
#==============================================================================
win.resizable(False,False)

#==============================================================================
# Start GUI
#==============================================================================
win.mainloop()
