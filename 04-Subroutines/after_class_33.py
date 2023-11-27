# 33.	Define a function f(n) that returns a string of n asterisks, separated by a slash sign. 
# Sample result:
# f(4) returns "*/*/*/*"
# f(1) returns "*"


def f(n):
    str_stars = ""
    for i in range(n):
        str_stars += "*" + "/"
    return str_stars[:-1]

print(f(4))
