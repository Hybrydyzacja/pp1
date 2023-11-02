# 29.	A washing machine allows you to wash a jacket, which takes 40 minutes, wash underwear, which takes 70 minutes, and wash shoes, which takes 20 minutes. 
# In addition, it is possible to program an additional rinse (15 minutes) and an additional spin (9 minutes). The washing machine settings are saved in variables. 
# Write a program that calculates and displays the total washing time.

product = input("Enter product name: ")

if product == "jacket":
    washing_time = 40
elif product == "underwear":
    washing_time = 70
elif product == "shoes":
    washing_time = 20
else:
    print("Wrong product name, try again")

rinse = input("Rinse [yes/no]? ")
spin = input ("Additional spin [yes/no]? ")

if rinse == "yes":
    washing_time += 15
if spin == "yes":
    washing_time += 9

print(washing_time)