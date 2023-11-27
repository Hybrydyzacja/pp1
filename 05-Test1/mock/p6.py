def f(number, even):
    suma = 0
    if even == True:
        for n in str(number):
            if int(n) % 2 == 0:
                suma += int(n)
            else:
                continue
    else:
        for n in str(number):
            if int(n) % 2 != 0:
                suma += int(n)
            else:
                continue

    return suma



if __name__ == '__main__':
    #check your program in this place
    print(f(3124,True))
    print(f(3124,False))
    print(f(20576,False))
    print(f(20576,True))
    print(f(13115,True))
