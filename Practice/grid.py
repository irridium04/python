import sys


def main():
    triangle()


def grid():
    valid = False
    while (not valid):
        try:
            cols = int(input("Please enter amount of columns for grid."))
            valid = True
            try:
                rows = int(input("Please enter amount of rows for grid."))
                valid = True
            except:
                print("Not an integer")
                valid = False
        except:
            print("Not an integer")
            valid = False

    for i in range(rows):
        for j in range(cols):
            sys.stdout.write("⭐")
        sys.stdout.write("\n")

def triangle():
    valid = False
    while (not valid):
        try:
            cols = int(input("Please enter amount of columns for grid."))
            valid = True
            try:
                rows = int(input("Please enter amount of rows for grid."))
                valid = True
            except:
                print("Not an integer")
                valid = False
        except:
            print("Not an integer")
            valid = False

    for i in range(rows):
        spaces = "  " * i
        stars = "⭐" * (cols - i)
        print(spaces + stars)


    

main()