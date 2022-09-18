import time
from tkinter import *
import random


def toss():
    x = random.choice(['1.png', '2.png', '3.png', '4.png', '5.png', '6.png'])
    return x


def img():
    global b1, b2
    for i in range(15):
        b1 = PhotoImage(file=(toss()))
        b2 = PhotoImage(file=(toss()))
        lab1['image'] = b1
        lab2['image'] = b2
        root.update()
        time.sleep(0.2)


root = Tk()

root.geometry('1440x900')
root.title('Roll the Dice! Give your best shot!')
root.resizable(height=False, width=False)
root.iconphoto(True, PhotoImage(file='logo.png'))


font = PhotoImage(file='font.png')
Label(root, image=font).pack()
lab1 = Label(root)
lab1.place(relx=0.3, rely=0.5, anchor=CENTER)

lab2 = Label(root)
lab2.place(relx=0.7, rely=0.5, anchor=CENTER)


Button(root, text='Throw it!', command=img).pack()

root.mainloop()
