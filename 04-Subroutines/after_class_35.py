# 35.	Two numbers and an operator are given. Define a function f(number1,number2,operator) that returns the result of an arithmetic operation. 
# The available operators are +,-,*,%,**. 

def f(number1, number2, operator):
    if operator == "+":
        return int(number1) + int(number2)
    elif operator == "-":
        return int(number1) - int(number2)
    elif operator == "*":
        return int(number1) * int(number2)
    elif operator == "**":
        return int(number1) ** int(number2)
    else:
        return int(number1) %  int(number2)


print(f(2,3, "+"))
print(f(2,3, "%"))
print(f(2,3, "**"))
print(f(2,3, "*"))
print(f(2,3, "-"))