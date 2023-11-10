# 33.	Write a program that converts a decimal number into a binary number.
# To convert a decimal number to binary, follow these steps:
# a.	Read a decimal number from the keyboard.
# b.	Divide the number by 2 and note the remainder.
# c.	Divide the quotient obtained by 2 and note the remainder.
# d.	Repeat the same process till we get 0 as the quotient.
# e.	Write the values of all the remainders starting from the bottom to the top. That will be the required binary number.


decimal = int(input("Enter positive decimal number: "))
# binary = int(str(bin(decimal))[2:])
# print(binary)

binary = ""
while decimal != 0:
    reminder = decimal % 2
    decimal = decimal // 2
    binary += str(reminder)

print(int((binary)[::-1]))