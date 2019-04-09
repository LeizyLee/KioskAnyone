

"""
make_wave = mic.getWaveFile()
make_wave.run()
GCS.run_quickstart()
"""
import DB
import tkinter
from tkinter import ttk
from PIL import Image, ImageTk

#===============================================================================
# 이미지 리사이징 함수
#===============================================================================
def resized_img(src):
    tmp = Image.open(src)
    tmp = tmp.convert("RGB")
    tmp2 = tmp.resize((200, 200))
    return (tmp2)

#===============================================================================
# DB 접속
#===============================================================================
db = DB.DBlist()
data = db.table_list
menuData = [i[2:] for i in data]
src = [i[-1] for i in menuData]
print(data)

# ===============================================================================
# 버튼 이벤트
# ===============================================================================

def button_press(checkboxVar, checklist, menuData):
    userData = [i[1:2] for i in menuData]
    sData = [i[0] for i in userData]
    tmp = [i.get() for i in checkboxVar]
    text = []
    textNum = 0
    result = []

    for i in range(0,6):
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

#===============================================================================
# GUI 생성 시작
#===============================================================================

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

checkboxVar = [tkinter.IntVar() for i in range(0,6)]
checklist = ['밥','면','국','튀김','매운','고기']
CheckBox_list = [ttk.Checkbutton(UpFrame, text="menu"+str(i), variable=checkboxVar[i]) for i in range(0,6)]
label_list = [ttk.Label(UpFrame, text="label__"+str(i)) for i in range(0,6)]

CheckBox_list[0].grid(column=0,row=1)
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

img = [ImageTk.PhotoImage(resized_img('C:/Users/User/Desktop/image/userCat/'+str(i+1)+'.jpg')) for i in range(0,6)]
for i in range(0,6):
    label_list[i].config(image=img[i])

label_list[0].grid(column=0,row=0)
label_list[1].grid(column=1, row=0)
label_list[2].grid(column=0, row=2)
label_list[3].grid(column=1, row=2)
label_list[4].grid(column=0, row=4)
label_list[5].grid(column=1, row=4)

SelectButton = tkinter.Button(DownFrame,text="다 골랐다면 눌러주세요!",command=lambda:button_press(checkboxVar, checklist, menuData)).grid(column=0,row=0)

root.mainloop()

