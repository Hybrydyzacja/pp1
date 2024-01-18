def f(word):
    new_word = ""
    i = 0
    # for n in range(len(word)):
    for letter in word:
        new_word += letter.upper()

    new_word += "-"
    return new_word[:-1]


print(f("book"))
