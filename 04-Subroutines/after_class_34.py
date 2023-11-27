# 34.	Define the function f(n), which returns numbers from 1 to n as a string. 
# Sample result:
# f(11) returns "12345


def f(n):
    str_numbers = ""
    for i in range(1, n+1):
        str_numbers += str(i)
    return str_numbers

print(f(11))