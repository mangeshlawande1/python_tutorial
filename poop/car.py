class Car :
    wheels = 4 # class variable
    def __init__(self, make, model, year, color):
        self.make = make# instance var
        self.model = model 
        self.year = year
        self.color = color
    
    def drive(self):
        print(f"This car is {self.model} model ")

    def stop(self):
        print(f"The model {self.model} has not Active yet");
