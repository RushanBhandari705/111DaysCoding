#Write a program to wipe out the content of a file using python.
def wipe_file_content(filename):
    try:
        with open(filename, 'w') as file:
            file.write("")  # Writing an empty string to the file to wipe its content
        print(f"The content of the file '{filename}' has been wiped out.")
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")