class card:
    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.value = card_value(rank)


def card_value(rank):
    if rank in ('jack', 'queen', 'king'):
        return 10
    elif rank == 'ace':
        return 11
    else:
        return int(rank)



