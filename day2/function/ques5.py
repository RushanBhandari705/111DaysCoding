#Repeat program 4 for a list of such words to be censored.
def replace_words_in_file(filename, target_words, replacement):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        
        for target_word in target_words:
            content = content.replace(target_word, replacement)
        
        with open(filename, 'w') as file:
            file.write(content)
        
        print(f"The words {target_words} have been replaced with '{replacement}' in the file '{filename}'.")
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")