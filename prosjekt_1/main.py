import random

print("This is a number guessing game. Pick a number between 1 and 100. You have 5 tries")

restart = input("Ready to start? (Yes/No): ")
restart = restart.lower()

while restart == "yes":
    attempts = 5
    player_guess = 0
    random_number = random.randint(2, 99)

    print("You have 5 attempts.")

    while player_guess != random_number and attempts != 0:
        player_guess = int(input("Pick a number between 1 and 100: \n"))

        # For testing
        print(random_number)

        if player_guess == random_number:
            break

        if player_guess > random_number:
           position = "above"
        elif player_guess < random_number:
            position = "below"

        attempts = attempts - 1

        if attempts > 0:
            print("You guessed wrong. Your number is ", position, " the random one. \nYou have ", attempts, " attempts left")
 
    if player_guess != random_number:
        print("Sorry! You did not manage to guess the number. You have reached the guessing limit.")
        restart = input("Want to try again? (Yes/No):\n")

    elif player_guess == random_number:
        attempts = 6 - attempts
        print("Congratulations! You guessed the number in ", attempts, " attempt(s).")
        restart = input("Want to try again? (Yes/No):\n")
