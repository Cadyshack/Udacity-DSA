# Huffman Coding Implementation

This project implements a complete Huffman coding solution in Python for data compression and decompression.

## Reasoning Behind Decisions:

Given the nature of Huffman Coding, I chose to use a min-heap as the priority queue (using Python heapq library), since it adds additional efficiency when building a Huffman Tree. The list comprehension creates the heap structure in one pass, while we get $O(1)$ access to lowest frequency character since the root always contains the minimum frequency character, providing constant-time access to highest-priority item (lower values = higher priority). The full reasoning between using a min-heap .vs a sorted list is as follows:

### Min-Heap: (n is number of unique characters)

- where **k** is number of unique characters
- Insert: $O(\log(k))$
- Extract minimum: $O(\log(k))$
- Build initial heap: $O(k)$
- Min-Heap Overall Total Complexity: $O(k\log(k))$

### Sorted List:

- Where **k** is number of unique characters
- Insert: $O(k)$ - requires finding position and shifting elements
- Extract minimum: $O(1)$ - just pop from front
- Build initial sorted list: $O(k\log(k))$
- Sorted List total overall complexity: $O(k^2)$

In conclusion, min-heap is significantly more efficient for Huffman tree construction ( $O(k\log(k))$ ) compared to using a sorted list ( $O(k^2)$ ), since the cost of reorganizing after each insertion becomes prohibitive if using a sorted list. The min-heap approach scales much better as the number of unique characters increases.

## Time Efficiency:

Time Efficiency is $O(n + k\log(k))$

- **n** represents the length of the string to be encoded
- **k** represents the number of unique characters in the string

## Space Efficiency:

Space Efficiency is $O(k)$

- **k** represents the number of unique characters in the string