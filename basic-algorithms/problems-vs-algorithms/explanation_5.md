
# Problem 5: Autocomplete with Tries

Completing the Jupyter Notebok where we created two classes (TrieNode and Trie), where the TrieNode represents a node in the Trie Tree data structure, also known as a prefix tree. Trie data structures shine when dealing with sequence data, whether it's characters, words, or network nodes. They take much less space then if we were to use a hashmap, which would take `O(1)` time to see if a word exists, but the memory size would then be `O(N * M)`, where **N** is the number of words and **M** is the maximum length of words. Furthermore, a hashmap would not allow us to do any suffix lookup for autocompletion.

The worst case space complexity of a Trie is `O(R * N * M)`, where **N** is the number of words, **M** is the maximum length of a word, while **R** is the numbe of pointers each node can have (i.e. size of alphabet, which is 26 for lowercase English letters). This is the worst case, where no prefix overlap happens, which is not typical. Typically, prefixes are shared which saves space, giving us a time complexity of `O(T)`, where **T** is the total characters in all inserted words.

---

## Efficiency

The time/space complexity of each method in our Trie data structure is as follows:

- **insert**: time complexity = `O(M)`; space complexity = `O(M)`, where **M** is the length of the word being inserted.
- **find**: time complexity = `O(M)`; space complexity = `O(1)`, where **M** is the length of the word being searched.
- **suffixes**: time complexity = `O(K)`; space complexity = `O(K)`, where **K** is the total number of characters in all suffixes found.

In the end using a Trie data structure allows us to do fast prefix-based lookups at the cost of potentially high space usage.
