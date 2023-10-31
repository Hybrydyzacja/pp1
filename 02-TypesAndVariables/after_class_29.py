import random

sum = 0
n = 0
while n < 3:
    roll = random.randint(1, 6)
    sum += roll
    n += 1

print(sum)


