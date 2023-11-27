# 37.	Define the function f(n), which returns the n-th value of the Fibonacci sequence. 
# The sequence is defined as follows: the first value of the sequence is 0, the second value is 1. 
# Each subsequent value is the sum of the previous two. Sample result:

def f(n):
    a = 0
    b = 1

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(n):
            c = a + b
            a = b
            b = c
        
    return b-a

print(f(5))
print(f(9))