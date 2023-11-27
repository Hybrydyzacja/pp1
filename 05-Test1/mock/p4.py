def f(card_number): 
    return card_number[:2] + "*"*10 + card_number[12:]


if __name__ == '__main__':
    #check your program in this place
    print(f("5290312400019022"))
    print(f("1111000022227777"))

