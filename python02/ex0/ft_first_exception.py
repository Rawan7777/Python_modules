#!/usr/bin/env python3

def check_temperature(temp_str: str) -> None:

    """Validate a temperature string and return an integer temperature"""

    print("Testing temperature:", temp_str)

    try:
        temp = int(temp_str)
    except ValueError:
        return f"Error: '{temp_str}' is not a valid number\n"
    else:
        if temp >= 0 and temp <= 40:
            return f"Temperature {temp}°C is perfect for plants!\n"
        elif temp > 40:
            return f"Error: {temp}°C is too hot for plants (max 40°C)\n"
        elif temp < 0:
            return f"Error: {temp}°C is too cold for plants (min 0°C)\n"


def test_temperature_input():

    """Run basic test cases for the check_temperature() function."""

    print("=== Garden Temperature Checker ===\n")

    print(check_temperature("25"))
    print(check_temperature("abc"))
    print(check_temperature("100"))
    print(check_temperature("-50"))

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":

    test_temperature_input()
