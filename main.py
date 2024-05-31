import engineCheckFolder
import time
import threading
import FullScan as handleFullScan

from tkinter import *

import globalVariable
from globalVariable import *
from src.engine import *

from src.realTime import RealTime
from tkinter import filedialog, messagebox

# --------------------Global Variable ---------------------#
isShowPopup = False
isOpenFile = False

virusName = []
virusPath = []
countPathVirusNow = []
hashList = []

# --------------------Global Variable End ---------------------#


# --------------------Tkinter Base Setup ---------------------#
# def print_position(event):
#     x = event.x
#     y = event.y
#     print("Position:", x, y)


window = Tk()

window.title("BitLink End-Point")
window.geometry("1200x780")
window.minsize("1200", "780")
window.maxsize("1200", "780")

winFrame = Frame(window, width="1200", height="780", bg="gray17")
winFrame.pack()
winFrame.pack_propagate(0)

window.geometry('1200x780+30+30')


# window.bind("<Button-1>", print_position)


# --------------------Tkinter Base Setup End ------------------#


def HomeFrame():
    # --------------------Global Var --------------------#
    global winFrame

    # --------------------Global Var End -----------------#

    winFrame.destroy()

    # --------------------Main Frame ---------------------#

    winFrame = Frame(window, width="1200", height="780", bg="gray17")
    winFrame.pack()
    winFrame.pack_propagate(0)

    # --------------------Main Frame End ------------------#

    # --------------------Logo Frame start --------------#

    # global logoLabelImg
    # logoLabelImg = PhotoImage(file='res\\Logo\\logo.png')
    # logoLabel = Label(winFrame, image=logoLabelImg, bg='gray17')
    # logoLabel.place(x=10, y=0)

    # global nameLabelImg
    # nameLabelImg = PhotoImage(file='res\\Logo\\b logo.png').subsample(2, 2)
    # nameLabel = Label(winFrame, image=nameLabelImg, bg='gray17')
    # nameLabel.place(x=90, y=20)
    # --------------------Logo Frame End ----------------#

    # --------------------Home Button --------------------#
    global homeButtonImg

    homeButtonImg = PhotoImage(file="res\\Home Frame\\Current\\Home.png")

    homeButton = Label(winFrame, image=homeButtonImg, bg="gray17", cursor="hand2")
    homeButton.place(x=300, y=570)

    # --------------------Home Button End------------------#

    # --------------------Scan Button ---------------------#

    scanButtonImg = PhotoImage(file="res\\Scan Frame\\Non-Hoved\\Scan.png")
    hovScanButtonImg = PhotoImage(file="res\\Scan Frame\\Hoved\\Scan.png")

    def ScanButtonEnterFrame(event):
        scanButton.config(image=hovScanButtonImg)

    def ScanButtonLeaveFrame(event):
        scanButton.config(image=scanButtonImg)

    def ScanButtonCall(event):
        ScanFrame()

    scanButton = Label(winFrame, image=scanButtonImg, bg="gray17", cursor="hand2")
    scanButton.place(x=520, y=570)

    scanButton.bind('<Enter>', ScanButtonEnterFrame)
    scanButton.bind('<Leave>', ScanButtonLeaveFrame)
    scanButton.bind('<Button-1>', ScanButtonCall)

    # #--------------------Scan Button End------------------#

    # #--------------------System Button -------------------#

    systemButtonImg = PhotoImage(file="res\\System Frame\\Non-Hoved\\System.png")
    hovsystemButtonImg = PhotoImage(file="res\\System Frame\\Hoved\\System.png")

    def SystemButtonEnterFrame(event):
        systemButton.config(image=hovsystemButtonImg)

    def SystemButtonLeaveFrame(event):
        systemButton.config(image=systemButtonImg)

    def SystemButtonCall(event):
        SystemFrame()

    systemButton = Label(winFrame, image=systemButtonImg, bg="gray17", cursor="hand2")
    systemButton.place(x=740, y=570)

    systemButton.bind('<Enter>', SystemButtonEnterFrame)
    systemButton.bind('<Leave>', SystemButtonLeaveFrame)
    systemButton.bind('<Button-1>', SystemButtonCall)

    # #--------------------System Button End ---------------#

    # #--------------------Animation --- ----------------#

    global robotImg
    robotImg = PhotoImage(file='res\\Home Frame\\Animation\\robotlink.png')

    robotAnimation = Label(winFrame, image=robotImg, bg="gray17")
    robotAnimation.place(x=405, y=150)

    global ani
    ani = 0

    def RobotAnimation():
        global ani

        if ani == 4:
            robotAnimation.place_configure(y=153)
            ani = 0

        elif ani == 2:
            robotAnimation.place_configure(y=150)

        ani += 1

        robotAnimation.after(200, RobotAnimation)

    RobotAnimation()

    # #--------------------Animation End ----------------#

    # #--------------------Sub-Frame --- ----------------#

    # #--------------------Proction-Frame --- ----------------#

    global protectionOn0Img

    protectionOn0Img = PhotoImage(file="res\\Home Frame\\Non-Hoved\\protection on0.png").subsample(2, 2)
    protectionOn0ImgHov = PhotoImage(file="res\\Home Frame\\Hoved\\protection on.png").subsample(2, 2)

    def ProtectionEnter(event):
        protectionOn0.config(image=protectionOn0ImgHov)

    def ProtectionLeave(event):
        protectionOn0.config(image=protectionOn0Img)

    def protectionOnClick(event):
        a = ["a", "b"]
        create_popup(a)

    protectionOn0 = Label(winFrame, image=protectionOn0Img, bg="gray17", cursor="hand2")
    protectionOn0.place(x=160, y=220)
    protectionOn0.bind('<Enter>', ProtectionEnter)
    protectionOn0.bind('<Leave>', ProtectionLeave)
    protectionOn0.bind("<Button-1>", protectionOnClick)

    # #--------------------Proction-Frame End ----------------#

    # #--------------------FireWall-Frame --- ----------------#

    global fireWallOnImg

    fireWallOnImg = PhotoImage(file="res\\Home Frame\\Non-Hoved\\fire wall on.png").subsample(2, 2)
    fireWallOnImgHov = PhotoImage(file="res\\Home Frame\\Hoved\\firewall.png").subsample(2, 2)

    def FireWallEnter(event):
        fireWallOn.config(image=fireWallOnImgHov)

    def FireWallLeave(event):
        fireWallOn.config(image=fireWallOnImg)

    fireWallOn = Label(winFrame, image=fireWallOnImg, bg="gray17", cursor="hand2")
    fireWallOn.place(x=830, y=220)

    fireWallOn.bind('<Enter>', FireWallEnter)
    fireWallOn.bind('<Leave>', FireWallLeave)

    # #--------------------FireWall-Frame End ----------------#

    # #--------------------QuickScan-Frame --- ----------------#

    global quickScanImg

    quickScanImg = PhotoImage(file="res\\Home Frame\\Non-Hoved\\quick scan.png").subsample(2, 2)
    quickScanImgHov = PhotoImage(file="res\\Home Frame\\Hoved\\Quck Scan.png").subsample(2, 2)

    def QuickScanEnter(e):
        quickScan.config(image=quickScanImgHov)

    def QuickScanLeave(e):
        quickScan.config(image=quickScanImg)

    quickScan = Label(winFrame, image=quickScanImg, bg="gray17", cursor="hand2")
    quickScan.place(x=150, y=280)
    quickScan.bind('<Enter>', QuickScanEnter)
    quickScan.bind('<Leave>', QuickScanLeave)

    # #--------------------QuickScan-Frame End ----------------#

    # #--------------------RamBooster-Frame --- ----------------#

    global ramBoosterImg

    ramBoosterImg = PhotoImage(file="res\\Home Frame\\Non-Hoved\\ram boost.png").subsample(2, 2)
    ramBoosterImgHov = PhotoImage(file="res\\Home Frame\\Hoved\\ram boost.png").subsample(2, 2)

    def RamBoosterEnter(e):
        ramBooster.config(image=ramBoosterImgHov)

    def RamBoosterLeave(e):
        ramBooster.config(image=ramBoosterImg)

    ramBooster = Label(winFrame, image=ramBoosterImg, bg="gray17", cursor="hand2")
    ramBooster.place(x=840, y=280)
    ramBooster.bind('<Enter>', RamBoosterEnter)
    ramBooster.bind('<Leave>', RamBoosterLeave)

    # #--------------------RamBooster-Frame End ----------------#

    # #--------------------Smart Scan-Frame --- ----------------#

    global smartScanLblImg

    smartScanLblImg = PhotoImage(file="res\\Home Frame\\Non-Hoved\\smart scan.png").subsample(2, 2)
    smartScanLblImgHov = PhotoImage(file="res\\Home Frame\\Hoved\\smart scan.png").subsample(2, 2)

    def smartScanLblEnter(e):
        smartScanLbl.config(image=smartScanLblImgHov)

    def smartScanLblLeave(e):
        smartScanLbl.config(image=smartScanLblImg)

    smartScanLbl = Label(winFrame, image=smartScanLblImg, bg="gray17", cursor="hand2")
    smartScanLbl.place(x=160, y=340)
    smartScanLbl.bind('<Enter>', smartScanLblEnter)
    smartScanLbl.bind('<Leave>', smartScanLblLeave)

    # #--------------------Smart Scan-Frame End ----------------#

    # #--------------------Help-Frame --- ----------------#

    global helpNsupportImg

    helpNsupportImg = PhotoImage(file="res\\Home Frame\\Non-Hoved\\help & support.png").subsample(2, 2)
    helpNsupportImgHov = PhotoImage(file="res\\Home Frame\\Hoved\\help.png").subsample(2, 2)

    def HelpEnter(e):
        helpNsupport.config(image=helpNsupportImgHov)

    def HelpLeave(e):
        helpNsupport.config(image=helpNsupportImg)

    helpNsupport = Label(winFrame, image=helpNsupportImg, bg="gray17", cursor="hand2")
    helpNsupport.place(x=830, y=340)
    helpNsupport.bind("<Enter>", HelpEnter)
    helpNsupport.bind("<Leave>", HelpLeave)

    # #--------------------Help-Frame End ----------------#

    # #--------------------Sub-Frame End ----------------#


