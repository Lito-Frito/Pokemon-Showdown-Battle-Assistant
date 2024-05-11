# -*- coding: utf-8 -*-
#  ^  so that we can use Japanese characters in the program

from textwrap import dedent
from type_input import find_types
from offense_calculator import offense_calculator
from defense_calculator import defense_calculator


def main():
    """This function calls a function for the offensive stats and another for the defensive ones.
    Both return a list of  multipliers for each type, given respective weaknesses and resistances"""

    # Program's name:
    battle_assistant = "べろべろ"

    # Welcome the user and explain the program:
    print(dedent(f"""\
                 Welcome to the Pokemon Showdown Battle Assistant!
                 Given the type(s) of a Pokemen, this program will answer the following:\n
                 * what types can it/can't it beat up ?
                 * what types can/can't beat it up ?\n
                 I'm BeroBero ({battle_assistant}) or Bero for short.
                 I'll be your battle assistant!\
                 """))
    
    # Teach user how to exit at any time
    input("\nAt any time, press CTL/CMD + C (try Z if C didn't work) to exit the program; press ENTER to continue.")
    
    start_analysis = True
    while start_analysis:
        try:                    
            # Determine the pokemon's type(s):
            pokemon_type1, pokemon_type2 = find_types() #start here next time 5/11/24

            # Run offensive & defensive analyses on the Pokemon's type(s):
            offensive_analysis = offense_calculator(pokemon_type1, pokemon_type2)
            defensive_analysis = defense_calculator(pokemon_type1, pokemon_type2)

            # Ask user if they want to continue and update still_playing accordingly:
            still_playing = True # will change to False if user enters "n" on L45
            while still_playing:

                # Ask the user to start another analysis
                keep_going = input("\nWould you like to continue? (y/n): ")

                if keep_going.lower() == "y":
                    break

                elif keep_going.lower() == "n":
                    still_playing = False
                    print("\n\nProgram finished.")
                    print("Thank you for using the Pokemon Showdown Battle Assistant, BeroBero! See you next time!")
                    exit()
                
                else:
                    # Tell the user what the appropriate answers are:
                    print("\n\nPlease enter 'y' or 'n' only.")
                    continue

        except KeyboardInterrupt:
            print("\n\nProgram interrupted....thank you for using the Pokemon Showdown Battle Assistant, BeroBero! See you next time!")
            exit()
    
    return

main()

# print("\nPlease enter y or n.")
#                 # Get the user to enter y or n:
#                 while user_input.lower() != "y" or user_input.lower() != "n":
#                     try_again = input("Would you like to continue? (y/n): ")
#                     if try_again.lower() != "y" or try_again.lower() != "n":
#                         print("\nPlease enter y or n.")
#                         continue
#                     else:
#                         user_input = try_again
#                         break
