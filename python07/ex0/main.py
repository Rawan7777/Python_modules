# from CreatureCard import *
from ex0.CreatureCard import CreatureCard

print("=== DataDeck Card Foundation ===\n")

print("Testing Abstract Base Class Design:\n")

fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
goblin_warrior = CreatureCard("Goblin Warrior", 4, "Epic", 6, 4)

print("CreatureCard Info:")
print(fire_dragon.get_card_info())

game_state = {'mana': 6}

print(f"\nPlaying {fire_dragon.name} with {game_state['mana']} mana available:")
print(f"Playable: {fire_dragon.is_playable(game_state['mana'])}\n")

print(f"Play result: {fire_dragon.play(game_state)}")

print(f"\n{fire_dragon.name} attacks {goblin_warrior.name}:")
print(f"Attack result: {fire_dragon.attack_target(goblin_warrior)}")

game_state['mana'] = 3

print(f"\nTesting insufficient mana ({game_state['mana']} available):")
print(f"Playable: {fire_dragon.is_playable(game_state['mana'])}\n")

print("Abstract pattern successfully demonstrated!")