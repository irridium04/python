class Element():

    def __init__(self, _name = "", _symbol = "", _series ="", _num = 1):
        self._name = _name
        self._symbol = _symbol
        self._series = _series
        self._num = _num

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        self._symbol = value

    @property
    def series(self):
        return self._series

    @series.setter
    def series(self, value):
        self._series = value

    @property
    def atomicNumber(self):
        return self._num

    @atomicNumber.setter
    def atomicNumber(self, value):
        self._num = value


    def printElement(self, index):
        print(f"""

{index})

Name: {self._name}
Symbol: {self._symbol}
Series: {self._series}
Atomic Number: {self._num}""")


elements = []


def main():

    shouldContinue = "y"
    while (shouldContinue == "y"):
        ans = 0
        while (ans != 1 and ans != 2 and ans != 3 and ans != 4):
            ans = menu()
        if (ans == 1):
            PrintElements()
        elif (ans == 2):
            AddElements()
        elif (ans == 3):
            RemoveElements()
        else:
            PrintRangeOfElements()

        shouldContinue = input(
            "Enter 'y' to run again or any other key to quit!\n").lower()

    print("\nGoodbye!\n")


def menu():
    try:
        print("""
Elements Menu -- Choose One

1. Print Elements
2. Add an Element
3. Remove an Element
4. Print A Range Of Elements By Atomic Number
        """)
        ans = int(input("Choose 1-4!\n"))
    except:
        ans = 0
    return ans


def PrintElements():
    print("\nElement List:")
    i = 1
    for element in elements:
        element.printElement(i)
        i += 1

    print()


def AddElements():
    print("\n------------------ Add To Elements ----------------------\n")
    element = Element()

    name = input("Please enter element name!\n")
    symbol = input(f"Please enter {name}'s symbol!\n")
    series = input("Please enter the element's series!\n")
    

    invalidInput = True
    while (invalidInput):
        try:
            atomicNum = int(input("Please enter element's atomic number! Must be a whole number!\n"))
            invalidInput = False
        except:
            print("That wasn't a whole number!")

    try:
        element.name = name
        element.symbol = symbol
        element.series = series
        element.atomicNumber = atomicNum

        elements.append(element)

        print("Succesfully Created element:\n")
        PrintElements()

    except Exception as e:
        print(f"""There was an error in saving your element! 

Error Info: 
{e}

""")


def RemoveElements():
    if (len(elements) != 0):
        PrintElements()
        invalidInput = True
        while (invalidInput):
            try:
                numToDelete = int(input(f"Choose 1-{len(elements)}!\n"))

                if (numToDelete < 1 or numToDelete > len(elements)):
                    print("Not a valid number!")
                else:
                    invalidInput = False
            except:
                print("That wasn't a whole number!")

        print(f"Deleting item {numToDelete}!")

        del elements[numToDelete - 1]

        print(f"Sucessfully deleted item {numToDelete}!\n")

        PrintElements()

    else:
        print("\nThere are no elements in your list!\n")


def PrintRangeOfElements():
    if (len(elements) == 0):
        print("\nThere are no elements in your list!\n")
        
    else:

        invalidInput = True
        while (invalidInput):
            try:
                start = int(input("Enter starting atomic number! Must be a whole number!\n"))
                end = int(input(f"Enter ending atomic number! Must be a whole number and greater than {start}!\n"))
                if(end <= start):
                    print("\nEnd value must be greater than start value!\n")
                else:
                    invalidInput = False
            except:
                print("Invalid start or end value!\n")


        elementRange = []
        for i in range(start, end + 1):
            for element in elements:
                if(element.atomicNumber == i):
                    elementRange.append(element)
        
        if(len(elementRange) == 0):
            print(f"\nNo elements found between {start} and {end}!\n")
        else:
            i = 1
            for element in elementRange:
                element.printElement(i)
                i += 1


main()