import time
import deck
import random


def get_card_value(card):
    value = 0
    card_values = {"A": 11,
                   "2": 2, "3": 3, "4": 4,
                   "5": 5, "6": 6, "7": 7,
                   "8": 8, "9": 9, "1": 10,
                   "J": 10, "Q": 10, "K": 10}
    value = int(card_values[card[0]])
    return value


def get_hand_value(hand):
    value = 0
    for card in hand:
        value += int(get_card_value(card))
    return value


def deal():
    hand = []
    for i in range(2):
        hand.append(shuffled_deck[0])
        shuffled_deck.remove(shuffled_deck[0])
        #  print(f"Next Card in deck: {shuffled_deck[0]}")
    return hand


def ace_value(hand, hand_value):
    hand_ace_value = hand_value
    for card in hand:
        if card[0] == 'A':
            #  For each Ace, subtract 10
            hand_ace_value -= 10
    if hand_value > 21 >= hand_ace_value:
        return hand_ace_value
    else:
        return hand_value


heart = "\u2746"
diamond = "\u2666"
spade = "\u2660"
club = "\u2663"
global user_hand
global dealer_hand
global user_value
global dealer_value
shuffled_deck = deck.deck
main_game_loop = True
a = "a"
of = " of BlackJack"
while main_game_loop:
    if len(shuffled_deck) < 10:
        print("Under 10 cards left in the deck. Not enough for a game.")
        quit()

    prompt = input(f"How about {a} game{of}? y for yes, n for no: ")
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
        #  user_hand = ["As", "5d"]      # uncomment/comment for testing specific hand values
        #  ---END HAND TESTING---  ####
        print(f"Your hand: {user_hand}")
        user_value = get_hand_value(user_hand)
        print(f"Your hand is worth: {user_value}")
        print(f"Dealer hand: {dealer_hand}")
        dealer_value = get_hand_value(dealer_hand)
        print(f"Dealer hand is worth: {dealer_value}")
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
                choice = input("Hit (h), Stand (s), Double Down (d), Split (Requires doubles) (t), \"deck left\" displays number of cards left: ")
                if choice == "deck left":
                    print(len(shuffled_deck))
                if choice == "h":
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
                        print(f"Your hand: {user_hand}")
                        print(f"You have {user_value}")
                    else:
                        print("Deck is empty. No more game. Bye!")
                        quit()
                elif choice == "s":
                    print("stand")
                    print("Player stands.")
                    print("Dealer's turn.")
                    break
                elif choice == 'd':
                    print("Double Down - not functional yet")
                elif choice == 't':
                    print("Split - not functional yet")
                else:
                    print("Invalid choice. Please try again.")
                # push happens if user gets black jack and dealer gets black jack. User still wins if they tie dealer.
                # if dealer is 17 or over, they lose instantly
            dealer_turn = True
            if user_turn:
                while dealer_turn:
                    if dealer_value < 21 and dealer_value <= user_value:
                        print(f"Dealer has {dealer_value}, Dealer must hit")
                        time.sleep(1)
                        dealer_hand.append(shuffled_deck[0])
                        shuffled_deck.remove(shuffled_deck[0])
                        dealer_value = get_hand_value(dealer_hand)
                        print(f"Dealer's hand: {dealer_hand} at {dealer_value}")
                    elif dealer_value > 21:
                        print("Dealer busts. Player wins!")
                        dealer_turn = False
                    elif user_value < dealer_value <= 21:
                        print("Dealer wins.")
                        dealer_turn = False
                        break
            game_on = False
            a = "another"
            of = ""
