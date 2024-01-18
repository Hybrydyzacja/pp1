countries = [
    {"name":"Poland", "population":38000000},
    {"name":"Germany", "population":64000000},
    {"name":"Greece", "population":18000000},
    {"name":"Finland", "population":34000000},
    {"name":"Italy", "population":41000000}
    ]

n = 0
print("COUNTRY", "POPULATION")

while n < len(countries):
    print(countries[n]["name"] + ": " + str(countries[n]["population"]))
    n += 1 