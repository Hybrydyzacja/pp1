def f(player1, player2):
    p1 = player1
    p2 = player2
    suma_p1 = 0
    suma_p2 = 0
    for symbol in p1:
        if symbol == "A" or symbol == "Q" or symbol == "K" or symbol == "J"  or symbol == "T":
            suma_p1 += 10
        else:
            suma_p1 += int(symbol)
    for symbol in p2:
        if symbol == "A" or symbol == "Q" or symbol == "K" or symbol == "J" or symbol == "T":
            suma_p2 += 10
        else:
            suma_p2 += int(symbol)

    return suma_p1 >= suma_p2
        

print(f("AJ972", "AQT72"))
print(f("9532", "K8"))