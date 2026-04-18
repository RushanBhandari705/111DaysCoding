#Create a class ‘Employee’ and add salary and increment properties to it.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.increment = 0

    def apply_increment(self, increment_amount):
        self.increment += increment_amount
        self.salary += increment_amount

    def __str__(self):
        return f"Employee: {self.name}, Salary: {self.salary}, Increment: {self.increment}"