import eulerlib
import math

"""
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack=11, Queen=12, King=13, Ace=14.

If two players have the same ranked hands then the rank made up of the highest value wins; 
for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, 
for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); 
if the highest cards tie then the next highest cards are compared, and so on.

-------------------

We have the following cards 

        2, 3, 4, 5, 6, 7, 8, 9, 10, Jack=11, Queen=12, King=13, Ace=14.
        
And the following kinds: Hearts (H), Diamond (D), Spades (S), Clubs (C)

Let's first define an algebra for the ranks.

We need a mapping that maps from 
    
    {2, 3, 4, ..., T, J, Q, K, A} to {2, 3, 4, ..., 10, 11, 12, 13, 14}
    
and the inverse of this map so can we can print it as a string.



"""

hand = ['8C', 'TS', 'KC', '9H', '4S', '7D', '2S', '5D', '3S', 'AC']

mapping = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
           '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

invmap = {v: k for k, v in mapping.items()}

"""
Implements all the equality operators based on the rank. This means
we will be able to compare cards and sort them.
"""

class Card:

    def __init__(self, card_str):
        self.rank = mapping[card_str[0]]
        self.color = card_str[1]

    """
    Implementation of all the equality operators so we can
    compare cards and sort them.
    """

    def __gt__(self, other):
        if self.rank > other.rank:
            return True
        return False

    def __ge__(self, other):
        if self.rank >= other.rank:
            return True
        return False

    def __lt__(self, other):
        if self.rank < other.rank:
            return True
        return False

    def __le__(self, other):
        if self.rank <= other.rank:
            return True
        return False

    def __eq__(self, other):
        return self.rank == other.rank

    def __repr__(self):
        return invmap[self.rank] + self.color

    """
    We also want to add two cards C1 and C2 and get an integer sum.
    """
    def __add__(self, other):
        if isinstance(other, int):
            return self.rank + other
        if isinstance(other, Card):
            return self.rank + other.rank
        raise Exception("Add operator not defined.")

    """
    We also want to take the sum(H) of a hand H.
    """
    def __radd__(self, other):
        if isinstance(other, int):
            return self.rank + other
        if isinstance(other, Card):
            return self.rank + other.rank
        raise Exception("Add operator not defined.")


"""
Now we have to implement a ranking for the hands also. The ranks are 

    1  = High Card: Highest value card.
    2  = One Pair: Two cards of the same value.
    3  = Two Pairs: Two different pairs.
    4  = Three of a Kind: Three cards of the same value.
    5  = Straight: All cards are consecutive values.
    6  = Flush: All cards of the same suit.
    7  = Full House: Three of a kind and a pair.
    8  = Four of a Kind: Four cards of the same value.
    9  = Straight Flush: All cards are consecutive values of same suit.
    10 = Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
    
We can again label these from 1, 2, ..., Royal Flush = 10.

So again we want an algebra for the hand itself, where we check for the rank.
If for example both ranks are 1, then we have to compare the sum of both players
hands to see which hand is better.

"""

class Hand:

    def __init__(self, rank, C):
        self.rank = rank
        self.C = C

    def __gt__(self, other):
        if self.rank > other.rank:
            return True
        return False

    def __ge__(self, other):
        if self.rank >= other.rank:
            return True
        return False

    def __lt__(self, other):
        if self.rank < other.rank:
            return True
        return False

    def __le__(self, other):
        if self.rank <= other.rank:
            return True
        return False

    def __eq__(self, other):
        return self.rank == other.rank

    def __repr__(self):
        return ' '.join(self.C) + ' (Rank {})'.format(self.rank)

    def __iter__(self):
        for c in self.C:
            yield c


h1 = Hand(1, hand)
h2 = Hand(1, hand)

print(h1)
print('h1==h1', h1 == h2)

"""
Now we need to determine the rank of a hand.
"""
def highest_value_card(H):
    return max(H)


print(highest_value_card(hand))

print(h1)
print(h1.C)

print(max(h1.C))

print('TS>AC', hand[1] > hand[-1])
