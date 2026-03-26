# 📜 The Codex — Module 06

> **Mastering Python's Import Mysteries**  
> *42 Network — Python Cursus*

---

## 📖 About

**The Codex** is the seventh module of the 42 Python cursus, themed around an Alchemical Laboratory where code organization is treated as a form of ancient magic. This module focuses on **Python's import system** — package initialization, import styles, absolute vs relative imports, and resolving circular dependencies — the fundamental skills that separate a script writer from a true software architect.

Building on polymorphism (Module 05), you now learn how to structure multi-file Python projects: turning directories into packages with `__init__.py`, controlling what each package exposes, and navigating the boundaries between modules without falling into the Circular Dependency Curse.

> 🗺️ You are an apprentice alchemist in the Alchemical Laboratory. Four sacred mysteries stand between you and mastery of the Codex.

---

## 🗂️ Project Structure

```
module06/
├── ft_sacred_scroll.py            ← Part I demo (repository root)
├── ft_import_transmutation.py     ← Part II demo (repository root)
├── ft_pathway_debate.py           ← Part III demo (repository root)
├── ft_circular_curse.py           ← Part IV demo (repository root)
└── alchemy/
    ├── __init__.py                ← Main sacred scroll
    ├── elements.py                ← Basic elemental spells
    ├── potions.py                 ← Advanced potion recipes
    ├── transmutation/
    │   ├── __init__.py
    │   ├── basic.py               ← Absolute-import transmutations
    │   └── advanced.py            ← Relative-import transmutations
    └── grimoire/
        ├── __init__.py
        ├── spellbook.py           ← Spell recorder (late import)
        └── validator.py           ← Ingredient validator
```

---

## 📋 Parts Overview

| Mystery | Part | Demo Script | Core Concept |
|---------|------|-------------|--------------|
| **I** | The Sacred Scroll | `ft_sacred_scroll.py` | `__init__.py` — package interface control |
| **II** | Import Transmutation | `ft_import_transmutation.py` | `import`, `from...import`, `as` — four styles |
| **III** | The Great Pathway Debate | `ft_pathway_debate.py` | Absolute vs relative imports |
| **IV** | Breaking the Circular Curse | `ft_circular_curse.py` | Late imports — circular dependency resolution |

---

## 🔧 Technical Requirements

- **Language:** Python 3.10+
- **Authorized imports:** All Python standard library modules (`datetime`, `math`, `os`, `sys`, etc.)
- **Authorized import styles:** `import`, `from...import`, `import...as`, relative imports (`.` and `..`)
- **Mandatory pattern:** Every package directory must have a proper `__init__.py`
- **Forbidden:** `eval()`, `exec()`, direct `sys.path` manipulation, `importlib`, external libraries
- **Style:** Clean, simple functions that return strings — the complexity is in the import structure, not the logic
- **Error handling:** Use `try/except` and return descriptive error strings — programs must never crash

---

## 📝 Part Details

### Mystery I — The Sacred Scroll

Learn the most fundamental package concept: **`__init__.py` controls what a package exposes**.

`alchemy/elements.py` defines four functions (`create_fire`, `create_water`, `create_earth`, `create_air`), but `alchemy/__init__.py` deliberately imports only two — making the other two accessible only via direct module access. The demo script proves this distinction by attempting both access paths and catching the resulting `AttributeError` gracefully.

**Key behavior:**
- `alchemy.elements.create_fire()` — always works (direct module access)
- `alchemy.create_fire()` — works (exposed in `__init__.py`)
- `alchemy.create_earth()` — raises `AttributeError` (not exposed)
- `alchemy.__version__` and `alchemy.__author__` — package metadata from `__init__.py`

```
$> python3 ft_sacred_scroll.py
=== Sacred Scroll Mastery ===

Testing direct module access:
alchemy.elements.create_fire(): Fire element created
alchemy.elements.create_water(): Water element created
alchemy.elements.create_earth(): Earth element created
alchemy.elements.create_air(): Air element created

Testing package-level access (controlled by __init__.py):
alchemy.create_fire(): Fire element created
alchemy.create_water(): Water element created
alchemy.create_earth(): AttributeError - not exposed
alchemy.create_air(): AttributeError - not exposed

Package metadata:
Version: 1.0.0
Author: Master Pythonicus
```

> 💡 `__init__.py` is the public API of your package. Everything imported there becomes `package.name`. Everything left out requires callers to know the internal module path. This is how libraries like `requests` or `flask` control their public surface.

Files: `alchemy/__init__.py`, `alchemy/elements.py`, `ft_sacred_scroll.py`

---

### Mystery II — Import Transmutation

Master **all four import styles** and understand what each one puts into your namespace.

`alchemy/potions.py` uses relative imports internally (`from .elements import ...`) to call elemental functions and compose their results into potion strings. The demo script then exercises every import style from the outside.

**Four import styles demonstrated:**

