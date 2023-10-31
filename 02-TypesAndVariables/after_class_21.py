# 21. A variable contains your height in cm.
# Write a program that displays your height both in cm and in feet and inches.

cm = int(input("Podaj wzrost w cm: "))
# 1 ft = 30.48 cm = 12 inch
 
ft = int(170 / 30.48)
inch =  int(round(((170 / 30.48) - ft) * 12,0))
print(f'I am {cm} tall, i.e. {ft} feet and {inch} inches')
