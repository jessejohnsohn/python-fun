import shutil, os, stat, datetime, time, Tkconstants, tkFileDialog, sqlite3
from Tkinter import *


class Lazy:
    def __init__(self, master):
                
        self.menu = Menu(master)
        master.config(menu=self.menu)

        self.subMenu = Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.subMenu)
        self.subMenu.add_command(label="Assign Incoming", command=self.chooseInFile)
        self.subMenu.add_command(label="Assign Outgoing", command=self.chooseOutFile)
        self.subMenu.add_separator()
        self.subMenu.add_command(label="Exit", command=self.leave)

        self.editMenu = Menu(self.menu)
        self.menu.add_cascade(label="Help", menu=self.editMenu)
        self.editMenu.add_command(label="Help", command=self.helpme)

        self.toolbar = Frame(master, bg="blue")
        #self.insertButt = Button(self.toolbar, text="Insert", command=self.doNothing)
        #self.insertButt.pack(side=LEFT, padx=2, pady=2)
        self.toolbar.pack(side=TOP, fill=X, pady=20)
        
        self.button_1 = Button(master, text="Incoming Folder", bg='blue', fg='white', command=self.chooseInFile)
        self.button_1.pack()

        self.button_2 = Button(master, text="Outgoing Folder", bg='red', fg='white', command=self.chooseOutFile)
        self.button_2.pack()

        self.button_3 = Button(master, text="Parse and Move", bg='black', fg='white', command=self.sorter)
        self.button_3.pack()
        
    def doNothing(self):
        print("ok ok I won't...")
    
    def chooseInFile(self):
        self.src = tkFileDialog.askdirectory(parent=root, title='Choose a file')

    def chooseOutFile(self):
        self.dst = tkFileDialog.askdirectory(parent=root, title='Choose a file')

    def sorter(self):
        now = datetime.datetime.now()
        for root, dirs, files in os.walk(self.src):
            for file in files:
                x = self.src + '/' + file
                timestamp = datetime.datetime.fromtimestamp(os.stat(x).st_mtime)
                y = (now - timestamp).total_seconds()
                z = 86400
                if y < z :
                    shutil.move(x, self.dst)

    def leave(self):
        root.destroy()

    def helpme(self):
        self.label_1 = Label(text="Just Click One of These!")
        self.label_1.pack(side=BOTTOM)
        
root = Tk()

b = Lazy(root)

root.mainloop()