| Style | Syntax | Effect on namespace |
|-------|--------|-------------------|
| Full module | `import alchemy.elements` | Access via `alchemy.elements.fn()` |
| Specific function | `from alchemy.elements import create_water` | Access via `create_water()` directly |
| Aliased | `from alchemy.potions import healing_potion as heal` | Access via `heal()` |
| Multiple | `from alchemy.elements import create_fire, create_earth` | Both directly in namespace |

```
$> python3 ft_import_transmutation.py
=== Import Transmutation Mastery ===

Method 1 - Full module import:
alchemy.elements.create_fire(): Fire element created

Method 2 - Specific function import:
create_water(): Water element created

Method 3 - Aliased import:
heal(): Healing potion brewed with Fire element created and Water element created

Method 4 - Multiple imports:
create_earth(): Earth element created
create_fire(): Fire element created
strength_potion(): Strength potion brewed with Earth element created and Fire element created

All import transmutation methods mastered!
```

> ⚠️ Each style has trade-offs. `import module` is explicit but verbose. `from module import fn` puts the name directly into your namespace. `as` aliases prevent name collisions. Know these trade-offs for your evaluation.

Files: `alchemy/potions.py`, `ft_import_transmutation.py`

---

### Mystery III — The Great Pathway Debate

Understand the **difference between absolute and relative imports** and when to use each.

`alchemy/transmutation/basic.py` uses an **absolute import** (`from alchemy.elements import ...`) — spelling out the full path from the project root. `alchemy/transmutation/advanced.py` uses **relative imports** (`from .basic import ...` and `from ..potions import ...`) — navigating the package tree with dots. Both reach the same functions via different paths.

**Absolute vs Relative:**

| Feature | Absolute | Relative |
|---------|----------|----------|
| Syntax | `from alchemy.elements import create_fire` | `from .basic import lead_to_gold` |
| Clarity | Explicit — full path always visible | Concise — location relative to current file |
| Portability | Works from anywhere on `sys.path` | Works only within a package |
| Refactoring | Must update all paths if package is renamed | Automatically follows the package |

```
$> python3 ft_pathway_debate.py
=== Pathway Debate Mastery ===

Testing Absolute Imports (from basic.py):
lead_to_gold(): Lead transmuted to gold using Fire element created
stone_to_gem(): Stone transmuted to gem using Earth element created

Testing Relative Imports (from advanced.py):
philosophers_stone(): Philosopher's stone created using Lead transmuted to gold using Fire element created and Healing potion brewed with Fire element created and Water element created
elixir_of_life(): Elixir of life: eternal youth achieved!

Testing Package Access:
alchemy.transmutation.lead_to_gold(): Lead transmuted to gold using Fire element created
alchemy.transmutation.philosophers_stone(): [same as above]

Both pathways work! Absolute: clear, Relative: concise
```

> 💡 The single dot (`.`) means "same package". The double dot (`..`) means "parent package". `from ..potions import healing_potion` in `advanced.py` climbs up to `alchemy/` then down into `potions.py` — like `../` in a shell path.

Files: `alchemy/transmutation/__init__.py`, `alchemy/transmutation/basic.py`, `alchemy/transmutation/advanced.py`, `ft_pathway_debate.py`

---

### Mystery IV — Breaking the Circular Curse *(Capstone)*

Learn to **identify and resolve circular import dependencies** using the late import technique.

A circular dependency occurs when module A imports from module B, and module B imports from module A — Python's import machinery cannot resolve this and raises an `ImportError`. The grimoire package demonstrates the problem and solves it: `spellbook.py` needs `validator.py` to check ingredients before recording a spell, but instead of a top-level import, it uses a **late import** — placing the `import` statement inside the function body so it is deferred until the function is actually called, not at module load time.

**Three curse-breaking methods (one must be chosen):**

| Method | Technique | How it works |
|--------|-----------|--------------|
| Late Import | `import` inside the function | Delays resolution until call time |
| Dependency Injection | Pass the function as a parameter | Removes the import entirely |
| Shared Module | Extract shared logic to a third module | Breaks the cycle at the graph level |

```
$> python3 ft_circular_curse.py
=== Circular Curse Breaking ===

Testing ingredient validation:
validate_ingredients("fire air"): fire air - VALID
validate_ingredients("dragon scales"): dragon scales - INVALID

Testing spell recording with validation:
record_spell("Fireball", "fire air"): Spell recorded: Fireball (fire air - VALID)
record_spell("Dark Magic", "shadow"): Spell rejected: Dark Magic (shadow - INVALID)

Testing late import technique:
record_spell("Lightning", "air"): Spell recorded: Lightning (air - VALID)

Circular dependency curse avoided using late imports!
All spells processed safely!
```

> ⚠️ **Do NOT create actual circular imports in your code.** Demonstrate understanding by implementing one solution cleanly. During evaluation you will be asked to explain why the circular dependency would occur and precisely how the late import pattern breaks it.

