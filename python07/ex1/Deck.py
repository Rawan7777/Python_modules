from ex0.Card import Card
import math
import random

class Deck:

    cards = []

    def add_card(self, card: Card) -> None:
        Deck.cards.append(card)

    def remove_card(self, card_name: str) -> bool:

        for card in Deck.cards:
            if card.name == card_name:
                Deck.cards.remove(card);
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(Deck.cards)

    def draw_card(self) -> Card:

        card = Deck.cards[0]
        self.remove_card(card.name)
        return card

    def get_deck_stats(self) -> dict:

        spell = 0
        artifact = 0
        creature = 0
        total_cost = 0

        for card in Deck.cards:
            if card.type == "Spell":
                spell += 1
            elif card.type == "Artifact":
                artifact += 1
            elif card.type == "Creature":
                creature += 1

            total_cost += card.cost
            

            avg_cost = total_cost / len(Deck.cards)

        return {
            "total_cards": len(Deck.cards),
            "creatures": creature,
            "spells": spell,
            "artifacts": artifact,
            "avg_cost": float(math.ceil(avg_cost))
        }
