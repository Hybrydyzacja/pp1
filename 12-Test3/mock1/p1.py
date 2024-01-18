
# (p1.py) Create a function f(word) that, for a given word, returns a string of characters in which the subsequent letters of the word form the so-called Mexican Wave. 
# Initially, the first letter of the word is capitalized and the remaining letters are lowercase. Then, the second letter of the word is capitalized and the remaining letters are lowercase, etc. Separate words with a minus sign. Example:
# f("book")  "Book-bOok-boOk-booK"



def f(word):
    new_word = []

    i = 0
    for my_word in word:
        my_word = (word[:i].lower() + word[i].upper() + word[(i+1):len(word)])
        new_word.append(my_word)
        i += 1
        
    return "-".join(new_word)


print(f("book"))
print(f("water"))
print(f("ok"))
print(f("a"))
print(f(""))