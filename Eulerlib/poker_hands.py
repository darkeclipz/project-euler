from eulerlib import time_it

# example hand: '5H 5C 6S 7S KD'
def score(hand):
    # cards = [(11, 'D'), (5, 'S'), (4, 'S'), (3, 'H'), (3, 'C')]
    cards = sorted([("23456789TJQKA".index(r), s) 
        for r, s in hand.split()])[::-1]
    # ranks = [11, 5, 4, 3, 3]
    ranks = [r for (r, _) in cards]
    # rcounts = [(11, 1), (5, 1), (4, 1), (3, 2)]
    rcounts = {r:ranks.count(r) for r in ranks}.items()
    # score = (2, 1, 1, 1)
    # ranks = (3, 11, 5, 4)
    score, ranks = zip(*sorted((v, k) for k, v in rcounts)[::-1])
    if len(score) == 5:
        straight = (ranks[0] - ranks[-1]) == 4
        flush = len({s for (_, s) in cards}) == 1
        if straight and flush:       score = (5, )
        elif not straight and flush: score = (3, 1, 3)
        elif straight:               score = (3, 1, 2)
    # result = ((2, 1, 1, 1), (3, 11, 5, 4))
    return score, ranks

# golfed version - 280 chars, a tweet
def f(H):
    z,s,L=zip,sorted,len
    R,U=z(*s([("23456789TJQKA".index(r),s)for r,s in H.split()])[::-1])
    S,R=z(*s((v,k)for k,v in{r:R.count(r)for r in R}.items())[::-1])
    c,s,f=L(S)==5,R[0]-R[-1]==4,L(set(U))==1
    return(((1,),(3,1,3)),((3,*S),(5,)))[s][f]if c else S,R

def poker_hands():
    total_wins = 0
    with open('poker.txt', 'r') as file:
        for line in file:
            if f(line[:14]) > f(line[15:]):
                total_wins += 1
    return total_wins

time_it(poker_hands)
