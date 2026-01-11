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

    # Get all types
    all_types = [t for t in defense_multiplier_dict if t != "none"]
    
    # Placeholder dictionary to help determine the final multiplier, given some type(s)
    calc_final_multiplier_dict = {t: 1.0 for t in all_types}

    # Update for first type
    for multiplier, types in defense_multiplier_dict[pokemon_type1].items():
        for t in types:
            calc_final_multiplier_dict[t] *= multiplier
    
    # Update for second type
    if pokemon_type2 != "none":
        for multiplier, types in defense_multiplier_dict[pokemon_type2].items():
            for t in types:
                calc_final_multiplier_dict[t] *= multiplier
    
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
            if multiplier == 4:
                eff_str = "Ultra Effective"
            elif multiplier == 2:
                eff_str = "Super Effective"
            elif multiplier == 0.5:
                eff_str = "Not Very Effective"
            elif multiplier == 0.25:
                eff_str = "Especially Not Effective"
            elif multiplier == 0:
                eff_str = "Immune (No Damage)"
            else:
                eff_str = f"{multiplier}x"
            mult_str = f"{multiplier}x"
            types_str = ", ".join(defense_analysis[multiplier])
            rows.append((eff_str, mult_str, types_str))
    
    # Find max lengths
    max_eff_len = max(len(eff_str) for eff_str, _, _ in rows) if rows else 0
    max_mult_len = max(len(mult_str) for _, mult_str, _ in rows) if rows else 0
    max_types_len = max(len(types_str) for _, _, types_str in rows) if rows else 0
    eff_width = max(20, max_eff_len + 2)
    mult_width = max(12, max_mult_len + 2)
    types_width = max(34, max_types_len + 2)
    
    # Print table
    print("┌" + "─" * eff_width + "┬" + "─" * mult_width + "┬" + "─" * types_width + "┐")
    print("│" + f"{' Effectiveness':<{eff_width}}" + "│" + f"{' Multiplier':<{mult_width}}" + "│" + f"{' Types':<{types_width}}" + "│")
    print("├" + "─" * eff_width + "┼" + "─" * mult_width + "┼" + "─" * types_width + "┤")
    for eff_str, mult_str, types_str in rows:
        print("│" + f" {eff_str:<{eff_width-1}}" + "│" + f" {mult_str:<{mult_width-1}}" + "│" + f" {types_str:<{types_width-1}}" + "│")
    print("└" + "─" * eff_width + "┴" + "─" * mult_width + "┴" + "─" * types_width + "┘")
    
    return calc_final_multiplier_dict
