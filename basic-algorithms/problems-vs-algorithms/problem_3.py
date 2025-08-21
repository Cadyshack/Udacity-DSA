"""
Problem 3: Rearrange Array Elements

Rearrange Array Elements so as to form two number such that their sum is 
maximum. Return these two numbers. You can assume that all array elements are 
in the range [0, 9]. The number of digits in both the numbers cannot differ by 
more than 1. You're not allowed to use any sorting function that Python 
provides and the expected time complexity is O(nlog(n)).

You should implement the function body according to the rearrange_digits 
function signature. Use the test cases provided below to verify that your 
algorithm is correct. If necessary, add additional test cases to verify that 
your algorithm works correctly.
"""

def rearrange_digits(input_list: list[int]) -> tuple[int, int]:
    """
    Rearrange the digits of the input list to form two numbers such that their 
    sum is maximized.

    This function sorts the input list in descending order and then alternates 
    the digits to form two numbers.

    Args:
    input_list (list[int]): A list of integers to be rearranged.

    Returns:
    tuple[int, int]: A tuple containing two integers formed by rearranging the 
    digits of the input list.
    """
    # Validate input_list is a list
    if not isinstance(input_list, list):
        raise TypeError("input_list must be of type list.")

    # Validate all elements in input_list are integers
    if not all(isinstance(x, int) for x in input_list):
        raise ValueError("All elements in input_list must be integers.")

    n = len(input_list)
    if n == 0:
        return (0, 0)
    elif n == 1:
        return (input_list[0], 0)
    
    # Start index represents the last non-leaf node, rather than start at n, since nodes beyond this point are leaves and already satidfy the heap property.
    start_index = (n // 2) - 1

    # Build a minheap
    for i in range(start_index, -1, -1):
        heapify(input_list, n, i)

    # Extract minimum number then heapify one by one to create sorted descending order list
    for i in range(n-1, 0, -1):
        input_list[i], input_list[0] = input_list[0], input_list[i]
        heapify(input_list, i, 0)
    
    num1: str | int = ""
    num2: str | int = ""
    for i in range(0, len(input_list)):
        if i % 2 == 0:
            num1 += str(input_list[i])
        else:
            num2 += str(input_list[i])
    
    return (int(num1), int(num2))


def heapify(arr: list[int], n: int, i: int) -> None:

    min_index = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and abs(arr[i]) > abs(arr[left_child]):
        min_index = left_child

    if right_child < n and abs(arr[min_index]) > abs(arr[right_child]):
        min_index = right_child

    if min_index != i:
        arr[i], arr[min_index] = abs(arr[min_index]), abs(arr[i])
        heapify(arr, n, min_index)

def test_function(test_case: tuple[list[int], list[int]]) -> None:
    """
    Test the rearrange_digits function with a given test case.

    Args:
    test_case (tuple[list[int], list[int]]): A tuple containing two elements:
        - A list of integers representing the input array to be rearranged.
        - A list of two integers representing the expected output.

    Returns:
    None: Prints "Pass" if the sum of the output from rearrange_digits matches 
    the sum of the expected output, otherwise prints "Fail".
    """
    output: tuple[int, int] = rearrange_digits(test_case[0])
    solution: list[int] = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")
        

if __name__ == '__main__':
    # Edge case: Single element list
    test_function(([9], [9, 0]))
    # Expected output: Pass

    # Normal case: Mixed positive and negative numbers
    test_function(([3, -2, 1, -4, 5], [531, 42]))
    # Expected output: Pass

    # Normal case: list with zeros
    test_function(([0, 0, 0, 0, 0], [0, 0]))
    # Expected output: Pass

    # Normal case: list with repeated numbers
    test_function(([2, 2, 2, 2, 2], [222, 22]))
    # Expected output: Pass

    test_function(([], [0, 0]))
    # Expected output: Pass

    # Array of edge cases that should all raise an error that are run in the try
    err_val = [
        ([None], [0, 0]),
        ([1, "2", 3, 4, 5], [531, 42]),
        (984, [94,8])
    ]

    # Run through the edge cases and print out the error message for each to confirm proper error handling
    for edge_case in err_val:
        try:
            test_function(edge_case)
            print(f"Pass: {edge_case} did not raise an error and passed the test")
        except ValueError as e:
            print(f"Input {edge_case}: Failed with ValueError - {e}")
        except TypeError as e:
            print(f"Input {edge_case}: Failed with TypeError - {e}")