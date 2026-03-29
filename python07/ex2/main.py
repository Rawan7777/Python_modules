from ex0.Card import Card
from ex2.Magical import Magical
from ex2.Combatable import Combatable
from ex2.EliteCard import EliteCard


print("=== DataDeck Ability System ===\n")

print("EliteCard capabilities:")

classes = [Card, Combatable, Magical]

for clas in classes:
    methods = [f for f in dir(clas) if callable(getattr(clas, f)) and not f.startswith("__")]

    print(f"- {clas.__name__}: {methods}")

print("\nPlaying Arcane Warrior (Elite Card):\n")

elite_card = EliteCard("Arcane Warrior", 5, "Epic", 5, 3, "melee")

game_state = {'mana': 20}

print("Combat phase:")
elite_card.play(game_state)
print(f"Attack result: {elite_card.attack("Enemy")}")
elite_card.play(game_state)
print(f"Defense result: {elite_card.defend(2)}")

print("\nMagic phase:")
print(f"Spell cast: {elite_card.cast_spell("Fireball", ["Enemy1", "Enemy2"])}")
elite_card.play(game_state)
print(f"Mana channel: {elite_card.channel_mana(7)}")

print("\nMultiple interface implementation successful!")
