def validate_ingredients(ingredients: str) -> str:

    valid_elements: list[str] = ["fire", "water", "earth", "air"]
    words: list[str] = ingredients.split()
    
    for word in words:
        if word in valid_elements:
            return f"{ingredients} - VALID"
    
    return f"{ingredients} - INVALID"
