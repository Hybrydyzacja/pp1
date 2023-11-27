# 1.
# def f(a,b):
#     if a>b:
#         return(f'{a}-{b}={a-b}')
#     else:
#         return(f'{a}+{b}={a+b}')

# print(f(20,8))
# print(f(8,12))
# print(f(7,7))


# __________________________________
# 2.
# def f(k):
#     list = [2, 3, 5, 7]
#     for i in range(1000):
#         for n in range(1, i+1):
#             if i % n == 0 and n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0:
#                 list.append(n)

#     set_prim = set(list)
#     return(sorted(set_prim))[k]
# print(f(25))


# ________________________________
# 3.
# from collections import Counter
# def f(string):
#     char_dict = Counter(string)
#     if len(string) >= 6:
#         if(len(char_dict) == len(string)):
#             return True
#         else:
#             return False
#     else:
#         return False
# print(f("xDabc1258"))
# lub
# def f(string):
#     set_string = set(string)
#     if len(string) >= 6:
#         if len(string) == len(set_string):
#             return True
#         else:
#             return False
#     else:
#         return False
# print(f("xb4758"))


# ________________________________
# 4.
# def f(w):
#     string_mod = ""
#     for i, n in enumerate(w):
#         if i % 2 == 0:
#             string_mod += n + "+"
#         else:
#             string_mod += n + "-"
#     last = len(string_mod)
#     return string_mod[:-1]
# print(f(""))


# def f(w):
#     string_mod = ""
#     for i, char in enumerate(w):
#         if i % 2 == 0:
#             string_mod += char + "+"
#         else:
#             string_mod += char + "++"

#     if len(string_mod) % 5 == 0:
#         return string_mod[:-2]
#     else:
#         return string_mod[:-1]
# print(f("99887766"))


# ________________________________
# 5.
# def f(a,b):
#     numbers_e = []
#     if a < b:
#         for number in range(a,b+1):
#             if number % 2 == 0:
#                 numbers_e.append(str(number))
#     numbers_ee = ",".join(numbers_e)
#     return numbers_ee
# print(f(201,211))


# ________________________________
# 6.
# from collections import Counter
# def f(t,c,n):
#     for char in t:
#         amount_dict = Counter(t)
#     for value in amount_dict:
#         number_in_dict = amount_dict[c]
#     return number_in_dict == n

# print(f("abbcccddddeeeeeffffff","e",5))

# def f(t, c, n):
#     counter = 0
#     for char in t:
#         if char == c:
#             counter += 1
#         else:
#             continue
#     return counter == n
# print(f("abbcccddddeeeeeffffff","a",1))


# ________________________________
# 7.
# def f(t):
#     numbers = []
#     for i in range(20, 15,-1):
#         numbers.append(str(i))
#     numbers_str = ",".join(numbers)
#     return(numbers_str)
# print(f((20, 15)))


# ________________________________
# 8.
# def f(n):
#     list = []
#     for num in str(n):
#         list.append(int(num))
#     return(sum(list))
# print(f(88077066))


# ________________________________
# 8. Fibbo
# def f(n):
#     a = 0
#     b = 1
#     if n == 0:
#         return 0
#     elif n == 1:
#         return b
#     else:
#         for i in range(1, n):
#             c = a + b
#             a = b
#             b = c
#         return a
# print(f(17))
