# 9
n1 = 5
n2 = 1
n3 = 8
n4 = 6
n5 = 3

a = n1+n2+n3+n4+n5
b = n1**2 + n2**2 + n3**2 + n4**2 + n5**2
c = n3/n5
d = n3 == n4
print(a, b, c, d)



# 10
name = input("Podaj imię: ")
age = input("Podaj wiek: ")
height = input("Podaj wzrost[cm]: ")

sentence = f'My name is {name}, I am {age} years old, and my height is {height} cm. In 6 years I will be {int(age)+6} years old.'
print(sentence)



# 11
# Write a program that calculates and displays the income of a family per person.
# To display the results in a readable form, use f-strings. Sample result:

father_inc = int(input("Podaj dochód ojca: "))
mother_inc = int(input("Podaj dochód matki: "))
people = int(input("Ile osób liczy rodzina: "))
total_inc = father_inc + mother_inc
inc_per_person = total_inc / people

result = f"""Enter father's income: {father_inc}
Enter mother's income: {mother_inc}
Enter number of people in family: {people}
Total income: {total_inc}
Income per person: {inc_per_person}"""
print(result)



# 13
# Write a program that calculates the surface area of a cube.
# Read the length of the side of the cube from the keyboard. Take into account that the input() function returns a string,
# not a number. To convert a string to a number, use the int() function.

side_lenght = int(input("Podaj długośc boku: "))
print(f'The surface area of a cube with side {side_lenght} is {side_lenght**3}')



### 14
# The radius of the circle has the value 5, stored in a variable.
# Write a program that calculates the area and circumference of the circle. Use the algorithm below.
# Calculation of circle area and circumference
# determine radius and PI
# calculate area
# calculate circumference
# display results

import math
radius = 5
area = round(math.pi * radius**2,4)
circumference = round(2 * math.pi * radius,4)
print(f'area = {area}, circumference = {circumference}')



### 15
# Write a program that reads temperature in degrees Celsius from the keyboard. 
# Then, the program calculates and displays the temperature in Kelvin and Fahrenheit. 
# Use comments to briefly describe the program's algorithm.

temp_cel = float(input("Podaj temperaturę w stopniach Celcjusza: "))
Kelvin = 273.15 + temp_cel
Fahrenheit = 1.8 * temp_cel + 32
print(f"Temperatura wynosi {temp_cel} stopni Celcujsza, co równa się {Kelvin} Kelvinom i {Fahrenheit} stopniom Fahrenheita")