##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################


def ScanFrame():
    # --------------------Global Var --------------------#
    global winFrame

    # --------------------Global Var End -----------------#

    winFrame.destroy()

    # --------------------Main Frame ---------------------#

    winFrame = Frame(window, width="1200", height="780", bg="gray17")
    winFrame.pack()
    winFrame.pack_propagate(0)

    # --------------------Main Frame End ------------------#

    # --------------------Logo Frame start --------------#

    # global logoLabelImg
    # logoLabelImg = PhotoImage(file='res\\Logo\\logo.png')
    # logoLabel = Label(winFrame, image=logoLabelImg, bg='gray17')
    # logoLabel.place(x=10, y=0)

    # global nameLabelImg
    # nameLabelImg = PhotoImage(file='res\\Logo\\b logo.png').subsample(2, 2)
    # nameLabel = Label(winFrame, image=nameLabelImg, bg='gray17')
    # nameLabel.place(x=90, y=20)
    # --------------------Logo Frame End ----------------#

    # --------------------Quick_Scan --------------------#

    global quickScanButton_1
    global quickScanButton_1_Hoved

    quickScanButton_1 = PhotoImage(file='res\\Scan Frame\\Non-Hoved\\Quick Scan.png').subsample(2, 2)
    quickScanButton_1_Hoved = PhotoImage(file='res\\Scan Frame\\Hoved\\Quick Scan.png').subsample(2, 2)

    def quickScanButton_1_Enter(e):
        quickScanButton_1place.config(image=quickScanButton_1_Hoved)

    def quickScanButton_1_Leave(e):
        quickScanButton_1place.config(image=quickScanButton_1)

    def scanFile(event):

        filename = filedialog.askopenfilename()
        if filename:
            engine = virusScannerAPI(filename)
            if engine != 0:
                print(engine)
                showPopupCheckFileInfo(engine)
            else:
                messagebox.showinfo("Thông báo", "No Virus Detected")

    quickScanButton_1place = Label(winFrame, image=quickScanButton_1, bg='gray17', cursor="hand2")
    quickScanButton_1place.place(x=530, y=100)

    quickScanButton_1place.bind('<Enter>', quickScanButton_1_Enter)
    quickScanButton_1place.bind('<Leave>', quickScanButton_1_Leave)
    quickScanButton_1place.bind("<Button-1>", scanFile)

    # --------------------Quick_Scan End ----------------#

    # --------------------Deep_Scan --------------------#

    global deepScanButton_1
    global deepScanButton_1_Hoved

    deepScanButton_1 = PhotoImage(file='res\\Scan Frame\\Non-Hoved\\Deep Scan.png').subsample(2, 2)
    deepScanButton_1_Hoved = PhotoImage(file='res\\Scan Frame\\Hoved\\Deep Scan.png').subsample(2, 2)

    def deepScanButton_1_Enter(e):
        deepScanButton_1place.config(image=deepScanButton_1_Hoved)

    def deepScanButton_1_Leave(e):
        deepScanButton_1place.config(image=deepScanButton_1)

    def scanFolder(event):
        folder_path = filedialog.askdirectory()
        task(folder_path)

    def task(pathFolder):
        time.sleep(2)
        time_execute = engineCheckFolder.folderScanner(pathFolder)

        popup = Toplevel(winFrame)
        popup.title("Scan folder")
        popup.minsize("600", "300")
        popup.maxsize("600", "300")
        window_width = window.winfo_width()
        window_height = window.winfo_height()
        popup.resizable(False, False)
        popup_width = 400
        popup_height = 200
        x_position = (window_width - popup_width) // 2
        y_position = (window_height - popup_height) // 2
        popup.geometry(f"{popup_width}x{popup_height}+{x_position}+{y_position}")
        popup.lift()
        custom_font = ("Helvetica", 14)

        if engineCheckFolder.virusName:
            for virus in engineCheckFolder.virusName:
                label = Label(popup, text=f"{virus}", wraplength=600, fg="#c52420", font=custom_font)
                label.pack()
        else:
            label = Label(popup, text="No Virus Detected", fg="#39ac4c", font=custom_font)
            label.pack()

        label_show_time = Label(popup, text=f"Time execute {time_execute}", fg="#39ac4c")
        label_show_time.pack()

    deepScanButton_1place = Label(winFrame, image=deepScanButton_1, bg='gray17', cursor="hand2")
    deepScanButton_1place.place(x=510, y=170)

    deepScanButton_1place.bind('<Enter>', deepScanButton_1_Enter)
    deepScanButton_1place.bind('<Leave>', deepScanButton_1_Leave)
    deepScanButton_1place.bind("<Button-1>", scanFolder)

    # --------------------Deep_Scan End ----------------#

    # --------------------Full_Scan --------------------#

    global fullScanButton_1
    global fullScanButton_1_Hoved

    fullScanButton_1 = PhotoImage(file='res\\Scan Frame\\Non-Hoved\\Full Scan.png').subsample(2, 2)
    fullScanButton_1_Hoved = PhotoImage(file='res\\Scan Frame\\Hoved\\Full Scan.png').subsample(2, 2)

    def fullScanButton_1_Enter(e):
        fullScanButton_1place.config(image=fullScanButton_1_Hoved)

    def fullScanButton_1_Leave(e):
        fullScanButton_1place.config(image=fullScanButton_1)

    def fullScanHandle(e):
        global isOpenFile
        global hashList

        frame_full_scan = Frame(winFrame)
        frame_full_scan.pack()
        full_scan = handleFullScan.FullScan(frame_full_scan)
        full_scan.textShower()
        full_scan.progressBarAni()
        isOpenFile = True
        full_scan.VirusFoundPathX()

    fullScanButton_1place = Label(winFrame, image=fullScanButton_1, bg='gray17', cursor="hand2")
    fullScanButton_1place.place(x=510, y=240)
    fullScanButton_1place.bind('<Enter>', fullScanButton_1_Enter)
    fullScanButton_1place.bind('<Leave>', fullScanButton_1_Leave)
    fullScanButton_1place.bind('<Button-1>', fullScanHandle)

    # --------------------Full_Scan End ----------------#

    # --------------------Custom_Scan --------------------#

    global CustomScanButton_1
    global CustomScanButton_1_Hoved

    CustomScanButton_1 = PhotoImage(file='res\\Scan Frame\\Non-Hoved\\Custom Scan.png').subsample(2, 2)
    CustomScanButton_1_Hoved = PhotoImage(file='res\\Scan Frame\\Hoved\\Custom Scan.png').subsample(2, 2)

    def CustomScanButton_1_Enter(e):
        CustomScanButton_1place.config(image=CustomScanButton_1_Hoved)

    def CustomScanButton_1_Leave(e):
        CustomScanButton_1place.config(image=CustomScanButton_1)

    def customBtn(e):
        print(len(hashList))

    CustomScanButton_1place = Label(winFrame, image=CustomScanButton_1, bg='gray17', cursor="hand2")
    CustomScanButton_1place.place(x=530, y=310)

    CustomScanButton_1place.bind('<Enter>', CustomScanButton_1_Enter)
    CustomScanButton_1place.bind('<Leave>', CustomScanButton_1_Leave)
    CustomScanButton_1place.bind('<Button-1>', customBtn)

    # --------------------Custom_Scan End ----------------#

    # --------------------Main Logo ----------------------#

    global scanFrameMainLogo
    global scanFrameMainLogoHoved
    scanFrameMainLogo = PhotoImage(file='res\\Scan Frame\\main logo.png')
    scanFrameMainLogoHoved = PhotoImage(file='res\\Scan Frame\\main logo hoved.png')

    def scanFrameMainLogoEnter(event):
        scanFrameMainLogoPlace.config(image=scanFrameMainLogoHoved)

    def scanFrameMainLogoLeave(event):
        scanFrameMainLogoPlace.config(image=scanFrameMainLogo)

    scanFrameMainLogoPlace = Label(winFrame, image=scanFrameMainLogo, bg='gray17', cursor="hand2")
    scanFrameMainLogoPlace.place(x=772, y=100)

    scanFrameMainLogoPlace.bind('<Enter>', scanFrameMainLogoEnter)
    scanFrameMainLogoPlace.bind('<Leave>', scanFrameMainLogoLeave)

    # --------------------Main Logo End-------------------#

    # --------------------Home Button --------------------#

    homeButtonImg = PhotoImage(file="res\\Home Frame\\Non-Hoved\\Home.png")
    hovHomeButtonImg = PhotoImage(file="res\\Home Frame\\Hoved\\Home.png")

    def HomeButtonEnterFrame(event):
        homeButton.config(image=hovHomeButtonImg)

    def HomeButtonLeaveFrame(event):
        homeButton.config(image=homeButtonImg)

    def HomeButtonCall(event):
        HomeFrame()

    homeButton = Label(winFrame, image=homeButtonImg, bg="gray17", cursor="hand2")
    homeButton.place(x=300, y=570)

    homeButton.bind('<Enter>', HomeButtonEnterFrame)
    homeButton.bind('<Leave>', HomeButtonLeaveFrame)
    homeButton.bind('<Button-1>', HomeButtonCall)

    # --------------------Home Button End------------------#

    # --------------------Scan Button ---------------------#

    global scanButtonImg

    scanButtonImg = PhotoImage(file="res\\Scan Frame\\Current\\Scan.png")

    scanButton = Label(winFrame, image=scanButtonImg, bg="gray17", cursor="hand2")
    scanButton.place(x=520, y=570)

    # #--------------------Scan Button End------------------#

    # #--------------------System Button -------------------#

    systemButtonImg = PhotoImage(file="res\\System Frame\\Non-Hoved\\System.png")
    hovsystemButtonImg = PhotoImage(file="res\\System Frame\\Hoved\\System.png")

    def SystemButtonEnterFrame(event):
        systemButton.config(image=hovsystemButtonImg)

    def SystemButtonLeaveFrame(event):
        systemButton.config(image=systemButtonImg)

    def SystemButtonCall(event):
        SystemFrame()

    systemButton = Label(winFrame, image=systemButtonImg, bg="gray17", cursor="hand2")
    systemButton.place(x=740, y=570)

    systemButton.bind('<Enter>', SystemButtonEnterFrame)
    systemButton.bind('<Leave>', SystemButtonLeaveFrame)
    systemButton.bind('<Button-1>', SystemButtonCall)

    def threadOpenFile():
        global hashList
        while True:
            if isOpenFile == True:
                with open(
                        "C:\\Users\\trinhhuynh\\Desktop\\DACN4\\src\\DataBase\\HashDataBase\\Md5\\md5HashOfVirus.unibit",
                        "r") as i:
                    hashList = i.readlines()
                    i.close()

            if len(hashList) > 0:
                io = Engine(hashList)
                globalVariable.virusFullScan = io.virusScannerMd5("C:\\Users\\trinhhuynh\\Desktop")
                globalVariable.statusHandleFullScan = True
                print(globalVariable.virusFullScan)
                break

    # tao thread
    threadOpenFile = threading.Thread(target=threadOpenFile)
    threadOpenFile.start()

    # #--------------------System Button End ---------------#


