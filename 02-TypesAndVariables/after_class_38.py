# number = input("Podaj numer: ")
# print(number[:3] + "-" + number[3:6] + "-" + number[6:])

def number_separated(number):
    number = str(number)
    return(number[:3] + "-" + number[3:6] + "-" + number[6:])
print(number_separated(123456789))