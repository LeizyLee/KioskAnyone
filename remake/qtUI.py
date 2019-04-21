import sys
import remake.UI
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from remake.Database import Sync
import threading

db = Sync.SyncCursor()
if db.deploy_image():
    pass
data = db.table_list
menuData = [i[1:] for i in data if not i[3] == None]

class MyWindow(QMainWindow, remake.UI.Ui_Openkiosk, threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        self.start()
        super().__init__()
        
        # ===============================================================================================
        #               메인 윈도우에 사용될 변수
        # ===============================================================================================
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

        self.KorMain = self.showImage('./res/korea.png')
        self.JapMain = self.showImage('./res/japan.png')
        self.ChiMain = self.showImage('./res/china.png')

        self.LeftLabel.setPixmap(self.ChiMain)
        self.MidLabel.setPixmap(self.KorMain)
        self.RightLabel.setPixmap(self.JapMain)

        self.LeftInfo.setText("중국")
        self.MidInfo.setText("한국")
        self.RightInfo.setText("일본")

        self.modeNum = 0
        self.listNum = 0
        self.money = 0
        self.Lnum, self.Mnum, self.Rnum = 0, 0, 1
        self.menu_control = []

        self.LeftBtn.clicked.connect(lambda: self.left_action())
        self.MidBtn.clicked.connect(lambda: self.center_action())
        self.RightBtn.clicked.connect(lambda: self.right_action())
        self.BackBtn.clicked.connect(lambda: self.back_event())
        self.VoiceBtn.clicked.connect(lambda: self.Using_GCS())
        self.FinalBtn.clicked.connect(lambda : self.finalbutton())
        
        self.KorData = [[i[0], i[2], i[3], i[4], self.showImage(i[5])] for i in data if i[1] == 'korea']
        self.JapData = [[i[0], i[2], i[3], i[4], self.showImage(i[5])] for i in data if i[1] == 'japan']
        self.ChiData = [[i[0], i[2], i[3], i[4], self.showImage(i[5])] for i in data if i[1] == 'china']

        self.ItemModel = QStandardItemModel()
        self.ItemList.setModel(self.ItemModel)

        # ===============================================================================================
        #               서브 윈도우에 사용될 변수
        # ===============================================================================================
        self.CompleteBtn.clicked.connect(lambda: self.CheckBtnClicked())
        self.UserCatImagebox = [self.RiceImage, self.NoodleImage, self.MeetImage, self.SoupImage, self.SpicyImage,
                                self.FriedImage, self.OilImage, self.HotImage]
        self.UserCatCheckBox = [self.RiceBtn, self.NoodleBtn, self.MeetBtn, self.SoupBtn, self.SpicyBtn, self.FriedBtn,
                                self.OilBtn, self.HotBtn]
        self.checklist = ['밥', '면', '고기', '국', '매운', '튀김', '기름', '뜨거운']
        self.subMode = 0
        self.subResult = []

        #image.setPixmap(QPixmap(dir))
        #화면 초기화
        for i in range(0,len(self.UserCatImagebox)):
            self.UserCatImagebox[i].setPixmap(QPixmap('./res/userCat/'+str(i+1)+'.jpg').scaled(200,200))
            self.UserCatCheckBox[i].setText(self.checklist[i])
        
        self.result_menu = []
        self.BackBtn_2.clicked.connect(lambda : self.subBackClicked())

    # ===============================================================================================
    #               메인 윈도우에 사용되는 버튼 클릭 이벤트
    # ===============================================================================================
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
            self.result_menu.append([self.menu_control[self.Mnum][0], self.menu_control[self.Mnum][1], self.menu_control[self.Mnum][-2]])
            self.ItemModel.appendRow(QStandardItem(self.result_menu[self.listNum][1] + ' ' + str(self.result_menu[self.listNum][-1]) + '원'))
            self.money = self.money + self.result_menu[self.listNum][-1]
            self.listNum = self.listNum + 1
            self.ResultLabel.setText('총액 : ' + str(self.money) + ' 원')
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
            self.ItemModel.clear()
            self.money = 0
            self.ResultLabel.setText("메뉴를 골라주세요")
        pass

    def showImage(self, dir):
        try:
            pixmap = QPixmap(dir)
            resizePixmap = pixmap.scaled(239,239)
            return resizePixmap
        except ValueError as e:
            print("경로를 잘못입력함")

    def finalbutton(self):
        db.sendSalesData(self.result_menu)
        self.back_event()

    def clicked_userCat(self):
        self.modeNum = 2
        self.FinalBtn.setText("정말 다 골랐나요?")
        if self.modeNum == 2:
            self.Rmain.hide()
            self.mighty.show()
            self.progressBar.hide()

    # ===============================================================================================
    #               서브 윈도우에 사용되는 버튼 클릭 이벤트
    # ===============================================================================================
    def subBackClicked(self):
        self.mighty.hide()
        self.Rmain.show()
        # 화면 초기화
        for i in range(0, len(self.UserCatImagebox)):
            self.UserCatImagebox[i].setPixmap(QPixmap('./res/userCat/' + str(i + 1) + '.jpg').scaled(200, 200))
            self.UserCatCheckBox[i].setText(self.checklist[i])
            self.UserCatCheckBox[i].setChecked(False)
        self.subMode = 0

    def CheckBtnClicked(self):
        if not self.subMode == 1:
            self.subMode = 1
            tmp = []
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
            self.find_menu(tmp)
        elif self.subMode == 1:
            for i in range(0, len(self.UserCatCheckBox)):
                if self.UserCatCheckBox[i].isChecked() == True:
                    self.result_menu.append(self.subResult[i][:-1])
                    self.ItemModel.appendRow(
                    QStandardItem(self.result_menu[self.listNum][1] + ' ' + str(self.result_menu[self.listNum][-1]) + '원'))
                    self.money = self.money + self.result_menu[self.listNum][-1]
                    self.listNum = self.listNum + 1
            self.ResultLabel.setText('총액 : ' + str(self.money) + ' 원')
            self.subBackClicked()


    def find_menu(self,tmp):
        #self.KorData = [[i[0], i[2], i[3], i[4], self.showImage(i[5])] for i in data if i[1] == 'korea']
        # 번호, 이름, 속성, 가격, 이미지태그
        for i in data:
            check = 0
            if i[3] == None:
                pass
            else:
                for j in i[3].split(","):
                    if j in tmp:
                        check = check + 1
                if check == len(tmp):
                    self.subResult.append([i[0],i[2],i[4],i[-2]])

        check = 0
        for i in self.UserCatImagebox:
            if check < len(self.subResult):
                i.setPixmap(self.resultImage(self.subResult[check][-1]))
                check = check+1
            else:
                i.setText("No image")

        check = 0
        for i in self.UserCatCheckBox:
            i.setChecked(False)
            if check < len(self.subResult):
                i.setText(str(self.subResult[check][1] + " " + str(self.subResult[check][2])+"원"))
                check = check + 1
            else:
                i.setText("")
        self.CompleteBtn.setText("메뉴 고르기가 완료되면\n눌러주세요")


    def resultImage(self, dir):
        try:
            pixmap = QPixmap(dir)
            resizePixmap = pixmap.scaled(200,200)
            return resizePixmap
        except ValueError as e:
            print("경로를 잘못입력함")

    def Using_GCS(self):
        from remake.GoogleCloud import googleCloudSpeech, sound_recorder

        getUserOpinion = sound_recorder.getWaveFile()
        getUserOpinion.run()
        tmp = googleCloudSpeech.run_quickstart()
        text = self.find_tag(tmp)
        if text == []:
            print("원하는 결과가 없습니다.")
        else:
            self.find_menu(text)
            self.subMode = 1



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
        if '뜨겁고' in text or '뜨거' in text:
            result.append('뜨거운')
        if '기름' in text:
            result.append('기름')
        return result


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    sys.exit(app.exec_())