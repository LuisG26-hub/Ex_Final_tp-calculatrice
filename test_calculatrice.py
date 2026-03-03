import unittest
from src.calculatrice import division, puissance, moyenne


class TestCalculatrice(unittest.TestCase):

    # --- Tests division ---
    def test_division_simple(self):
        self.assertEqual(division(10, 2), 5.0)

    def test_division_decimales(self):
        self.assertEqual(division(5, 2), 2.5)

    def test_division_zero(self):
        with self.assertRaises(ZeroDivisionError):
            division(10, 0)

    # --- Tests puissance ---
    def test_puissance_positive(self):
        self.assertEqual(puissance(2, 3), 8.0)

    def test_puissance_zero(self):
        self.assertEqual(puissance(5, 0), 1.0)

    def test_puissance_negative(self):
        with self.assertRaises(ValueError):
            puissance(2, -1)

    # --- Tests moyenne ---
    def test_moyenne_valeurs(self):
        self.assertAlmostEqual(moyenne([10, 20, 30]), 20.0)

    def test_moyenne_liste_vide(self):
        with self.assertRaises(ValueError):
            moyenne([])