import random
number = int(input("Please Enter a number:"))
guesses = random.randint(1, 100)
count = 1

while number <=100 and number >=1 :
    count+=1
    if number > guesses:
        print("your guess is too high")
        number = int(input("Please Enter a number:"))
    elif number < guesses:
        print("your guess is too low")
        number = int(input("Please Enter a number:"))
    elif number == guesses:
        print("You chose correctly")
        print("your guesses are", + count)
        break