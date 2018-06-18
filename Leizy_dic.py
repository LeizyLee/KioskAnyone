# -*- coding : utf-8 -*-
import collections

class LeDict:
    def __init__(self):
        self.menu_list = collections.OrderedDict()
        self.PointList = []
        print("!")

    def is_int(self, _str="", _name=""):
        flag = True
        result = ""

        while flag:
            if not _name == "":
                result = input("%s %s"%(_name, _str))
            else:
                result = input(_str)
            try:
                int(result)
            except ValueError:
                print("오로지 숫자만 입력하시오.")
            else:
                flag = False

        return result

    def set_Dic(self):
        # 지역변수 선언
        file = open('menulist.txt', 'r')
        a = file.readline().strip()
        #a = self.is_int("카테고리의 갯수를 입력해주세요. : ")
        for i in range(0,int(a)):
            #s = input("%d번째 카테고리의 이름을 정해주세요. : " %(i+1))
            s = file.readline().strip()

            # 지역변수 선언
            n = file.readline().strip()

            #n = self.is_int("의 아이템 갯수는 어떻게 됩니까? : ",s)
            tmp_list = []

            for j in range(0,int(n)):
                item = file.readline().strip()
                #item = input("%d 번째의 아이템 이름을 정해주세요. :"%(j+1))
                tmp_list.append(item)

            self.menu_list[s] = tmp_list
            del(tmp_list)

    def show_Dic(self):
        print("\n\n-!-한글로 카테고리를 작성했을 시, 테이블의 형태가 비정살일 수도 있음 -!-\n\n")
        keys_list = list(self.menu_list.keys())
        items_list = list(self.menu_list.values())

        print("---------------------------------------------------------------------------------------")
        print("|   카테고리   |                              아 이 템    항 목                          |")
        print("---------------------------------------------------------------------------------------")
        for i in range(0, len(keys_list)):
            print("|"+str(keys_list[i]).ljust(14) + "|" + str(items_list[i]).rjust(70) + "|")
        print("---------------------------------------------------------------------------------------")

    def change_Dic_KeyName(self, _before="", _after = ""):
        self.menu_list[_after] = self.menu_list.pop(_before)

    def is_exist_Key(self, _key=""):
        if _key in list(self.menu_list.keys()):
            return False
        else:
            return True

    def is_exist_Value(self, _Key="", _Value=""):
        if _Value in list(self.menu_list.get(_Key)):
            return False
        else:
            return True

    def add_key(self, _key):
        if self.is_exist_Key(_key):
            self.menu_list[_key] = ""
        else:
            print("이미 존재하는 키")

    def add_value(self, _key, _value):
        if self.is_exist_Value(_key,_value):
            self.menu_list[_key] = _value
        else:
            print("이미 해당 값이 들어있음")

    def Do_Run(self):
        tnum = 0
        tlist = []
        self.PointList = list(self.menu_list.keys())
        tmp = ''

        while tmp == 'R':
            print("시작을 원하시면 R을 눌러주세요!")
            tmp = input()

        tmp = input("카테고리를 선택해주세요. 첫 항목은 %s입니다. \n그리고 선택을 희망하시면 E를 입력해주세요."%self.PointList[tnum])
        while tmp == 'E':
            if tmp == 'a':
                if tnum == 0:
                    tnum = len(self.PointList) - 1
                    tmp = input("현재 항목은 %s입니다."%self.PointList[tnum])
            elif tmp == 'd':
                if tnum == len(self.PointList) - 1:
                    tnum = 0
                    tmp = input("현재 항목은 %s입니다."%self.PointList[tnum])
            else:
                tmp = input("잘못된 입력입니다. 다시 입력해주세요 -> ")
        tlist = self.menu_list.values(self.PointList[tnum])
        print("카테고리 선택이 완료되었습니다. 이제 아이템을 선택해주세요. 첫 항목은 %s입니다. 선택은 전과 동입니다.\n"%tlist)

    def __del__(self):
        del(self.menu_list)
