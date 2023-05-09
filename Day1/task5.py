ls=[(20,30,40),(30,50,80),(30,70,60)]
ls2=[]
for i in range(len(ls)):
    a=ls[i][0]
    b=ls[i][1]
    c=100
    new_tuple=(a,b,c)
    ls2.append(new_tuple)
print(ls2)