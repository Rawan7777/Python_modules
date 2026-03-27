from .elements import create_fire, create_water, create_earth, create_air

fire: str = create_fire()
water: str = create_water()
def healing_potion() -> str:
    return f"Healing potion brewed with {fire} and {water}"

earth: str = create_earth()
def strength_potion() -> str:
    return f"Strength potion brewed with {earth} and {fire}"

air: str = create_air()
def invisibility_potion() -> str:
    return f"Invisibility potion brewed with {air} and {water}"

def wisdom_potion() -> str:
    return f"Wisdom potion brewed with all elements: {fire}, {water}, {earth}, {air}"
