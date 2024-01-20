# (p1.py) Create a function f(n) that returns the difference between the largest and smallest odd digit contained in the number n. When the number n does not contain odd digits, the function returns -1. 
# Example:
# f(10852) -> 4
# f(7235973) -> 6
# f(4388) -> 0
# f(846206) -> -1


def f(n):
    number_list = []
    for number in str(n):
        number = int(number)
        if number % 2 != 0:
            number_list.append(number)
        else:
            continue
    if len(number_list) > 0: 
        minumum = min(number_list)
        maximum = max(number_list)
    else:
        return -1

    
    return(maximum-minumum)
    



print(f(10852))
print(f(7235973))
print(f(4388))
print(f(846206))