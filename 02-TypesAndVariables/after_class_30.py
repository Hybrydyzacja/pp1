import random

number = random.randint(1, 6)
print(f"Dice rolled: {number}")
print(f"Specjal number: {number == 1 or number == 6}")