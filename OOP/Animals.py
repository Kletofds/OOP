###################################
# Animals Class
# Kelton Figurski
###################################

class Animals:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

class Dog(Animals):
    def __init__(self, name, age, color):
        super().__init__(name, age, color)
        
    def printchar(self):
        name = self.name
        print("Name:", name)
        age = self.age
        print("Age:", age)
        color = self.color
        print("Color:", color)
        
class Cat(Animals):
    def __init__(self, name, age, color):
        super().__init__(name, age, color)
        
    def printchar(self):
        name = self.name
        print("Name:", name)
        age = self.age
        print("Age:", age)
        color = self.color
        print("Color:", color)
    


