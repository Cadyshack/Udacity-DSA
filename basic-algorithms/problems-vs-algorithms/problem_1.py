"""
Problem 1: Square Root of an Integer

In this problem, you need to find the square root of a given integer without using 
any Python libraries. You should return the floor value of the square root.

Below is a function signature that serves as a starting point for your implementation. 
Your task is to complete the body of the function. Additionally, some test cases are 
provided to help you verify the correctness of your implementation. If necessary, add 
test cases to verify that your algorithm is working properly.

The expected time complexity is O(log(n)).
"""

def sqrt(number: int) -> int:
    """
    Calculate the floored square root of a number

    Args:
    number(int): Number to find the floored square root

    Returns:
    int: Floored square root
    """
    if number == 0:
        return 0
    elif number in [1, 2, 3] :
        return 1
    else:
        start = 0
        end = number
        
        while start <= end:
            mid = (start + end) // 2
            floor_value = mid ** 2
            ceiling_value = (mid + 1) ** 2
            if floor_value <= number < ceiling_value:
                return mid
            elif floor_value > number:
                end = mid
            else:   # floor_value < number
                start = mid

    return -1

if __name__ == "__main__":
    # Test cases
    print("Pass" if 3 == sqrt(9) else "Fail")   # Expected Output: Pass
    print("Pass" if 0 == sqrt(0) else "Fail")   # Expected Output: Pass
    print("Pass" if 4 == sqrt(16) else "Fail")  # Expected Output: Pass
    print("Pass" if 1 == sqrt(1) else "Fail")   # Expected Output: Pass
    print("Pass" if 5 == sqrt(27) else "Fail")  # Expected Output: Pass
    print("Pass" if 1 == sqrt(3) else "Fail")  # Expected Output: Pass
    print("Pass" if 2 == sqrt(4) else "Fail")  # Expected Output: Pass
    print("Pass" if 3162 == sqrt(10000001) else "Fail") # Expected Output: Pass

