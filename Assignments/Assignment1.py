import tkinter as tk


theFrame = tk.Tk()

# add title

theFrame.title("Calculator")

# height and width
frameWidth = 370
frameHeight = 190


# get screen size
scrnH = theFrame.winfo_screenheight()
scrnW = theFrame.winfo_screenwidth()


# calculate center of screen

xpos = int((scrnW / 2) - (frameWidth / 2))
ypos = int((scrnH / 2) - (frameHeight / 2))


theFrame.geometry(f"{frameWidth}x{frameHeight}+{xpos}+{ypos}")

def addBoxes():
    try:
        ans = float(inNum1.get("1.0", "end")) + float(inNum2.get("1.0", "end"))
        stringAns = str(ans)
    except :
        stringAns = "Error"
    finally:
        lblAns["text"] = stringAns


def subtractBoxes():
    print("Subtract")


def multiplyBoxes():
    print("Multiply")


def divideBoxes():
    print("Divide")


def expBoxes():
    print("expontental")

def nRootBoxes():
    print("N root")

def logBoxes():
    print("Logarithm")

def clearBoxes():
    print("Clear")

def focusNextWidget():
    print("Next Widget")




theFrame.configure(bg ='#202020')

tk.Label(theFrame, text="Number 1", bg="#b31200", fg="#FFFFFF").place(x=10, y=10)


inNum1 = tk.Text(theFrame, height=1, width=10)
inNum1.place(x=100,y=10)

tk.Label(theFrame, text="Number 2", bg="#b31200", fg="#FFFFFF").place(x=10, y=40)


inNum2 = tk.Text(theFrame, height=1, width=10)
inNum2.place(x=100, y=40)



bttnAdd = tk.Button(theFrame, text="+", height=2,width=10,command = addBoxes).place(x=10,y=70)
bttnSubtract = tk.Button(theFrame, text="-", height=2, width=10,command=subtractBoxes).place(x=100, y=70)
bttnMultiply = tk.Button(theFrame, text="X", height=2,width=10, command=multiplyBoxes).place(x=190, y=70)
bttnDivide = tk.Button(theFrame, text="/", height=2,width=10, command=divideBoxes).place(x=280, y=70)
bttnExp = tk.Button(theFrame, text="X^Y", height=2, width=10,command=expBoxes).place(x=10, y=130)
bttnNroot = tk.Button(theFrame, text="X rt Y", height=2, width=10, command=nRootBoxes).place(x=100, y=130)
bttnLog = tk.Button(theFrame, text="log x(Y)", height=2,width=10, command= logBoxes).place(x=190, y=130)
bttnClear = tk.Button(theFrame, text="Clear", height=2, width=10, bg="#b31200", fg="#ffffff", command =clearBoxes).place(x=280, y=130)


lblAns = tk.Label(theFrame, text="", bg="#b31200",fg="#FFFFFF").place(x=200, y=10)

# bttnClear.bind("<Return>", clearBoxes)
# bttnClear.bind("<Button-1>", clearBoxes)
# bttnClear.bind("<Tab>", focusNextWidget)


theFrame.mainloop()