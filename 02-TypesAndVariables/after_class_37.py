# The employee file contains the employee's data in a descriptive form. Write a program in which the personal_data variable contains employee data:
# "Mr. John May, born on 1998-02-16"
# Display the employee's name, surname, initials and date of birth on separate lines. Sample result:
# Description: Mr. John May, born on 1998-02-16
# Name: John
# Surname: May
# Initials: JM
# Born: 1998-02-16


personal_data = "Mr. John May, born on 1998-02-16"

print(
    f"Descripton: {personal_data}\nName: {personal_data[4:8]}\nSurname: {personal_data[9:12]}\nInitials: {personal_data[4]}{personal_data[9]}\nBorn: {personal_data[22:]}")