Files: `alchemy/grimoire/__init__.py`, `alchemy/grimoire/spellbook.py`, `alchemy/grimoire/validator.py`, `ft_circular_curse.py`

---

## 🧠 Concepts Introduced

| Concept | First seen | Python mechanism |
|---------|-----------|-----------------|
| Package creation | Part I | Directory + `__init__.py` |
| Package public API | Part I | Imports inside `__init__.py` |
| Package metadata | Part I | `__version__`, `__author__` attributes |
| Hidden functions | Part I | Not imported in `__init__.py` → `AttributeError` |
| Full module import | Part II | `import alchemy.elements` |
| Specific function import | Part II | `from module import fn` |
| Aliased import | Part II | `import fn as alias` |
| Multiple import | Part II | `from module import a, b` |
| Relative same-package import | Part III | `from .module import fn` |
| Relative parent-package import | Part III | `from ..module import fn` |
| Absolute import | Part III | `from alchemy.module import fn` |
| Circular dependency | Part IV | Two modules importing each other at load time |
| Late import | Part IV | `import` inside a function body |

---

## 🔗 Import Style Reference

```python
# Style 1 — Full module import
import alchemy.elements
alchemy.elements.create_fire()         # must use full dotted path

# Style 2 — Specific function import
from alchemy.elements import create_fire
create_fire()                          # available directly by name

# Style 3 — Aliased import
from alchemy.potions import healing_potion as heal
heal()                                 # shorter name, avoids collisions

# Style 4 — Multiple specific imports
from alchemy.elements import create_fire, create_earth
create_fire()
create_earth()
```

---

## 🔗 Absolute vs Relative Reference

```python
# Absolute — written in alchemy/transmutation/basic.py
from alchemy.elements import create_fire       # full path from project root

# Relative, same package — written in alchemy/transmutation/advanced.py
from .basic import lead_to_gold               # . = alchemy/transmutation/

# Relative, parent package — written in alchemy/transmutation/advanced.py
from ..potions import healing_potion          # .. = alchemy/
```

---

## 🔗 Late Import Pattern Reference

```python
# Top-level import — dangerous if there is a cycle
# (runs at module load time, may trigger circular ImportError)
from .validator import validate_ingredients

# Late import — safe, breaks the cycle
def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients   # deferred to call time
    result = validate_ingredients(ingredients)
    if "VALID" in result:
        return f"Spell recorded: {spell_name} ({result})"
    return f"Spell rejected: {spell_name} ({result})"
```

---

## 🚀 Running the Experiments

Always run demo scripts from the **repository root** (the directory that *contains* the `alchemy/` folder) so absolute imports resolve correctly:

```bash
# Run from the directory that CONTAINS alchemy/
python3 ft_sacred_scroll.py
python3 ft_import_transmutation.py
python3 ft_pathway_debate.py
python3 ft_circular_curse.py
```

> ⚠️ Running from inside a subdirectory will break absolute imports like `from alchemy.elements import ...` because Python will not find the `alchemy` package on its path.

---

## ⚠️ Important Rules

- **Every package directory must have `__init__.py`** — without it, Python treats the folder as a namespace package and relative imports will fail
- **Never use `eval()`, `exec()`, or modify `sys.path`** — these are forbidden dark magic
- **Never use `importlib`** for dynamic imports
- **No external libraries** — Python standard library only
- Functions should be **simple and return strings** — the challenge is the import structure, not the business logic
- Programs must **never crash** — handle `AttributeError`, `ImportError`, and other exceptions gracefully
- Run all demo scripts from the **project root**, not from inside any subdirectory

---

## 🤖 AI Usage Policy

AI tools are **permitted** with the following rules:

- ✅ Use AI to explore how `__init__.py` transforms a folder into a package, understand why circular imports fail, and clarify dot notation in relative imports
- ✅ Only submit code you **fully understand** and can explain line by line
- ❌ During peer evaluation you'll be asked to explain what happens when Python encounters an `__init__.py`, why a late import breaks a circular dependency, and when to prefer absolute over relative imports — "I got it from AI" is not an answer
- ❌ Do not copy-paste solutions you cannot trace through manually

---

## 📦 Submission

Submit all files via your **Git repository**. Only files tracked in the repo will be evaluated. All files and directories must be at the **repository root**.

Files to submit:
- `ft_sacred_scroll.py`
- `ft_import_transmutation.py`
- `ft_pathway_debate.py`
- `ft_circular_curse.py`
- `alchemy/__init__.py`
- `alchemy/elements.py`
- `alchemy/potions.py`
- `alchemy/transmutation/__init__.py`
- `alchemy/transmutation/basic.py`
- `alchemy/transmutation/advanced.py`
- `alchemy/grimoire/__init__.py`
- `alchemy/grimoire/spellbook.py`
- `alchemy/grimoire/validator.py`

---

*"A true Python alchemist understands that good code organization is like a well-organized laboratory — everything has its place, and you can find any spell quickly when you need it."*
