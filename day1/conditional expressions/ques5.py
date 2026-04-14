#Write a program which finds out whether a given name is present in a list or not.
names = ["Rushan", "Alson", "Sudip", "Sulav"]
name = input("Enter the name to search for: ")

if name in names:
    print("The name is present in the list.")
else:
    print("The name is not present in the list.")