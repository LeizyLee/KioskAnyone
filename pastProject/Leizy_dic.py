# -*- coding : utf-8 -*-
import collections
"""
__name__ : "Leizy_Lee"
__date__ : "2018-09-04"
__Email__ : "hwansang5@gmail.com"
__Project__ : "Unmmaned Kiosk"
"""
# 포함도 -> 버튼이벤트 > UI > 내부 매커니즘
"""

def Rasp.오른쪽버튼:
    버튼 동작시 오른쪽 버튼UI (클릭 이벤트) 발생

def UI.오른쪽버튼클릭:
    리스트에서 항목 하나를 오른쪽으로 이동!


메인
Rasp.오른쪽()

결과
(클릭 전)현재 항목 - 커피
(Rasp.오른쪽() 실행 후) 현재 항목 - 맥주
"""
class unManBeta:
    def __init__(self):
        self.menulist = collections.OrderedDict()
   
    def addKey(self, _key):
        if _key in list(self.menulist.keys()):
            print("이미 있는 키\n")
        else:
            self.menulist[_key] = []

    def modifyKey(self, _key, _modify):
        self.menulist[_modify] = self.menulist.pop(_key)

    def delKey(self, _key):
        del self.menulist[_key]

    def addKeyItem(self, _key, _item):
        if _item in list(self.menulist.get(_key)):
            print("이미 존재하는 값")
        else:
            self.menulist[_key].append(_item)

    def set_Dic(self):
        # 지역변수 선언
        file = open('menulist.txt', 'r')
        #file = codecs.open('menulist.txt', 'r', 'UTF8')
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

            self.menulist[s] = tmp_list
            del(tmp_list)

    def __del__(self):
        print("종료\n")

    def show(self):
        print("\n\n-!-한글로 카테고리를 작성했을 시, 테이블의 형태가 비정살일 수도 있음 -!-\n\n")
        keys_list = list(self.menulist.keys())
        items_list = list(self.menulist.values())

        print("---------------------------------------------------------------------------------------")
        print("|   카테고리   |                              아 이 템    항 목                          |")
        print("---------------------------------------------------------------------------------------")
        for i in range(0, len(keys_list)):
            print("|"+str(keys_list[i]).ljust(14) + "|" + str(items_list[i]).rjust(70) + "|")
        print("---------------------------------------------------------------------------------------")

    def save_data(self):
        key_list = list(self.menulist.keys())
        items_list = list(self.menulist.values())
        print(key_list, items_list)
        print(items_list[0][0])
        f = open("menulist.txt",'w')
        data = str(len(key_list)) + "\n"
        f.write(data)
        for i in range(0,len(key_list)):
            data = str(key_list[i]) + "\n"
            f.write(data)
            data = str(len(items_list[i])) + "\n"
            f.write(data)
            for j in range(0, len(items_list[i])):
                data = str(items_list[i][j]) + "\n"    
                f.write(data)
    def get_key(self):
        return self.menulist.keys()

    def get_item(self, _key):
        _tmp = list(self.menulist.keys())
        _tmp_item = list(self.menulist.values())
        for i in range(0,len(_tmp)):
            if _key in _tmp[i]:
                return _tmp_item[i]



