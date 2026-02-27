import unittest

from tip_calculator import compute_tip


class TipCalculatorTests(unittest.TestCase):
    def test_standard_math(self):
        result = compute_tip(100.0, 15.0, people=2)
        self.assertEqual(result.tip_amount, 15.0)
        self.assertEqual(result.total, 115.0)
        self.assertEqual(result.per_person, 57.5)

    def test_rounding(self):
        result = compute_tip(86.4, 18.0, people=3)
        self.assertEqual(result.tip_amount, 15.55)
        self.assertEqual(result.total, 101.95)
        self.assertEqual(result.per_person, 33.98)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            compute_tip(-1, 10)
        with self.assertRaises(ValueError):
            compute_tip(10, -1)
        with self.assertRaises(ValueError):
            compute_tip(10, 10, people=0)


if __name__ == "__main__":
    unittest.main()
