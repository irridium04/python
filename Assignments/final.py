# Collin Shook
# Final
# December 13 2022

import numpy as np
import matplotlib as mpl
import sys
import pandas as pd
from matplotlib import pyplot as plt


# --------------------- Global Variables ----------------------------

courses = []

months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
visitors = [100, 150, 175, 200, 300, 500, 600, 700, 400, 300, 200, 250]

visitorDataSet = list(zip(months, visitors))
sdata = [80,114,111,103,114,97,109,109,105,110,103,32,105,115,32,102,117,110,10,97,110,100,32,10,80,121,116,104,111,110,32,105,115,32,103,114,101,97,116,33]

# ------------------------- Classes ------------------------------------------------------

class Course():

    def __init__(self, _prefix = "", _coursenum = "", _title = ""):
        self._prefix = _prefix
        self._coursenum = _coursenum
        self._title = _title


    @property
    def prefix(self):
        return self._prefix

    @prefix.setter
    def prefix(self, val):
        self._prefix = val

    
    @property
    def coursenum(self):
        return self._coursenum

    @coursenum.setter
    def coursenum(self, val):
        self._coursenum = val    


    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, val):
        self._title = val


    def printCourse(self, index):
        print(f"{index}) {self._prefix} {self._coursenum} {self._title}")
        




# --------------------------- Functions --------------------------------------------------


def main():
    shouldContinue = "y"

    while(shouldContinue != "n"):
        menu()

        shouldContinue = input("Enter 'n' to quit or 'y' to continue!\n").lower()

    print("Goodbye\n")


def menu():
    invalidInput = True

    while(invalidInput):
        try:
            print("""
Final Exam Menu

1. Course classes.
2. Visitor Dataframe.
3. Print ascii message.
            """)

            choice = int(input("Choose 1-3!\n"))

            if(choice < 1 or choice > 3):
                print("Invalid answer!")
            else:
                invalidInput = False

        except:
            print("Invalid input!")


        if(choice == 1):
            Q1()
        elif (choice == 2):
            Q2()
        else:
            Q3()



def Q1():
    Q1menu()

def Q1menu():
    invalidInput = True

    while(invalidInput):
        try:
            print("""
Courses Menu

1. Print Courses
2. Add a course.
3. Remove a course.
            """)

            choice = int(input("Choose 1-3!\n"))

            if(choice < 1 or choice > 3):
                print("Invalid answer!")
            else:
                invalidInput = False

        except:
            print("Invalid input!")


        if(choice == 1):
            printCourses()
        elif (choice == 2):
            addCourse()
        else:
            removeCourse()

def printCourses():
    print()
    i = 1
    for course in courses:
        course.printCourse(i)
        i += 1

    print()


def addCourse():
    prefix = input("Enter course prefix!\n")
    invalidInput = True

    while(invalidInput):
        try:
            coursenum = int(input("Enter course number. Must be a whole number!\n"))
            invalidInput = False
        except:
            print("That wasn't a whole number!")

    title = input("Enter course title!\n")


    course = Course()

    course.prefix = prefix
    course.coursenum = coursenum
    course.title = title

    courses.append(course)

    printCourses()


def removeCourse():
    if (len(courses) == 0):
        print("No Courses to remove!")
    else:
        printCourses()

        invalidInput = True
        while(invalidInput):
            try:
                pos = int(input(f"Enter an index to delete! 1-{len(courses)}!\n"))
                if(pos < 1 or pos > len(courses)):
                    print("Invalid input")
                else:
                    invalidInput = False
            except:
                print("invalid input")

        ans = input(f"Type in 'YES' to confirm deletion of course {pos}!")

        if (ans == "YES"):
            del courses[pos - 1]
            print(f"Deleted course {pos}!")
            printCourses()
        else:
            print("Deletion Cancelled!")


def Q2():
    df = pd.DataFrame(data = visitorDataSet, index = months, columns=["Months", "Visitors"])
   
    minVisitors = df["Visitors"].min()
    maxVisitors = df["Visitors"].max()


    print(f"Max visitors: {maxVisitors}")
    print(f"Min visitors: {minVisitors}")

    df.plot(kind = 'line')

    plt.xlabel('Months')
    plt.ylabel('Visitors')
    plt.title(label='Visitations', loc='center')
   
    plt.show()

def Q3():
    for char in sdata:
        sys.stdout.write(chr(char))
    print()
    print()

    
main()