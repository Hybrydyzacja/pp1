# 19.	Write a program that calculates the sum of even numbers in the range <1,10>.

sum = 0
for i in range(1, 11):
    if i % 2 == 0:
        sum += i
print(sum)


sum = 0
n = 1
while n <= 10:
    if n % 2 == 0:
        sum += n
    n += 1
print(sum)
