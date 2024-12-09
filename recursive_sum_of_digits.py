import math
import unittest

def sum_of_digits(number: int) -> int:
    """
    Recursively compute the sum of digits for a given integer.

    Args:
        number (int): A non-negative integer whose digits will be summed.

    Returns:
        int: The sum of all digits in the number.

    Raises:
        ValueError: If input is not an integer.

    Examples:
        >>> sum_of_digits(123)
        6
        >>> sum_of_digits(0)
        0
        >>> sum_of_digits(9876)
        30
    """
    # Handle input validation
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")
    
    # Convert negative numbers to positive
    number = abs(number)
    
    # Base case: when number is reduced to 0
    if number == 0:
        return 0
    
    # Recursive case: extract last digit and add to recursive call
    return (number % 10) + sum_of_digits(number // 10)

def analyze_time_complexity(n: int) -> dict:
    """
    Analyze the time and space complexity for the sum_of_digits function.

    Args:
        n (int): The number to analyze.

    Returns:
        dict: A dictionary containing complexity analysis details.
    """
    # Number of recursive calls is proportional to the number of digits
    digit_count = 1 if n == 0 else math.floor(math.log10(abs(n))) + 1
    
    return {
        "time_complexity": f"O({digit_count})",
        "space_complexity": f"O({digit_count})",
        "recursive_depth": digit_count,
        "digit_count": digit_count
    }