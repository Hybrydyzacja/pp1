# 39.	A sentence is an ordered group of words separated by spaces (spaces). 
# Define a function f(sentence) that returns a sentence with spaces removed. 
# Sample result:
# f("integrated development environment") returns "integrateddevelopmentenvironment"

def f(sentence):
    x = sentence.split()
    y = "".join(x)
    return y
print(f("integrated development environment"))