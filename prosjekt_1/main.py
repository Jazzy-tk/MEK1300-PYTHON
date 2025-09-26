import random

print("This is a number guessing game. Pick a number between 1 and 100. You have 5 tries")

restart ='' #La til her
while restart != 'yes' and restart != 'no':    #La til her
    restart = input("Ready to start? (Yes/No): ")
    restart = restart.lower()

while restart == "yes":
    attempts = 5
    player_guess = 0
    random_number = random.randint(1, 100)

    print("You have 5 attempts.")

    while player_guess != random_number and attempts != 0:
        player_input = input("Pick a number between 1 and 100: \n")   #endret her, tok vekk int og endret navn fra guess til input

        if player_input.isdigit() and int(player_input) > 1 and int(player_input) < 100:       #La til her
            player_guess = int(player_input)  #La til her
        else: #La til her
            print('That is not a number between 1 and 100') #La til her
            continue #La til her

        # For testing
        print(random_number)

        if player_guess == random_number:
            print('You guessed the right number')
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
