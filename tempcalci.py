from tkinter import *

root = Tk()


def click():
    print('butten pressed ')


b = Button(root, text='Button', command=click)
b.pack()

root.mainloop()
