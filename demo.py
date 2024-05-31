from tkinter import *
from tkinter import filedialog
import random
import os
import time


window = Tk()

window.title("BitLink Aqua")
window.geometry('1100x600')
window.maxsize("1100","600")
window.minsize("1100","600")

nj = Frame(window, width=1100, height = 600)
nj.pack()
nj.pack_propagate(0)


def quickScanFrame():
    global nj
    global backButtonImg
    global prog0
    global prog1
    global prog2
    global prog3
    global prog4
    global prog5
    global io
    global ranHashShower
    global samB
    global rMVirus

    with open("src/DataBase/HashDataBase/Sha256/virusHash.unibit", "r") as nr:
        samB = nr.readlines()
        nr.close()

    nj.destroy()

    nj = Frame(window, width=1100, height=600)
    nj.pack()
    nj.pack_propagate(0)

    io = 0

    def removeVirusBtn():
        try:
            with open("switch_virusscanner.bb", "r") as bb:
                io = list(bb.readlines())
                bb.close()
        except:
            pass

        try:
            for i in io:
                i = i[0:len(i) - 1]
                print(i, " Removed")
                os.remove(i)
        except:
            pass

    removeVirusBtn()

    def progressBarAni():
        global io

        progLabel.configure(image=progList[io])

        io += 1

        id = progLabel.after(500, progressBarAni)

        if io == 5:
            io = 0
            try:
                with open("switch_io.bb", "r") as nri:
                    xxc = nri.read()
                    nri.close()

                if xxc == "1" or xxc == 1:
                    progLabel.after_cancel(id)

            except:
                pass



    def textShower():
        global samB

        ranHashShower.configure(state='normal')
        ranHashShower.delete("1.0", END)
        ranHashShower.insert(INSERT, samB[random.randint(0, len(samB) - 1)])

        id = ranHashShower.after(100, textShower)

        try:
            with open("switch_io.bb", "r") as nri:
                xxc = nri.read()
                nri.close()

            if xxc == "1" or xxc == 1:
                ranHashShower.after_cancel(id)

        except:
            pass

    def VirusFoundPathX():
        try:
            with open("switch_virusscanner.bb", "r") as X:
                cc = X.readlines()
                X.close()

            virusFoundPaths.configure(state='normal')
            virusFoundPaths.delete("1.0", END)
            virusFoundPaths.insert(INSERT, cc)

        except:
            pass

        id = virusFoundPaths.after(200, VirusFoundPathX)

    backButtonImg = PhotoImage(file="res\\back button.png").subsample(4, 4)
    prog0 = PhotoImage(file="res\\progress bar\\0.png").subsample(1, 3)
    prog1 = PhotoImage(file="res\\progress bar\\1.png").subsample(1, 3)
    prog2 = PhotoImage(file="res\\progress bar\\2.png").subsample(1, 3)
    prog3 = PhotoImage(file="res\\progress bar\\3.png").subsample(1, 3)
    prog4 = PhotoImage(file="res\\progress bar\\4.png").subsample(1, 3)
    prog5 = PhotoImage(file="res\\progress bar\\5.png").subsample(1, 3)
    progList = [prog0, prog1, prog2, prog3, prog4, prog5]

    bitLinkMainLabel = Label(nj, text="Quick Scan", font="Times 21 bold")
    bitLinkMainLabel.pack(side=TOP, pady=20)

    backButton = Button(nj, image=backButtonImg, bd=0, command=mainFrameNj)
    backButton.place(x=10, y=10)

    progLabel = Label(nj, image=prog0)
    progLabel.place(x=250, y=70)

    pathLabel = Label(nj, text="Virus Scanner", font="Times 20 bold")
    pathLabel.place(x=350, y=130)

    ranHashShower = Text(nj, width=50, height=1, bd=0, font=('Sans Serif', 13, 'bold'), foreground="green")
    ranHashShower.place(x=350, y=170)
    ranHashShower.insert(INSERT, "Write Something About Yourself")
    ranHashShower.configure(state='disabled')

    virusDetet = Label(nj, text="Virus Found", font="Times 20 bold")
    virusDetet.place(x=350, y=230)

    virusFoundPaths = Text(nj, width=100, height=10, bd=0, font=('Sans Serif', 13, 'bold'), foreground="red")
    virusFoundPaths.place(x=50, y=290)
    virusFoundPaths.insert(INSERT, "No Virus Found")
    virusFoundPaths.configure(state='disabled')

    rMVirus = Button(nj, text="Remove Virus", font="Times 20 bold", command=removeVirusBtn)
    rMVirus.place(x=350, y=230)

    textShower()

    progressBarAni()



quickScanFrame()

window.mainloop()