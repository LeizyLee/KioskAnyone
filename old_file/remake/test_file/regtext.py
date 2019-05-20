import re
from os import listdir

src = "C:/Users/User/Desktop/image/Kioskimg"

filelst = [i for i in listdir(src)]
print(filelst)
dlist = [src+'/'+i for i in filelst]
print(dlist)

text = "C:/Users/User/Desktop/image/Kioskimg/korea/"
kor = "korea"
regex = re.compile(r'[C:/Users/User/Desktop/image/Kioskimg/]+\w+')
matchobj = regex.search(text)
dir = matchobj.group()

tmp = [regex.search(i) for i in dlist]
dtmp = [i.group() for i in tmp]
print(dtmp)