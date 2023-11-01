# 8.	The speed limit on a motorway in Poland is 140 km/h. 
# Write a program that checks whether a car exceeded the speed limit. If so, a warning is displayed.
speed_limit = 140
car_speed = int(input("Enter car speed km/h: "))
if car_speed > speed_limit:
    print("Warning: speed limit exceeded!")


# 9.	A test is passed when the number of correctly completed tasks is at least 50%. Write a program that checks whether the test is passed. 
# The total number of test tasks and the number of correctly completed tasks are included in variables.
tasks = int(input("Enter number of tasks: "))
corect_answers = int(input("Enter number of correct answers: "))
if corect_answers / tasks * 100 >= 50:
    print("Test passed")
else:
    print("Try again")


# 10.	Write a program to calculate the absolute value of a number entered from the keyboard. Sample result:
# Enter number: -17
# |-17| = 17
number = int(input('Enter number: '))
print(f'Absolute value of {number} is {abs(number)}')


# 11.	Write a program that checks whether the number entered from the keyboard is even or odd. Sample result:
# Enter number: 27
# Number is odd
number = int(input("Enter number: "))
if number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")


# 12.	Write a program that checks that two people are adults. Read people’s data from the keyboard.
first_person_name = input("Enter your name(1): ")
first_person_age = int(input("Enter tour age(1): "))
second_person_name = input("Enter your name(2): ")
second_person_age = int(input("Enter tour age(2): "))
if first_person_age >= 18 and second_person_age >= 18:
    print(f'Both {first_person_name} and {second_person_name} are adults')
elif first_person_age >= 18 and second_person_age < 18:
    print(f'Only {first_person_name} is an adult')
elif first_person_age < 18 and second_person_age >= 18:
    print(f'Only {second_person_name} is an adult')
else:
    print("Neither of you are adults")


# 13.	A user enters two integer numbers from the keyboard. 
# Write a program that checks whether at least one of them is not negative.
number_one = int(input("Enter number 1: "))
number_two = int(input("Enter number 2: "))
print(number_one >= 0 or number_two >= 0)



