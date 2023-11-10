# 35.	Write a program that displays numbers from 1 to 30. If the number is divisible by 3 then the program displays the word 'THREE'. 
# Next, if the number is divisible by 5 then the program displays the word 'FIVE'. 
# Finally, if the number is divisible by both 3 and 5 then the program displays the word 'BINGO'. 

for number in range(1, 31):
    if number % 3 == 0 and number % 5 == 0:
        print("BINGO")
    elif number % 3 == 0:
        print("THREE")
    elif number % 5 == 0:
        print("FIVE")
    else:
        print(number)


# def f(max_value):
#     numbers = []
#     for number in range(1, max_value+1):
#         if number % 3 == 0 and number % 5 == 0:
#             number = "BINGO"
#             numbers.append(number)
#         elif number % 3 == 0:
#             number = "THREE"
#             numbers.append(number)
#         elif number % 5 == 0:
#             number = "FIVE"
#             numbers.append(number)
#         else:
#             numbers.append(number)
#     return(numbers)
# print(f(30))
