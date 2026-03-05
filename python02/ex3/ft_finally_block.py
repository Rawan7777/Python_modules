#!/usr/bin/env python3

def water_plants(plant_list):

    """Water each plant in the given list.
    param plant_list: List of plant names
    raises ValueError: If an invalid plant is found"""

    print("Opening watering system")

    for plant in plant_list:
        if not plant:
            raise ValueError(f"Error: Cannot water {plant} - invalid plant!")
        print(f"Watering {plant}")


def test_watering_system():

    """Run test cases for the garden watering system."""

    print("=== Garden Watering System ===")

    print("\nTesting normal watering...")
    plants = ["tomato", "lettuce", "carrots"]
    try:
        water_plants(plants)
    except ValueError as error:
        print(error)
    finally:
        print("Closing watering system (cleanup)")
    print("Watering completed successfully!")

    print("\nTesting with error...")
    plants = ["tomato", None]
    try:
        water_plants(plants)
    except ValueError as error:
        print(error)
    finally:
        print("Closing watering system (cleanup)")

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