##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################


def SystemFrame():
    # --------------------Global Var --------------------#
    global winFrame

    # --------------------Global Var End -----------------#

    winFrame.destroy()

    # --------------------Main Frame ---------------------#

    winFrame = Frame(window, width="1200", height="780", bg="gray17")
    winFrame.pack()
    winFrame.pack_propagate(0)

    # --------------------Main Frame End ------------------#

    # --------------------Logo Frame start --------------#

    # global logoLabelImg
    # logoLabelImg = PhotoImage(file='res\\Logo\\logo.png')
    # logoLabel = Label(winFrame, image=logoLabelImg, bg='gray17')
    # logoLabel.place(x=10, y=0)

    # global nameLabelImg
    # nameLabelImg = PhotoImage(file='res\\Logo\\b logo.png').subsample(2, 2)
    # nameLabel = Label(winFrame, image=nameLabelImg, bg='gray17')
    # nameLabel.place(x=90, y=20)
    # --------------------Logo Frame End ----------------#

    # --------------------Protection --------------------#

    global protectionButton_1
    global protectionButton_1_Hoved

    protectionButton_1 = PhotoImage(file='res\\System Frame\\Non-Hoved\\protection.png').subsample(2, 2)
    protectionButton_1_Hoved = PhotoImage(file='res\\System Frame\\Hoved\\protection.png').subsample(2, 2)

    def protectionButton_1_Enter(e):
        protectionButton_1place.config(image=protectionButton_1_Hoved)

    def protectionButton_1_Leave(e):
        protectionButton_1place.config(image=protectionButton_1)

    protectionButton_1place = Label(winFrame, image=protectionButton_1, bg='gray17', cursor="hand2")
    protectionButton_1place.place(x=530, y=100)

    protectionButton_1place.bind('<Enter>', protectionButton_1_Enter)
    protectionButton_1place.bind('<Leave>', protectionButton_1_Leave)

    # --------------------Protection End ----------------#

    # --------------------Firewall --------------------#

    global firewallButton_1
    global firewallButton_1_Hoved

    firewallButton_1 = PhotoImage(file='res\\System Frame\\Non-Hoved\\firewall.png').subsample(2, 2)
    firewallButton_1_Hoved = PhotoImage(file='res\\System Frame\\Hoved\\firewall.png').subsample(2, 2)

    def firewallButton_1_Enter(e):
        firewallButton_1place.config(image=firewallButton_1_Hoved)

    def firewallButton_1_Leave(e):
        firewallButton_1place.config(image=firewallButton_1)

    firewallButton_1place = Label(winFrame, image=firewallButton_1, bg='gray17', cursor="hand2")
    firewallButton_1place.place(x=510, y=170)

    firewallButton_1place.bind('<Enter>', firewallButton_1_Enter)
    firewallButton_1place.bind('<Leave>', firewallButton_1_Leave)

    # --------------------Firewall End ----------------#

    # --------------------System Health --------------------#

    global systemHealthButton_1
    global systemHealthButton_1_Hoved

    systemHealthButton_1 = PhotoImage(file='res\\System Frame\\Non-Hoved\\system health.png').subsample(2, 2)
    systemHealthButton_1_Hoved = PhotoImage(file='res\\System Frame\\Hoved\\system health.png').subsample(2, 2)

    def systemHealthButton_1_Enter(e):
        systemHealthButton_1place.config(image=systemHealthButton_1_Hoved)

    def systemHealthButton_1_Leave(e):
        systemHealthButton_1place.config(image=systemHealthButton_1)

    systemHealthButton_1place = Label(winFrame, image=systemHealthButton_1, bg='gray17', cursor="hand2")
    systemHealthButton_1place.place(x=510, y=240)

    systemHealthButton_1place.bind('<Enter>', systemHealthButton_1_Enter)
    systemHealthButton_1place.bind('<Leave>', systemHealthButton_1_Leave)

    # --------------------System Health End ----------------#

    # --------------------System Report --------------------#

    global systemReportButton_1
    global systemReportButton_1_Hoved

    systemReportButton_1 = PhotoImage(file='res\\System Frame\\Non-Hoved\\system report.png').subsample(2, 2)
    systemReportButton_1_Hoved = PhotoImage(file='res\\System Frame\\Hoved\\system report.png').subsample(2, 2)

    def systemReportButton_1_Enter(e):
        systemReportButton_1place.config(image=systemReportButton_1_Hoved)

    def systemReportButton_1_Leave(e):
        systemReportButton_1place.config(image=systemReportButton_1)

    systemReportButton_1place = Label(winFrame, image=systemReportButton_1, bg='gray17', cursor="hand2")
    systemReportButton_1place.place(x=530, y=310)

    systemReportButton_1place.bind('<Enter>', systemReportButton_1_Enter)
    systemReportButton_1place.bind('<Leave>', systemReportButton_1_Leave)

    # --------------------System Report End ----------------#

    # --------------------Main Logo ----------------------#

    global systemFrameMainLogo
    global systemFrameMainLogoHoved
    systemFrameMainLogo = PhotoImage(file='res\\System Frame\\main frame logo.png')
    systemFrameMainLogoHoved = PhotoImage(file='res\\System Frame\\main frame logo hoved.png')

    def systemFrameMainLogoEnter(event):
        systemFrameMainLogoPlace.config(image=systemFrameMainLogoHoved)

    def systemFrameMainLogoLeave(event):
        systemFrameMainLogoPlace.config(image=systemFrameMainLogo)

    systemFrameMainLogo = PhotoImage(file='res\\System Frame\\main frame logo.png')
    systemFrameMainLogoPlace = Label(winFrame, image=systemFrameMainLogo, bg='gray17')
    systemFrameMainLogoPlace.place(x=772, y=100)

    systemFrameMainLogoPlace.bind('<Enter>', systemFrameMainLogoEnter)
    systemFrameMainLogoPlace.bind('<Leave>', systemFrameMainLogoLeave)

    # --------------------Main Logo End-------------------#

    # --------------------Home Button --------------------#

    homeButtonImg = PhotoImage(file="res\\Home Frame\\Non-Hoved\\Home.png")
    hovHomeButtonImg = PhotoImage(file="res\\Home Frame\\Hoved\\Home.png")

    def HomeButtonEnterFrame(event):
        homeButton.config(image=hovHomeButtonImg)

    def HomeButtonLeaveFrame(event):
        homeButton.config(image=homeButtonImg)

    def HomeButtonCall(event):
        HomeFrame()

    homeButton = Label(winFrame, image=homeButtonImg, bg="gray17", cursor="hand2")
    homeButton.place(x=300, y=570)

    homeButton.bind('<Enter>', HomeButtonEnterFrame)
    homeButton.bind('<Leave>', HomeButtonLeaveFrame)
    homeButton.bind('<Button-1>', HomeButtonCall)

    # --------------------Home Button End------------------#

    # --------------------Scan Button ---------------------#

    scanButtonImg = PhotoImage(file="res\\Scan Frame\\Non-Hoved\\Scan.png")
    hovScanButtonImg = PhotoImage(file="res\\Scan Frame\\Hoved\\Scan.png")

    def ScanButtonEnterFrame(event):
        scanButton.config(image=hovScanButtonImg)

    def ScanButtonLeaveFrame(event):
        scanButton.config(image=scanButtonImg)

    def ScanButtonCall(event):
        ScanFrame()

    scanButton = Label(winFrame, image=scanButtonImg, bg="gray17", cursor="hand2")
    scanButton.place(x=520, y=570)

    scanButton.bind('<Enter>', ScanButtonEnterFrame)
    scanButton.bind('<Leave>', ScanButtonLeaveFrame)
    scanButton.bind('<Button-1>', ScanButtonCall)

    # #--------------------Scan Button End------------------#

    # #--------------------System Button -------------------#

    global systemButtonImg

    systemButtonImg = PhotoImage(file="res\\System Frame\\Current\\System.png")

    systemButton = Label(winFrame, image=systemButtonImg, bg="gray17", cursor="hand2")
    systemButton.place(x=740, y=570)

    # #--------------------System Button End ---------------#


