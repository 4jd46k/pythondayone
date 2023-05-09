size =int(input("enter the size of list"))
print("enter the words")
word =[input() for i in range(size)]
ls = []
for i in range(len(word)):
    ls.append(len(word[i]))
print(ls)
