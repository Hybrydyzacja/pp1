# 39.	The price of the product on the price tag is given before and after the discount is applied. 
# Write a program that allows you to enter the product price and discount. 
# Display the product price, discount, discounted product price, and the difference between the product price before and after the discount. 
# Display all prices with two decimal places. 
# Sample result:
# Enter price: 24.72
# Enter discount %: 15
# Price with discount: 21.01
# Reduction: 3.71


price = float(input("Enter price: "))
discount = float(input("Enter discount [%]: "))
reduction = round(price * discount / 100,2)
price_with_disc = round(price - reduction,2)

print(f'Price with discount {price_with_disc}\nReduction {reduction}')

# def sale(price, discount):
#     reduction = round(price * discount / 100,2)
#     price_with_disc = round(price - reduction,2)
#     return(f'Price with discount {price_with_disc}\nReduction {reduction}')

# print(sale(24.72,15))