#!/usr/bin/env python3

def garden_operations(error_type, file_name=None):

    """Raise different garden-related errors based on the error_type."""

    if error_type == ValueError:
        int("abc")

    elif error_type == ZeroDivisionError:
        10 / 0

    elif error_type == FileNotFoundError:
        open(file_name, "r")

    elif error_type == KeyError:
        data = {}
        print(data["missing_plant"])

    elif error_type == "multiple":
        int("abc")
        10 / 0
        open(file_name, "r")
        data = {}
        print(data["missing_plant"])


def test_error_types():

    """Call garden_operations() with try/except blocks for each error."""

    print("=== Garden Error Types Demo ===\n")

    try:
        print("Testing ValueError...")
        garden_operations(ValueError)
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")

    try:
        print("Testing ZeroDivisionError...")
        garden_operations(ZeroDivisionError)
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")

    try:
        print("Testing FileNotFoundError...")
        file_name = "missing.txt"
        garden_operations(FileNotFoundError, file_name)
    except FileNotFoundError:
        print(f"Caught FileNotFoundError: No such file '{file_name}'\n")

    try:
        print("Testing KeyError...")
        garden_operations(KeyError)
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")

    try:
        print("Testing multiple errors together...")
        garden_operations("multiple")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
