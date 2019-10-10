import random
dealt_cards = []
deck_of_cards = [
    ['ace', 'heart'],
    ['ace', 'diamonds'],
    ['ace', 'spades'],
    ['ace', 'clubs'],
    ['2', 'heart'],
    ['2', 'diamonds'],
    ['2', 'spades'],
    ['2', 'clubs'],
    ['3', 'heart'],
    ['3', 'diamonds'],
    ['3', 'spades'],
    ['3', 'clubs'],
    ['4', 'heart'],
    ['4', 'diamonds'],
    ['4', 'spades'],
    ['4', 'clubs'],
    ['5', 'heart'],
    ['5', 'diamonds'],
    ['5', 'spades'],
    ['5', 'clubs'],
    ['6', 'heart'],
    ['6', 'diamonds'],
    ['6', 'spades'],
    ['6', 'clubs'],
    ['7', 'heart'],
    ['7', 'diamonds'],
    ['7', 'spades'],
    ['7', 'clubs'],
    ['8', 'heart'],
    ['8', 'diamonds'],
    ['8', 'spades'],
    ['8', 'clubs'],
    ['9', 'heart'],
    ['9', 'diamonds'],
    ['9', 'spades'],
    ['9', 'clubs'],
    ['10', 'heart'],
    ['10', 'diamonds'],
    ['10', 'spades'],
    ['10', 'clubs'],
    ['jack', 'heart'],
    ['jack', 'diamonds'],
    ['jack', 'spades'],
    ['jack', 'clubs'],
    ['queen', 'heart'],
    ['queen', 'diamonds'],
    ['queen', 'spades'],
    ['queen', 'clubs'],
    ['king', 'heart'],
    ['king', 'diamonds'],
    ['king', 'spades'],
    ['king', 'clubs'],
]

def get_card_num():
    global dealt_cards
    global deck_of_cards
    if len(dealt_cards) == 35:
        print('Reshuffling deck')
        dealt_cards.clear()

    card_num = random.randrange(0, 52)
    if card_num in dealt_cards:
        return 'repeat'
    else:
        dealt_cards.append(card_num)
        return deck_of_cards[card_num]
def card_value(value):
    if value in ('jack', 'queen', 'king'):
        return 10
    elif value == 'ace':
        return 11
    else:
        return int(value)

card = 'repeat'
for i in range(1,50):
    while card == 'repeat':
        card = get_card_num()
    print(card)
    print(card[0])
    print(card_value(card[0]))
    card = 'repeat'
