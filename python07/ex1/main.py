from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck

print("=== DataDeck Deck Builder ===\n")

print("Building deck with different card types...")

fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
lightning_bolt = SpellCard("Lightning Bolt", 3, "Legendary", "damage")
mana_crystal = ArtifactCard("Mana Crystal", 2, "Legendary", 1, "Permanent: +1 mana per turn")

deck = Deck()

deck.add_card(fire_dragon)
deck.add_card(lightning_bolt)
deck.add_card(mana_crystal)

deck.shuffle()

print(f"Deck stats: {deck.get_deck_stats()}\n")

print("Drawing and playing cards:\n")

game_state = {'mana': 6}

while deck.cards:
    card = deck.draw_card()
    print(f"Drew: {card.name} ({card.type})")
    print(f"Play result: {card.play(game_state)}\n")

print("Polymorphism in action: Same interface, different card behaviors!")