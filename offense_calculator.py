"""Given the type(s) of a Pokemen, this program will answer:
* what types can/can't the Pokemon beat up ?

It prints the following information to the user:
* Strong against: {formatted_result}
* Weak against: {formatted_result}
* Ineffective against: {formatted_result}"""

from Dicts.offense_dict import offense_multiplier_dict

def get_all_offensive_multipliers(def_type1, def_type2):
    """Calculate offensive multipliers for all types against the given defending types."""
    mults = {}
    for attacking_type in offense_multiplier_dict:
        if attacking_type == "none":
            continue
        mult = 1
        for def_type in [def_type1, def_type2]:
            if def_type != "none":
                for multiplier, types in offense_multiplier_dict[attacking_type].items():
                    if def_type in types:
                        mult *= multiplier
                        break
        mults[attacking_type] = mult
    return mults

def get_opponent_offensive_mults(opponent_type1, opponent_type2):
    """Calculate offensive multipliers for the opponent against all types."""
    mults = {}
    for defender in offense_multiplier_dict:
        if defender == "none":
            continue
        mult = 1
        for opponent_type in [opponent_type1, opponent_type2]:
            if opponent_type != "none":
                for multiplier, types in offense_multiplier_dict[opponent_type].items():
                    if defender in types:
                        mult *= multiplier
                        break
        mults[defender] = mult
    return mults

def print_offensive_table(pokemon_type1, pokemon_type2):
    """Print the offensive analysis table for the given Pokemon types."""
    mults = get_opponent_offensive_mults(pokemon_type1, pokemon_type2)
    
    offense_table = {
        4: [],
        2: [],
        1: [],
        0.5: [],
        0.25: [],
        0: []
    }
    
    for t, mult in mults.items():
        offense_table[mult].append(t)
    
    formal_types = ([pokemon_type1[0].upper() + pokemon_type1[1:], pokemon_type2[0].upper() + pokemon_type2[1:]])
    if pokemon_type2 == "none":
        formal_types_str = formal_types[0]
    else:
        formal_types_str = " & ".join(formal_types)
    
    print(f"\nHere's the offensive analysis (what types {formal_types_str} can beat up):")
    print(f"\n{formal_types_str} ~~~")
    
    # Collect rows
    rows = []
    for multiplier in sorted(offense_table.keys(), reverse=True):
        if offense_table[multiplier] != [] and multiplier != 1:
            if multiplier == 4:
                mult_str = "Ultra Effective"
            elif multiplier == 2:
                mult_str = "Super Effective"
            elif multiplier == 0.5:
                mult_str = "Not Very Effective"
            elif multiplier == 0.25:
                mult_str = "Mostly Ineffective"
            elif multiplier == 0:
                mult_str = "Ineffective (Immune)"
            else:
                mult_str = f"{multiplier}x"
            types_str = ", ".join(offense_table[multiplier])
            rows.append((mult_str, types_str))
    
    # Find max length for types
    max_types_len = max(len(types_str) for _, types_str in rows) if rows else 0
    types_width = max(34, max_types_len + 2)
    mult_width = 20  # Wider for descriptive labels
    
    print("\nOffensive Analysis Table:")
    print("┌" + "─" * mult_width + "┬" + "─" * types_width + "┐")
    print("│" + f"{' Effectiveness':<{mult_width}}" + "│" + f"{' Types':<{types_width}}" + "│")
    print("├" + "─" * mult_width + "┼" + "─" * types_width + "┤")
    for mult_str, types_str in rows:
        print("│" + f" {mult_str:<{mult_width-1}}" + "│" + f" {types_str:<{types_width-1}}" + "│")
    print("└" + "─" * mult_width + "┴" + "─" * types_width + "┘")

def offense_calculator(pokemon_type1, pokemon_type2):
    """This function will calculate the offensive multiplier for the pokemon's type(s)"""

    pokemon_types = [pokemon_type1, pokemon_type2]
    
    offense_analysis = {}

    # Look up pokemon's types in offense_multiplier_dict and populate offense_analysis with its values
    offense_analysis[pokemon_type1] = offense_multiplier_dict[pokemon_type1]
    if pokemon_type2 != "none":
        offense_analysis[pokemon_type2] = offense_multiplier_dict[pokemon_type2]

    # Create a formal format for printing both user-given types e.g. ["normal", "ice"]-> "Normal & Ice":
    formal_types = ([pokemon_type1[0].upper() + pokemon_type1[1:], pokemon_type2[0].upper() + pokemon_type2[1:]])
    non_list_of_formal_types = " & ".join(formal_types)

    # Print offense_analysis in a clean format
    print(f"\nHere's the offensive analysis (what types {non_list_of_formal_types} can/can't beat up):")
    for type in offense_analysis:
        # Create a formal format for each given type (e.g. "normal" -> "Normal"):
        formal_type = type[0].upper() + type[1:]

        print(f"\n{formal_type} is ~~~")

        for multiplier in offense_analysis[type]:
            # Create a clean format use in output
            formatted_result = str(multiplier) + "x " + "=> " + str(offense_analysis[type][multiplier])
            
            # Return strong matchups
            if multiplier == 2:
                print(f"Strong against: {formatted_result}")

            # Return weak matchups
            if multiplier == 0.5:
                print(f"\nWeak against: {formatted_result}")

            # Return matchups with no effect
            if multiplier == 0:
                print(f"\nIneffective against: {formatted_result}:")
    
    return
