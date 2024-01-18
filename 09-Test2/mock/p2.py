def f(arr):
    set_arr = set(arr)
    str_arr = ""
    for element in set_arr:
        str_arr += str(element)
    counter = 0
    for number in arr:
        if str(number) == str_arr[0]:
            counter += 1

    if counter == 1:
        return int(str_arr[0])
    else:
        return int(str_arr[1])
            


print(f([7, 7, 7, 7, 7, 5, 7, 7]))
