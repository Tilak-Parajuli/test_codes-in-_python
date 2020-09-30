# number guessing game 
winning_number =13
guessing_number=input("Guess the number between 10 to 20 :")
guessing_number =int(guessing_number)
if guessing_number == winning_number:
    print("YOU WON!!!!")
else:
    if winning_number > guessing_number:
        print("TOO LOW")
    else:
        print("TOO HIGH!!")       