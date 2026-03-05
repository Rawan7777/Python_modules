print("=== Pathway Debate Mastery ===")

print("\nTesting Absolute Imports (from basic.py):")
from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
print(f"lead_to_gold(): {lead_to_gold()}")
print(f"stone_to_gem(): {stone_to_gem()}")

print("\nTesting Relative Imports (from advanced.py):")
from alchemy.transmutation.advanced import philosophers_stone, elixir_of_life
print(f"philosophers_stone(): {philosophers_stone()}")
print(f"elixir_of_life(): {elixir_of_life()}")

print("\nTesting Package Access:")
import alchemy.transmutation
print(f"alchemy.transmutation.lead_to_gold(): {alchemy.transmutation.lead_to_gold()}")
print(f"alchemy.transmutation.philosophers_stone(): {alchemy.transmutation.philosophers_stone()}")

print("\nBoth pathways work! Absolute: clear, Relative: concise")
