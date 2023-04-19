# Collin Shook
# Assignment 6
# 10-27-2022

import random


gameCollection = []
zombies = []
trucks = []

# ------------------------- Classes -----------------------------------


# --------------------- Game Collection Class -------------------------



class GameTitle():

    def __init__(self, _title = "", _platform = "", _price = "", _yearPurchased = ""):
        self._title = _title
        self._platform = _platform
        self._price = _price
        self._yearPurchased = _yearPurchased


    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        self._title = value



    @property
    def platform(self):
        return self._platform

    @platform.setter
    def platform(self, value):
        self._platform = value



    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    


    @property
    def yearPurchased(self):
        return self._yearPurchased

    @yearPurchased.setter
    def yearPurchased(self, value):
        self._yearPurchased = value


    def PrintGame(self, num):
        print(f"\n--------- {num + 1}. ----------\n")
        print(f"Title: {self._title}.")
        print(f"Platform: {self._platform}.")
        print(f"Price: ${self._price}.")
        print(f"Year Purchased: {self._yearPurchased}.")
        print()

# ---------------End Of Game Collection Class --------------------------


# --------------------- Zombie Class -------------------------



class Zombie():

    def __init__(self, _name="", _gender="", _city="", _type=""):
        self._name = _name
        self._gender = _gender
        self._city = _city
        self._type = _type

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    def PrintZombie(self, num):
        print(f"\n--------- {num + 1}. ----------\n")
        print(f"Name: {self._name}.")
        print(f"Gender: {self._gender}.")
        print(f"City: {self._city}.")
        print(f"Type: {self._type}.")
        print()

# ---------------End Of Zombie Class --------------------------


# ----------------------- Vehicle ------------------------------

class Vehicle():
    def __init__(self, _make="", _model="", _truckYear=""):
        self._make = _make
        self._model = _model
        self._truckYear = _truckYear 

# ---------------------- End Of Vehicle Class ------------------------------

# ------------------------ Truck ----------------------------------

class Truck(Vehicle):
    def __init__(self, _make="", _model="", _truckYear="", _truckColor="" , _bedCapacity="", _towingCapacity=""):
        self._truckColor = _truckColor
        self._bedCapacity = _bedCapacity
        self._towingCapacity = _towingCapacity

        Vehicle.__init__(self, _make, _model, _truckYear)

    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, value):
        self._make = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def truckYear(self):
        return self._truckYear

    @truckYear.setter
    def truckYear(self, value):
        self._truckYear = value

    @property
    def truckColor(self):
        return self._truckColor 

    @truckColor.setter
    def truckColor(self, value):
        self._truckColor = value

    @property
    def bedCapacity(self):
        return self._bedCapacity

    @bedCapacity.setter
    def bedCapacity(self, value):
        self._bedCapacity = value

    @property
    def towingCapacity(self):
        return self._towingCapacity

    @towingCapacity.setter
    def towingCapacity(self, value):
        self._towingCapacity = value


    def PrintTruck(self, num):
        print(f"\n--------- {num + 1}. ----------\n")
        print(f"Name: {self._make}.")
        print(f"Model: {self._model}.")
        print(f"Year: {self._truckYear}.")
        print(f"Color: {self._truckColor}.")
        print(f"Bed Capacity: {self._bedCapacity} sqft.")
        print(f"Towing Capacity: {self._towingCapacity} lbs.")
        print()


# ------------------- End Of Truck Class -----------------------------


# --------------- End Of Classes --------------------------------------



# -------------------- Main And Menu ----------------------------------

def main():
    shouldContinue = "y"
    while (shouldContinue == "y"):
        ans = 0
        while (ans != 1 and ans != 2 and ans != 3):
            ans = menu()
        if (ans == 1):
            Q1()
        elif (ans == 2):
            Q2()
        else:
            Q3()

        shouldContinue = input("Enter 'y' to run again or any other key to quit!\n").lower()


    print("\nGoodbye!\n")


