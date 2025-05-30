from collections import OrderedDict
from typing import Any, Optional

class LRU_Cache:
    """
    A class to represent a Least Recently Used (LRU) cache.

    Attributes:
    -----------
    capacity : int
        The maximum number of items the cache can hold.
    cache : OrderedDict[int, Any]
        The ordered dictionary to store cache items.
    """

    def __init__(self, capacity: int) -> None:
        """
        Initializes the LRU_Cache with a given capacity.

        Parameters:
        -----------
        capacity : int
            The maximum number of items the cache can hold.
        """
        self.capacity = capacity
        self.cache : OrderedDict[int, Any] = OrderedDict()


    def get(self, key: int) -> Optional[Any]:
        """
        Get the value of the key if the key exists in the cache, otherwise return -1.

        Parameters:
        -----------
        key : int
            The key to be accessed in the cache.

        Returns:
        --------
        Optional[Any]
            The value associated with the key if it exists, otherwise -1.
        """
        if key not in self.cache:
            return -1
        else:
            # Move the accessed item to the end of the OrderedDict to mark it as recently used
            self.cache.move_to_end(key)
            return self.cache[key]
        

    def set(self, key: int, value: Any) -> None:
        """
        Set or insert the value if the key is not already present. When the cache reaches 
        its capacity, it should invalidate the least recently used item before inserting 
        a new item.

        Parameters:
        -----------
        key : int
            The key to be inserted or updated in the cache.
        value : Any
            The value to be associated with the key.
        """
        if self.capacity <= 0:
            # Should consider raising an exception in the __init__ method anytime someone sets capacity to 0
            return
        if key in self.cache:
            # Update the value and mark it as recently used
            self.cache.move_to_end(key)
            self.cache[key] = value
        else:
            if len(self.cache) >= self.capacity:
                # Remove the first (least recently used) item from the cache
                self.cache.popitem(last=False)
            # Insert the new key-value pair
            self.cache[key] = value


if __name__ == '__main__':
    # Testing the LRU_Cache class

    # Test Case 1: Basic functionality
    our_cache = LRU_Cache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    assert our_cache.get(1) == 1, "Failed: Expected 1 to be returned for key 1"
    assert our_cache.get(2) == 2, "Failed: Expected 2 to be returned"
    assert our_cache.get(9) == -1, "Failed: Expected -1 because 9 is not in the cache"
    our_cache.set(5, 5)
    our_cache.set(6, 6)  # This should evict key 3
    assert our_cache.get(3) == -1, "Failed: Expected -1 returned since 3 was evicted"  # Returns -1, 3 was evicted
    print("Test Case 1 Passed: Handling basic functionality")

    # Test Case 2: Edge case - Cache with capacity 0 and None values
    edge_cache = LRU_Cache(0)
    edge_cache.set(1, None)  # Should not store anything due to 0 capacity
    assert edge_cache.get(1) == -1, "Failed: Expected -1 returned due to 0 capacity"
    edge_cache = LRU_Cache(1)
    edge_cache.set(1, None)  # Testing None as value
    assert edge_cache.get(1) == None, "Failed: Expected None for key 1"  # Should return None
    edge_cache.set(2, "test")  # Should evict key 1
    assert edge_cache.get(1) == -1, "Failed: Expected -1, since key 1 should have been evicted"
    assert edge_cache.get(2) == "test", "Failed: Expected the string 'test' for key 2" # Should return string value
    print("Test Case 2 Passed: Handling edge case cache with capacity 0 and None values")

    # Test Case 3: Large number of operations
    large_cache = LRU_Cache(3)
    # Test with large numbers
    large_cache.set(1000000, "large_key")
    large_cache.set(2000000, "larger_key")
    large_cache.set(3000000, "largest_key")
    assert large_cache.get(1000000) == "large_key", "Failed: Expected the string 'large_key'"
    large_cache.set(4000000, "new_key") # Add a new item to trigger eviction
    # 2000000 should be evicted since 1000000 was recently accessed
    assert large_cache.get(2000000) == -1, "Failed: Expected -1 returned"
    assert large_cache.get(1000000) == "large_key", "Failed: Expected 'large_key' string returned"
    assert large_cache.get(3000000) == "largest_key", "Failed: Expected 'largest_key' string returned"
    assert large_cache.get(4000000) == "new_key", "Failed: Expected 'new_key' string returned"
    large_value = 10**18  # A very large value
    large_cache.set(1, large_value) # testing adding a very large value
    assert large_cache.get(1) == large_value, f"Failed: Expected {large_value} returned"
    print("Test Case 3 Passed: Handling large number of operations")