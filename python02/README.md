# 🛡️ Garden Guardian — Module 02

> **Data Engineering for Smart Agriculture**  
> *42 Network — Python Cursus*

---

## 📖 About

**Garden Guardian** is the third module of the 42 Python cursus, building directly on the OOP foundations from Module 01 (*CodeCultivation*). This module focuses entirely on **exception handling and resilient data pipeline design** — the skills that separate hobby scripts from production-grade systems.

You'll learn how Python signals problems, how to catch and recover from them gracefully, how to define your own error types, and how to ensure cleanup always happens — even when things go wrong. All through the lens of a smart agricultural monitoring system.

---

## 🗂️ Project Structure

```
module02/
├── ex0/
│   └── ft_first_exception.py
├── ex1/
│   └── ft_different_errors.py
├── ex2/
│   └── ft_custom_errors.py
├── ex3/
│   └── ft_finally_block.py
├── ex4/
│   └── ft_raise_errors.py
└── ex5/
    └── ft_garden_management.py
```

---

## 📋 Exercises Overview

| Exercise | File | Key Concept |
|----------|------|-------------|
| **Ex00** — Agricultural Data Validation Pipeline | `ft_first_exception.py` | `try/except`, basic exception catching |
| **Ex01** — Different Types of Problems | `ft_different_errors.py` | Built-in exception types, multi-except |
| **Ex02** — Making Your Own Error Types | `ft_custom_errors.py` | Custom exceptions, exception inheritance |
| **Ex03** — Finally Block — Always Clean Up | `ft_finally_block.py` | `try/except/finally`, resource cleanup |
| **Ex04** — Raising Your Own Errors | `ft_raise_errors.py` | `raise`, input validation, error messages |
| **Ex05** — Garden Management System | `ft_garden_management.py` | Full integration of all exception techniques |

---

## 🔧 Technical Requirements

- **Language:** Python 3.10+
- **Linting:** All code must pass `flake8` standards
- **Structure:** Each exercise in its own file
- **Docstrings:** Required for all functions and classes
- **Crash policy:** Programs must **never crash** — all errors must be caught and handled
- Show both **normal operations** and **error scenarios** in each exercise
- Use built-in exceptions appropriately before creating custom ones

---

## 📝 Exercise Details

### Ex00 — Agricultural Data Validation Pipeline

Your first `try/except` block. Sensor data from the field can be corrupted or out of range — your validation layer must catch bad data before it corrupts your analytics.

**Functions to implement:**
- `check_temperature(temp_str)` — validates a string temperature reading
- `test_temperature_input()` — demonstrates all test cases

**Validation rules:** temperature must be a valid number between 0°C and 40°C.

```
$> python3 ft_first_exception.py
=== Garden Temperature Checker ===
Testing temperature: 25
Temperature 25°C is perfect for plants!
Testing temperature: abc
Error: 'abc' is not a valid number
Testing temperature: 100
Error: 100°C is too hot for plants (max 40°C)
Testing temperature: -50
Error: -50°C is too cold for plants (min 0°C)
All tests completed - program didn't crash!
```

Authorized: `try`, `except`, `int()`, `print()`

---

### Ex01 — Different Types of Problems

Python has a rich hierarchy of built-in exceptions. Each maps to a specific category of failure — you need to know them to handle them precisely.

**Functions to implement:**
- `garden_operations()` — triggers each error type
- `test_error_types()` — catches and explains each one, including a multi-error `except` block

**Exception types covered:**

| Exception | Scenario |
|-----------|----------|
| `ValueError` | Converting `"abc"` to `int` |
| `ZeroDivisionError` | Dividing harvest by zero plots |
| `FileNotFoundError` | Opening a missing sensor log file |
| `KeyError` | Looking up a plant not in the registry dict |

```
$> python3 ft_different_errors.py
=== Garden Error Types Demo ===
Testing ValueError...
Caught ValueError: invalid literal for int()
Testing ZeroDivisionError...
Caught ZeroDivisionError: division by zero
Testing FileNotFoundError...
Caught FileNotFoundError: No such file 'missing.txt'
Testing KeyError...
Caught KeyError: 'missing_plant'
Testing multiple errors together...
Caught an error, but program continues!
All error types tested successfully!
```

Authorized: `try`, `except`, `ValueError`, `ZeroDivisionError`, `FileNotFoundError`, `KeyError`, `print()`

---

### Ex02 — Making Your Own Error Types

Built-in exceptions aren't always specific enough. Custom exceptions make your errors self-documenting and allow callers to catch only what they care about.

**Exception hierarchy to implement:**
```
Exception
└── GardenError          ← base class for all garden problems
    ├── PlantError       ← problems with individual plants
    └── WaterError       ← problems with the watering system
```

**Key demonstration:** catching `GardenError` must also catch `PlantError` and `WaterError` — because of inheritance.

```
$> python3 ft_custom_errors.py
=== Custom Garden Errors Demo ===
Testing PlantError...
Caught PlantError: The tomato plant is wilting!
Testing WaterError...
Caught WaterError: Not enough water in the tank!
Testing catching all garden errors...
Caught a garden error: The tomato plant is wilting!
Caught a garden error: Not enough water in the tank!
All custom error types work correctly!
```

Authorized: `class`, `Exception`, `try`, `except`, `raise`, `print()`

---

### Ex03 — Finally Block — Always Clean Up

The `finally` block guarantees cleanup code runs whether execution succeeds or fails. Critical for closing connections, files, and hardware interfaces like irrigation valves.

**Functions to implement:**
- `water_plants(plant_list)` — simulates a watering cycle with resource open/close
- `test_watering_system()` — tests both the happy path and the error path

**Key rule:** `"Closing watering system (cleanup)"` must print in **both** the success and failure cases.