def showPopupCheckFileInfo(info):
    popup = Toplevel(winFrame)
    popup.title("File name: " + info['nameFile'])
    popup.minsize("600", "300")
    popup.maxsize("600", "300")
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    popup.resizable(False, False)
    popup_width = 400
    popup_height = 200
    x_position = (window_width - popup_width) // 2
    y_position = (window_height - popup_height) // 2
    popup.geometry(f"{popup_width}x{popup_height}+{x_position}+{y_position}")
    popup.lift()

    custom_font = ("Helvetica", 16)
    custom_color = "#c52420"

    for threat in info['popular_threat_category']:
        popular_threat_category = Label(popup, text=f"Threat category: {threat['value']} count: {threat['count']}",
                                        font=custom_font, fg=custom_color)
        popular_threat_category.pack()
    type_tag = Label(popup, text=f"Type tag: {info['type_tag']}", font=custom_font, fg=custom_color)
    md5 = Label(popup, text=f"Md5: {info['md5']}", font=custom_font, fg=custom_color)
    malicious = Label(popup, text=f"Malicious: {info['malicious']}", font=custom_font, fg=custom_color)
    nameFile = Label(popup, text=f"File name: {info['nameFile']}", font=custom_font, fg=custom_color)
    type_tag.pack()
    md5.pack()
    malicious.pack()
    nameFile.pack()


