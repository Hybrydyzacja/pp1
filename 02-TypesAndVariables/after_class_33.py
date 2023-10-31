# password  = input("Enter password: ")
# print(f'Password is valid: {len(password)>=8}')


def check_password(password):
    return((len(password)) >= 8)

print(check_password("XaaaaaaD"))
