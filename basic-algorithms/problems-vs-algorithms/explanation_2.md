
# Problem 2: Search in a Rotated Sorted Array

The solution to this problem is just a modified version of binary search, since binary search is done in `O(log(n))` time. I use binary search to first find the pivot point (the index where the lowest integer is found, which was the first item in the sorted list before being rotated). This pivot is found in `O(log(n))`. Once we find the pivot, we compare the target number to the first item in the array. Knowing that the array is a rotated sorted array, if the target is larger or equal to the first item of this array, then we know it lies in the sub array to the left of the pivot, otherwise it lies in the sub array starting at the pivot and ending at the last item of the array. Knowing which sub array to look in, we then do a second binary search in this specific sub array to find the target number index, or return -1 otherwise.

By simply trackig the start and end index and adjusting these variables to search in the proper sub array of the given `input_list`, we keep the space complexity at a constant time of `O(1)`. We could have saved each sub array in their own variables to make the code a bit more readable, but at large numbers of n, that would add `O(n)` space complexity.

Although we're doing binary search twice, performing two `O(log n)` operations sequentially is still `O(log n)`, since constant factors are ignored in Big O notation.
