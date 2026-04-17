#Create a class “Programmer” for storing information of few programmers working at Microsoft.
class Programmer:
    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Programming Language: {self.language}")