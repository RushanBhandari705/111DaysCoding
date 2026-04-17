#Write a program to find out the line number where python is present from ques 6.
def find_line_number(filename, word):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines, start=1):
                if word in line:
                    print(f"The word '{word}' is present on line {i}.")
    except FileNotFoundError:
        print(f"The log file '{filename}' does not exist.")