from textwrap import dedent

def find_types():
    """This function determines the pokemon's type(s) and return them to the main function"""
    
    # Get first type and ensure type is valid:
    while True:
        pokemon_type1 = input("\nWhat is the pokemon's first type? > ").lower()

        if validate_type(pokemon_type1) is True:
            break

    # Get second type and ensure type is valid:
    while True:
        pokemon_type2 = input("\nWhat is the pokemon's second type? > ").lower().strip()

        if pokemon_type2 in ["none", ""]:
            pokemon_type2 = "none"
            break

        if pokemon_type2 == pokemon_type1:
            print("\nYou entered the same type as the first type. Please enter a different type or 'none'.")
            continue

        if validate_type(pokemon_type2) is True:
            break
    
    return pokemon_type1, pokemon_type2

def validate_type(pokemon_type):
    """This function creates a list of all acceptable types to be checked against the user's input"""
    
    # List of all acceptable types to be checked against the user's input:
    acceptable_types = [
        "normal", "fire", "water", "electric", "grass", "ice", "fighting", "poison", "ground",
        "flying", "psychic", "bug", "rock", "ghost", "dragon", "dark", "steel", "fairy"
        ]
    
    error_prompt = f"""You entered: "{pokemon_type}", which isn't valid; Here is a list of all valid types:"""
    valid_examples = "\n* " + "\n* ".join(acceptable_types)

    if pokemon_type in acceptable_types:
        return True
    
    else:
        print(error_prompt)
        print(valid_examples)
        return False
