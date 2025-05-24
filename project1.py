import random

x = random.randint(1, 100)
# print("x "+ str(x))  # For debugging purposes, you can see the number
while True:
    guess = input("Guess a number between 0 and 100: ")
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    guess = int(guess)
    if guess < 0 or guess > 100:
        print("The number should be between 0 and 100.")
        continue
    elif guess < x:
        print("Too low!")
    elif guess > x:
        print("Too high!")
    else:
        print("Congratulations! You guessed the number.")
        break