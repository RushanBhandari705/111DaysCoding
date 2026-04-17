#Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 – year old.
def generate_multiplication_tables(start, end):
    for i in range(start, end + 1):
        filename = f"Multiplication_Table_{i}.txt"
        with open(filename, 'w') as file:
            file.write(f"Multiplication Table of {i}\n")
            file.write("-" * 20 + "\n")
            for j in range(1, 11):
                file.write(f"{i} x {j} = {i * j}\n")
        print(f"Multiplication table for {i} has been written to {filename}")