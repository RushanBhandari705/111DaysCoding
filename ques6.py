#Can you change the self-parameter inside a class to something else (say “harry”). Try changing self to “slf” or “harry” and see the effects.
class MyClass:
    def __init__(harry, value):
        harry.value = value

    def display(harry):
        print(f"The value is: {harry.value}")
        