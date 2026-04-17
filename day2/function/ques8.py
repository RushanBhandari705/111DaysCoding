#Write a program to make a copy of a text file “this. txt”
def copy_file(source, destination):
    try:
        with open(source, 'r') as src_file:
            content = src_file.read()
        
        with open(destination, 'w') as dest_file:
            dest_file.write(content)
        
        print(f"File '{source}' has been copied to '{destination}'.")
    except FileNotFoundError:
        print(f"The file '{source}' does not exist.")