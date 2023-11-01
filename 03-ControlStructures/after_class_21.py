# 21.	Write a program that displays two numbers entered from the keyboard in ascending order.
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

if first_number>second_number:        
    print(f'{second_number}, {first_number}')
else:
    print(f'{first_number}, {second_number}')