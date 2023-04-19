
class City():

    def __init__(self, _name = "", _state = "", _population = 0):
        self._name = _name
        self._state = _state
        self._population = _population


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, value):
        self._population = value


    def printCity(self, index):
        print(f"""

{index})
Name: {self._name}
State: {self._state}
Population: {self._population}""")


city_data = ["Kalispell", "Chicago", "Butte", "Coram"]
states_data = ["MT", "IL", "MT","MT"]
pop_data = [36000, 1500000, 30000, 500]

cities = []

def main():

    # initialization of existing cities

    for i in range(len(city_data)):
        cities.append("")
        cities[i] = City(city_data[i], states_data[i], pop_data[i])


    shouldContinue = "y"
    while (shouldContinue == "y"):
        ans = 0
        while (ans != 1 and ans != 2 and ans != 3):
            ans = menu()
        if (ans == 1):
            PrintCities()
        elif (ans == 2):
            AddCities()
        else:
            RemoveCities()

        shouldContinue = input(
            "Enter 'y' to run again or any other key to quit!\n").lower()

    print("\nGoodbye!\n")


def menu():
    try:
        print("""
Cities Menu -- Choose One

1. Print Cities
2. Add a City
3. Remove a City
        """)
        ans = int(input("Choose 1-3!\n"))
    except:
        ans = 0
    return ans



def PrintCities():
    print("\nCity List:")
    i = 1
    for city in cities:
        city.printCity(i)
        i += 1

    print()


def AddCities():
    print("\n------------------ Add To Cities ----------------------\n")
    city = City()

    name = input("Please enter city name!\n")
    state = input("Please enter state that the city is in!\n")

    invalidInput = True
    while (invalidInput):
        try:
            population = int(input("Please enter city population! Must be a whole number!\n"))
            invalidInput = False
        except:
            print("That wasn't a whole number!")

    try:
        city.name = name
        city.state = state
        city.population = population

        cities.append(city)

        print("Succesfully Created city:\n")
        city.printCity(len(cities))

    except Exception as e:
        print(f"""There was an error in saving your city! 

Error Info: 
{e}

""")



def RemoveCities():
    if (len(cities) != 0):
        PrintCities()
        invalidInput = True
        while (invalidInput):
            try:
                numToDelete = int(input(f"Choose 1-{len(cities)}!\n"))

                if (numToDelete < 1 or numToDelete > len(cities)):
                    print("Not a valid number!")
                else:
                    invalidInput = False
            except:
                print("That wasn't a whole number!")

        print(f"Deleting item {numToDelete}!")

        del cities[numToDelete - 1]

        print(f"Sucessfully deleted item {numToDelete}!\n")

        PrintCities()

    else:
        print("There are no cities in your list!")


main()