def create_popup(listPath):
    global isShowPopup

    popup = Toplevel(winFrame)
    popup.title("Popup")

    popup.minsize("600", "300")
    popup.maxsize("600", "300")

    # Lấy kích thước của cửa sổ gốc
    window_width = window.winfo_width()
    window_height = window.winfo_height()

    popup.resizable(False, False)

    # Lấy kích thước của popup
    popup_width = 400
    popup_height = 200

    # Xu ly nut x
    popup.protocol("WM_DELETE_WINDOW", lambda: on_closing(popup))

    # Tính toán vị trí cho popup
    x_position = (window_width - popup_width) // 2
    y_position = (window_height - popup_height) // 2
    # Đặt vị trí cho popup
    popup.geometry(f"{popup_width}x{popup_height}+{x_position}+{y_position}")
    popup.lift()

    virusPath = Label(popup, text="Virus")

    create_labels(popup, listPath)
    isShowPopup = True

    buttonReload = Button(popup, text="Reload", highlightthickness=0,
                          command=lambda: reloadBtn(popup))
    buttonReload.place(x=100, y=100)


def reloadBtn(root):
    for widget in root.winfo_children():
        if widget and widget.cget("text") != "Reload":
            widget.destroy()
    create_labels(root, pathVirus)


def on_closing(root):
    global isShowPopup

    if messagebox.askokcancel("Thoát", "Bạn có chắc chắn muốn thoát không?"):
        root.destroy()
        isShowPopup = False


