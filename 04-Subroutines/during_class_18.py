def numbers(n):
    numbers_str = ""
    for i in range(1, n):
        numbers_str += (str(i) + " ")
    numbers_str = numbers_str.rstrip()
    return(numbers_str)


print(numbers(7))
