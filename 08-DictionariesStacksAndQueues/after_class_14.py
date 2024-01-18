winter_semester = {
    "math":60,
    "programming":30,
    "history":15
}

hours = 0
for key, value in winter_semester.items():
    hours += (winter_semester[key])

print(f"The total number of hours in the winter semester is {hours}")


# hours = 0
# x = winter_semester.values()
# for value in x:
#     hours += value

# print(hours)