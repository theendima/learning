class Cat: # Саоздание класса и описание можно добавлять
    name = None
    age = None
    isHappy = None

    def __init__(self, name = None, age = None, isHappy = None): #создание конструктора
        self.set_data(name, age, isHappy)
        self.get_data()

    def set_data(self, name = None, age = None, isHappy = None):
        self.name = name
        self.age = age
        self.isHappy = isHappy

    def get_data(self):
         print("Имя :", self.name, "Возраст", self.age, " . Happy:", self.isHappy)

cat1  = Cat("Biba", 3, True)
#cat1.set_data("Biba", 3, True)
cat1.set_data("Dolb", 2)


cat2 = Cat("Biba", 2, False)
#cat2.set_data("Boba", 2, False)


#cat1.get_data()
#cat2.get_data()