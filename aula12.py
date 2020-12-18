from tkinter import *

janela = Tk()


lb1 = Label(janela, text="SIDE1", bg="white")
lb2 = Label(janela, text="SIDE2", bg="red")
lb3 = Label(janela, text="ANCHOR1", bg="white")
lb4 = Label(janela, text="ANCHOR2", bg="red")

lb1.pack(side=LEFT)#define uma extrmidade a um componente
lb2.pack(side=LEFT)
lb3.pack(anchor=W) #define um sentido a um componente. Side fica por padrão como TOP
lb4.pack(side=BOTTOM, anchor=W)


janela["bg"] = "black"

janela.geometry("400x300+200+200")
janela.mainloop()
