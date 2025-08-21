"""
Problem 2: Search in a Rotated Sorted Array

You are given a sorted array that has been rotated at a random pivot point. 
For example, [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2].

You are also given a target value to search for. If the target is found in the 
array, return its index; otherwise, return -1. Assume there are no duplicates 
in the array, and the runtime complexity of your algorithm must be O(log n).

You should implement the function body according to the rotated_array_search 
function signature. Use the test cases provided below to verify that your 
algorithm is correct. If necessary, add additional test cases to verify that 
your algorithm works correctly.
"""

def rotated_array_search(input_list: list[int], number: int) -> int:
    """
    Find the index by searching in a rotated sorted array

    Args:
    input_list (list[int]): Input array to search
    number (int): Target number to find

    Returns:
    int: Index of the target number or -1 if not found
    """
    
    # Validate input_list is a list
    if not isinstance(input_list, list):
        raise TypeError("input_list must be of type list.")

    # Validate all elements in input_list are integers
    if not all(isinstance(x, int) for x in input_list):
        raise ValueError("All elements in input_list must be integers.")

    # Validate number is an integer
    if not isinstance(number, int):
        raise TypeError("number must be an integer.")
    
    if len(input_list) == 0:
        return -1

    low = 0
    high = len(input_list) - 1
    while low < high:
        mid = (low + high) // 2
        if input_list[mid] > input_list[high]:
            low = mid + 1
        else:
            high = mid
    
    # low is now set to the index of the smallest int a.k.a the pivot index
    pivot = low
    start = 0
    end = len(input_list) - 1
    
    if number >= input_list[0]:
        # the target is in the left sub array
        end = pivot
    else:
        start = pivot

    while start <= end:
        mid = (start + end) // 2
        mid_num = input_list[mid]

        if number == mid_num:
            return mid
        elif number < mid_num:
            end = mid - 1
        else:
            start = mid + 1
    
    return -1

# Test function using provided test cases
def test_function(test_case: tuple[list[int], int]) -> None:
    """
    Test the rotated_array_search function with a given test case.

    Args:
    test_case (list[list[int], int]): A list containing two elements:
        - A list of integers representing the input array to search.
        - An integer representing the target number to find.

    Returns:
    None: Prints "Pass" if the rotated_array_search function returns the same 
    result as the linear_search function, otherwise prints "Fail".
    """
    input_list: list[int] = test_case[0]
    number: int = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

def linear_search(input_list: list[int], number: int) -> int:
    """
    Perform a linear search for a target number in a list of integers.

    Args:
    input_list (list[int]): The list of integers to search through.
    number (int): The target number to find in the list.

    Returns:
    int: The index of the target number if found, otherwise -1.
    """
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

if __name__ == '__main__':
    # Edge case: Empty input list
    test_function(([], 5))
    # Expected output: Pass

    # Normal case: Number at the beginning of the list
    test_function(([4, 5, 6, 7, 0, 1, 2], 4))
    # Expected output: Pass

    # Normal case: Number at the end of the list
    test_function(([4, 5, 6, 7, 0, 1, 2], 2))
    # Expected output: Pass

    # Normal case: Number in the middle of the list
    test_function(([4, 5, 6, 7, 0, 1, 2], 6))
    # Expected output: Pass

    test_function(([10, 11, 12, 13, 14, 15, 16, 5, 6, 7, 8], 9))
    # Expected output: Pass

    test_function(([0, 1, 2, 3, 4, 5, 6, -5, -4, -3, -2, -1], -3))
    # Expected output: Pass

    test_index = rotated_array_search([0, 1, 2, 3, 4, 5, 6, -5, -4, -3, -2, -1], -3)
    print(f"test value is: {test_index}")
    # Expected ouput: "test value is: 9"

    # Array of edge cases that should all raise an error
    err_val = [
        ([None], 8),
        ([4,5,6,0,1,2], None),
        ([4,5,"6",0,1,2], 1)
        ]
    
    # Run through the array of edge cases and print out the raised error for each to validate proper error handling
    for edge_case in err_val:
        try:
            test_function(edge_case)
            print(f"Pass: {edge_case} did not raise an error and passed the test")
        except ValueError as e:
            print(f"Input {edge_case}: Failed with ValueError - {e}")
        except TypeError as e:
            print(f"Input {edge_case}: Failed with TypeError - {e}")