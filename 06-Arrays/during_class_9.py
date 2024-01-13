# 9.	An array contains values: 2, 3, 7, 5, 4. Create a program that displays:
# a.	the array
# b.	number of elements
# c.	first value
# d.	second value
# e.	last value
# f.	last but one value (do not use negative index values)
# g.	sum of the first and last value
# h.	middle value
# i.	all array values separated by a single space (use a loop statement)


array = [2, 3, 7, 5, 4]

print(array)
print(len(array))
print(array[0])
print(array[1])
print(array[-1])
print(array[0]+array[-1])
print(array[int(len(array)/2)])
for element in array:
    print(element, end=" ")
