# 44.	Write a program that calculates the sum and arithmetic mean of numbers entered from the keyboard.
# Entering 0 ends entering numbers. Sample result
# Enter number: 15
# Enter number: 8
# Enter number: 10
# Enter number: 0
# RESULT: Quantity=3, Sum=33, Mean=11

counter = 0
suma = 0
mean = 0
n = 1
while n != 0:
    n = int(input("Enter number: "))
    if n == 0:
        print(f'RESULT: Quantity={counter}, Sum={suma}, Mean={int(mean)}')
        break
    else:
        counter += 1
        suma += n
        mean = (suma / counter)

