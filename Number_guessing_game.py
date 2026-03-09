from random import randint

easy_level_turns = 10
hard_level_turns = 5

def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("You guessed too high")
        return turns - 1
    elif user_guess < actual_answer:
        print("You guessed too low")
        return turns - 1
    else:
        print(f"You get it! The answer was {actual_answer}")


def number_guess():
    choice = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
    if choice == "easy":
        return easy_level_turns
    else:
        return hard_level_turns


def game():
    print("Welcome to the number Guessing Game:")
    print("I am thinking of number between 1 and 100.")
    answer = randint(1, 100)

    turns = number_guess()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts to guess the number.")
        guess = int(input("Guess a number between 1 and 100:"))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have run out of guesses, You Loose!!")
            return
        elif guess != answer:
            print("Guess Again!")
game()