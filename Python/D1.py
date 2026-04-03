l=[10,78,89,2]
b=l[0]
for i in range(len(l)):
    if l[i]>b:
        b=l[i]
print("The largest element is: ",b)