# 43.	Write a program that displays the first twenty words of the Fibonacci sequence. 
# The sequence is defined as follows: the first term is equal to 0, the second is equal to 1, each subsequent term is the sum of the previous two. 


i = 0
j = 1
next_number = i
n = 1

while n <= 10:
    print(next_number, end=" ")
    n += 1
    i, j = j, next_number
    next_number = i + j
print()