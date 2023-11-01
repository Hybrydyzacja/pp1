# 25.	In one of the online stores, a 25% discount is charged for each product purchased over two. 
# Write a program that calculates the amount to be paid. 
# Read the number of purchased products and the product price from the keyboard.

number = int(input("Enter number of products: "))
price = float(input("Enter price: "))

if number > 0:
    if number <= 2:
        amount = price
    else:
        amount = price*2 + (number-2)*(price*0.75)
        
print(amount) 