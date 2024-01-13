# 27.	An array contains integer numbers: 12, 6, 4, 9, 10. Create a program that displays the array values graphically as below.
# Define a function star(n) that returns the given number of asterisks as a string. Use a defined function in the program.
# 12: ************
#  6: ******
#  4: ****
#  9: *********
# 10: **********


def star(n):
    output = ""
    for number in n:
        output += (str(number) + ": " + "*"*number) #how to return with new line?#

    return output


print(star([12, 6, 4, 9, 10]))
