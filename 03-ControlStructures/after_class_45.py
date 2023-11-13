# 45.	A natural number greater than 1 is called a prime if it has exactly 2 natural factors with the values 1 and this number. 
# Write a program that finds N leading prime numbers. Read the value of N from the keyboard. 
# Using loop statements check that the number N is divisible only by 1 and by N.

n = int(input("Enter number: "))
counter = 0
for i in range(1, n+1):
    if n % i == 0:
        counter +=1
    else:
        continue
if counter == 1 or counter == 2:
    print("Primary")
else:
    print("Not primary")