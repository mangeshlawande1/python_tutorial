class Animal :
    def eat(self):
        print("This animal is eating ")


class Rabbit(Animal):
    def eat(self):
        print("The rabbit eat carrot mostly. ")



rabbit = Rabbit()
rabbit.eat()