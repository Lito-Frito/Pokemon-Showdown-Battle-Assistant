# Pokemon-Showdown-Battle-Assistant

A simple assistant to help you strategize during a Pokemon battle

![Battle-Assistant-Logo](https://user-images.githubusercontent.com/56422761/268390826-51329e3f-cbb9-47bb-9e40-2bf7b1706891.png)

<!-- Replit badge -->
## [![Run on Repl.it](https://repl.it/badge/github/Lito_Frito/Pokemon-Showdown-Battle-Assistant)](https://replit.com/@Lito-Frito/Pokemon-Showdown-Battle-Assistant)

This is a simple CLI app to help people who play Pokemon. I made this because I haven't played since Gen1 and I wanted a tool to help me keep track of all the new type matchups (e.g. what type is effective against or takes greater damage from some other type).

If you want to get back into Pokemon, or if you can never keep track of what beats what, this tool is for you. The "battle assistant" will ask you for two types. It will then return all the types that are strong/weak against the given types.

E.g. if you input "grass" and "ice" (shout out to Abomasnow; Snow is in the way), this is a snippet of what the output will look like:

*Grass is:
*Strong against: 2x => ['water', 'ground', 'rock']*

*Weak against: 0.5x => ['fire', 'grass', 'poison', 'flying', 'bug', 'dragon', 'steel']*

*Ice is:
*Strong against: 2x => ['grass', 'ground', 'flying', 'dragon']*

*Weak against: 0.5x => ['fire', 'water', 'ice', 'steel']*

This snippet is just the offensive analysis; it will also tell you the defensive analysis.

## What This Includes

- `main.py`: The script that houses and calls all the other important scripts
- `type_input.py`: Respoonsible for determiming valid input and collecting potentially two types from the user
- `offense_calculator.py` & `defense_calculator.py`: Takes the inputs from `type_input.py` and runs an offensive and defensive analyses (see above for example)

# Getting Started

## Requirements

- Python3
- a CLI (if you're on Windows, this is the Command Prompt; for Linux and Mac, this is your terminal)

## Quick Start

You can go to [repl.it](https://replit.com/@Lito-Frito/Pokemon-Showdown-Battle-Assistant) where I'm hosting the app in a personal repl.
