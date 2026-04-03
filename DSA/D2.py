l=[9,56,76,100,2]
s=l[0]
for i in range(len(l)):
    if s>l[i]:
        s=l[i]
print("The Smallest element is: ",s)