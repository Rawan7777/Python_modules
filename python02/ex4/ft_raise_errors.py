#!/usr/bin/env python3

def check_plant_health(plant_name, water_level, sunlight_hours):

    """Check whether a plant is healthy based on given parameters."""

    if not plant_name:
        raise ValueError("Error: Plant name cannot be empty!")

    if water_level > 10:
        raise ValueError(
            f"Error: Water level {water_level} is too high (max 10)"
        )

    if water_level < 1:
        raise ValueError(
            f"Error: Water level {water_level} is too low (min 1)"
        )

    if sunlight_hours > 12:
        raise ValueError(
            f"Error: Sunlight hours {sunlight_hours} is too high (max 12)"
        )

    if sunlight_hours < 2:
        raise ValueError(
            f"Error: Sunlight hours {sunlight_hours} is too low (min 2)"
        )

    print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks():

    """Run test cases for the plant health checker."""

    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    try:
        check_plant_health("tomato", 5, 10)
    except ValueError as error:
        print(error)

    print("\nTesting empty plant name...")
    try:
        check_plant_health("", 5, 10)
    except ValueError as error:
        print(error)

    print("\nTesting bad water level...")
    try:
        check_plant_health("tomato", 15, 10)
    except ValueError as error:
        print(error)

    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 1)
    except ValueError as error:
        print(error)

    print("\nAll error-raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
