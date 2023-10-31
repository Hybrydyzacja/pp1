# 24. Vehicle registration numbers in Kraków start with the letters KR or KK. 
# Write a program that checks whether the vehicle registration number entered from the keyboard means a vehicle from Krakow. 
# Display True whether a car is from Kraków or False otherwise. 

registration = input("Enter vehicle registration number: ")

print("Car from Cracow:", registration[:2] == "KK" or registration[:2] == "KR")
