import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5 import QtCore
import time

from remake import DB
import threading

#form_class = uic.loadUiType("../qtDesigner/v2.ui")[0]
Ui_MainWindow = uic.loadUiType("../qtDesigner/v3.ui")[0]

db = DB.DBlist()
data = db.table_list
menuData = [i[1:] for i in data]
src = [i[-2] for i in menuData]
src = [i.replace('\\', '/') for i in src]
for i in menuData:
    print(i[:-1])
class MyWindow(QMainWindow, Ui_MainWindow, threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        self.start()
        super().__init__()

        self.setupUi(self)
        self.mighty.hide()
        self.CatBtn.clicked.connect(lambda : self.clicked_userCat())

        self.Background.setPixmap(QPixmap('C:/Users/User/Desktop/19_01/rsz_2back.jpg'))
        self.pushButton.setStyleSheet(
            '''
            QPushButton{image:url(C:/Users/User/Desktop/19_01/ConfirmBtn.jpg); border:0px;}
            '''
        )
        self.pushButton.clicked.connect(lambda : self.firstClicked())

        self.KorMain = self.showImage('C:/res/korea.png')
        self.JapMain = self.showImage('C:/res/japan.png')
        self.ChiMain = self.showImage('C:/res/china.png')

        self.LeftLabel.setPixmap(self.ChiMain)
        self.MidLabel.setPixmap(self.KorMain)
        self.RightLabel.setPixmap(self.JapMain)

        self.LeftInfo.setText("중국")
        self.MidInfo.setText("한국")
        self.RightInfo.setText("일본")

        self.KorData = [[i[0], i[2], i[3], i[4], self.showImage(i[5])] for i in data if i[1] == 'korea']
        self.JapData = [[i[0], i[2], i[3], i[4], self.showImage(i[5])] for i in data if i[1] == 'japan']
        self.ChiData = [[i[0], i[2], i[3], i[4], self.showImage(i[5])] for i in data if i[1] == 'china']
        self.checklist = ['밥', '면', '국', '튀김', '매운', '고기', '뜨거운', '기름']


        self.modeNum = 0
        self.listNum = 0
        self.Lnum, self.Mnum, self.Rnum = 0, 0, 1
        self.menu_control = []
        self.result_menu = []

        self.LeftBtn.clicked.connect(lambda : self.left_action())
        self.MidBtn.clicked.connect(lambda : self.center_action())
        self.RightBtn.clicked.connect(lambda : self.right_action())
        self.BackBtn.clicked.connect(lambda : self.back_event())
        self.VoiceBtn.clicked.connect(lambda : self.Using_GCS())

    def Using_GCS(self):
        userData = [i[2:3] for i in menuData]
        sData = [i[0] for i in userData]
        result = []

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
                print(result)
            except IndexError as e:
                print("일치하는 결과가 없습니다~")

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

    def firstClicked(self):
        self.pushButton.hide()
        self.Background.hide()

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

    def btnTextSet(self):
        self.LeftBtn.setText("<----")
        self.MidBtn.setText("선택")
        self.RightBtn.setText("---->")

    def set_image(self):
        self.LeftLabel.setPixmap(self.menu_control[self.Lnum][-1])
        self.RightLabel.setPixmap(self.menu_control[self.Rnum][-1])
        self.MidLabel.setPixmap(self.menu_control[self.Mnum][-1])

        self.LeftInfo.setText(str(self.menu_control[self.Lnum][1] + '\n' + str(self.menu_control[self.Lnum][3])))
        self.MidInfo.setText(str(self.menu_control[self.Mnum][1] + '\n' + str(self.menu_control[self.Mnum][3])))
        self.RightInfo.setText(str(self.menu_control[self.Rnum][1] + '\n' + str(self.menu_control[self.Rnum][3])))

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
            self.result_menu.append(self.menu_control[self.Mnum])
            self.listNum = self.listNum + 1
        pass

    def back_event(self):
        if self.modeNum == 0:
            pass
        elif self.modeNum == 1:
            self.modeNum = 0
            self.Lnum, self.Mnum, self.Rnum = 0, 0, 1
            self.menu_control.clear()
            self.LeftLabel.setPixmap(self.ChiMain)
            self.MidLabel.setPixmap(self.KorMain)
            self.RightLabel.setPixmap(self.JapMain)
            self.LeftBtn.setText("중식")
            self.MidBtn.setText("한식")
            self.RightBtn.setText("일식")
            self.LeftInfo.setText("중국")
            self.MidInfo.setText("한국")
            self.RightInfo.setText("일본")
        pass

    def showImage(self, dir):
        try:
            pixmap = QPixmap(dir)
            resizePixmap = pixmap.scaled(239,239)
            return resizePixmap
        except ValueError as e:
            print("경로를 잘못입력함")

    def clicked_userCat(self):
        self.Rmain.hide()
        self.mighty.show()
        self.progressBar.hide()
        self.CompleteBtn.clicked.connect(lambda : self.CheckBtnClicked())
        self.UserCatImagebox = [self.RiceImage, self.NoodleImage, self.MeetImage, self.SoupImage, self.SpicyImage,
                                self.FriedImage, self.OilImage, self.HotImage]
        self.UserCatCheckBox = [self.RiceBtn, self.NoodleBtn, self.MeetBtn, self.SoupBtn, self.SpicyBtn, self.FriedBtn,
                                self.OilBtn, self.HotBtn]



    def CheckBtnClicked(self):
        tmp = []
        result = []
        if self.RiceBtn.isChecked() == True:
            tmp.append('밥')
        if self.NoodleBtn.isChecked() == True:
            tmp.append('면')
        if self.SoupBtn.isChecked() == True:
            tmp.append('국')
        if self.SpicyBtn.isChecked() == True:
            tmp.append('매운')
        if self.HotBtn.isChecked() == True:
            tmp.append('뜨거운')
        if self.FriedBtn.isChecked() == True:
            tmp.append('튀김')
        if self.MeetBtn.isChecked() == True:
            tmp.append('고기')
        if self.OilBtn.isChecked() == True:
            tmp.append('기름')
        for i in menuData:
            check = 0
            for j in i[2].split(","):
                if j in tmp:
                    check = check + 1
            if check == len(tmp):
                result.append(i[:-1])
        print(tmp)
        print(result)
        check = 0
        for i in self.UserCatImagebox:
            if check < len(result):
                i.setPixmap(self.resultImage(result[check][-1]))
                check = check+1
            else:
                i.setText("No image")

        check = 0
        for i in self.UserCatCheckBox:
            i.setChecked(False)
            if check < len(result):
                i.setText(str(result[check][1] + " " + str(result[check][3])+"원"))
                check = check + 1
            else:
                i.setText("")
    def resultImage(self, dir):
        try:
            pixmap = QPixmap(dir)
            resizePixmap = pixmap.scaled(200,200)
            return resizePixmap
        except ValueError as e:
            print("경로를 잘못입력함")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    sys.exit(app.exec_())