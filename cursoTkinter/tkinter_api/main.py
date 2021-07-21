import requests
import json
from tkinter import *

class MovieData:

    def __init__(self):
        self.window = Tk()
        self.window.title("Movie Data")
        self.window.geometry("450x300+300+150")
        self.window.resizable(0, 0)

                
        self.frame = Frame(self.window)
        self.frame.pack()
        self.text_entry = Entry(self.frame, font="arial 16", width=30)
        self.text_entry.grid(row=0, column=0)

        self.button_search = Button(self.frame, text="Search", font="arial 13", command=self.search)
        self.button_search.grid(row=0, column=1)

        self.list = Listbox(self.window)
        self.list.pack(fill=BOTH, expand=YES)


        self.window.mainloop()

    def search(self):
        try:
            request = requests.get("http://www.omdbapi.com/?t="+self.text_entry.get()+"+&apikey=4743fedd")
            dict = json.loads(request.text)
            print(dict)

            self.list.delete(0, END)
            self.list.insert(END, ("Title: " + dict["Title"]))
            self.list.insert(END, ("Year: " + dict["Year"]))
            self.list.insert(END, ("Released: " + dict["Released"]))
        except:
            self.list.delete(0, END)
            self.list.insert(END,"Movie not found!!")

MovieData()
