# 16.	A program contains two functions:
# a.	hotel_list(hotels) that returns a list of hotels names, separated by a comma sign
# b.	avg_price(hotels) that returns the average room price for a given list of hotels, rounded to an integer value
# Write a program that calculates and displays the average price for a room in hotels in Krakow and Sopot and indicates in which cities hotels are cheaper.


Hotels_in_Krakow = [
    {"name": "Sky", "price": 320.00},
    {"name": "Metropol", "price": 480.00},
    {"name": "New Port", "price": 420.00},
    {"name": "Aparthotel", "price": 390.00}
]
Hotels_in_Sopot = [
    {"name": "Focus", "price": 510.00},
    {"name": "Aqua", "price": 345.00},
    {"name": "La Boutique", "price": 390.00},
    {"name": "Marina", "price": 410.00}
]


i = 0
hotels_krakow = []
for key, value in Hotels_in_Krakow:
    hotels_krakow.append(Hotels_in_Krakow[i][key]) 
    i += 1
print(", ".join(hotels_krakow))

j = 0
hotels_sopot = []
for key, value in Hotels_in_Sopot:
    hotels_sopot.append(Hotels_in_Sopot[j][key]) 
    j += 1
print(", ".join(hotels_sopot))



