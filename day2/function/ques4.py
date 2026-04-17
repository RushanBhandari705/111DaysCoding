#A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file. 
def replace_word_in_file(filename, target_word, replacement):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        
        updated_content = content.replace(target_word, replacement)
        
        with open(filename, 'w') as file:
            file.write(updated_content)
        
        print(f"The word '{target_word}' has been replaced with '{replacement}' in the file '{filename}'.")
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")