def create_labels(root, data):
    numColumn = 0
    numRow = 0
    for i, item in enumerate(data):
        label = Label(root, text=f"Path: {item}")
        button = Button(root, text="Delete file", highlightthickness=0, width=10, height=0,
                        command=lambda: handleRemovePathFile(root, item))
        labelSpace = Label(root, text="      ")

        label.grid(row=numRow, column=numColumn)
        numColumn += 1
        labelSpace.grid(row=numRow, column=numColumn)
        numColumn += 1
        button.grid(row=numRow, column=numColumn, sticky="e")
        numRow += 1
        labelFake = Label(root, text="    ")
        labelFake.grid(row=numRow)
        numRow += 1

        numColumn = 0


def handleRemovePathFile(root, pathFile):
    if messagebox.askokcancel("Remove", "Bạn có chắc chắn muốn xóa không ?") and pathVirus:
        os.remove(pathFile)
        pathVirus.remove(pathFile)
        reloadBtn(root)


def runRealTimeProtection():
    time.sleep(5)
    RealTime()


def handleThreadCheckShowPopupLoop():
    while True:
        if (isShowPopup == False and pathVirus):
            print("handleThreadCheckShowPopupLoop")
            if (pathVirus):
                create_popup(pathVirus)

        # Thực hiện sau mỗi 10 giây
        time.sleep(10)


threadRealTime = threading.Thread(target=runRealTimeProtection)
threadCheckShowPopup = threading.Thread(target=handleThreadCheckShowPopupLoop)

threadRealTime.start()
threadCheckShowPopup.start()

HomeFrame()
window.mainloop()

# def process1():
#     HomeFrame()
#     window.mainloop()
#
#
# def process2():
#     RealTime()
#
#
# if __name__ == "__main__":
#     p1 = multiprocessing.Process(target=process1)
#     p2 = multiprocessing.Process(target=process2)
#
#     p1.start()
#     p2.start()
#
#     p1.join()
#     p2.join()
