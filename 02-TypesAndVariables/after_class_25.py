# 25.People up to and including 26 years of age are exempt from paying taxes in Poland. 
# Write a program that, based on the person's age entered from the keyboard, 
# displays True if the person is exempt from paying taxes and displays False otherwise.

age = int(input("Enter age: "))
print("Exemption from paying taxes: ", age <= 26)