def menu():
    try:
        print("""
Classes Menu -- Choose One

1. Track Video Game Collection
2. Create Zombies
3. Track Trucks
        """)
        ans = int(input("Choose 1-3!\n"))
    except:
        ans = 0
    return ans


# ----------------------- End Of Main and Menu ---------------------------




# ------------------------------ Q1 --------------------------------------

def Q1():
    ans = 0

    while (ans != 1 and ans != 2 and ans != 3):
        ans = Q1Menu()
    if (ans == 1):
        AddVideoGames()
    elif (ans == 2):
        RemoveVideoGames()
    else:
        PrintVideoGames()


def Q1Menu():
    try:
        print("""
--- Video Game Collection ---

1. Add a video game
2. Remove a video game
3. Print Colletion
        """)
        ans = int(input("Choose 1-3!\n"))
    except:
        ans = 0
    return ans

def AddVideoGames():
    print("\n------------------ Add To Video Game Collection ----------------------\n")
    gameInstance = GameTitle()


    gameTitle = input("Please Enter a Title!\n")
    gamePlatform = input("Please Enter Game Platform!\n")

    invalidInput = True
    while(invalidInput):
        try:
            gamePrice = float(input("Please enter game price! Must be a number!\n"))
            invalidInput = False
        except:
            print("That wasn't a number!")

    invalidInput = True
    while (invalidInput):
        try:
            gameYearPurchased = int(input("Please enter year of game purchase! Must be a whole number!\n"))
            invalidInput = False
        except:
            print("That wasn't a whole number!")

    try:
        gameInstance.title = gameTitle
        gameInstance.platform = gamePlatform
        gameInstance.price = gamePrice
        gameInstance.yearPurchased = gameYearPurchased

        gameCollection.append(gameInstance)

        print("Succesfully Created Game:\n")
        gameInstance.PrintGame(0)

    except Exception as e:
        print(f"""There was an error in saving to your collection! 

Error Info: 
{e}

""")
    


def RemoveVideoGames():
    if(len(gameCollection) != 0):
        PrintVideoGames()
        invalidInput = True
        while (invalidInput):
            try:
                numToDelete = int(input(f"Choose 1-{len(gameCollection)}!\n"))

                if(numToDelete < 1 or numToDelete > len(gameCollection)):
                    print("Not a valid number!")
                else:
                    invalidInput = False
            except:
                print("That wasn't a whole number!")


        print(f"Deleting item {numToDelete}!")

        del gameCollection[numToDelete - 1]

        print(f"Sucessfully deleted item {numToDelete}!\n")

        PrintVideoGames()

    else:
        print("Collection is empty!")

    

def PrintVideoGames():
    print("------ Game Collection ------\n")
    i = 0
    for game in gameCollection:
        game.PrintGame(i) 
        i += 1


# ------------------------------- End Of Q1 -------------------------


# --------------------------------- Q2 ------------------------------

def Q2():
    ans = 0

    while (ans != 1 and ans != 2 and ans != 3):
        ans = Q2Menu()
    if (ans == 1):
        AddZombies()
    elif (ans == 2):
        RemoveZombies()
    else:
        PrintZombies()


def Q2Menu():
    try:
        print("""
--- Zombies ---

1. Add a set of zombies
2. Remove zombies
3. Print zombies
        """)
        ans = int(input("Choose 1-3!\n"))
    except:
        ans = 0
    return ans

def AddZombies():
    genders = ["M" , "F"]
    cities = ["Helena", "Butte", "Missoula" , "Bozeman"]
    types = ["Walker" , "Runner" , "Voodoo", "Ghoul", 
    "Crawler", "Screamer", "Bonies"]

    invalidInput = True
    while(invalidInput):
        try:
            numOfZombies = int(input("Enter how many zombies to create!\n"))
            invalidInput = False
        except:
            print("Invalid Input!")


    currentNumOfZombies = len(zombies)
    for i in range(numOfZombies):

        name = f"Zombie {i+ currentNumOfZombies + 1}"
        gender = genders[random.randint(0, len(genders) - 1)]
        city = cities[random.randint(0, len(cities) - 1)]
        type = types[random.randint(0, len(types) - 1)]


        zombie = Zombie(name, gender, city, type)

        zombies.append(zombie)



