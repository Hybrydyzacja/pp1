# 17.	An array contains values: [[0,0,0],[0,0,0],[0,0,0]]. Create a program that replaces the values of the main diagonal with 1.
# Use proper loop statements. Display the modified array.

array = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

i = 0
j = 0
while i < len(array):
    array[i][j] = 1
    i += 1
    j += 1
    
print(array)
