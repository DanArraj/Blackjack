import random
import draw_card
import tkinter as tk
height = 400
width = 400
p1_value = 0
dealer_value = 0
p1c1 = get_card()  # player 1 card 1
p1c2 = get_card()
dealerc1 = get_card()
dealerc2 = get_card()



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
topmessagetext = ''

def get_card_num():
    global dealt_cards
    global deck_of_cards
    global repeat
    if len(dealt_cards) == 35:
        topmessage['text'] = 'Reshuffling deck\n'
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
    global topmessagetext
    global p1_value
    global dealer_value
    p1c1 = get_card()       #player 1 card 1
    p1c2 = get_card()
    dealerc1 = get_card()
    dealerc2 = get_card()
    p1_value = p1c1.value + p1c2.value
    dealer_value = dealerc1.value +dealerc2.value
    if p1_value == 21 and dealer_value == 21:   #player and dealer have natural blackjack
        topmessage['text'] = f'You are dealt a {p1c1.rank} of {p1c1.suit} and a {p1c2.rank} of {p1c2.suit}. Blackjack!!'
        topmessage['text'] = f'The dealer is dealt a {dealerc1.rank} of {dealerc1.suit} and a {dealerc2.rank} of {dealerc2.suit}. The dealer has a blackjack too!\n You tie!'
        if input('play again?\n').lower() == 'yes':
            hand_of_cards()
        return
    elif p1_value == 21 and dealer_value != 21: #just the player has a natural blackjack
        topmessage['text'] = f'You are dealt a {p1c1.rank} of {p1c1.suit} and a {p1c2.rank} of {p1c2.suit}. Blackjack!!'
        topmessage['text'] = f'The dealer is dealt a {dealerc1.rank} of {dealerc1.suit} and a {dealerc2.rank} of {dealerc2.suit}.\n You win!!!'
        if input('play again?\n').lower() == 'yes':
            hand_of_cards()
        return
    topmessagetext += f'You are dealt a {p1c1.rank} of {p1c1.suit} and a {p1c2.rank} of {p1c2.suit}. \nYour hand has a value of {p1_value}.\n'
    topmessagetext += f'The dealer is dealt a {dealerc1.rank} of {dealerc1.suit} and another card face down. \nThe dealer is showing a value of {dealerc1.value}.\n'
    topmessagetext += f'The dealer is showing {dealerc1.value} and you have a value of {p1_value}. Would you like to hit or stay?\n'
    return

def hit_stay(move):
    global topmessagetext
    global p1_value
    global dealer_value
    if move == 'hit':
        p1c3 = get_card()
        p1_value += p1c3.value
        if ('ace' in [p1c1.rank, p1c2.rank, p1c3.rank]) and p1_value > 21:
            p1_value -= 10
        topmessagetext += f'You are dealt a {p1c3.rank} of {p1c3.suit}. Your hand has a value of {p1_value}'
        if p1_value > 21:
            topmessagetext += f'You bust!'
            # if input('play again?\n').lower() == 'yes':
            #     hand_of_cards()
            return
        else:
            topmessagetext += f'The dealer is showing {dealerc1.value} and you have a value of {p1_value}. Would you like to hit or stay?\n'
    return


    topmessagetext += f'Dealer flips over their second card and it is a {dealerc2.rank} of {dealerc2.suit}. The dealers hand has a value of {dealer_value}'
    if dealer_value == 21:   #just dealer has natural blackjack
        topmessagetext += f'Dealer has a blackjack!! You lose!'
        # if input('play again?\n').lower() == 'yes':
        #     hand_of_cards()
        return
    while dealer_value <= 16:   #if dealers hand is less than 17 they must hit
        dealerc3 = get_card()
        dealer_value += dealerc3.value
        if ('ace' in [dealerc1.rank, dealerc2.rank, dealerc3.rank]) and dealer_value > 21:
            dealer_value -= 10
        topmessage['text'] = f'Dealer hits and deals themself a {dealerc3.rank} of {dealerc3.suit}. Their hand has a value of {dealer_value}'
        if dealer_value > 21:
            topmessage['text'] = 'Dealer busts! You win!'
            if input('play again?\n').lower() == 'yes':
                hand_of_cards()
            return
    topmessage['text'] = 'Dealer stays.'
    if p1_value > dealer_value:
        topmessage['text'] = f'Your hand has a value of {p1_value} and the dealer has a hand of {dealer_value}. You win!'
    elif dealer_value > p1_value:
        topmessage['text'] = f'Your hand has a value of {p1_value} and the dealer has a hand of {dealer_value}. Dealer wins!'
    else:
        topmessage['text'] = f'Your hand has a value of {p1_value} and the dealer has a hand of {dealer_value}. Its a tie!'
    if input('play again?\n').lower() == 'yes':
        hand_of_cards()
    return

leftbuttontext = 'Hit'
rightbuttontext = 'stay'

root = tk.Tk()
canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()
background_image = tk.PhotoImage(file='playingcards.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1,relheight=1)

topframe = tk.Frame(root, bg='black',bd=5)
topframe.place(relx=.1,rely=.1,relheight=.5,relwidth=.8)
topmessage = tk.Message(topframe, anchor='nw', justify='left', width=310)
topmessage.place(relheight=1,relwidth=1)

bottomframe = tk.Frame(root, bg='black',bd=5)
bottomframe.place(relx=.1,rely=.7,relheight=.25,relwidth=.8)
leftbutton = tk.Button(bottomframe, text=leftbuttontext, command=lambda: hit_stay('hit'))
leftbutton.place(relx=0, relwidth=0.4, relheight=1)
rightbutton = tk.Button(bottomframe, text=rightbuttontext, command=lambda: hit_stay('stay'))
rightbutton.place(relx=0.6, relwidth=0.4, relheight=1)

topmessagetext += 'Welcome to the blackjack table!\n'
hand_of_cards()
topmessagetext += 'Goodbye\n'
topmessage['text'] = topmessagetext

root.mainloop()





