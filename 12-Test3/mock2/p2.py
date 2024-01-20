# (p2.py) Create a function f(x,y,d) that returns true when the string of digits d appears in any number between x and y.
# Otherwise, the function returns false.
# Example:
# f(10,15,"14") -> True
# f(100,120,"11") -> True
# f(205,210,"04") -> False


def f(x, y, d):
    numbers_list = ""
    for number in range(x, y+1):
        numbers_list += str(number)

    if d in numbers_list:
        return True
    else:
        return False


print(f(10, 15, "14"))
print(f(100,120,"11"))
print(f(205,210,"04"))
