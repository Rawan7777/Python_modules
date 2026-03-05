#!/usr/bin/env python3

class GardenError(Exception):

    """Base exception for all garden-related errors."""


class PlantError(GardenError):

    """Exception raised for plant-related problems."""

    def __init__(self, message_error="PlantError occured"):
        super().__init__(message_error)


class WaterError(GardenError):

    """Exception raised for watering-related problems."""

    def __init__(self, message_error="GardenError occured"):
        super().__init__(message_error)


def main():

    """Demonstrate custom garden error handling."""

    print("=== Custom Garden Errors Demo ===\n")

    try:
        print("Testing PlantError...")
        raise PlantError("The tomato plant is wilting!")
    except PlantError as error:
        print(f"Caught PlantError: {error}\n")

    try:
        print("Testing WaterError...")
        raise WaterError("Not enough water in the tank!")
    except WaterError as error:
        print(f"Caught WaterError: {error}\n")

    print("Testing catching all garden errors...")

    errors = [
        PlantError("The tomato plant is wilting!"),
        WaterError("Not enough water in the tank!")
        ]

    for error in errors:
        try:
            raise error
        except GardenError as caught_error:
            print(f"Caught a garden error: {caught_error}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
