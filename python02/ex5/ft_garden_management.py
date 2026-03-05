#!/usr/bin/env python3

class GardenError(Exception):

    """Base garden exception."""


class PlantError(GardenError):

    """Plant-related exception."""


class WaterError(GardenError):

    """Water-related exception."""


class Plant:

    """Represents a plant in the garden."""

    def __init__(self, name, water, sun):
        self.name = name
        self.water = water
        self.sun = sun

    def water_plant(self):
        """Increase plant water level."""
        self.water += 1


class GardenManager:

    """Manages plants, watering system and health checks."""

    def __init__(self):
        self.plants = []
        self.water_tank = 2

    def add_plant(self, plant):

        """Add plant to garden."""

        if not plant.name:
            raise PlantError("Plant name cannot be empty!")
        self.plants.append(plant)
        print(f"Added {plant.name} successfully")

    def water_plants(self):

        """Water all plants safely."""

        opened = False
        try:
            if self.water_tank <= 0:
                raise WaterError("Not enough water in tank")

            print("Opening watering system")
            opened = True

            for plant in self.plants:
                plant.water_plant()
                self.water_tank -= 1
                print(f"Watering {plant.name} - success")

        finally:
            if opened:
                print("Closing watering system (cleanup)")

    def check_health(self, plant):

        """Check plant health."""

        name = plant.name

        if plant.water > 10:
            raise PlantError(
                f"Error checking {name}: Water level {plant.water} "
                "is too high (max 10)"
            )
        if plant.water < 1:
            raise PlantError(
                f"Error checking {name}: Water level {plant.water} "
                "is too low (min 1)"
            )
        if plant.sun > 12:
            raise PlantError(
                f"Error checking {name}: Sunlight hours {plant.sun} "
                "is too high (max 12)"
            )
        if plant.sun < 2:
            raise PlantError(
                f"Error checking {name}: Sunlight hours {plant.sun} "
                "is too low (min 2)"
            )

        print(f"{name}: healthy (water: {plant.water}, sun: {plant.sun})")


def main():

    """Run garden management demo."""

    print("=== Garden Management System ===\n")

    manager = GardenManager()

    print("Adding plants to garden...")

    tomato = Plant("tomato", 4, 8)
    lettuce = Plant("lettuce", 14, 11)
    error = Plant("", 0, 0)

    try:
        manager.add_plant(tomato)
        manager.add_plant(lettuce)
        manager.add_plant(error)
    except PlantError as e:
        print(f"Error adding plant: {e}")

    print("\nWatering plants...")
    try:
        manager.water_plants()
    except WaterError as e:
        print(f"Watering error: {e}")

    print("\nChecking plant health...")
    try:
        manager.check_health(tomato)
        manager.check_health(lettuce)
    except PlantError as e:
        print(e)

    print("\nTesting error recovery...")
    try:
        manager.water_plants()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    main()
