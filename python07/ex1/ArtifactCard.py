from ex0.Card import Card

class ArtifactCard(Card):

    def __init__(self, name: str, cost: int, rarity: str, durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = f"Permanent: +{self.cost / 2:.0f} mana per turn"
        self.type = "Artifact"

    
    def play(self, game_state: dict) -> dict:

        game_state['mana'] -= self.cost

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect
        }

    def activate_ability(self) -> dict:

        return {
            "artifact": self.name,
            "effect": self.effect
        }
