from random import randint
import random


# ? 1st Version:


def guess_number(num, attempts):
    # generate a random number between 1 and 'num'
    answer = random.randint(1, num)
    guess = 0

    print(
        f"\nIm thinking of a number between 1 and {num}\nYou have {attempts} attempts"
    )
    print(f"Pssst, the correct answer is {answer}")

    while guess != answer and attempts != 0:
        try:
            guess = int(input(f"\nPlease choose a number between 1 and {num}: "))
        except:
            print("please use numbers only!")
            continue
        if guess < 1 or guess > num:
            print(f"\n* please use only numbers between 1 and {num} *")
            continue
        if guess < answer:
            print("wrong input. too low")
        elif guess > answer:
            print("wrong input. too high")
        attempts -= 1
        if guess != answer:  # print this only if the user guessed incorrectly
            print(f"you have {attempts} more attempts!")
    # if the guessed number is equal to the random number, then the loop is over
    if attempts == 0:
        print(f"You lost! The number was: {answer}")
    else:
        print(f"\ncongratulations! You guessed the correct number: {answer}")


def start_game():
    while True:
        print("Welcome to the Number Guessing Game!")
        try:
            maxsize = int(input("Select the maximal range of numbers: "))
        except ValueError:
            print("please use numbers only")
            continue
        difficulty = input("Choose a difficulty: type 'easy' or 'hard': ").lower()
        if difficulty == "easy":
            guess_number(maxsize, 10)
            break
        elif difficulty == "hard":
            guess_number(maxsize, 5)
            break
        else:
            print("Please type correctly")


# start_game()
# ^ Uncomment to play!

# ? 2nd Version:

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("\nToo high.")
        return turns - 1
    elif guess < answer:
        print("\nToo low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


def set_difficulty():
    while True:
        level = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if level == "easy":
            return EASY_LEVEL_TURNS
        elif level == "hard":
            return HARD_LEVEL_TURNS
        else:
            print("please type correctly")
            continue


def game():
    # Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")
    turns = set_difficulty()  # 5 or 10
    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess a number.
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("please use number only")
            continue
        if guess < 1 or guess > 100:
            print("please use only numbers between 1 and 100")
            continue
        # Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


# game()
# ^ Uncomment to play!


# ? 3rd Version - Compueter guess using binary search


def computer_guess(x):
    low = 1
    high = x
    feedback = ""

    while feedback != "c":
        if low != high:
            # if low = high, this means we removed all the incorrect answers and were left with only the correct answer
            guess = random.randint(low, high)

            guess == low  # could also be 'high'
            feedback = input(
                f"is {guess} too high 'H' too low 'L' or correct 'C'?\n".lower()
            )
            if feedback != "h" and feedback != "l" and feedback != "c":
                print("please use the letters 'h', 'l', 'c' only!")
            elif feedback == "h":
                high = guess - 1
            elif feedback == "l":
                low = guess + 1
            else:  # feedback == 'c'
                print(
                    f"The computer guessed the right number!\nYour number is: {guess}"
                )
        else:
            # if we got out of the loop and now low == high then were left with only the correct number.
            # we will not print the *guessed* number, but we will print the value of 'low' or 'high'
            # (guess is not the correct answer in this case)
            print(f"The computer guessed the right number!\nYour number is: {low}")
            break


def maxrange():
    while True:
        try:
            maxsize = int(input("\nSelect the maximal range of numbers: "))
        except ValueError:
            print("please use numbers only")
            continue
        print(
            "The computer will try to guess your selected number, between 1 and",
            maxsize,
        )
        computer_guess(maxsize)


# maxrange()
# ^ Uncomment to play!
