# 24.	A computer program analyses the price of a product in an online store.
# If the product price decreases by at least 10%, the program displays a purchase recommendation:

previous_price = 200.00
current_price = 140.00
discount = (previous_price - current_price) / previous_price * 100

print(f"Buy the product!!\nProduct price reduced by {int(discount)}%")
