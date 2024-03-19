"""Dict of types vs their offensive effectiveness against other types"""
defense_multiplier_dict = {
        "normal": {
            2: ["fighting"],
            1: ["normal", "fire", "water", "electric", "grass", "ice", "poison", "ground", "flying", "psychic", "bug", "rock", "dragon", "dark", "steel", "fairy"],
            0: ["ghost"]
        },
        "fire": {
            2: ["water", "ground", "rock"],
            1: ["normal", "electric", "fighting", "poison", "flying", "psychic", "ghost", "dragon", "dark"],
            0.5: ["fire", "grass", "ice", "bug", "steel", "fairy"]
        },
        "water": {
            2: ["electric", "grass"],
            1: ["normal", "fighting", "poison", "ground", "flying", "psychic", "bug", "rock", "ghost", "dragon", "dark", "fairy"],
            0.5: ["fire", "water", "ice", "steel"]
        },
        "electric": {
            2: ["ground"],
            1: ["normal", "fire", "water", "ice", "fighting", "poison", "psychic", "bug", "rock", "ghost", "dragon", "dark", "fairy"],
            0.5: ["electric", "flying", "steel"]
        },
        "grass": {
            2: ["fire", "ice", "poison", "flying", "bug"],
            1: ["normal", "fighting", "psychic", "rock", "ghost", "dragon", "dark", "steel", "fairy"],
            0.5: ["water", "electric", "grass", "ground"]
        },
        "ice": {
            2: ["fire", "fighting", "rock", "steel"],
            1: ["normal", "water", "electric", "grass", "poison", "ground", "flying", "psychic", "bug", "ghost", "dragon", "dark", "fairy"],
            0.5: ["ice"]
        },
        "fighting": {
            2: ["flying", "psychic", "fairy"],
            1: ["normal", "fire", "water", "electric", "grass", "ice", "fighting", "poison", "ground", "ghost", "dragon", "steel"],
            0.5: ["bug", "rock", "dark"]
        },
        "poison": {
            2: ["ground", "psychic"],
            1: ["normal", "fire", "water", "electric", "ice", "flying", "rock", "ghost", "dragon", "dark", "steel"],
            0.5: ["grass", "fighting", "poison", "bug", "fairy"]
        },
        "ground": {
            2: ["water", "grass", "ice"],
            1: ["normal", "fire", "fighting", "ground", "flying", "psychic", "bug", "ghost", "dragon", "dark", "steel", "fairy"],
            0.5: ["poison", "rock"],
            0: ["electric"]
        },
        "flying": {
            2: ["electric", "ice", "rock"],
            1: ["normal", "fire", "water", "poison", "flying", "psychic", "ghost", "dragon", "dark", "steel", "fairy"],
            0.5: ["grass", "fighting", "bug"],
            0: ["ground"]
        },
        "psychic": {
            2: ["bug", "ghost", "dark"],
            1: ["normal", "fire", "water", "electric", "grass", "ice", "poison", "ground", "flying", "rock", "dragon", "steel", "fairy"],
            0.5: ["fighting", "psychic"]
        },
        "bug": {
            2: ["fire", "flying", "rock"],
            1: ["normal", "water", "electric", "ice", "poison", "psychic", "bug", "ghost", "dragon", "dark", "steel", "fairy"],
            0.5: ["grass", "fighting", "ground"]
        },
        "rock": {
            2: ["water", "grass", "fighting", "ground", "steel"],
            1: ["electric", "ice", "psychic", "bug", "rock", "ghost", "dragon", "dark", "fairy"],
            0.5: ["normal", "fire", "poison", "flying"]
        },
        "ghost": {
            2: ["ghost", "dark"],
            1: ["fire", "water", "electric", "grass", "ice", "ground", "flying", "psychic", "rock", "dragon", "steel", "fairy"],
            0.5: ["poison", "bug"],
            0: ["normal", "fighting"]
        },
        "dragon": {
            2: ["ice", "dragon", "fairy"],
            1: ["normal", "fighting", "poison", "ground", "flying", "psychic", "bug", "rock", "ghost", "dark", "steel"],
            0.5: ["fire", "water", "electric", "grass"]
        },
        "dark": {
            2: ["fighting", "bug", "fairy"],
            1: ["normal", "fire", "water", "electric", "grass", "ice", "poison", "ground", "flying", "rock", "dragon", "steel"],
            0.5: ["ghost", "dark"],
            0: ["psychic"]
        },
        "steel": {
            2: ["fire", "fighting", "ground"],
            1: ["water", "electric", "ghost", "dark"],
            0.5: ["normal", "grass", "ice", "flying", "psychic", "bug", "rock", "dragon", "steel", "fairy"],
            0: ["poison"]
        },
        "fairy": {
            2: ["poison", "steel"],
            1: ["normal", "fire", "water", "electric", "grass", "ice", "ground", "flying", "psychic", "rock", "ghost", "fairy"],
            0.5: ["fighting", "bug", "dark"],
            0: ["dragon"]
        }
    }
