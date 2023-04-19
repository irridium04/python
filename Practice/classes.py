class Person():
    def __init__(self, _firstName, _lastName, _city):
        self._firstName = _firstName
        self._lastName = _lastName
        self._city = _city



class Voter(Person):
    def __init__(self, _firstName, _lastName, _city, _party, _precinct):
        self._party = _party
        self._precinct = _precinct
        Person.__init__(self, _firstName, _lastName, _city)

    @property
    def firstName(self):
        return self._firstName
    
    @firstName.setter
    def firstName(self, value):
        self._firstName = value

    @property
    def lastName(self):
        return self._lastName

    @lastName.setter
    def lastName(self, value):
        self._lastName = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value

    @property
    def party(self):
        return self._party

    @party.setter
    def party(self, value):
        self._party = value

    @property
    def precinct(self):
        return self._precinct

    @precinct.setter
    def precinct(self, value):
        self._precinct = value


def main():
    v1 = Voter()


main()