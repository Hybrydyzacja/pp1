# 42.	Write a program that allows you to enter a binary, four-digit number. Convert the entered number from binary to decimal value. 
# Do not use available Python functions. 
# Sample result:
# Enter binary number: 0110
# Binary number in decimal notation: 6


number = input("Podaj number binarny: ")
number = int(number)

# x = number % 10
# y = int(number / 10)%10
# z = int(number / 100)%10
# k = int(number / 1000)%10
# print(x,y,z,k)
# decimal = x* 2**0+y* 2**1+z *2**2+k* 2**3
# print(decimal)

decimal = 0
n = 0
for n in range(len(str(number))):
    x = number % 10
    decimal+= (x * 2**n) 
    number = int(number / 10)
    n+=1
print(decimal)

