import random
print("Welcome to the Rock Pape Scissors Game")
print("stone,paper,scissors!!!!!!!!!")
def game():
    w = input("What do you choose?")
    if w != 'rock' and w != 'paper' and w != 'scissors':
        print("You entered wrong choice")
    else:
        twist = ['rock','paper','scissors']
        h = random.choice(twist)
        print(h)
        if h == w:
            print("It's a tie")
        elif w == 'rock' and h == 'paper':
            print("You lost")
        elif w == 'paper' and h == 'rock':
            print("You won")
        elif w == 'scissors' and h == 'paper':
            print("You won")
        elif w == 'paper' and h == 'scissors':
            print("You lost")
        elif w == 'rock' and h == 'scissors':
            print("You won")
        elif w == 'scissors' and h == 'rock':
            print("You lost")
        else:
            print("It's a tie")

know = True
while know:
    game()
    ask = input("Do you want to play again? Type 'yes' or 'no':").lower()
    if ask == 'yes':
        know = True
    elif ask == 'no':
        know = False
        print("Thank You For Playing...!!!")
    else:
        print("You Entered Wrong Choice.")
