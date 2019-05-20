

"""
make_wave = mic.getWaveFile()
make_wave.run()
GCS.run_quickstart()
"""
from remake import DB
import tkinter
from tkinter import ttk
from PIL import Image, ImageTk



root = '' #Main Window object
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
menuData = [i[1:] for i in data]
src = [i[-1] for i in menuData]
src = [i.replace('\\', '/') for i in src]
print(src)
temp = [i.replace('\\','/') for i in [j[-1] for j in [k[1:] for k in data]]]
print(temp)
#srcForPython = [i.replace('\\','/') for i in src]


# ===============================================================================
# 버튼 이벤트
# ===============================================================================

def button_press(checkboxVar, checklist, menuData):
    userData = [i[2:3] for i in menuData]
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
    show_result(result)

def find_tag(text):
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


def UsingGCS(checklist, menuData):
    userData = [i[2:3] for i in menuData]
    sData = [i[0] for i in userData]
    textNum = 0
    result = []
    tmp = []

    from remake.GoogleCloud import googleCloudSpeech, sound_recorder

    getUserOpinion = sound_recorder.getWaveFile()
    getUserOpinion.run()
    tmp = googleCloudSpeech.run_quickstart()
    text = find_tag(tmp)
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
            show_result(result)
        except IndexError as e:
            print("일치하는 결과가 없습니다~")

def show_result(result):
    global root
    sub_main = tkinter.Toplevel(root)
    mighty = ttk.Frame(sub_main)
    sub_main.title("결과 화면")
    sub_main.resizable(True, True)
    mighty.pack(fill=None, expand=True)

    list_num = len(result)
    src = [i[-1].replace('\\','/') for i in result]
    print(src[0])
    Imgsrc = [ImageTk.PhotoImage(resized_img(src[i])) for i in range(0,list_num)]
    label_list = [tkinter.Label(mighty, image=Imgsrc[i]) for i in range(0, list_num)]
    row = 0
    for i in range(0, list_num):
        if i%2 == 0:
            row = row + 1
        label_list[i].grid(column=i%2, row=row)
    print(row)
    sub_main.geometry(str(450)+'x'+str(row*200+50))
    result = ''
    sub_main.mainloop()


def set_userInterface():
    global root
    root.destroy()
    UserCategory()

#===============================================================================
# GUI 생성 시작
#===============================================================================

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
                                  command=lambda: button_press(checkboxVar, checklist, menuData)).grid(column=0, row=0)

    MicBtn = tkinter.Button(DownFrame, text="취향 조사",
                            command=lambda : UsingGCS(checklist, menuData)).grid(column=0, row=1)

    root.mainloop()


# 메인 윈도우
def drawGUI():
    global root
    root = tkinter.Tk()
    mighty = ttk.Frame(root)
    root.title("Lazy Lee")
    root.geometry("700x300")
    root.resizable(True, True)
    mighty.pack(fill=None, expand=True)

    #===============================================================================
    # 프레임 생성
    #===============================================================================
    UpFrame = ttk.Frame(mighty)
    UpFrame.grid(column=0, row=0)
    # 위젯 컨테이너
    Up_left = ttk.Frame(UpFrame)
    Up_right = ttk.Frame(UpFrame)
    Up_center = ttk.Frame(UpFrame)
    Up_left.grid(column=0, row=0)
    Up_center.grid(column=1, row=0)
    Up_right.grid(column=2, row=0)

    DownFrame = ttk.Frame(mighty)
    DownFrame.grid(column=0, row=1)

    MidFrame = ttk.Frame(mighty)
    MidFrame.grid(column=0, row=2)

    #===============================================================================
    # 상단 이미지 라벨 생성
    #===============================================================================
    src = 'C:\\Users\\User\\Desktop\\image\\Kioskimg'.replace('\\','/')
    china_img = ImageTk.PhotoImage(Image.open(src+'/china.png'))
    left_label = tkinter.Label(Up_left, image=china_img)
    left_label.grid(column=0, row=0)

    korea_img = ImageTk.PhotoImage(Image.open(src+'/korea.png'))
    center_label = tkinter.Label(Up_center, image=korea_img)
    center_label.grid(column=1, row=0)

    japan_img= ImageTk.PhotoImage(Image.open(src+'/japan.png'))
    right_label = tkinter.Label(Up_right, image=japan_img)
    right_label.grid(column=2, row=0)



    #===============================================================================
    #  버튼 생성
    #===============================================================================
    def left_action():
        pass
    Lbtn = tkinter.Button(DownFrame, command=left_action)
    Lbtn.config(text="  중식  ", font=('',15))
    Lbtn.grid(column=0, row=0)
    Lbtn.grid_configure(padx=0, pady=4)


    def right_action():
        pass
    Rbtn = tkinter.Button(DownFrame, command=right_action)
    Rbtn.config(text="  일식  ", font=('',15))
    Rbtn.grid(column=2, row=0)
    Rbtn.grid_configure(padx=0, pady=4)

    def center_action():
        pass
    button = tkinter.Button(DownFrame, command=center_action)
    button.config(text="  한식  ", font=('',15))
    button.grid(column=1, row=0)
    button.grid_configure(padx=125, pady=4)

    User_button = tkinter.Button(DownFrame, text="카테고리 입력", command=lambda : set_userInterface())
    User_button.grid(column=1, row=1)

    #===============================================================================
    # GUI 실행
    #===============================================================================
    root.mainloop()

UserCategory()


