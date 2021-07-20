from tkinter import *
from tkinter import filedialog
from pytube import YouTube


class Dowloader:

    def __init__(self):
        self.window = Tk()
        self.window.title("Youtube Downloader")
        self.window.resizable(0,0)
        self.window.geometry("1080x540")
        
        self.img_logo = PhotoImage(file="assets/logo.png")

        self.audio = False
        self.video = False

        self.frame = Frame(self.window, bg="white", pady=40)
        self.frame.pack(fill="x")

        self.label_logo = Label(self.frame, image=self.img_logo, bg="white")
        self.label_logo.pack()

        self.frame2 = Frame(self.window, pady=20)
        self.frame2.pack()

        self.label_insert = Label(self.frame2, text="Insert Link: ", font="Arial 12")
        self.label_insert.pack(side="left")

        self.link = Entry(self.frame2, font="Arial 20", width=50)
        self.link.pack(side="left")

        self.play = Button(self.frame2, bg="red", text=">", bd=0,fg="white", width=4, height=2, command=lambda: self.download(self.link.get())).pack()
        
        self.frame3 = Frame(self.window)
        self.frame3.pack()

        self.radio1 = Radiobutton(self.frame3, text="Audio", value=0, command=self.validate_audio).pack(side="left")
        self.radio2 = Radiobutton(self.frame3, text="Video", value=1, command=self.validate_video).pack(side="left")
        self.radio3 = Radiobutton(self.frame3, text="Audio e Video", value=2, command=self.validate_all).pack(side="left")
        

        self.window.mainloop()

    def validate_audio(self):
        self.audio = True
        self.video = False

    def validate_video(self):
        self.audio = False
        self.video = True

    def validate_all(self):
        self.audio = False
        self.video = False

    def download(self, link):
        try:
            if self.audio:
                pasta = filedialog.askdirectory()
                YouTube(link).streams.filter(only_audio=True).first().dowload(pasta)
                self.complete()
            elif self.video:
                pasta = filedialog.askdirectory()
                YouTube(link).streams.filter(only_video=True).first().dowload(pasta)
                self.complete()
            else:
                pasta = filedialog.askdirectory()
                YouTube(link).streams.first().dowload(pasta)
                self.complete()
        except:
            self.msn()

    def msn(self):
        window = Toplevel()
        window.title("ERROR")
        window.resizable(0,0)
        window.geometry("300x200")
        
        text = Label(window, text="Link not valid", pady=30)
        text.pack()

        button_exit = Button(window, text="OK", command=window.destroy)
        button_exit.pack()

    def complete(self):
        window = Toplevel()
        window.title("Complete")
        window.resizable(0,0)
        window.geometry("300x200")
        
        text = Label(window, text="Download complete", pady=30)
        text.pack()

        button_exit = Button(window, text="OK", command=window.destroy)
        button_exit.pack()

Dowloader()