```
$> python3 ft_finally_block.py
=== Garden Watering System ===
Testing normal watering...
Opening watering system
Watering tomato
Watering lettuce
Watering carrots
Closing watering system (cleanup)
Watering completed successfully!

Testing with error...
Opening watering system
Watering tomato
Error: Cannot water None - invalid plant!
Closing watering system (cleanup)
Cleanup always happens, even with errors!
```

Authorized: `try`, `except`, `finally`, `print()`

---

### Ex04 — Raising Your Own Errors

Sometimes your program needs to actively signal that something is wrong — not just catch external failures. The `raise` keyword lets you enforce business rules and domain constraints.

**Function to implement:**
- `check_plant_health(plant_name, water_level, sunlight_hours)` — validates all three inputs and raises `ValueError` with a descriptive message for each invalid case

**Validation rules:**

| Parameter | Valid range |
|-----------|-------------|
| `plant_name` | Non-empty string |
| `water_level` | 1 – 10 |
| `sunlight_hours` | 2 – 12 |

```
$> python3 ft_raise_errors.py
=== Garden Plant Health Checker ===
Testing good values...
Plant 'tomato' is healthy!
Testing empty plant name...
Error: Plant name cannot be empty!
Testing bad water level...
Error: Water level 15 is too high (max 10)
Testing bad sunlight hours...
Error: Sunlight hours 0 is too low (min 2)
All error raising tests completed!
```

Authorized: `try`, `except`, `raise`, `ValueError`, `print()`

---

### Ex05 — Garden Management System *(Capstone)*

Bring everything together into a full `GardenManager` class that demonstrates professional-grade exception handling in a real system context.

**`GardenManager` class requirements:**
- `add_plant()` — uses `raise` to reject invalid plant names
- `water_plants()` — uses `try/except/finally` with guaranteed cleanup
- `check_plant_health()` — uses custom exceptions from Ex02 patterns
- Continues operating after individual failures (partial failure tolerance)
- Returns helpful, user-facing error messages throughout

```
$> python3 ft_garden_management.py
=== Garden Management System ===
Adding plants to garden...
Added tomato successfully
Added lettuce successfully
Error adding plant: Plant name cannot be empty!
Watering plants...
Opening watering system
Watering tomato - success
Watering lettuce - success
Closing watering system (cleanup)
Checking plant health...
tomato: healthy (water: 5, sun: 8)
Error checking lettuce: Water level 15 is too high (max 10)
Testing error recovery...
Caught GardenError: Not enough water in tank
System recovered and continuing...
Garden management system test complete!
```

> ⚠️ **Evaluation note:** This exercise will be scrutinized closely. You must be able to explain exactly how each `try/except/finally` block works and why each custom exception was chosen.

Authorized: `class`, `Exception`, `try`, `except`, `finally`, `raise`, `print()`

---

## 🧠 Concepts Introduced

| Concept | First seen |
|---------|-----------|
| `try / except` | Ex00 |
| Built-in exception types (`ValueError`, `KeyError`, etc.) | Ex01 |
| Multi-exception `except` blocks | Ex01 |
| Custom exception classes | Ex02 |
| Exception inheritance hierarchy | Ex02 |
| `finally` block for guaranteed cleanup | Ex03 |
| `raise` keyword — proactive error signaling | Ex04 |
| Full system integration of all techniques | Ex05 |

---

## 🔗 Exception Hierarchy Reference

```
BaseException
└── Exception
    ├── ValueError          ← bad data type / format / value
    ├── ZeroDivisionError   ← math divide-by-zero
    ├── FileNotFoundError   ← missing file or path
    ├── KeyError            ← missing dictionary key
    └── GardenError         ← your custom base (Ex02+)
        ├── PlantError      ← your custom plant-specific error
        └── WaterError      ← your custom water-specific error
```

---

## 🚀 Running the Exercises

Each exercise is a standalone program:

```bash
cd ex0/ && python3 ft_first_exception.py
cd ex1/ && python3 ft_different_errors.py
cd ex2/ && python3 ft_custom_errors.py
cd ex3/ && python3 ft_finally_block.py
cd ex4/ && python3 ft_raise_errors.py
cd ex5/ && python3 ft_garden_management.py
```

To check linting across all files:

```bash
flake8 ex0/ ex1/ ex2/ ex3/ ex4/ ex5/
```

---

## ⚠️ Important Rules

- Programs must **never crash** — every possible exception must be handled
- Show both **success paths** and **error paths** in every exercise
- Each exercise must be in **its own file**
- **Docstrings** required for all functions and classes
- Do **not** use a bare `except Exception` as a lazy catch-all — be specific
- Use the **most specific** exception type available for each situation

---

## 🤖 AI Usage Policy

AI tools are **permitted** with the following rules:

- ✅ Use AI to explore concepts, understand exception flows, and generate test ideas
- ✅ Only submit code you **fully understand** and can explain
- ❌ Do not copy-paste AI output blindly — especially for error handling, where subtle bugs hide easily
- ❌ During peer evaluation, you will be asked to **explain every `try/except` block** and demonstrate live error scenarios

> Your peers share your environment — they can catch bugs that AI misses. Use them as a quality checkpoint.

---

## 📦 Submission

Submit all files via your **Git repository**. Only files tracked in the repo will be evaluated.

Files to submit:
- `ex0/ft_first_exception.py`
- `ex1/ft_different_errors.py`
- `ex2/ft_custom_errors.py`
- `ex3/ft_finally_block.py`
- `ex4/ft_raise_errors.py`
- `ex5/ft_garden_management.py`

---

*"Robust systems aren't built to avoid failures — they're designed to gracefully handle the unexpected. Your digital greenhouse needs to be as resilient as nature itself."*
