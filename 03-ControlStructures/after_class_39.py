# 39.	The variables a and b contain the dimensions of the sides of the rectangle. 
# Write a program that creates the following rectangle with dimensions a and b. 


a = int(input("Enter a value: "))
b = int(input("Enter b value: "))

for i in range(a):
    if i == 0 or i == a-1:
        print("*" * b)
    else:
        print("*" + " " * (b-2) + "*")
