# create a txt file with the following data
#The txt file contains students id,name and marks of a module
#ID001, Harry, 85
#ID002, Bob, 78
#ID003, Shyan, 92

with open("students.txt", "w") as file:
    file.write("ID001, Harry, 85\n")
    file.write("ID002, Bob, 78\n")
    file.write("ID003, Shyan, 92\n")

