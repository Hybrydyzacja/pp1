# 23.	Write a program that calculates a dog's age in dog’s years. For the first two years, 
# a dog's life is equal to 10.5 human years. After that, each dog year is equal to 4 human years.

dogs_age_h = float(input("Enter the dog's age in human years: "))
if dogs_age_h <= 2:
    dogs_age_d = dogs_age_h * 10.5
else:
    dogs_age_d = 2 * 10.5 + (dogs_age_h-2) * 4

print(f"The dog's age in dog’s years is {int(dogs_age_d)} years.") #maybe better float than int?