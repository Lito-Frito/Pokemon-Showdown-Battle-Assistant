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
    formal_types = " & ".join(formal_types)

    # Start printing the final result to the user:
    print(f"\nHere's the defensive analysis (what types are strong/weak) against {formal_types}:")
    print(f"\n{formal_types} ~~~")

    # Print defense_analysis in a clean format:
    for multiplier in defense_analysis:
        formal_multiplier = str(multiplier) + "x" + " => "
        if defense_analysis[multiplier] != [] and multiplier != 1:
            print(f"\n{analysis_prompts[multiplier]} {formal_multiplier} {defense_analysis[multiplier]}:")
    
    return
