class Animal:
    alive = True
    def eat(self):
        print("This animal is eating ");


    def sleep(self):
        print("This animal is sleeping !!")
    


class Rabbit(Animal):
    def run(self):
        print("The rabbit runs faster !!")


class Fish(Animal):
    def swim(self):
        print("Fish are alive in water !!")

class Hawk(Animal):
    def fly(self):
        print("the bird can fly for long time.")

# def __name__ : "__main__":
