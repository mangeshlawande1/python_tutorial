## prevent a user from creating an object of that class
# a ghost class
# compels a user to override abstract methods in a child class

# abstract class : a class which contains one or more abstract methods
# abstract method :: a method taht has a declaration but does not have an implementation .

from abc import ABC, abstractmethod


class Vehicle:

    @abstractmethod
    def go(self):
        return self
    
    @abstractmethod
    def stop(self):
        return self



class Car(Vehicle):
    def go(self):
        print("You drive the car.")
        return self

    def stop(self):
        print("This car is stopped !!")
        return self

class Motorcycle(Vehicle):
    def go(self):
        print("You ride the Motor-Cycle")
        return self


    def stop(self):
        print("This Motor-cycle is stopped !!");
        return self

vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

# vehicle.go().stop()
car.go().stop()
motorcycle.go().stop()


