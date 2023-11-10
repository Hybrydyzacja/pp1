# 37.	Write a program that creates the following pattern. Sample result:
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

stars = int(input("Enter maximum number of stars: "))
for n in range(1, stars+1):
    print("* "*n)
for i in range(stars-1, 0, -1):
    print("* " * i)

