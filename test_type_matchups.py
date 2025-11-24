import unittest
from offense_calculator import get_opponent_offensive_mults
from defense_calculator import defense_calculator

class TestTypeMatchups(unittest.TestCase):
    types = ["normal", "fire", "water", "electric", "grass", "ice", "fighting", "poison", "ground", "flying", "psychic", "bug", "rock", "ghost", "dragon", "dark", "steel", "fairy"]

    def test_single_types_offensive(self):
        """Test offensive multipliers for single types against all others."""
        for attacker in self.types:
            with self.subTest(attacker=attacker):
                mults = get_opponent_offensive_mults(attacker, "none")
                # Assert no mult is None and all are floats
                for defender, mult in mults.items():
                    self.assertIsInstance(mult, (int, float))
                    self.assertGreaterEqual(mult, 0)

    def test_single_types_defensive(self):
        """Test defensive multipliers for single types against all others."""
        for defender in self.types:
            with self.subTest(defender=defender):
                mults = defense_calculator(defender, "none")
                for attacker, mult in mults.items():
                    self.assertIsInstance(mult, (int, float))
                    self.assertGreaterEqual(mult, 0)

    def test_dual_types_offensive(self):
        """Test offensive multipliers for dual types against all others."""
        for i, type1 in enumerate(self.types):
            for type2 in self.types[i+1:]:  # Avoid duplicates
                with self.subTest(type1=type1, type2=type2):
                    mults = get_opponent_offensive_mults(type1, type2)
                    for defender, mult in mults.items():
                        self.assertIsInstance(mult, (int, float))
                        self.assertGreaterEqual(mult, 0)

    def test_dual_types_defensive(self):
        """Test defensive multipliers for dual types against all others."""
        for i, type1 in enumerate(self.types):
            for type2 in self.types[i+1:]:
                with self.subTest(type1=type1, type2=type2):
                    mults = defense_calculator(type1, type2)
                    for attacker, mult in mults.items():
                        self.assertIsInstance(mult, (int, float))
                        self.assertGreaterEqual(mult, 0)

    # Specific known matchups for Gen 9
    def test_electric_offensive(self):
        mults = get_opponent_offensive_mults("electric", "none")
        self.assertEqual(mults["water"], 2)
        self.assertEqual(mults["flying"], 2)
        self.assertEqual(mults["ground"], 0)
        self.assertEqual(mults["electric"], 0.5)

    def test_electric_defensive(self):
        mults = defense_calculator("electric", "none")
        self.assertEqual(mults["ground"], 2)
        self.assertEqual(mults["flying"], 0.5)
        self.assertEqual(mults["steel"], 0.5)

    def test_ghost_offensive(self):
        mults = get_opponent_offensive_mults("ghost", "none")
        self.assertEqual(mults["psychic"], 2)
        self.assertEqual(mults["ghost"], 2)
        self.assertEqual(mults["normal"], 0)
        self.assertEqual(mults["dark"], 0.5)

    def test_ghost_defensive(self):
        mults = defense_calculator("ghost", "none")
        self.assertEqual(mults["ghost"], 2)
        self.assertEqual(mults["dark"], 2)
        self.assertEqual(mults["poison"], 0.5)
        self.assertEqual(mults["bug"], 0.5)
        self.assertEqual(mults["normal"], 0)
        self.assertEqual(mults["fighting"], 0)

    def test_fire_water_dual_offensive(self):
        mults = get_opponent_offensive_mults("fire", "water")
        self.assertEqual(mults["grass"], 1)  # fire 2x, water 0.5 -> 1
        self.assertEqual(mults["fire"], 1.0)  # fire 0.5, water 2 -> 1
        self.assertEqual(mults["rock"], 1)  # fire 0.5, water 2 -> 1

    def test_fire_water_dual_defensive(self):
        mults = defense_calculator("fire", "water")
        self.assertEqual(mults["water"], 1.0)  # fire 2, water 0.5 -> 1
        self.assertEqual(mults["grass"], 1.0)  # fire 0.5, water 2 -> 1
        self.assertEqual(mults["electric"], 2.0)  # fire 1, water 2 -> 2

if __name__ == '__main__':
    unittest.main()
