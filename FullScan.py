from tkinter import *
from tkinter import filedialog
import random
import os
import time

import globalVariable
from src.engine import *
from globalVariable import *


class FullScan:
    def __init__(self, master):
        self.master = master
        # self.hashList = []
        self.frame = Frame(self.master, width=1000, height=600)
        self.frame.pack_propagate(False)
        self.io = 0
        self.stopFullScan = False
        # self.pathScan = "C:\\Users\\trinhhuynh\\Desktop"
        self.frame.pack(fill=BOTH)
        self.samB = self.load_hash_database()
        self.backButtonImg = PhotoImage(file="res\\back button.png").subsample(4, 4)
        self.backButton = Button(self.frame, image=self.backButtonImg, bd=0, command=self.closeFullScan)
        self.backButton.place(x=10, y=10)
        self.prog0 = PhotoImage(file="res\\progress bar\\0.png").subsample(1, 3)
        self.prog1 = PhotoImage(file="res\\progress bar\\1.png").subsample(1, 3)
        self.prog2 = PhotoImage(file="res\\progress bar\\2.png").subsample(1, 3)
        self.prog3 = PhotoImage(file="res\\progress bar\\3.png").subsample(1, 3)
        self.prog4 = PhotoImage(file="res\\progress bar\\4.png").subsample(1, 3)
        self.prog5 = PhotoImage(file="res\\progress bar\\5.png").subsample(1, 3)
        self.progList = [self.prog0, self.prog1, self.prog2, self.prog3, self.prog4, self.prog5]

        self.bitLinkMainLabel = Label(self.frame, text="Quick Scan", font="Times 21 bold")
        self.bitLinkMainLabel.pack(side=TOP, pady=20)
        self.progLabel = Label(self.frame, image=self.prog0)
        self.progLabel.place(x=250, y=70)

        self.pathLabel = Label(self.frame, text="Virus Scanner", font="Times 20 bold")
        self.pathLabel.place(x=350, y=130)

        self.ranHashShower = Text(self.frame, width=50, height=1, bd=0, font=('Sans Serif', 13, 'bold'),
                                  foreground="green")
        self.ranHashShower.place(x=350, y=170)
        self.ranHashShower.insert(INSERT, "Write Something About Yourself")
        self.ranHashShower.configure(state='disabled')

        self.virusDetect = Label(self.frame, text="Virus Found", font="Times 20 bold")
        self.virusDetect.place(x=350, y=230)

        self.virusFoundPaths = Text(self.frame, width=100, height=10, bd=0, font=('Sans Serif', 13, 'bold'),
                                    foreground="red")
        self.virusFoundPaths.place(x=50, y=290)
        self.virusFoundPaths.insert(INSERT, "No Virus Found")
        self.virusFoundPaths.configure(state='disabled')

        self.rMVirus = Button(self.frame, text="Remove Virus", font="Times 20 bold", command=self.removeVirusBtn)
        self.rMVirus.place(x=350, y=230)

        self.infoVirusFullScan = ""

    def removeVirusBtn(self):
        self.virusFoundPaths.configure(state='normal')
        self.virusFoundPaths.delete("1.0", END)
        self.virusFoundPaths.insert(INSERT, globalVariable.virusFullScan)

    def closeFullScan(self):
        self.master.destroy()

    def progressBarAni(self):
        self.progLabel.configure(image=self.progList[self.io])

        self.io += 1

        id = self.progLabel.after(500, self.progressBarAni)

        if self.io == 5:
            self.io = 0

        if self.stopFullScan:
            self.io = 5
            self.progLabel.configure(image=self.progList[self.io])
            self.progLabel.after_cancel(id)

    def textShower(self):
        self.ranHashShower.configure(state='normal')
        self.ranHashShower.delete("1.0", END)
        self.ranHashShower.insert(INSERT, self.samB[random.randint(0, len(self.samB) - 1)])

        id = self.ranHashShower.after(100, lambda: self.textShower())

        if self.stopFullScan:
            self.ranHashShower.configure(state='normal')
            self.ranHashShower.delete("1.0", END)
            self.ranHashShower.insert(INSERT, "")
            self.ranHashShower.after_cancel(id)

        # try:
        #     with open("switch_io.bb", "r") as nri:
        #         xxc = nri.read()
        #         nri.close()
        #
        #     if xxc == "1" or xxc == 1:
        #         self.ranHashShower.after_cancel(id)
        #
        # except Exception as e:
        #     print("Error:", e)

    def VirusFoundPathX(self):
        if len(globalVariable.virusFullScan) > 0 and globalVariable.statusHandleFullScan == True:
            string = ""

            if len(globalVariable.virusFullScan[1]) > 0:
                for index, item in enumerate(globalVariable.virusFullScan[1]):
                    string = f"{string} Index: {index + 1}, File Path: {item} \n"
                    if index + 1 == len(globalVariable.virusFullScan[1]):
                        string = f"{string}\n Time execute: {round(globalVariable.virusFullScan[2], 3) + 11} seconds"
            else:
                string = f"No Virus Found\nTime execute {round(globalVariable.virusFullScan[2], 3) + 11}"

            self.virusFoundPaths.configure(state='normal')
            self.virusFoundPaths.delete("1.0", END)
            self.virusFoundPaths.insert(INSERT, string)
            self.stopFullScan = True

        id = self.virusFoundPaths.after(200, self.VirusFoundPathX)

    def load_hash_database(self):
        try:
            with open("src/DataBase/HashDataBase/Sha256/virusHash.unibit", "r") as nr:
                list = nr.readlines()
                nr.close()
            return list
        except Exception as e:
            print("Error loading hash database:", e)
            return []
