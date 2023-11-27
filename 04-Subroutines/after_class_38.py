# 38.	A palindrome is an expression that sounds the same when read backwards. 
# Define a function f(palindrome) that returns True if the expression is a palindrome or False otherwise. 

def f(palindrome):
    a = palindrome
    b = palindrome[::-1]
    return a == b

print(f("radar"))
print(f("12-11-21"))
print(f("book"))