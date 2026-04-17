#Write a program to mine a log file and find out whether it contains ‘python’.
def check_word_in_log(filename, word):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            if word in content:
                print(f"The word '{word}' is present in the log file '{filename}'.")
            else:
                print(f"The word '{word}' is not present in the log file '{filename}'.")
    except FileNotFoundError:
        print(f"The log file '{filename}' does not exist.")