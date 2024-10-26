class CardDeck:
    def __init__(self):
        self.index = 0
        self.card_suit = ["Червей", "Бубен", "Пик", "Кресты"]
        numbers = [str(_) for _ in range(2, 11)]
        self.card_ranks = numbers + ["Валет", "Дама", "Король", "Туз"]
        self.cards = [f"{rank} {suit}"
                      for suit in self.card_suit
                      for rank in self.card_ranks]

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.cards):
            raise StopIteration
        card = self.cards[self.index]
        self.index += 1
        return card


if __name__ == "__main__":
    deck = CardDeck()
    for card in deck:
        print(card, end="; ")
        if "Туз" in card:
            print()
