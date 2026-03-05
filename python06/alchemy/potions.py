from .elements import create_fire, create_water, create_earth, create_air

fire = create_fire()
water = create_water()
def healing_potion():
    return f"Healing potion brewed with {fire} and {water}"

earth = create_earth()
def strength_potion():
    return f"Strength potion brewed with {earth} and {fire}"

air = create_air()
def invisibility_potion():
    return f"Invisibility potion brewed with {air} and {water}"

def wisdom_potion():
    return f"Wisdom potion brewed with all elements: {fire}, {water}, {earth}, {air}"
