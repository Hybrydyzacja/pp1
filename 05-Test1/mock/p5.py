def f(binary_number):
    c = 0
    for n in binary_number:
        if n != "0" and n != "1":
            c += 1
    return c == 0


if __name__ == '__main__':
    #check your program in this place
    print(f("101101"))
    print(f("1011201"))
    print(f("1010b1"))