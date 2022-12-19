from tkinter import *

root = Tk()
root.geometry('600x400+700+300')

l = Label(root, text='text one\n text two\n text three\n text four\n text five\n', bg="red", fg="#fff", font=("Comic Sans MS", 20, "bold"),)
l.pack()

root.mainloop()