"""
Problem 3: Rearrange Array Elements

Given an input array consisting of only 0, 1, and 2, sort the array in a single 
traversal. You're not allowed to use any sorting function that Python provides.

Note that O(n) does not necessarily mean single-traversal. For e.g. if you 
traverse the array twice, that would still be an O(n) solution but it will not 
count as single traversal.

You should implement the function body according to the sort_012 function 
signature. Use the test cases provided below to verify that your algorithm is 
correct. If necessary, add additional test cases to verify that your algorithm 
works correctly.
"""

def sort_012(input_list: list[int]) -> list[int]:
    """
    Sort an array consisting only of 0s, 1s, and 2s in a single traversal.

    This function uses the Dutch National Flag algorithm to sort the array in-place.

    Args:
    input_list (list[int]): A list of integers where each integer is either 0, 1, or 2.

    Returns:
    list[int]: The sorted list with all 0s, followed by all 1s, and then all 2s.
    """
    # Validate input_list is a list
    if not isinstance(input_list, list):
        raise TypeError("input_list must be of type list.")

    # Validate all elements in input_list are integers
    if not all(isinstance(x, int) for x in input_list):
        raise ValueError("All elements in input_list must be integers.")
    
    # Validate that all int in the list are either 0, 1, or 2
    if not all(x in (0,1,2) for x in input_list):
        print("There is an element that is not 0, 1, or 2")

    index_0 = 0
    front_index = 0
    index_2 = len(input_list) - 1

    while front_index <= index_2:
        if input_list[front_index] == 0:
            input_list[index_0], input_list[front_index] = input_list[front_index], input_list[index_0]
            index_0 += 1
            front_index += 1
        elif input_list[front_index] == 1:
            front_index += 1
        else:  # input_list[front_index] == 2
            input_list[front_index], input_list[index_2] = input_list[index_2], input_list[front_index]
            index_2 -= 1

    return input_list


def test_function(test_case: list[int]) -> None:
    """
    Test the sort_012 function with a given test case.

    Args:
    test_case (list[int]): A list containing one element:
        - A list of integers where each integer is either 0, 1, or 2, 
          representing the input array to be sorted.

    Returns:
    None: Prints the sorted array and "Pass" if the output from sort_012 
    matches the sorted input array, otherwise prints "Fail".
    """
    sorted_array: list[int] = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

if __name__ == "__main__":
    # Edge case: Empty input list
    test_function([])
    # Expected output: Pass

    # Edge case: Only two numbers in list
    test_function([2,0])
    # Expected output: Pass

    # Normal case: Mixed elements
    test_function([0, 1, 2, 0, 1, 2])
    # Expected output: Pass

    # Normal case: Already sorted list
    test_function([0, 0, 1, 1, 2, 2])
    # Expected output: Pass

    # Normal case: Reverse sorted list
    test_function([2, 2, 1, 1, 0, 0])
    # Expected output: Pass

    # Edge case: Not all elements are 0, 1, or 2
    test_function([1,0,2,9,0])
    # Expected output: Fail - and "There is an element that is not 0, 1, or 2"

    # Array of edge cases that should all raise an error
    err_val = [
        12,
        [0,None, "string"]
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