import tkinter
from tkinter import ttk
from tkinter import font
from tkinter import scrolledtext
from PIL import Image, ImageTk

class node:
    def __init__(self):
        self.next = self
        self.imgData = None

    def insert_img(self, src):
        self.imgData = ImageTk.PhotoImage(Image.open(src))

    def next_node(self):
        self.next = node()

Node = node()
Node.insert_img('./res/img/1도기.png')
Node.next_node()

root = tkinter.Tk()
self = ttk.Frame(root)
root.title("Lazy Lee")
root.geometry("700x350")
root.resizable(True, True)
self.pack(fill=None, expand=True)

Limg = ImageTk.PhotoImage(Image.open('./res/img/1도기.png'))
Llabel = tkinter.Label(self, image=Node.imgData)
Llabel.grid(column=0, row=0)


img = ImageTk.PhotoImage(Image.open('./res/img/2도기.png'))
label = tkinter.Label(self, image=Node.next.imgData)
label.grid(column=1, row=0)

Rimg = ImageTk.PhotoImage(Image.open('./res/img/3도기.png'))
Rlabel = tkinter.Label(self, image=Rimg)
Rlabel.grid(column=2, row=0)