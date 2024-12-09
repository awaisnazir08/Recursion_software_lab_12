import unittest
from recursive_parser import evaluate_expression

class TestEvaluateExpression(unittest.TestCase):
    def test_basic_operations(self):
        self.assertAlmostEqual(evaluate_expression("3 + 5"), 8)
        self.assertAlmostEqual(evaluate_expression("10 - 4"), 6)
        self.assertAlmostEqual(evaluate_expression("6 * 7"), 42)
        self.assertAlmostEqual(evaluate_expression("8 / 2"), 4)

    def test_operator_precedence(self):
        self.assertAlmostEqual(evaluate_expression("3 + 5 * 2"), 13)
        self.assertAlmostEqual(evaluate_expression("10 - 4 / 2"), 8)

    def test_parentheses(self):
        self.assertAlmostEqual(evaluate_expression("(3 + 5) * 2"), 16)
        self.assertAlmostEqual(evaluate_expression("10 - (4 + 2)"), 4)

    def test_floating_point_numbers(self):
        self.assertAlmostEqual(evaluate_expression("3.5 + 2.1"), 5.6)
        self.assertAlmostEqual(evaluate_expression("6.2 * 3.5"), 21.7)

    def test_invalid_expressions(self):
        with self.assertRaises(ValueError):
            evaluate_expression("3 +")
        with self.assertRaises(ValueError):
            evaluate_expression("(3 + 5")
        with self.assertRaises(ValueError):
            evaluate_expression("3 / 0")
        with self.assertRaises(ValueError):
            evaluate_expression("abc + 5")

    def test_empty_expression(self):
        with self.assertRaises(ValueError):
            evaluate_expression("")

if __name__ == "__main__":
    unittest.main()
