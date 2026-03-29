from ex0.Card import Card

class SpellCard(Card):

    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.effect = f"Deal {self.cost} {self.effect_type} to target"
        self.type = "Spell"

    
    def play(self, game_state: dict) -> dict:

        game_state['mana'] -= self.cost

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect
        }

    def resolve_effect(self, targets: list) -> dict:

        return {
            "spell": self.name,
            "targets": targets,
            "resolved": True
        }
