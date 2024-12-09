import unittest
from recursive_binary_search import RecursiveBinarySearch
class TestRecursiveBinarySearch(unittest.TestCase):
    def test_integer_search(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(RecursiveBinarySearch.binary_search_recursive(arr, 3), 2)
        self.assertEqual(RecursiveBinarySearch.binary_search_recursive(arr, 6), -1)
    
    def test_string_search(self):
        arr = ["apple", "banana", "cherry"]
        self.assertEqual(RecursiveBinarySearch.binary_search_recursive(arr, "banana"), 1)
    
    def test_multiple_indices(self):
        arr = [1, 2, 2, 2, 3, 4]
        self.assertEqual(RecursiveBinarySearch.binary_search_all_indices(arr, 2), [1, 2, 3])
    
    def test_error_handling(self):
        with self.assertRaises(ValueError):
            RecursiveBinarySearch.binary_search_recursive([], 5)
        
        with self.assertRaises(TypeError):
            RecursiveBinarySearch.binary_search_recursive([3, 2, 1], 2)

if __name__ == '__main__':
    unittest.main()