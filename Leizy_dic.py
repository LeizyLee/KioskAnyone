# -*- coding : utf-8 -*-
import collections

class LeDict:
    def __init__(self):
        self.menu_list = collections.OrderedDict()
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
        a = self.is_int("카테고리의 갯수를 입력해주세요. : ")

        for i in range(0,int(a)):
            s = input("%d번째 카테고리의 이름을 정해주세요. : " %(i+1))

            # 지역변수 선언
            n = self.is_int("의 아이템 갯수는 어떻게 됩니까? : ",s)
            tmp_list = []

            for j in range(0,int(n)):
                item = input("%d 번째의 아이템 이름을 정해주세요. :"%(j+1))
                tmp_list.append(item)

            self.menu_list[s] = tmp_list
            del(tmp_list)

    def show_Dic(self):
        print("한글로 카테고리를 작성했을 시, 테이블의 형태가 비정살일 수도 있음")
        keys_list = list(self.menu_list.keys())
        items_list = list(self.menu_list.values())
        print(keys_list)
        print(items_list)

        print(self.menu_list)
        print("---------------------------------------------------------------------")
        print("|카테고리 |                   아 이 템    항 목                     |")
        print("---------------------------------------------------------------------")
        for i in range(0, len(keys_list)):
            print("|"+str(keys_list[i]).ljust(9) + "|" + str(items_list[i]).rjust(58) + "|")
        print("---------------------------------------------------------------------")

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

    def __del__(self):
        del(self.menu_list)
        print("--")

def main():
    Leizy = LeDict()
    Leizy.set_Dic()
    Leizy.show_Dic()


main()