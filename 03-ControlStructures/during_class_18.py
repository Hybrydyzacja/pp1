# 18.	Write a program that calculates values for the following fractions: 1/2, 1/3, ..., 1/10. 
# First, Use the "while" statement, then, the "for" statement. 
# Sample result: 
# 1/1 = 1.0
# 1/2 = 0.5
# 1/3 = 0.3333333333333333
# …
# 1/10 = 0.1

i = 1
while i <= 10:
    print(f"1/{i} = {1/i}")
    i += 1

for n in range(1,11):
    print(f"1/{n} = {1/n}")