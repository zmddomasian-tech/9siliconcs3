#Parent class
class Animal:
    def __init__(self, name: str):
        self.name = name
    def eat(self):
        pass
    def make_sound(self):
        pass

#Class lion
class Lion(Animal):
    def make_sound(self):
        print(f"{self.name} roars loudly!")
    def eat(self):
        print(f"{self.name} eats fresh meat.")

#Class Elephant
class Elephant(Animal):
    def make_sound(self):
        print(f"{self.name} trumpets!")
    def eat(self):
        print(f"{self.name} eats grass and fruits.")
      
#Class Monkey
class Monkey(Animal):
    def make_sound(self):
        print(f"{self.name} chatters!")
    def eat(self):
        print(f"{self.name} eats bananas.")
