# 24.	An array contains values: 15, 8, 31, 47, 2, 19. Create a program that calculates and displays
# the array and the arithmetic mean of array values. Use the “for” loop statement.

array = [15, 8, 31, 47, 2, 19]
suma = 0
for element in array:
    suma += element

mean = round(suma / len(array),4)
print(mean)
