
## Reasoning Behind Decisions:

The implementation uses Python's `OrderDict` data structure, which is used to mimic a type of Queue with it's FIFO approach. This is ideal because, internally, an OrderDict uses a combination of a regular dictionary (for fast lookups) and a doubly linked list (to maintain the order). This provides `O(1)` time complexity for insertion, deletions, and lookups while preserving the order of elements. The built-in methods `move_to_end()` and  `popitem()` can easily be used to implement a First In, First Out approach that satisfies our LRU cache needs.

## Time Efficiency:

All operations in the LRU Cache have `O(1)` time complexity.

- **Get Operation**: O(1)
  - Dictionary lookup is O(1)
  - Moving item to end using `move_to_end()` is O(1)
- **Set Operation**: O(1)
  - Dictionary insertion/update is O(1)
  - Removing least recently used item with `popitem()` is O(1)
  - Moving existing items to end is O(1)

## Space Efficiency:

The space complexity is `O(n)` where `n` is the capacity of the cache:

- The cache stores at most `capacity` number of key-value pairs
- Each entry in the OrderedDict contains:
  - The key (integer)
  - The value (any type)
  - Internal pointers for the doubly-linked list
