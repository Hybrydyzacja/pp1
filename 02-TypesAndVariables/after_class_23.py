# 23. The length of the sides of the triangle is a, b and c. Write a program that calculates the area of the triangle 
# (using the Heron formula) and the triangle circumference. Read the values of the triangle sides from the keyboard.

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

circumference = a + b + c
area = circumference / 2

print(circumference, area)