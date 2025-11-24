"""Given the type(s) of a Pokemen, this program will answer:
* what types can/can't beat it up ?

It prints the following information to the user:
'{formal_types} ~~~
take STRONG damage from: 2x =>  [ list of types]
take STRONG damage from: 2x =>  [list of types]"""

from Dicts.defense_dict import defense_multiplier_dict

def defense_calculator(pokemon_type1, pokemon_type2):
    # The final result that's returned to the user will populate here
    defense_analysis = {
        4: [],
        2: [],
        1: [],
        0.5: [],
        0.25: [],
        0: []
    }

    # Placeholder dictionary to help determine the final multiplier, given some type(s)
    calc_final_multiplier_dict = {
        # E.g. "normal": 1
    }

    # Append the first type to multiplier_dict to determine final multiplier:
    for multiplier in defense_multiplier_dict[pokemon_type1]:
        for defense_dict_type in defense_multiplier_dict[pokemon_type1][multiplier]:
            calc_final_multiplier_dict[defense_dict_type] = multiplier
    
    # Repeat for second type && compare its multiplier to determine final one:
    if pokemon_type2 != "none":
        for multiplier in defense_multiplier_dict[pokemon_type2]:
            for defense_dict_type in defense_multiplier_dict[pokemon_type2][multiplier]:
                # Compare the multipliers and multiply them to determine the new multiplier for that type:
                if defense_dict_type in calc_final_multiplier_dict:
                    calc_final_multiplier_dict[defense_dict_type] *= multiplier
    
    # Insert data into defense_analysis in a clean format
    for type in calc_final_multiplier_dict:
        # Insert the type into the correct list in defense_analysis
        defense_analysis[calc_final_multiplier_dict[type]].append(type)
    
    # Dictionary for analysis prompts:
    analysis_prompts = {
        4: "take *VERY* STRONG damage from:",
        2: "take STRONG damage from:",
        1: "take regular damage from:", # Shouldn't print since this isn't the default multiplier
        0.5: "take WEAK damage from:",
        0.25: "take *VERY* WEAK damage from:",
        0: "take *NO* damage from:"
    }
    
    # Create a formal format for the output e.g. ["normal", "ice"]-> "Normal & Ice":
    formal_types = ([pokemon_type1[0].upper() + pokemon_type1[1:], pokemon_type2[0].upper() + pokemon_type2[1:]])
    if pokemon_type2 == "none":
        formal_types_str = formal_types[0]
    else:
        formal_types_str = " & ".join(formal_types)

    # Start printing the final result to the user:
    print(f"\nHere's the defensive analysis (what types are strong/weak) against {formal_types_str}:")
    print(f"\n{formal_types_str} ~~~")

    # Print defense_analysis in a table format
    print("\nDefensive Analysis Table:")
    
    # Collect rows
    rows = []
    for multiplier in sorted(defense_analysis.keys(), reverse=True):
        if defense_analysis[multiplier] != [] and multiplier != 1:
            mult_str = f"{multiplier}x"
            types_str = ", ".join(defense_analysis[multiplier])
            rows.append((mult_str, types_str))
    
    # Find max length for types
    max_types_len = max(len(types_str) for _, types_str in rows) if rows else 0
    types_width = max(34, max_types_len + 2)
    
    # Print table
    print("┌" + "─" * 12 + "┬" + "─" * types_width + "┐")
    print("│" + " Multiplier " + "│" + f"{' Types':<{types_width}}" + "│")
    print("├" + "─" * 12 + "┼" + "─" * types_width + "┤")
    for mult_str, types_str in rows:
        print("│" + f" {mult_str:<10} " + "│" + f" {types_str:<{types_width-1}}" + "│")
    print("└" + "─" * 12 + "┴" + "─" * types_width + "┘")
    
    return calc_final_multiplier_dict
