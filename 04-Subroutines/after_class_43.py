# 43.	A text contains any number of words. Define a function f(name) that returns the acronym (first letters of all words). Sample result:
# f("Internet of Things") returns "IoT"
# f("For Your Information") returns "FYI"
# f("Python") returns "P"

def f(sentence):
    a = ""
    sentence_spl = sentence.split()
    for word in sentence_spl:
        a += word[0]
    return a

print(f("Internet of Things")) 
print(f("For Your Information")) 
print(f("Python")) 