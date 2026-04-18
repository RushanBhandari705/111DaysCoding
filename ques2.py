#Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’.
class Animals:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Animal: {self.name}"

class Pets(Animals):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species

    def __str__(self):
        return f"Pet: {self.name}, Species: {self.species}"

class Dog(Pets):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed

    def bark(self):
        return f"{self.name} the {self.breed} barks: Woof!"

    def __str__(self):
        return f"Dog: {self.name}, Breed: {self.breed}"