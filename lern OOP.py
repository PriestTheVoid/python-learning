class Person:
    def __init__(self, name, age): #инициализация класса
        self.Name = name #атрибут класса
        self.Age = age #атрибут класса

tom = Person("Tom", 17) #объект класса
bob = Person("Bob", 26) #объект класса

print(tom.Name)
print(tom.Age)

tom.Work = "Subway"

print(tom.Work)