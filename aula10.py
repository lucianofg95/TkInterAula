from tkinter import *

janela = Tk()

lb1=Label(janela,text="Label  1", bg="green")
lb2=Label(janela,text="Label  2", bg="red")
lb3=Label(janela,text="Label  3", bg="yellow")
lb4=Label(janela,text="Label  4", bg="blue")

lb1.pack(side=LEFT)
lb2.pack(side=RIGHT)
lb3.pack(side=TOP)
lb4.pack(side=BOTTOM)

janela.geometry("400x300+200+200")
janela.mainloop()


