import os
from PIL import Image, ImageTk
import tkinter


#tmp = Image.open('C:/Users/User/Desktop/image/Kiosk img/korea/ramyen.jpg')


root = tkinter.Tk()
root.title("Lazy Lee")
root.geometry("500x500")
root.resizable(True,True)

tmp = Image.open('C:/Users/User/Desktop/image/Kioskimg/korea/korea.png')
tmp = tmp.convert("RGB")
tmp2 = tmp.resize((200,200))
img = ImageTk.PhotoImage(tmp2)
label = tkinter.Label(root, image=img)
label.grid(column=0, row=0)

root.mainloop()


"""
for i in file_list:
    temp1=Image.open(path_dir+'/'+i)
    temp1=temp1.convert("RGB")
    temp2=temp1.resize((100,100))
    temp2.save(path_dir+'/'+i)
"""