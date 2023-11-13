# 40.	The 'university' variable contains the name of university where you are studying.
# Write a program that displays the contents of the variable with an extra space between characters (add a space between each character)

sentence = "Krakow University of Economics"
result = " ".join(sentence)
print(result)

for char in sentence:
    print(char + " ", end= '')

