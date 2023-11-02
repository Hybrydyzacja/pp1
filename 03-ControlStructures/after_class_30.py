# 30.	Write a program that allows you to convert time in 24-hour format to 12-hour format. 
# The time in 24-hour format (hh:mm) is read from the keyboard. Sample result:
# Enter time (24-hour format): 16:32
# Time in 12-hour format: 4:32pm

time = input("Enter time 24h format: ")
time_splited = time.split(":")
if int(time_splited[0]) >= 12:
    hour = int(time_splited[0]) - 12
    time_changed = str(hour) + ":" + time_splited[1] +"pm"
else:
    hour = time_splited[0]
    time_changed = str(hour) + ":" + time_splited[1] +"am"

print(f'Time in 12-hour format: {time_changed}')


