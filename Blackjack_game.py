import random

def deal_card():
    """This function randomly chooses two cards from cards list"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """This function calculates the score of a cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw!!!"
    elif c_score == 0:
        return "Yoy Lose..,Opponent has Blackjack!"
    elif u_score == 0:
        return "You Win with a Blackjack!"
    elif u_score > 21:
        return "You went over.You Lose!!"
    elif c_score > 21:
        return "Opponent went over. You Win!!"
    elif u_score > c_score:
        return "You Win..!!"
    else:
        return "You Lose..!!"
    
def play_game():
    user_card = [ ]
    computer_card = [ ]
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"Your cards are: {user_card} current score is: {user_score} ")
        print(f"Computer's First card is: {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            ask = input("Do you want to draw another card? (yes/no)").lower()
            if ask == "yes":
                user_card.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f"Your final Cards: {user_card} and Final score is: {user_score}")
    print(f"Computer's final cards: {computer_card} and Final score is: {computer_score}")

    print(compare(user_score, computer_score))

while input("Do you want to play A game of Blackjack? (yes/no)").lower() == "yes":
    print("\n" * 30)
    play_game()
