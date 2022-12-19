from tkinter import *

root = Tk()
root.title('Мое первое GUI приложение')
# root.iconbitmap('/home/oo7/project1/project1/tkiter/python.ico')
root.geometry('600x400+800+300')
# root.config(bg='#000')
# root['bg'] = 'red'

a = 0
b = 0

def ten():
    global a
    a = 10
def five():
    global b
    b = 5
def plus():
    print(a + b) 
def minus():
    print(a - b) 
def umnoj():
    print(a * b) 
def delenie():
    print(a / b) 

btn_ten = Button(root, text="10", command=ten, width=2)
btn_ten.pack()
btn_five = Button(root, text="5", command=five, width=2)
btn_five.pack()
btn_plus = Button(root, text="+", command=plus, width=2)
btn_plus.pack()
btn_minus = Button(root, text="-", command=minus, width=2)
btn_minus.pack()
btn_umnoj = Button(root, text="*", command=umnoj, width=2)
btn_umnoj.pack()
btn_delenie = Button(root, text="/", command=delenie, width=2)
btn_delenie.pack()

root.mainloop()