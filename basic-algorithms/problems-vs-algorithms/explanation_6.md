
# Problem 6: Unsorted Integer Array

This problem does not require any sorting algorithm and is performed in `O(n)` time complexity with `O(1)` space complexity. The solution is fairly straight forward. You simply save the first integer as both the `max_val` and the `min_val`, then iterate through each number in the array to the saved value. If the number is smaller then `min_val`, it then gets saved as the new `min_val`, if the number is larger than the `max_val`, this number gets saved as the new `max_val`. After iterating through the array once (i.e. `O(n)`), we have the largest and smallest values in the array, and did not need to sort the array in any way to get our answer.

