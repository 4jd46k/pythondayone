word=input("enter the string")
if len(word) <2:
    print("empty string")
else:
    print(f"{word[0]}{word[1]}{word[-2]}{word[-1]}")
