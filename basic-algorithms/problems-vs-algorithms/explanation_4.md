
# Problem 4: Dutch National Flag Problem

To solve the Dutch National Flag Problem, we implemented the Dutch National Flag algorithm. The Dutch National Flag algorithm is a classic algorithm proposed by Edsger Dijkstra. Its purpose is to sort an array containing three distinct elements (0, 1, and 2 in our case) in a single pass, efficiently grouping all elements of the same kind together. The algorithm works by keeping track of three pointers:

- **index_0**: marks the boundary for the lowest value (i.e 0)
- **front_index**: traverses the array
- **index_2**: marks the boundary for the highest value (i.e. 2)

The main idea is to move all the 0s to the beginning, move all the 2s to the end, and leave all the 1s in the middle. This algorithm sorts the array in-place in a single pass, achieving `O(n)` time complexity and `O(1)`space complexity.
