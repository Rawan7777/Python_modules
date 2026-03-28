from Card import Card

class CreatureCard(Card):

    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int):

        super().__init__(name, cost, rarity)
        self.type = "Creature"
        self.attack = attack
        self.health = health
        self.effect = "Creature summoned to battlefield"

    def play(self, game_state: dict) -> dict:

        game_state['mana'] -= self.cost

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect
        }
    
    def attack_target(self, target) -> dict:

        return{
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": self.attack > target.health
        }