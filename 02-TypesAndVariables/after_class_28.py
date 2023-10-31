# 28.	Correct body weight has a significant impact on health. 
# Write a program that calculates the Body Mass Index (BMI) based on your height in cm and weight in kg. 
# A user enters data from the keyboard. Find the formula on the Internet for calculating the BMI. Then, using your program, 
# check that you have the correct weight.  Display the calculated BMI and display True if the weight is within the valid range, or display False otherwise. 

height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

BMI = weight / (height/100)**2
# correct <18,5-25)
print(f"Your BMI index: {BMI}\nCorrect weight: {BMI >= 18.5 and BMI < 25}")

