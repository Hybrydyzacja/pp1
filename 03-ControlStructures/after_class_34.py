# 34.	There are coins of 1, 2 and 5 Polish Zlotys (PLN). Write a program showing any amount (natural number) 
# read from the keyboard with as few coins as possible.

amount = int(input("Enter the amount in PLN: "))

coins = 0
coins5 = (amount // 5)
amount = amount % 5
coins2 = (amount // 2)
amount = amount % 2
coins1 = (amount // 1)

coins = coins5 + coins2 + coins1
print(f'You need following coins:\n5zł - {coins5}\n2zł - {coins2}\n1zł - {coins1}\nNumber of coins: {coins}')

