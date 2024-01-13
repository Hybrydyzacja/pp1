# 25.	An array contains values: 15, 8, 31, 47, 2, 19. Create a program that calculates and displays 
# the array and the arithmetic mean of array values. Use the “while” loop statement.

array = [15, 8, 31, 47, 2, 19]

i = 0
suma = 0
while i < len(array):
    suma += array[i]
    i += 1

mean = round(suma / len(array),4)
print(mean)