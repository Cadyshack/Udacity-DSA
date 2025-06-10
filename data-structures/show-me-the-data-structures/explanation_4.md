
# Problem 4: Active Directory

In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such. Where User is represented by str representing their ids. Our function needs to efficiently look up whether the user is in a group or any sub-group belonging to the group.

## Reasoning Behind Decisions

The problem requires efficiently checking if a user exists in a group or any of its subgroups, which can be arbitrarily nested. To solve this, I implemented a `Group` class that supports adding users and subgroups, and an `is_user_in_group` function that uses an iterative depth-first search (DFS) to traverse the group hierarchy. This approach avoids recursion depth issues and is robust for deeply nested structures. This solution is both time- and space-efficient, leveraging set membership for fast user checks and an iterative DFS for robust traversal of the group hierarchy.

## Time Efficiency
Time Efficiency is $O(G)$

- **User Lookup:** Users are stored in a set, so checking if a user is in a group is O(1) on average.
- **Traversal:** In the worst case, the function may need to visit every group and check each group's user set. If there are G groups and U users per group, the worst-case time complexity is $O(G)$, since user lookup is $O(1)$ and each group is visited once.
- **Overall:** The approach is efficient for both shallow and deeply nested group structures, and scales well with the number of users per group due to set-based lookup.

## Space Efficiency
Space Efficiency is $$

- **Data Structure:** Each group stores its users in a set and its subgroups in a list. The space required is $O(G + U)$, where **G** is the number of groups and **U** is the total number of users across all groups.
- **Search Stack:** The iterative DFS uses a stack that, in the worst case, can grow to $O(G)$ if all groups are nested linearly. However, this is generally much smaller in practice.

