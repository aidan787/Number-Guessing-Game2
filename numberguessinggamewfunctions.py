
import random

def generate_number():
    secret = random.randint(1, 100)
    return secret

def get_guess():
    guess = int(input("Enter Your Guess! "))
    return guess

def track_attempts(attempts):
    attempts = attempts + 1
    return attempts

def check_guess(guess, secret):
    if guess == secret:
        print("You Have Guessed The Correct Number!")
        return True
    elif guess > secret:
        print("Your Guess Was Too High!")
        return False
    else:
        print("Your Guess Was Too Low!")
        return False

def play_game():
    print("Welcome To The Number Guessing Game!")
    print("The Computer Has Secretly Chosen A Number Between 1 And 100.")
    print("Type Your Guess Below And I'll Tell You If The Answer Is Higher Or Lower.")
    print("See How Few Attempts It Takes You To Guess Correctly!")

    secret = generate_number()
    attempts = 0

    while True:
        guess = get_guess()
        attempts = track_attempts(attempts)
        result = check_guess(guess, secret)

        if result == True:
            print(f"It Took You {attempts} Attempts!")
            break

play_game()

                