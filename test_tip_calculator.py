import io
import unittest
from contextlib import redirect_stdout

from tip_calculator import compute_tip, render_breakdown, run_live_demo


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

    def test_render_breakdown(self):
        output = render_breakdown(compute_tip(50, 20, 2))
        self.assertIn("Bill: $50.00", output)
        self.assertIn("Tip (20.0%): $10.00", output)
        self.assertIn("Per person (2): $30.00", output)

    def test_live_demo_output(self):
        stream = io.StringIO()
        with redirect_stdout(stream):
            run_live_demo()
        text = stream.getvalue()
        self.assertIn("LIVE DEMO: US Tip Calculator", text)
        self.assertIn("Solo diner (standard)", text)
        self.assertIn("Group dinner (great)", text)


if __name__ == "__main__":
    unittest.main()