def RemoveZombies():
    if (len(zombies) != 0):
        PrintZombies()
        invalidInput = True
        while (invalidInput):
            try:
                numToDelete = int(input(f"Choose 1-{len(zombies)}!\n"))

                if (numToDelete < 1 or numToDelete > len(zombies)):
                    print("Not a valid number!")
                else:
                    invalidInput = False
            except:
                print("That wasn't a whole number!")

        print(f"Deleting item {numToDelete}!")

        del zombies[numToDelete - 1]

        print(f"Sucessfully deleted item {numToDelete}!\n")

        PrintZombies()

    else:
        print("There are no zombies here!")


def PrintZombies():
    print("------ Zombies ------\n")
    i = 0
    for zombie in zombies:
        zombie.PrintZombie(i)
        i += 1


# --------------------------------- End Of Q2 ------------------------------


def Q3():
    ans = 0

    while (ans != 1 and ans != 2 and ans != 3):
        ans = Q3Menu()
    if (ans == 1):
        AddTrucks()
    elif (ans == 2):
        RemoveTrucks()
    else:
        PrintTrucks()


def Q3Menu():
    try:
        print("""
--- Tracking Trucks ---

1. Add a truck
2. Remove a truck
3. Print trucks
        """)
        ans = int(input("Choose 1-3!\n"))
    except:
        ans = 0
    return ans


def AddTrucks():
    print("\n------------------ Add To Trucks ----------------------\n")
    truck = Truck()

    make = input("Please Enter a Vehicle Make!\n")
    model = input("Please Enter Vehicle Model!\n")
    truckColor = input("Please Enter a Truck Color!\n")
    
    invalidInput = True
    while (invalidInput):
        try:
            truckYear = int(
                input("Please enter truck year! Must be a whole number!\n"))
            invalidInput = False
        except:
            print("That wasn't a whole number!")

    invalidInput = True
    while (invalidInput):
        try:
            bedCapacity = float(input("Please enter truck bed capacity (sqft)! Must be a number!\n"))
            invalidInput = False
        except:
            print("That wasn't a number!")

    invalidInput = True
    while (invalidInput):
        try:
            towingCapacity = float(input("Please enter truck towing capacity (lbs)! Must be a number!\n"))
            invalidInput = False
        except:
            print("That wasn't a number!")

    try:
        truck.make = make
        truck.model = model
        truck.truckYear = truckYear
        truck.truckColor = truckColor
        truck.bedCapacity = bedCapacity
        truck.towingCapacity = towingCapacity

        trucks.append(truck)

        print("Succesfully Created Truck:\n")
        truck.PrintTruck(0)

    except Exception as e:
        print(f"""There was an error in saving your truck! 

Error Info: 
{e}

""")



def RemoveTrucks():
    if (len(trucks) != 0):
        PrintTrucks()
        invalidInput = True
        while (invalidInput):
            try:
                numToDelete = int(input(f"Choose 1-{len(trucks)}!\n"))

                if (numToDelete < 1 or numToDelete > len(trucks)):
                    print("Not a valid number!")
                else:
                    invalidInput = False
            except:
                print("That wasn't a whole number!")

        print(f"Deleting item {numToDelete}!")

        del trucks[numToDelete - 1]

        print(f"Sucessfully deleted item {numToDelete}!\n")

        PrintTrucks()

    else:
        print("There are no trucks in your list!")


def PrintTrucks():
    print("------ Trucks ------\n")
    i = 0
    for truck in trucks:
        truck.PrintTruck(i)
        i += 1



main()