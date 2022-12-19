from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title('GUI приложение')
# root.iconbitmap('/home/oo7/project1/project1/tkiter/python.ico')
root.geometry('600x400+800+300')

imgs = ImageTk.PhotoImage(file='python-logo.png')
l_logo = Label(root, image = imgs)
l_logo.pack()

root.mainloop()