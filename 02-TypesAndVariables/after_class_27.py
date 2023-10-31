# 27.Write a program that checks whether the number entered from the keyboard is between -10 and 10. 
# Display True if the number is in the given range, and False otherwise.

number = int(input("Enter number: "))
print("Number in the range <-10,10>:", number <= 10 and number >= -10)