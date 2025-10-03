## multi-level inheritance :: when a derived class inherits from more than one derived class (child) 

class Prey :

    def flee(self):
        print("This animal flees")

    

class Predator:
    def hunt(self):
        print("This animal is hunting ");


class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass 


