import time
import random
import gameascii
import constants
from constants import PROMPT_CHOICE  # HIT_KEY, STAND_KEY, DOUBLE_KEY, SPLIT_KEY, QUIT_KEY,
from colors import PURPLE, GREEN, RED, YELLOW, CYAN, RESET, PLAYER, DEALER

DECK = constants.DECK
shuffled_deck = DECK
CARD_COUNT_VALUES = constants.CARD_COUNT_VALUES
CARD_VALUES = constants.CARD_VALUES
WINNING_SCORE = constants.WINNING_SCORE

player_hand = []
dealer_hand = []
player_score = 0
dealer_score = 0
running_count = 0
true_count = 0  # Multiple deck counting on TODO list
main_game_loop = True
a = constants.PROMPT_INITIAL  # sets verbiage for 'another game' question
of = constants.PROMPT_SUFFIX  # sets verbiage for 'another game' question


def maintain_card_count(card):
    """Updates running_count, TODO: true_count = running_count / decks left"""
    global running_count
    #  print(f"{card} means {card_count_values[card[0]]} to the total")
    running_count += CARD_COUNT_VALUES[card[0]]


def bool_convert(message_response):
    """Converts 'y' or 'n' to 'True' or 'False', respectively"""
    message_response = message_response.lower()
    if message_response == 'y':
        return True
    else:
        return False


def get_card_value(card):
    """Calculates card value, 1h = 10 of hearts."""
    value = int(CARD_VALUES[card[0]])
    return value


def get_hand_value(hand):
    """Calculates hand value."""
    ace = False
    value = 0
    #  Get raw hand value first
    for card in hand:
        value += int(get_card_value(card))
        if card[0] == 'A':
            ace = True
    #  Aces are a curveball in BlackJack, if there's an Ace in hand, need to check if their values should be adjusted
    if ace:
        return hand_with_ace_value(hand, value)
    return value


def hand_with_ace_value(hand, hand_value):
    """Determines Ace = 1 or 11. If 11 pushes hand over 21, Ace value = 1"""
    hand_ace_value = hand_value
    for card in hand:
        if card[0] == 'A':
            #  For each Ace, subtract 10, this is a gray area with blackjack,
            #    still researching this rule...might be preference
            hand_ace_value -= 10
    # hand_value > WINNING_SCORE and hand_ace_value <= WINNING_SCORE:
    if hand_value > WINNING_SCORE >= hand_ace_value:  # if value of the hand with A=11 is > 21 and the recalculated hand
        return hand_ace_value                         # with A = 1 is less than 21, this is the hand value to return
    else:
        return hand_value                             # Ace is still worth 11 because hand is still <= 21


def deal():
    """Deals 2 cards from top of shuffled deck and returns them in list"""
    hand = []
    for i in range(2):
        hand.append(shuffled_deck[0])
        shuffled_deck.remove(shuffled_deck[0])
        maintain_card_count(hand[i])
        #  print(f"Next Card in deck: {shuffled_deck[0]}")
    return hand


def dealer(dealer_hand_value, player_hand_value):
    global dealer_score
    global WINNING_SCORE
    time.sleep(1)
    dealer_must_hit = dealer_hand_value < WINNING_SCORE and dealer_hand_value <= player_hand_value
    if dealer_must_hit:
        print(f"{DEALER} has {dealer_hand_value}, {DEALER} must hit")
        dealer_hand.append(shuffled_deck[0])
        maintain_card_count(shuffled_deck[0])
        shuffled_deck.remove(shuffled_deck[0])
        dealer_score = get_hand_value(dealer_hand)
        print(f"{YELLOW}Dealer's{RESET}{YELLOW} hand: {dealer_hand} "
              f"at {dealer_score}{RESET}")
        return True
    dealer_loss = dealer_hand_value > WINNING_SCORE
    if dealer_loss:
        print(f"{DEALER} busts. {PLAYER} wins!")
        return False
    dealer_win = player_score < dealer_hand_value <= WINNING_SCORE
    if dealer_win:
        print(f"{DEALER} wins.")
        return False


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
        print("Under 10 cards left in the shoe (the cards left to deal). Not enough for a game.")
        quit()

    prompt = input(f"How about {a} game{of}? {GREEN}y{RESET} for {GREEN}yes"
                   f"{RESET}, {RED}n{RESET} for {RED}no{RESET}: ")
    count_cards = bool_convert(input("Do you want to see card counting (Hi-Lo System)?").lower())
    if count_cards:
        print("The running count will be updated each time a card is dealt. "
              "\nThe higher the running count, the higher the advantage for you! High running count = HIT, low = STAND")
    if a == 'a':
        deck_num = int(input("How many decks would you like to play with? "))
        for _ in range(0, deck_num - 1):
            shuffled_deck.extend(DECK)
        random.shuffle(shuffled_deck)
    if prompt == 'n':
        quit()
    elif prompt == 'y':
        player_hand = deal()          # uncomment/comment for real deal from deck
        dealer_hand = deal()          # uncomment/comment for real deal from deck
        #    ---HAND TESTING---    ####
        #  player_hand = ["As", "Ad"] # uncomment/comment for testing specific hand values
        #  ---END HAND TESTING---  ####
        print(f"{PURPLE}Your hand: {player_hand}{RESET}")
        player_score = get_hand_value(player_hand)
        print(f"{PURPLE}Your hand is worth: {player_score}{RESET}")
        print(f"{YELLOW}Dealer hand: {dealer_hand}{RESET}")
        dealer_score = get_hand_value(dealer_hand)
        print(f"{YELLOW}Dealer hand is worth: {dealer_score}{RESET}")
        print("What would you like to do?")
        game_on = True
        while game_on:
            player_turn = True
            while player_turn:
                if player_score == WINNING_SCORE:
                    if len(player_hand) == 2:
                        print("BLACKJACK! ", end="")
                    print("You win!")
                    player_turn = False
                    break
                elif player_score > WINNING_SCORE:
                    print("You busted!")
                    player_turn = False
                    break
                display_running_count()
                choice = input(PROMPT_CHOICE).lower()

                if choice == "q":
                    quit()
                elif choice == "deck":
                    print(len(shuffled_deck))
                elif choice == "h":
                    print("hit")
                    if len(shuffled_deck) > 0:
                        player_hand.append(shuffled_deck[0])
                        shuffled_deck.remove(shuffled_deck[0])
                        player_score = get_hand_value(player_hand)
                        print(f"{PURPLE}Your hand: {player_hand}")
                        print(f"You have {player_score}{RESET}")
                    else:
                        print("Deck is empty. No more game. Bye!")
                        quit()
                elif choice == "s":
                    print(f"{PLAYER} stands.")
                    print(f"{YELLOW}Dealer's{RESET} turn.")
                    break
                elif choice == 'd':
                    print("Double Down - not functional yet")
                elif choice == 't':
                    print("Split - not functional yet")
                else:
                    print(f"{RED}Invalid choice. Please try again.{RESET}")
            dealer_turn = True
            if player_turn:
                while dealer_turn:
                    dealer_turn = dealer(dealer_score, player_score)

            game_on = False
            a = constants.PROMPT_ANOTHER         # sets verbiage for 'another game' question
            of = constants.PROMPT_SUFFIX_EMPTY   # sets verbiage for 'another game' question
