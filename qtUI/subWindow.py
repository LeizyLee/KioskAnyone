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

        self.modeNum = 0
        self.listNum = 0
        self.Lnum, self.Mnum, self.Rnum = 0, 0, 1
        self.menu_control = []
        self.result_menu = []

        self.LeftBtn.clicked.connect(lambda : self.left_action())
        self.MidBtn.clicked.connect(lambda : self.center_action())
        self.RightBtn.clicked.connect(lambda : self.right_action())
        self.BackBtn.clicked.connect(lambda : self.back_event())

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



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    sys.exit(app.exec_())