
# Problem 7: Request Routing in a Web Server with a Trie

## Reasoning Behind the Design

- **Trie Data Structure:**  
	The code uses a Trie (prefix tree) to efficiently store and retrieve URL route handlers. This is because many routes share common prefixes (e.g., `/home`, `/home/about`), and a Trie avoids redundant storage and speeds up lookups by traversing only the relevant path segments.

- **Separation of Concerns:**  
	The solution separates the logic into three classes:  
	- `RouteTrieNode` for individual path segments,  
	- `RouteTrie` for managing the tree structure and handler storage,  
	- `Router` for user-facing operations like adding and looking up handlers.  
	This modularity makes the code easier to maintain and extend.

- **Handler Assignment:**  
	Handlers are only assigned to nodes that represent complete, valid routes. This ensures that partial matches (e.g., `/home` when only `/home/about` is registered) do not return incorrect handlers.

- **Path Normalization:**  
	The `split_path` method ensures that paths are split into segments and that trailing slashes or empty paths are handled consistently, so `/about` and `/about/` are treated the same.

- **Not Found Handler:**  
	If a route is not found, a default "not found" handler is returned, providing a clear response for invalid paths.

---

### Efficiency

- **Time Complexity:**  
	- **Insert (add_handler):** O(L), where L is the number of segments in the path. Each segment is processed once.
	- **Lookup:** O(L), for the same reason, each segment is checked in sequence.
	- Both operations are very efficient, even for large numbers of routes.

- **Space Complexity:**  
	- O(N * L), where N is the number of unique routes and L is the average number of segments per route.  
	- The Trie structure is space-efficient because shared prefixes are only stored once, reducing redundancy.

---

### Summary

- The Trie-based approach is chosen for its efficiency and suitability for hierarchical path matching.
- The code is modular, robust to edge cases, and efficient in both time and space.
- This design is scalable and well-suited for web server routing, where fast and memory-efficient path lookups are essential.
