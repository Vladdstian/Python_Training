# Blackjack project
from art import logo
import random 
from replit import clear

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def print_status(a_player, a_dealer, final=False):
    if final:
        print(
            f"Your final hand: {a_player['cards']}, final score: {a_player['score']} ")
        print(
            f"Dealer's final hand: {a_dealer['cards']}, final score: {a_dealer['score']}")
    else:
        print(
            f"Your hand: {a_player['cards']}, score: {a_player['score']} ")
        print(f"Dealer's first card: {a_dealer['cards'][0]}")


def draw_cards(no_cards=1):
    cards = []
    for card_draws in range(no_cards):
        cards.append(random.choice(deck))
    return cards


def calculate_score(a_player):
    a_player['score'] = 0
    for card in a_player['cards']:
        a_player['score'] += card
    if 11 in a_player['cards'] and a_player['score'] > 21:
        a_player['score'] -= 10
        a_player['cards'][a_player['cards'].index(11)] = 1


def end_game(a_player, a_dealer):
    if a_player['score'] == a_dealer['score'] == 21:
        print_status(a_player, a_dealer, True)
        print("It's a draw! Both players have Blackjack")
        return True
    elif a_player['score'] == 21:
        print_status(a_player, a_dealer, True)
        print("You have a Blackjack. You win!")
        return True
    elif a_dealer['score'] == 21:
        print_status(a_player, a_dealer, True)
        print("You loose. Your opponent has a Blackjack!")
        return True
    elif a_player['score'] > 21:
        print_status(a_player, a_dealer, True)
        print("You went over 21. You loose!")
        return True
    elif a_dealer['score'] > 21:
        print_status(a_player, a_dealer, True)
        print("Opponent went over. You win!")
        return True
    else:
        return False


def winner_check(a_player, a_dealer):
    if a_player['score'] < a_dealer['score']:
        print_status(a_player, a_dealer, True)
        print("You loose!")
    elif a_dealer['score'] < a_player['score']:
        print_status(a_player, a_dealer, True)
        print("You win!")
    else:
        print_status(a_player, a_dealer, True)
        print("It's a draw!")


while True:
    new_game_choice = input(
        "\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if new_game_choice == 'y':
        clear()
        print(logo)
        player = {
            'cards': [],
            'score': 0,
            'draw': True,
        }
        dealer = {
            'cards': [],
            'score': 0,
            'draw': True,
        }

        while True:
            if len(player['cards']) == 0:
                player['cards'] += draw_cards(2)
                dealer['cards'] += draw_cards(2)

            calculate_score(player)
            calculate_score(dealer)

            print_status(player, dealer)

            while not end_game(player, dealer):
                if player['draw']:
                    draw_another = input(
                        "Type 'y' to get another card, type 'n' to pass: ").lower()
                    if draw_another == 'y':
                        clear()
                        print(logo)
                        player['cards'] += draw_cards()
                        calculate_score(player)
                        print_status(player, dealer)
                        continue
                    player['draw'] = False

                if dealer['draw']:
                    if dealer['score'] < player['score'] and dealer['score'] < 15:
                        clear()
                        print(logo)
                        dealer['cards'] += draw_cards()
                        calculate_score(dealer)
                        continue
                    dealer['draw'] = False

                if dealer['draw'] == player['draw'] == False:
                    clear()
                    print(logo)
                    winner_check(player, dealer)
                    break
            break

    else:
        break
