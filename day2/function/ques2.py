#The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.
def game():
    # Simulating a game and returning a score
    import random
    score = random.randint(0, 100)  # Random score between 0 and 100
    print(f"Your score: {score}")
    return score