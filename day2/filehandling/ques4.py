#Add a static method in problem 2, to greet the user with hello
class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        return self.number ** 2

    def cube(self):
        return self.number ** 3

    def square_root(self):
        return self.number ** 0.5

    @staticmethod
    def greet_user():
        print("Hello, user!")