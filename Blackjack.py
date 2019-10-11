import random
import draw_card

dealt_cards = []
deck_of_cards = [
    ['ace', 'hearts'],
    ['ace', 'diamonds'],
    ['ace', 'spades'],
    ['ace', 'clubs'],
    ['2', 'hearts'],
    ['2', 'diamonds'],
    ['2', 'spades'],
    ['2', 'clubs'],
    ['3', 'hearts'],
    ['3', 'diamonds'],
    ['3', 'spades'],
    ['3', 'clubs'],
    ['4', 'hearts'],
    ['4', 'diamonds'],
    ['4', 'spades'],
    ['4', 'clubs'],
    ['5', 'hearts'],
    ['5', 'diamonds'],
    ['5', 'spades'],
    ['5', 'clubs'],
    ['6', 'hearts'],
    ['6', 'diamonds'],
    ['6', 'spades'],
    ['6', 'clubs'],
    ['7', 'hearts'],
    ['7', 'diamonds'],
    ['7', 'spades'],
    ['7', 'clubs'],
    ['8', 'hearts'],
    ['8', 'diamonds'],
    ['8', 'spades'],
    ['8', 'clubs'],
    ['9', 'hearts'],
    ['9', 'diamonds'],
    ['9', 'spades'],
    ['9', 'clubs'],
    ['10', 'hearts'],
    ['10', 'diamonds'],
    ['10', 'spades'],
    ['10', 'clubs'],
    ['jack', 'hearts'],
    ['jack', 'diamonds'],
    ['jack', 'spades'],
    ['jack', 'clubs'],
    ['queen', 'hearts'],
    ['queen', 'diamonds'],
    ['queen', 'spades'],
    ['queen', 'clubs'],
    ['king', 'hearts'],
    ['king', 'diamonds'],
    ['king', 'spades'],
    ['king', 'clubs'],
]
repeat = True

def get_card_num():
    global dealt_cards
    global deck_of_cards
    global repeat
    if len(dealt_cards) == 35:
        print('Reshuffling deck')
        dealt_cards.clear()

    card_num = random.randrange(0, 52)
    if card_num in dealt_cards:
        return
    else:
        repeat = False
        dealt_cards.append(card_num)
        return deck_of_cards[card_num]
def get_card():
    global repeat
    while repeat == True:
        card = get_card_num()
    repeat = True
    return draw_card.card(card[0],card[1],card[0])
def hand_of_cards():
    p1c1 = get_card()       #player 1 card 1
    p1c2 = get_card()
    dealerc1 = get_card()
    dealerc2 = get_card()
    p1_value = p1c1.value + p1c2.value
    dealer_value = dealerc1.value +dealerc2.value
    print(f'You are dealt a {p1c1.rank} of {p1c1.suit} and a {p1c2.rank} of {p1c2.suit}. Your hand has a value of {p1_value}.')
    print(f'The dealer is dealt a {dealerc1.rank} of {dealerc1.suit} and another card face down. The dealer is showing a value of {dealerc1.value}.')
    move = input(f'The dealer is showing {dealerc1.value} and you have a value of {p1_value}. Would you like to hit or stay?\n').lower()
    while move == 'hit':
        p1c3 = get_card()
        p1_value += p1c3.value
        if p1c3.rank == 'ace' and p1_value > 21:
            p1_value -= 10
        print(f'You are dealt a {p1c3.rank} of {p1c3.suit}. Your hand has a value of {p1_value}')
        if p1_value > 21:
            print(f'You bust!')
            if input('play again?\n').lower() == 'yes':
                hand_of_cards()
            return
        else:
            move = input(f'The dealer is showing {dealerc1.value} and you have a value of {p1_value}. Would you like to hit or stay?\n').lower()
    print(f'Dealer flips over their second card and it is a {dealerc2.rank} of {dealerc2.suit}. The dealers hand has a value of {dealer_value}')
    while dealer_value <= 16:   #if dealers hand is less than 17 they must hit
        dealerc3 = get_card()
        dealer_value += dealerc3.value
        if dealerc3.rank == 'ace' and dealer_value > 21:
            dealer_value -= 10
        print(f'Dealer hits and deals themself a {dealerc3.rank} of {dealerc3.suit}. Their hand has a value of {dealer_value}')
        if dealer_value > 21:
            print('Dealer busts! You win!')
            if input('play again?\n').lower() == 'yes':
                hand_of_cards()
            return
    print('Dealer stays.')
    if p1_value > dealer_value:
        print(f'Your hand has a value of {p1_value} and the dealer has a hand of {dealer_value}. You win!')
    elif dealer_value > p1_value:
        print(f'Your hand has a value of {p1_value} and the dealer has a hand of {dealer_value}. Dealer wins!')
    else:
        print(f'Your hand has a value of {p1_value} and the dealer has a hand of {dealer_value}. Its a tie!')
    if input('play again?\n').lower() == 'yes':
        hand_of_cards()
    return

print('Welcome to the blackjack table!')
hand_of_cards()
print('Goodbye')