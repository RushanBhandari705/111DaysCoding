#Write a python program to rename a file to “renamed_by_ python.txt.
import os   
def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"File '{old_name}' has been renamed to '{new_name}'.")
    except FileNotFoundError:
        print(f"The file '{old_name}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")