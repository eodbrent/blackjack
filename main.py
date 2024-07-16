import time
import deck
import random
import gameascii

user_hand = []
dealer_hand = []
user_value = 0
dealer_value = 0
running_count = 0
true_count = 0  # Multiple deck counting on TODO list
shuffled_deck = deck.deck
main_game_loop = True
a = "a"
of = " of BlackJack"
PURPLE = "\033[35m"
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
CYAN = "\033[31m"
RESET = "\033[0m"
PLAYER = PURPLE + "Player" + RESET
DEALER = YELLOW + "Dealer" + RESET

def maintain_card_count(card):
    """Updates running_count, TODO: true_count = running_count / decks left"""
    global running_count
    card_count_values = {"A": -1,
                     "1": -1, "J": -1, "Q": -1, "K": -1,
                     "7": 0, "8": 0, "9": 0,
                     "2": 1, "3": 1, "4": 1, "5": 1, "6": 1}
    #  print(f"{card} means {card_count_values[card[0]]} to the total")
    running_count += card_count_values[card[0]]


def bool_convert(message_response):
    """Converts 'y' or 'n' to 'True' or 'False', respectively"""
    message_response = message_response.lower()
    if message_response == 'y':
        return True
    else:
        return False


def get_card_value(card):
    """Calculates card value."""
    value = 0
    card_values = {"A": 11,
                   "2": 2, "3": 3, "4": 4,
                   "5": 5, "6": 6, "7": 7,
                   "8": 8, "9": 9, "1": 10,
                   "J": 10, "Q": 10, "K": 10}
    value = int(card_values[card[0]])
    return value


def get_hand_value(hand):
    """Calculates hand value."""
    value = 0
    for card in hand:
        value += int(get_card_value(card))
    return value


def deal():
    """Deals 2 cards from top of shuffled deck"""
    hand = []
    for i in range(2):
        hand.append(shuffled_deck[0])
        shuffled_deck.remove(shuffled_deck[0])
        maintain_card_count(hand[i])
        #  print(f"Next Card in deck: {shuffled_deck[0]}")
    return hand


def ace_value(hand, hand_value):
    """Determines Ace = 1 or 11. If 11 pushes hand over 21, Ace value = 1"""
    hand_ace_value = hand_value
    for card in hand:
        if card[0] == 'A':
            #  For each Ace, subtract 10
            hand_ace_value -= 10
    if hand_value > 21 >= hand_ace_value:
        return hand_ace_value
    else:
        return hand_value


def display_running_count():
    """Prints running count value."""
    print(f"{CYAN}Card Counting - Running Total: {running_count}{RESET}")


heart = "\u2746"
diamond = "\u2666"
spade = "\u2660"
club = "\u2663"
#  TODO: Ascii art for GUI
#  print(gameascii.heart)
#  print(gameascii.diamond)
#  print(gameascii.club)
#  print(gameascii.spade)
while main_game_loop:
    if len(shuffled_deck) < 10:
        print("Under 10 cards left in the deck. Not enough for a game.")
        quit()

    prompt = input(f"How about {a} game{of}? {GREEN}y{RESET} for {GREEN}yes{RESET}, {RED}n{RESET} for {RED}no{RESET}: ")
    count_cards = bool_convert(input("Do you want to see card counting (Hi-Lo System)?").lower())
    if count_cards:
        print("The running count will be updated each time a card is dealt. The higher the running count, the higher the advantage for you!")
    if a == 'a':
        deck_num = int(input("How many decks would you like to play with? "))
        for _ in range(0, deck_num - 1):
            shuffled_deck.extend(deck.deck)
        random.shuffle(shuffled_deck)
    if prompt == 'n':
        quit()
    elif prompt == 'y':
        user_hand = deal()            # uncomment/comment for real deal from deck
        dealer_hand = deal()          # uncomment/comment for real deal from deck
        #    ---HAND TESTING---    ####
        #  user_hand = ["As", "5d"]   # uncomment/comment for testing specific hand values
        #  ---END HAND TESTING---  ####
        print(f"{PURPLE}Your hand: {user_hand}{RESET}")
        user_value = get_hand_value(user_hand)
        print(f"{PURPLE}Your hand is worth: {user_value}{RESET}")
        print(f"{DEALER}{YELLOW} hand: {dealer_hand}{RESET}")
        dealer_value = get_hand_value(dealer_hand)
        print(f"{DEALER}{YELLOW} hand is worth: {dealer_value}{RESET}")
        print("What would you like to do?")
        game_on = True
        while game_on:
            user_turn = True
            while user_turn:
                if user_value == 21:
                    print("You win!")
                    user_turn = False
                    break
                elif user_value > 21:
                    print("You busted!")
                    user_turn = False
                    break
                display_running_count()
                choice = input("Hit (h), Stand (s), Double Down (d), Split (Requires doubles) (t), Quit (q), \"deck\" displays number of cards left: ").lower()

                if choice == "q":
                    quit()
                elif choice == "deck":
                    print(len(shuffled_deck))
                elif choice == "h":
                    print("hit")
                    if len(shuffled_deck) > 0:
                        user_hand.append(shuffled_deck[0])
                        shuffled_deck.remove(shuffled_deck[0])
                        user_value = get_hand_value(user_hand)
                        for card in user_hand:
                            if card[0] == 'A':
                                user_value = ace_value(user_hand, user_value)
                                print("You had an Ace. We just checked if it needed to be 11 or 1")
                                break
                        print(f"{PURPLE}Your hand: {user_hand}")
                        print(f"You have {user_value}{RESET}")
                    else:
                        print("Deck is empty. No more game. Bye!")
                        quit()
                elif choice == "s":
                    print("stand")
                    print(f"{PLAYER} stands.")
                    print(f"{YELLOW}Dealer's{RESET} turn.")
                    break
                elif choice == 'd':
                    print("Double Down - not functional yet")
                elif choice == 't':
                    print("Split - not functional yet")
                else:
                    print("{RED}Invalid choice. Please try again.")
            dealer_turn = True
            if user_turn:
                while dealer_turn:
                    if dealer_value < 21 and dealer_value <= user_value:
                        print(f"{DEALER} has {dealer_value}, {DEALER} must hit")
                        time.sleep(1)
                        dealer_hand.append(shuffled_deck[0])
                        maintain_card_count(shuffled_deck[0])
                        shuffled_deck.remove(shuffled_deck[0])
                        dealer_value = get_hand_value(dealer_hand)
                        print(f"{YELLOW}Dealer's{RESET} hand: {dealer_hand} at {dealer_value}")
                    elif dealer_value > 21:
                        print(f"{DEALER} busts. {PLAYER} wins!")
                        dealer_turn = False
                    elif user_value < dealer_value <= 21:
                        print(f"{DEALER} wins.")
                        dealer_turn = False
                        break
            game_on = False
            a = "another"
            of = ""
