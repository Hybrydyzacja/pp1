# 21.	An array contains natural numbers: 15, 8, 31, 47, 2, 19. Create a program that displays the contents of the array in reverse order.

array = [15, 8, 31, 47, 2, 19]
array_reversed = array[::-1]
array_reversed2 = list(reversed(array))
print(array_reversed)
print(array_reversed2)
print(array)
array.reverse()
print(array)