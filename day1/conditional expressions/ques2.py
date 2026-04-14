#Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user

subject1 = float(input("Enter marks for subject 1: "))
subject2 = float(input("Enter marks for subject 2: "))
subject3 = float(input("Enter marks for subject 3: "))

total_marks = subject1 + subject2 + subject3
percentage = (total_marks / 300) * 100

if percentage >= 40 and subject1 >= 33 and subject2 >= 33 and subject3 >= 33:
    print("The student has passed.")
else:
    print("The student has failed.")