def validate_ingredients(ingredients: str) -> str:

    valid_elements: list[str] = ["fire", "water", "earth", "air"]
    words: list[str] = ingredients.split()
    
    for word in words:
        if not word in valid_elements:
            return f"{ingredients} - INVALID"

    return f"{ingredients} - VALID"
    
