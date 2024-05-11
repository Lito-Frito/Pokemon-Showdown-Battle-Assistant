"""Given the type(s) of a Pokemen, this program will answer:
* what types can/can't the Pokemon beat up ?

It prints the following information to the user:
* Strong against: {formatted_result}
* Weak against: {formatted_result}
* Ineffective against: {formatted_result}"""

from Dicts.offense_dict import offense_multiplier_dict

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
