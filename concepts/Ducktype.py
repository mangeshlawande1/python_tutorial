### duck typing :: concept where the class is less important than the methods/ attribute
# class type  is not checked id minimum methods/attributes are present
# "If it walks like a duck, and quacks like a duck, then must be a duck "
# 

class Duck :
    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is quacking !!")


class Chicken:
    def walk(self):
        print("The chicken is walkig !!")

    def talk(self):
        print("the chicken is clucking")


class Person():
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter! ");

        
duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck);

person.catch(chicken);


