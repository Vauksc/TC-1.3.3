#main file

computer_cards_in_play = []
user_cards_in_play = []

def computer_move():
    computer_cards_in_play += computer_deck[0].face_up(True)
    computer_deck.pop(0) 

def user_move():
    if input("Press 'Enter' to make a move"):
        computer_cards_in_play += computer_deck[0].face_up(True)
        computer_deck.pop(0)

def compare_last_cards():
    if computer_cards_in_play[-1:].rank > user_cards_in_play[-1:].rank:
        return_cards("computer") # merge both cards in play, shuffle and append to computer's deck
    elif computer_cards_in_play[-1:].rank < user_cards_in_play[-1:].rank:
        return_cards("user") # merge both cards in play, shuffle and append to user's deck
    elif computer_cards_in_play[-1:].rank == user_cards_in_play[-1:].rank:
        war() # both place a face down card and face up card, check again

def war():
    computer_cards_in_play += computer_deck[0]
    computer_deck.pop(0)
    computer_move()
    user_cards_in_play += user_deck[0]
    user_deck.pop(0)
    user_move()
    compare_last_cards()

def return_cards(winner):
    return_pile += computer_cards_in_play + user_cards_in_play
    for card in return_pile:
        card.face_up(False)
    random.shuffle(return_pile)
    if winner == "computer":
        computer_deck += return_pile
    if winner == "user":
        user_deck += return_pile

def print_cards_in_play():
    print("Computer: ", end="")
    for card in computer_cards_in_play:
        print(card, end="")
    print()
    print("User: ", end="")
    for card in user_cards_in_play:
        print(card, end="")
    print()

def main():
    computer_move()
    user_move()
    compare_last_cards()