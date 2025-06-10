# Problem 6: Union and Intersection of Two Linked Lists

The task for this problem is to fill out the union and intersection functions. The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. For example, the union of A = [1, 2] and B = [3, 4] is [1, 2, 3, 4].

The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both sets A and B. For example, the intersection of A = [1, 2, 3] and B = [2, 3, 4] is [2, 3].

The code can take in two linked lists and return a new linked list that is composed of either the union or intersection, respectively.

Time and Space Efficiency for both functions use the following variables

- **n** = length of first LinkedList
- **m** = length of second LinkedList
- **u** = number of unique elements in both LinkedLists
- **i** = number of intersection elements

## Union Function

### Reasoning Behind Decisions:

For the `union` function, I aimed to combine two sets into one, ensuring that all elements are unique and no duplicates exist. I chose set operations because they're efficient and clearly express the intent of merging collections without repetition. This approach also leverages built-in language features, making the code more readable and maintainable. By looping through both LinkedLists and adding to the same `union_set` rather than creating two seperate sets and creating a union between them removes additional processing needed in creating the union of two sets.

Also worth noting, I'm tracking the tail in our LinkedList which improves the LinkedList append function to work with a time efficiency of $O(1)$ rather than $O(n)$ for every append if tail is not tracked. This affects both the `union` and the `interseciton` function equally.

### Time Efficiency:

Time Complexity is: $O(n + m + u)$.

- Traversing both LinkedLists is done in $O(n + m)$. 
- Inserting into a set happens in $O(1)$ per operation
- Appending each unique value from this set to the `union_linked_list` is $O(u)$

### Space Efficiency:

Space Complexity is $O(u)$ extra space for the union function.


## Intersection Function

### Reasoning Behind Decisions:

By converting both linked lists to sets, we enable fast $O(1)$ average-time lookups and efficient set intersection operations. This avoids nested loops, which would be $O(n \times m)$. Each list is traversed only once to build the sets, keeping traversal time at $O(n + m)$. The set intersection operation is $O(\min(n, m))$, much faster than comparing every element in both LinkedLists. Only intersecting elements are appended to the result list, which is $O(i)$, where $i$ is the number of intersection elements.

In the end, storing both sets requires $O(n + m)$ extra space, but this is necessary for the time efficiency gained.

### Time Efficiency:

Time complexity is: $O(n + m +i)

- Traverse both lists: $O(n + m)$
- Set intersection: $O(min(n,m))$
- Appending each intersecting value: $O(i)$, where **i** is the number of intersection elements between the two linked lists

### Space Efficiency:

Space Complexity is: $O(n + m)$
