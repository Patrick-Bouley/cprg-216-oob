class Car:
   
    def __init__(self, color_val, make_val, model_val, speed):
        self.color = color_val
        self.make = make_val
        self.model = model_val
        self.__speed = speed
        # The double _ encapsulates the variable meaning we cannot access this variable anywhere else but here. which prevents the user from messing up the code 

    def set_color(self,value):
        self.color = value

    def set_make(self, value):
        self.make = value

    def set_model(self, value):
        self.model = value

    def drive(self):
        pass

    def accelerate(self):
        self.__speed += 5

    def deccelerate(self):
        self.__speed -= 5

    def brake(self):
        self.__speed = 0