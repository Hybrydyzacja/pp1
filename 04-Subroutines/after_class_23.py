# 23.	Create a program that calculates how many times the given letter appears in any text. 
# Then create a program and check how many times the letter ‘e’ appears in the text below. 
# In a separate module, define a function for making calculations. Sample result:
# You never get a second chance to make a first impression
# The number of letter 'e': 7

def f(sentence, letter):
    counter = 0
    for n in sentence:
        if n == letter:
            counter +=1 
    return counter

print(f("You never get a second chance to make a first impression", "e"))