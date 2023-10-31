def convert_number(number):
    hex_num = hex(number)
    binary_num = bin(number)

    return(number, binary_num, hex_num)

print(convert_number(125))