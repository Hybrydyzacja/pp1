# 30.	Create a function f(number, even) that computes the sum of the digits of a number. 
# When the value of the even parameter is True, the function returns the sum of the even digits. 
# When the value of the even parameter is False, the function returns the sum of the odd digits. 
# Sample result:
# f(3124,True) returns 6
# f(3124,False) returns 4



def f(number, even):
    suma = 0
    if even:
        for i in str(number):
            if int(i) % 2 == 0:
                suma += int(i)
            else:
                continue
    else:
        for i in str(number):
            if int(i) % 2 != 0:
                suma += int(i)
            else:
                continue
    return suma


print(f(3124,True)) 
print(f(3124,False)) 
print(f(20576,False)) 
print(f(20576,True))
print(f(13115,True))
