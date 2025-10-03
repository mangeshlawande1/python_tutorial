## the method chaining:: calling multiple method sequenially 
# each call perform an action on the same object and retuen self .


class Car :
    def turn_on(self):
        print("You start the engine! ")
        return self
    
    def drive(self):
        print("You drive the car ")
        return self

    def brake(self):
        print("You Stop on the brakes. ")
        return self
    
    def turn_off(self):
        print("You turn off the Engine !!");
        return self
    
car = Car()

# car.turn_on()
# car.drive()

# car.turn_on().drive()
# car.brake().turn_off()

car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()
