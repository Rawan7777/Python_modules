from ex0.Card import Card
from .Combatable import Combatable
from .Magical import Magical

class EliteCard(Card, Combatable, Magical):

    channeled = 0

    def __init__(self, name, cost, rarity, attack_power, defense_power, combat_type):

        super().__init__(name, cost, rarity)

        self.attack_power = attack_power
        self.defense_power = defense_power
        self.combat_type = combat_type
        self.alive = True
        self.damage_stats = 0
        self.damage_taken = 0
        self.mana_used_stats = 0

    def play(self, game_state: dict) -> dict:

        game_state['mana'] -= self.cost
        self.mana_used_stats += self.cost
        EliteCard.channeled += 1

        return {
            "player": self.name,
            "mana_used": self.cost,
        }

    def attack(self, target) -> dict:

        self.damage_stats += self.attack_power

        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
            "combat_type": self.combat_type
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:

        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": self.cost
        }

    def channel_mana(self, amount: int) -> dict:

        return {
            "channeled": EliteCard.channeled,
            "total_mana": amount
        }

    def get_magic_stats(self) -> dict:
        
        return {
            "name": self.name,
            "cpst": self.cpst,
            "rarity": self.rarity,
            "attack_power": self.attack_power,
            "defense_power": self.defense_power,
            "combat_type": self.combat_type,
            "alive": self.alive
        }

    def defend(self, incoming_damage: int) -> dict:

        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "damage_blocked": self.defense_power,
            "still_alive": self.alive
        }
    
    def get_combat_stats(self) -> dict:
        
        return {
            "damage_stats": self.damage_stats,
            "damage_taken": self.damage_taken,
            "mana_used_stats": self.mana_used_stats
        }
