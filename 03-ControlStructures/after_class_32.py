# 32.	Yes-no question are often used in surveys to gauge people's attitudes with regard to specific ideas or beliefs. 
# Write a program that displays a survey consisting of three questions. Save the answers to logical type variables. 
# Then view the survey result. Sample result:
# Are you interested in computer science? (Y/N): Y 
# Do you like playing computer games? (Y/N): N
# Do you have an Instagram account? (Y/N): Y
# Interested in computer science: Yes
# Playing computer games: No
# Has an Instagram account: Yes


first_question = input("Are you interested in computer science? (Y/N): ")
second_question = input("Do you like playing computer games? (Y/N): ")
third_question = input("Do you have an Instagram account? (Y/N): ")

if first_question == "Y":
    first_question = True
    print("Interested in computer science: Yes")
elif first_question == "N":
    first_question = False
    print("Interested in computer science: No")
else:
    print('You can use only "Y" or "N"')

if second_question == "Y":
    second_question = True
    print("Playing computer games: Yes")
elif second_question == "N":
    second_question = False
    print("Playing computer games: No")
else:
    print('You can use only "Y" or "N"')

if third_question == "Y":
    third_question = True
    print("Has an Instagram account: Yes")
elif third_question == "N":
    third_question = False
    print("Has an Instagram account: No")
else:
    print('You can use only "Y" or "N"')
