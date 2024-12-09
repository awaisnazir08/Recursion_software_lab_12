import unittest
from recursive_sum_of_digits import sum_of_digits, analyze_time_complexity

class TestSumOfDigits(unittest.TestCase):
    """Unit tests for sum_of_digits function."""
    
    def test_positive_numbers(self):
        """Test sum of digits for various positive numbers."""
        test_cases = [
            (123, 6),
            (9876, 30),
            (1000, 1),
            (54321, 15)
        ]
        for number, expected in test_cases:
            with self.subTest(number=number):
                self.assertEqual(sum_of_digits(number), expected)
    
    def test_zero(self):
        """Test sum of digits for zero."""
        self.assertEqual(sum_of_digits(0), 0)
    
    def test_single_digit(self):
        """Test sum of digits for single digit numbers."""
        for i in range(10):
            self.assertEqual(sum_of_digits(i), i)
    
    def test_negative_numbers(self):
        """Test sum of digits handles negative numbers."""
        test_cases = [
            (-123, 6),
            (-9876, 30),
            (-1000, 1)
        ]
        for number, expected in test_cases:
            with self.subTest(number=number):
                self.assertEqual(sum_of_digits(number), expected)
    
    def test_invalid_input(self):
        """Test that invalid inputs raise a ValueError."""
        with self.assertRaises(ValueError):
            sum_of_digits("not a number")
        with self.assertRaises(ValueError):
            sum_of_digits(3.14)

def main():
    """Demonstrate the sum_of_digits function with example usage."""
    # Example numbers
    test_numbers = [0, 123, 9876, -54321]
    
    for num in test_numbers:
        digit_sum = sum_of_digits(num)
        complexity = analyze_time_complexity(num)
        
        print(f"Number: {num}")
        print(f"Sum of Digits: {digit_sum}")
        print("Complexity Analysis:")
        for key, value in complexity.items():
            print(f"  {key}: {value}")
        print()

if __name__ == "__main__":
    # Run the main demonstration
    main()
    
    # Optionally run unit tests
    unittest.main(argv=[''], exit=False)