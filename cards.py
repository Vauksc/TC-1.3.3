class Card:

    SUITS = ("clubs", "spades", "hearts", "diamonds")

    SUIT_SYMB = {"clubs" : "♣",
                 "spades" : "♠",
                 "hearts" : "♥",
                 "diamonds": "♦",
                 }

    RANKS = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "j": 11,
        "q": 12,
        "k": 13,
        "a": 14,
    }

    face_up = False

    def __init__(self, suit="", rank="", face_up=False):
        self.suit = suit
        self.rank = rank
        self.face_up = face_up


    def __str__(self):
        return (f"{self.rank} {Card.SUIT_SYMB[self.suit]}")

    @property
    def rank(self):
        return self._rank


    @rank.setter
    def rank(self, rank):
        self._rank = rank

    @property
    def suit(self):
        return self._suit


    @suit.setter
    def suit(self, suit):
        self._suit = suit


    @property
    def face_up(self):
        return self._face_up


    @face_up.setter
    def face_up(self, face_up):
        self._face_up = face_up

    @classmethod
    def deck_creation(cls):
"""Creates a deck of 52 cards """

        deck = []
        for suit in cls.SUITS:
            for rank in cls.RANKS:
                card = Card()
                card.suit=suit
                card.rank=rank
                deck.append(card)
        return deck

