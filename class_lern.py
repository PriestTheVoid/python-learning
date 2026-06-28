class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def info(self):
        print(f"Name: {self.__name} , Age: {self.__age}")

tom = Person("Tom", 27)
tom.info()

tom.__name = "notTom"
tom.info()

tom._Person__name = "notTom" #способ обойти инкапсуляцию и изменить значение 
tom.info()