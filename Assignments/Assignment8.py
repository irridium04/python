# Collin Shook
# November 15, 2022
# Tkinter


import sys
import tkinter as tk
import math
from tkinter import messagebox

theFrame = tk.Tk()

# add title

theFrame.title("Quadratic Calculator")

# height and width
frameWidth = 285
frameHeight = 170


# get screen size
scrnH = theFrame.winfo_screenheight()
scrnW = theFrame.winfo_screenwidth()


# calculate center of screen

xpos = int((scrnW / 2) - (frameWidth / 2))
ypos = int((scrnH / 2) - (frameHeight / 2))


theFrame.geometry(f"{frameWidth}x{frameHeight}+{xpos}+{ypos}")


def calc():
    try:
        a = float(inNum1.get("1.0", "end"))
        b = float(inNum2.get("1.0", "end"))
        c = float(inNum3.get("1.0", "end"))

        print(f"A:{a} B:{b} C:{c}")

        ans1 = (((b * -1) + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a))
        
        stringAns1 = str(round(ans1, 8))
        
    except:
        stringAns1 = "Error"
    finally:
        lblAns1["text"] = stringAns1

    try:
        a = float(inNum1.get("1.0", "end"))
        b = float(inNum2.get("1.0", "end"))
        c = float(inNum3.get("1.0", "end"))

        ans2 = (((b * -1) - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a))

        stringAns2 = str(round(ans2, 8))
    except:
        stringAns2 = "Error"
    finally:
        lblAns2["text"] = stringAns2




def clearBoxes():
    inNum1.delete("1.0", "end")
    inNum2.delete("1.0", "end")
    inNum3.delete("1.0", "end")


def focusNextWidget():
    print("Next Widget")


def closeWindow():
    if messagebox.askokcancel("Quit", "Do you want to exit?"):
        theFrame.destroy()
        sys.exit(0)


theFrame.configure(bg='#202020')

tk.Label(theFrame, text="A", bg="#b31200",
         fg="#FFFFFF").place(x=10, y=10)


inNum1 = tk.Text(theFrame, height=1, width=10)
inNum1.place(x=40, y=10)

tk.Label(theFrame, text="B", bg="#b31200",
         fg="#FFFFFF").place(x=10, y=40)


inNum2 = tk.Text(theFrame, height=1, width=10)
inNum2.place(x=40, y=40)

tk.Label(theFrame, text="C", bg="#b31200",
         fg="#FFFFFF").place(x=10, y=70)


inNum3 = tk.Text(theFrame, height=1, width=10)
inNum3.place(x=40, y=70)

tk.Label(theFrame, text="X1:", bg="#b31200",
         fg="#FFFFFF").place(x=150, y=10)

tk.Label(theFrame, text="X2:", bg="#b31200",
         fg="#FFFFFF").place(x=150, y=40)

bttnCalc = tk.Button(theFrame, text="Calculate", height=2, width=10, command=calc)
bttnCalc.place(x=10, y=110)

bttnClear = tk.Button(theFrame, text="Clear", height=2, width=10, bg="#b31200", fg="#ffffff", command=clearBoxes)
bttnClear.place(x=195, y=110)


lblAns1 = tk.Label(theFrame, text="", bg="#1200b3", fg="#FFFFFF")
lblAns1.place(x=190, y=10)
lblAns2 = tk.Label(theFrame, text="", bg="#1200b3", fg="#FFFFFF")
lblAns2.place(x=190, y=40)

bttnClear.bind("<Return>", clearBoxes)
bttnClear.bind("<Button-1>", clearBoxes)
bttnClear.bind("<Tab>", focusNextWidget)


theFrame.mainloop()
