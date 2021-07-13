import tkinter

class App:

    def __init__(self, title, x, y):

        window = tkinter.Tk()
        window.title(title)
        window.minsize(width=x, height=y)
        window.mainloop()

obj = App("Window",360,640)
obj2 = App("APP",640,360)