from typing import List, Union, TypeVar, Optional

T = TypeVar('T', int, str)  # Generic type for integers or strings

class RecursiveBinarySearch:
    @staticmethod
    def binary_search_recursive(arr: List[T], target: T, 
                                low: Optional[int] = None, 
                                high: Optional[int] = None) -> int:
        """
        Perform a recursive binary search to find the index of the target value.
        
        Args:
            arr (List[T]): A sorted array to search 
            target (T): The value to search for
            low (Optional[int]): The lower bound of the search range (default: start of array)
            high (Optional[int]): The upper bound of the search range (default: end of array)
        
        Returns:
            int: Index of the target if found, otherwise -1
        
        Raises:
            ValueError: If the input array is None or empty
            TypeError: If the array is not sorted
        """
        # Error handling for null or empty array
        if arr is None:
            raise ValueError("Array cannot be None")
        
        if not arr:
            raise ValueError("Array cannot be empty")
        
        # Initialize low and high if not provided
        if low is None:
            low = 0
        if high is None:
            high = len(arr) - 1
        
        # Validate sorting (basic check)
        if any(arr[i] > arr[i+1] for i in range(len(arr)-1)):
            raise TypeError("Array must be sorted in ascending order")
        
        # Base case: search range is invalid
        if low > high:
            return -1
        
        # Calculate midpoint
        mid = (low + high) // 2
        
        # Compare target with midpoint element
        if arr[mid] == target:
            return mid
        
        # Recursive cases
        if target < arr[mid]:
            # Search lower half
            return RecursiveBinarySearch.binary_search_recursive(arr, target, low, mid - 1)
        else:
            # Search upper half
            return RecursiveBinarySearch.binary_search_recursive(arr, target, mid + 1, high)
    
    @staticmethod
    def binary_search_all_indices(arr: List[T], target: T) -> List[int]:
        """
        Find all indices of a target value in a sorted array.
        
        Args:
            arr (List[T]): A sorted array to search
            target (T): The value to search for
        
        Returns:
            List[int]: List of all indices where target is found
        """
        if not arr:
            return []
        
        # Find an initial occurrence
        initial_index = RecursiveBinarySearch.binary_search_recursive(arr, target)
        
        if initial_index == -1:
            return []
        
        # Find all indices
        indices = [initial_index]
        
        # Search left
        left = initial_index - 1
        while left >= 0 and arr[left] == target:
            indices.insert(0, left)
            left -= 1
        
        # Search right
        right = initial_index + 1
        while right < len(arr) and arr[right] == target:
            indices.append(right)
            right += 1
        
        return indices

# Demonstration and Testing
def main():
    # Integer array test
    int_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    print("Integer Array Tests:")
    print("Search 5:", RecursiveBinarySearch.binary_search_recursive(int_arr, 5))
    print("Search 11:", RecursiveBinarySearch.binary_search_recursive(int_arr, 11))
    
    # Multiple occurrences test
    repeated_arr = [1, 2, 2, 2, 3, 4, 5]
    print("\nMultiple Occurrences Test:")
    print("All indices of 2:", RecursiveBinarySearch.binary_search_all_indices(repeated_arr, 2))
    
    # String array test
    str_arr = ["apple", "banana", "cherry", "date", "elderberry"]
    
    print("\nString Array Tests:")
    print("Search 'cherry':", RecursiveBinarySearch.binary_search_recursive(str_arr, "cherry"))
    print("Search 'grape':", RecursiveBinarySearch.binary_search_recursive(str_arr, "grape"))

if __name__ == "__main__":
    main()