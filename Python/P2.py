"""Question: Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated 
sequence on a single line. Suppose the following input is supplied to the program: 8 Then, the output should be: 40320

Hints: In case of input data being supplied to the question, it should be assumed to be a console input."""

# CODE HERE

n = int(input("Enter the Number: "))
f=1
for i in range(1,n+1):
    f=f*i
print(f)

# But in Interviews they Prefer 'RECURSIVE FUNCTION' so do it using recursion

def fac(x):
    if x==0:
        return 1
    else:
        return x * fac(x-1)
x=int(input())
print(fac(x))

"""
Input : 8
Output: 40320
"""
