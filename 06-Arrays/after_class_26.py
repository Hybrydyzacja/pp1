# 26.	An array contains a list of Polish names: Genowefa, Onufry, Celestyna, Alojzy, Pankracy.
# Create a program that displays the longest name (consisting of the largest number of characters).


array = ["Onufry", "Genowefa", "Celestyna", "Alojzy", "Pankracy"]

longest_name = ""
i = 0
for name in array:
    if len(array[i]) > len(longest_name):
        longest_name = array[i]
    else:
        continue
    i += 1

print(longest_name)
