# 38.	Write a program that creates the following pattern. Sample result:
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

number = int(input("Enter number: "))

for n in range(1,number+1):
    print(str(n)*n)
