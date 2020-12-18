from tkinter import *

janela = Tk()

janela.title("LOGIN")

lb1 = Label(janela, text="Login: ")
lb2 = Label(janela, text="Senha: ")

ad1 = Entry(janela, )
ad2 = Entry(janela, show='*' )

bt1 = Button(janela, text="Confirmar")

lb1.grid(row=0, column=0)
lb2.grid(row=1, column=0)
ad1.grid(row=0, column=1)
ad2.grid(row=1, column=1)
bt1.grid(row=2, column=1)

janela.geometry("")

janela.mainloop()

