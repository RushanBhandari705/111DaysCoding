
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary
        self._increment = 0

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value
        self._increment = value - self._salary

    @property
    def salaryAfterIncrement(self):
        return self._salary + self._increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, value):
        self._increment = value - self._salary

    def __str__(self):
        return f"Employee: {self.name}, Salary: {self._salary}, Increment: {self._increment}"
