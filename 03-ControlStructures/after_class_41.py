# 41.	The payment card is secured with a four-digit PIN code (0805). 
# Write a program that checks if the PIN code entered in the payment terminal is correct. 
# The user has up to three possibilities for entering a PIN code. In case of three unsuccessful attempts, the card is blocked. 
# Sample result:
# Enter the PIN code: 2398
# Incorrect...
# Enter the PIN code: 0912
# Incorrect...
# Enter the PIN code: 7860
# Incorrect...
# Sorry, your payment card has been blocked.


PIN_code = "0805"
# PIN_code_guess = input("Enter PIN code: ")
guesses = 0

while guesses < 3:
    guess = input("Enter PIN code: ")
    if guess == PIN_code:
        print("Correct")
        break
    elif guess != PIN_code:
        print("Incorrect...")
        guesses += 1
        if guesses == 3:
            print("Sorry, your payment card has been blocked.")

        
        
    
