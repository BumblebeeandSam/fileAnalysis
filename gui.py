from tkinter import *
import hexDump

class FileAnalyzer:
    def __init__(self, master):
        self.master = master
        master.title("File Analyzer")

        # self.label = Label(master, text="This is our file analyzer.")
        # self.label.pack()

        # self.message = Message(master, text="Hi.")
        # self.message.configure(font = 'TkFixedFont')
        # self.message.pack(side=LEFT)
        
        # self.greet_button = Button(master, text="Greet", command=self.greet)
        # self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

# import tkinter as tk

class Example(Frame):
    def __init__(self, root, text):

        Frame.__init__(self, root)
        self.text = text
        self.canvas = Canvas(root, borderwidth=0, background="#ffffff") # background of the canvas
        self.frame = Frame(self.canvas, background="#ffffff") # background of  the frame
        self.vsb = Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw", 
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

        self.populate()
#        self.Label.configure(font = 'TkFixedFont')

    def populate(self):
        count = 0
        text = self.text.split("\n")
        '''Put in some fake data'''
        for row in text:
            content1 = row[0:8]
            content2 = row[8:50]
            content3 = row[50:]
            Label(self.frame, text=content1, font='TkFixedFont', width=len(content1)).grid(row=count, column=1)
            Label(self.frame, text=content2, font='TkFixedFont', width=len(content2)).grid(row=count, column=2)
            Label(self.frame, text=content3, font='TkFixedFont', width=len(content3)).grid(row=count, column=3)
            
            # Label(self.frame, text=content2, width=len(content2)).grid(row=count, column=2)
            # t="this is the second column for row %s" %row
            # Label(self.frame, text=t).grid(row=row, column=1)
            count += 1

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

if __name__ == "__main__":
    filename = "/home/samuel/Projects/fileAnalysis/hexDump.py"
    root = Tk()
    my_gui = FileAnalyzer(root)
    Example(root, hexDump.main()).pack(side="top", fill="both", expand=True)
    root.mainloop()
