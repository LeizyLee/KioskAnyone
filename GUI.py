import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import *
import UnmanedRack

#==============================================================================
# Create GUI instance
#==============================================================================
win = tk.Tk()


#==============================================================================
#메뉴 데이터 불러오기
#==============================================================================
menu = UnmanedRack.unManBeta()
menu.set_Dic()


#==============================================================================
#데이터 처리를 위한 변수들 및 초기화
#==============================================================================
tmp_l = 0
tmp_m = 1
tmp_r = 2
tmp_list = list(menu.get_key())

window_state = 1


#==============================================================================
# Add a title
#==============================================================================
win.title("Python GUI")


#==============================================================================
# 관리의 편의성을 위해 Mighty 추가
#==============================================================================
mighty = ttk.LabelFrame(win, text='Mighty Python')
mighty.grid(column=0, row=0)
mighty.pack(fill=NONE, anchor=CENTER, expand=TRUE)



#==============================================================================
# 메뉴를 순차적으로 보여줄 라벨 프레임 추가
#==============================================================================
UpFrame = ttk.LabelFrame(mighty, text='Show Menu List')
UpFrame.grid(column=0, row=0, ipadx='4m', ipady='1m', padx='2m', pady='1m')

MIddlesubFrame = ttk.LabelFrame(mighty)
MIddlesubFrame.grid(column=0, row=1)


#==============================================================================
#이벤트를 처리할 버튼 프레임을 추가
#==============================================================================
DButtonFrame = ttk.LabelFrame(mighty, text='Button Action')
DButtonFrame.grid(column=0, row=2)

#==============================================================================
# Add a Label
#==============================================================================
Afont=font.Font(size=15)
Bfont=font.Font(size=18)

a_label = ttk.Label(UpFrame, text="-1", anchor="center", font=Afont, width=8, justify=LEFT)
a_label.grid(column=0, row=0, sticky='w')
b_label = ttk.Label(UpFrame, text="", anchor="center", font=Bfont, width=8, justify=CENTER)
b_label.grid(column=1, row=0,sticky='w')
c_label = ttk.Label(UpFrame, text="1", anchor="center", font=Afont, width=8, justify=RIGHT)
c_label.grid(column=2, row=0,sticky='w')

sub_label = ttk.Label(MIddlesubFrame, text="sub list")
sub_label.grid(column=1, row=2,sticky='w')


#==============================================================================
# Button Click Event Function
#==============================================================================
def click_me():
    global window_state, tmp_l, tmp_m, tmp_r
    global tmp_list, menu
    if window_state == 1:
        sub_label.configure(text='데이터를 불러오고 프로그램을 시작합니다.')
        a_label.config(text=str(tmp_list[tmp_l]))
        b_label.config(text=str(tmp_list[tmp_m]))
        c_label.config(text=str(tmp_list[tmp_r]))
        action.config(text="선택")
        window_state = 0
    elif window_state == 0:
        window_state = 2
        tmp_list = menu.get_item(tmp_list[tmp_m])
        tmp_l = 0
        tmp_m = 1
        tmp_r = 2
        a_label.config(text=str(tmp_list[tmp_l]))
        b_label.config(text=str(tmp_list[tmp_m]))
        c_label.config(text=str(tmp_list[tmp_r]))
    elif window_state == 2:
        MIddlesubFrame.grid_forget()
        action.config(text="최종")
        LeBtn.config(text="포장")
        RgBtn.config(text="매장")
    else:
        pass

def click_Up():
    sub_label.config(text="going up")

def click_Down():
    sub_label.config(text="going down")

def click_left():
    global tmp_l, tmp_m, tmp_r, window_state, menu
    if window_state == 0 or window_state == 2:
        tmp_l = tmp_l - 1
        tmp_m = tmp_m - 1
        tmp_r = tmp_r - 1
        if tmp_l < 0:
            tmp_l = len(tmp_list) - 1
        elif tmp_m < 0:
            tmp_m = len(tmp_list) - 1
        elif tmp_r < 0:
            tmp_r = len(tmp_list) - 1
        a_label.config(text=str(tmp_list[tmp_l]))
        b_label.config(text=str(tmp_list[tmp_m]))
        c_label.config(text=str(tmp_list[tmp_r]))
        sub_label.config(text=menu.get_item(tmp_list[tmp_m]))
    else:
        pass

def click_right():
    global tmp_l, tmp_m, tmp_r, window_state, menu
    if not window_state == 1:
        tmp_l = tmp_l + 1
        tmp_m = tmp_m + 1
        tmp_r = tmp_r + 1
        if tmp_l == len(tmp_list):
            tmp_l = 0
        elif tmp_m == len(tmp_list):
            tmp_m = 0
        elif tmp_r == len(tmp_list):
            tmp_r = 0
        a_label.config(text=str(tmp_list[tmp_l]))
        b_label.config(text=str(tmp_list[tmp_m]))
        c_label.config(text=str(tmp_list[tmp_r]))
        sub_label.config(text=menu.get_item(tmp_list[tmp_m]))
    else:
        pass


#==============================================================================
# Adding a Button
#==============================================================================
action = ttk.Button(DButtonFrame, text="Click Me!", command=click_me)
action.grid(column=1,row=1)
upBtn = ttk.Button(DButtonFrame, text="Up!", command=click_Up)
upBtn.grid(column=1,row=0)
DownBtn = ttk.Button(DButtonFrame, text="Down!", command=click_Down)
DownBtn.grid(column=1, row=2)
LeBtn = ttk.Button(DButtonFrame, text="Left!", command=click_left)
LeBtn.grid(column=0, row=1)
RgBtn = ttk.Button(DButtonFrame, text="Right!", command=click_right)
RgBtn.grid(column=2,row=1)


#==============================================================================
#GUI 창 크기 조절 메소드
#==============================================================================
win.resizable(False,False)


#==============================================================================
# Start GUI
#==============================================================================
win.mainloop()
