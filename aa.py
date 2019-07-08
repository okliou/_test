import random


class Card:
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __lt__(self, other):
        # 检查大小
        if self.rank < other.rank: return True
        if self.rank > other.rank: return False

        # 大小相同，对比花色
        return self.suit < other.suit

    def __gt__(self, other):
        # # 检查大小
        # if self.rank > other.rank: return True
        # if self.rank < other.rank: return False
        #
        # # 大小相同，对比花色
        # return self.suit > other.suit

        # 元组比较(优先比较的在前面)
        t1 = self.rank, self.suit
        t2 = other.rank, other.suit

        return t1 > t2


class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card: Card):
        self.cards.append(card)

    def move_card(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def shuffle(self):
        random.shuffle(self.cards)


class Hand(Deck):
    def __init__(self, lable=''):
        self.cards = []
        self.lable = lable


if __name__ == '__main__':
    a = Card(2, 11)
    b = Card(3, 11)

    print(a > b)

    aa = Deck()
    print(aa)
    print('='*50)
    aa.shuffle()
    print(aa)
