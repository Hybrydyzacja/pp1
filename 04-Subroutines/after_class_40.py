# 40.	Define a function f(number) that returns the sum of repeated digits in a number. 
# Sample result:
# f(1027) returns 0
# f(230335) returns 9
# f(513553007) returns 21 


from collections import Counter
def f(n):
    n = str(n)
    numbers_dict = Counter(n)
    suma = 0
    for key, value in numbers_dict.items():
        if value > 1:
            suma += int(key) * value
    return suma

print(f(1027) )
print(f(230335))
print(f(513553007))