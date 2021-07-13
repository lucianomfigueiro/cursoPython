from tkinter import * 

class Calc:
    def __init__(self):

        self.window = Tk()
        self.window.title("Calculadora")
        self.window.resizable(0,0)

        self.screen_number = Entry(self.window, font="Arial 20 bold",fg="black", width=26)
        self.screen_number.pack()

        self.frame = Frame(self.window)
        self.frame.pack()

        #Botões teclado numerico
        self.button_1 = Button(self.frame, bg="#5497e3", text="1", bd=0, font="Arial 20 bold",fg="white", width=5, height=3, command=lambda: self.touch("1"))
        self.button_2 = Button(self.frame, bg="#5497e3", text="2", bd=0, font="Arial 20 bold",fg="white", width=5, height=3, command=lambda: self.touch("2"))
        self.button_3 = Button(self.frame, bg="#5497e3", text="3", bd=0, font="Arial 20 bold",fg="white", width=5, height=3, command=lambda: self.touch("3"))
        self.button_4 = Button(self.frame, bg="#5497e3", text="4", bd=0, font="Arial 20 bold",fg="white", width=5, height=3, command=lambda: self.touch("4"))
        self.button_5 = Button(self.frame, bg="#5497e3", text="5", bd=0, font="Arial 20 bold",fg="white", width=5, height=3, command=lambda: self.touch("5"))
        self.button_6 = Button(self.frame, bg="#5497e3", text="6", bd=0, font="Arial 20 bold",fg="white", width=5, height=3, command=lambda: self.touch("6"))
        self.button_7 = Button(self.frame, bg="#5497e3", text="7", bd=0, font="Arial 20 bold",fg="white", width=5, height=3, command=lambda: self.touch("7"))
        self.button_8 = Button(self.frame, bg="#5497e3", text="8", bd=0, font="Arial 20 bold",fg="white", width=5, height=3, command=lambda: self.touch("8"))
        self.button_9 = Button(self.frame, bg="#5497e3", text="9", bd=0, font="Arial 20 bold",fg="white", width=5, height=3, command=lambda: self.touch("9"))
        
        self.button_1.grid(row=0,column=0)
        self.button_2.grid(row=0,column=1)
        self.button_3.grid(row=0,column=2)
        self.button_4.grid(row=1,column=0)
        self.button_5.grid(row=1,column=1)
        self.button_6.grid(row=1,column=2)
        self.button_7.grid(row=2,column=0)
        self.button_8.grid(row=2,column=1)
        self.button_9.grid(row=2,column=2)

        #Botões operações
        self.button_adicao = Button(self.frame, bg="orange", text="+", bd=0, font="Arial 20 bold",fg="white", width=5, height=3, command=lambda: self.touch("+"))
        self.button_subtracao = Button(self.frame, bg="orange", text="-", bd=0, font="Arial 20 bold",fg="white", width=5, height=3, command=lambda: self.touch("-"))
        self.button_divisao = Button(self.frame, bg="orange", text="/", bd=0, font="Arial 20 bold",fg="white", width=5, height=3, command=lambda: self.touch("/"))
        self.button_multiplicacao = Button(self.frame, bg="orange", text="*", bd=0, font="Arial 20 bold",fg="white", width=5, height=3, command=lambda: self.touch("*"))
        self.button_limpar = Button(self.frame, bg="orange", text="C", bd=0, font="Arial 20 bold",fg="white", width=5, height=3, command=self.clean)
        self.button_igual= Button(self.frame, bg="orange", text="=", bd=0, font="Arial 20 bold",fg="white", width=12, height=3, command=self.total)

        self.button_divisao.grid(row=0,column=3)
        self.button_multiplicacao.grid(row=1,column=3)
        self.button_subtracao.grid(row=2,column=3)
        self.button_adicao.grid(row=3,column=3)
        self.button_limpar.grid(row=3,column=2)
        self.button_igual.grid(row=3,column=0, columnspan=2)

        self.window.mainloop()

    def touch(self, num):
        self.screen_number.insert(END,num)

    def clean(self):
        self.screen_number.delete(0,END)

    def total(self):
        t = eval(self.screen_number.get())
        self.screen_number.delete(0,END)
        self.screen_number.insert(0,str(t))

Calc()