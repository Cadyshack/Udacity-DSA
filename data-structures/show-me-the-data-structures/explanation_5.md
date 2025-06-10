# Problem 5: Blockchain

A Blockchain is a sequential chain of records, similar to a linked list. Each block contains some information and how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created, and text strings as the data.

## Reasoning Behind Decisions:

A Python list is utilized to store the blocks, offering $O(1)$ time complexity for appending new blocks and efficient sequential access, which aligns with the append-only characteristic of blockchains. Each block encapsulates a UTC timestamp for consistency, the transaction data, the hash of the previous block, and its own hash. This structure ensures both the integrity and immutability of the blockchain. The SHA-256 algorithm is employed for cryptographic security, making it computationally impractical to alter the chain, while the genesis block is initialized with a previous hash value of "0", thereby establishing the starting point of the blockchain.

## Time Efficiency:

Time Efficiency is in $O(1)$
Both `add_block(data)` and `create_genesis_block(data)` are done in constant time of $O(1)$, with the most expensive coming from the `__repr__` method which itterates through all blocks in linear time of $O(n)$ but this isn't taken into consideration since it is only there for our purposes and does not affect anything when creating a Blockchain.

## Space Efficiency:

Space Complexity is in $O(n)$, where **n** represents the number of blocks in the blockchain.
Each block is stored in a list, so for n blocks, space is $O(n)$
Each block stores its own data, timestamp, previous_hash, and hash, all of which are $O(1)$ per block (assuming data is not arbitrarily large)