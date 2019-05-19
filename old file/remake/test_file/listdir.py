import tkinter
from tkinter import ttk
from tkinter import font
from tkinter import scrolledtext
from PIL import Image, ImageTk
import os
from os import listdir
src = "C:/Users/User/Desktop/image/Kioskimg"

"""
filelst = [i for i in listdir(src)]
print(filelst)
dlist = [src+'/'+i for i in filelst]
print(dlist)

tmp = os.listdir(src)
print(tmp)
"""

num = 4
text = '크다' if num > 5 else '작다'
print(text)

