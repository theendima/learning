class Building:
    __year = None
    __city = None

    def __init__(self, year, city):
        self.year = year
        self.city = city

    def get_info(self):
        print("Лет: ", self.year, "City :", self.city)


class School(Building):
    people = None

    def __init__(self, people, year, city):
        super(School, self).__init__(year, city)
        self.people = people

    def get_info(self):
        super().get_info()
        print("People: ", self.people)

class Home(Building):
    pass

class house(Building):
    pass
   
school = School(101, 2000, "Tir")
school.get_info()
home = Building(2001, "Tir")
house = Building(2002, "Tir")
house.get_info()
print(school.year)
     
