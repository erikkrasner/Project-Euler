#!/usr/bin/env python
# 376
# 9.133 s

class Card(str):
    def translate(self, rank):
        if rank.isdigit():
            return int(rank)
        return {'T':10,'J':11,'Q':12,'K':13,'A':14}[rank]
    def rank(self):
        return self.translate(self[0])
    def suit(self):
        return self[1]

class Hand(tuple):
    HIGH_CARD,PAIR,TWO_PAIR,THREE_OF_A_KIND,STRAIGHT,FLUSH,FULL_HOUSE,FOUR_OF_A_KIND,STRAIGHT_FLUSH = range(9)
    def by_ranks(self):
        by_ranks = {}
        for rank in range(2,15):
            instances = filter(lambda card: card.rank() == rank,self)
            if instances:
                by_ranks[rank] = instances
        return by_ranks
    def min_rank(self):
        return min(self.by_ranks().keys())
    def max_rank(self):
        return max(self.by_ranks().keys())
    def by_suits(self):
        by_suits = {}
        for suit in ("S","D","C","H"):
            instances = filter(lambda card: card.suit() == suit,self)
            if instances:
                by_suits[suit] = instances
        return by_suits
    def straight(self):
        ranks = self.by_ranks()
        min_rank = self.min_rank()
        if len(ranks) == 5:
            if sorted(ranks.keys()) == range(min_rank, min_rank + 5):
                return (self.STRAIGHT, self.max_rank())
        return 0
    def flush(self):
        if len(self.by_suits()) == 1:
            return (self.FLUSH, self.max_rank())
        return 0
    def straight_flush(self):
        if self.straight() and self.flush():
            return (self.STRAIGHT_FLUSH, self.max_rank())
        return 0
    def n_of_a_kind(self,num_of_a_kind,num_matching_sets):
        ranks = self.by_ranks()
        matching_sets = filter(lambda x: len(ranks[x]) == num_of_a_kind, ranks.keys())
        if len(matching_sets) == num_matching_sets:
            return max(matching_sets)
        return 0
    def four_of_a_kind(self):
        score = self.n_of_a_kind(4,1)
        if score:
            return (self.FOUR_OF_A_KIND, score, self.max_rank())
        return 0
    def full_house(self):
        score1 = self.n_of_a_kind(3,1)
        score2 = self.n_of_a_kind(2,1)
        if score1 and score2:
            return (self.FULL_HOUSE, score1,score2)
        return 0
    def two_pair(self):
        score = self.n_of_a_kind(2,2)
        if score:
            return (self.TWO_PAIR, score, self.max_rank())
        return 0
    def three_of_a_kind(self):
        score = self.n_of_a_kind(3,1)
        if score:
            return (self.THREE_OF_A_KIND, score, self.max_rank())
        return 0
    def pair(self):
        score = self.n_of_a_kind(2,1)
        if score:
            return (self.PAIR, score, self.max_rank())
        return 0
    def high_card(self):
        return (self.HIGH_CARD, self.max_rank())
    def value(self):
        for func in [self.straight_flush,self.four_of_a_kind,self.full_house,self.flush,self.straight,self.three_of_a_kind,self.two_pair,self.pair,self.high_card]:
            score = func()
            if score:
                return score
    def beats(self,other_hand):
        alt_value = other_hand.value()
        for index,score in enumerate(self.value()):
            if score > alt_value[index]:
                return True
            if score < alt_value[index]:
                return False

def num_winning_hands():
    total = 0
    poker_file = open('poker.txt','r')
    for row in poker_file:
        cards = map(Card,row.split())
        hand1, hand2 = Hand(cards[:5]),Hand(cards[5:])
        if hand1.beats(hand2):
            total += 1
    return total

print num_winning_hands()
