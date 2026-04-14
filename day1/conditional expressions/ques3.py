#A spam comment is defined as a text containing following keywords: “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.
comment = input("Enter the comment: ")

if "Make a lot of money" in comment or "buy now" in comment or "subscribe this" in comment or "click this" in comment:
    print("This is a spam comment.")
else:
    print("This is not a spam comment.")