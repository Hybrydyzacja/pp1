def f(name):
    acronym = ""
    for word in name.split():
        acronym += word[0]
    return acronym


if __name__ == '__main__':
    # check your program in this place
    print(f("For Your Information"))
    print(f("Hello Poland Krakow university"))
