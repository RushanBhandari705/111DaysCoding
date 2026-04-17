#Create a class with a class attribute a; create an object from it and set ‘a’directly using ‘object.a = 0’. Does this change the class attribute?
class MyClass:
    a = 10  # Class attribute

# Create an object of MyClass
obj = MyClass()

# Change the attribute 'a' using the object
obj.a = 0

# Print the class attribute and the object attribute
print("Class attribute:", MyClass.a)  # Output: 10
print("Object attribute:", obj.a)     # Output: 0