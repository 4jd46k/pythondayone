word=input("enter the string")
if len(word) <3:
    print(word)
else:
    if "ing" not in word[-3:]:
        print(word+"ing") 
    else: 
        print(word+"ly")      

