import heapq
import sys
from collections import defaultdict
from typing import Optional, Any

# Huffman Tree Node
class HuffmanNode:
    """
    A class to represent a node in the Huffman Tree.

    Attributes:
    -----------
    char : Optional[str]
        The character stored in the node.
    freq : int
        The frequency of the character.
    left : Optional[HuffmanNode]
        The left child node.
    right : Optional[HuffmanNode]
        The right child node.
    """

    def __init__(self, freq: int, char: Optional[str] = None, left: Optional['HuffmanNode'] = None, right: Optional['HuffmanNode'] = None) -> None:
        """
        Constructs all the necessary attributes for the HuffmanNode object.

        Parameters:
        -----------
        char : Optional[str]
            The character stored in the node.
        freq : int
            The frequency of the character.
        """
        self.freq = freq
        self.char = char
        self.left = None
        self.right = None
    
    # set a node for the left child
    def set_left_child(self,left) -> None:
        self.left = left
    
    # set a node for the right child
    def set_right_child(self, right) -> None:
        self.right = right
    
    # get the node of left child
    def get_left_child(self) -> Optional['HuffmanNode']:
        return self.left
    
    # get the node of right child
    def get_right_child(self) -> Optional['HuffmanNode']:
        return self.right

    def is_leaf(self) -> bool:
        return self.left is None and self.right is None

    def __lt__(self, other: 'HuffmanNode') -> bool:
        """
        Less-than comparison operator for HuffmanNode.

        Parameters:
        -----------
        other : HuffmanNode
            The other HuffmanNode to compare with.

        Returns:
        --------
        bool
            True if the frequency of this node is less than the other node, False otherwise.
        """
        return self.freq < other.freq
    
    def __str__(self) -> str:
        return f"Node({(self.freq, self.char)})"
    
    def __repr__(self) -> str:
        return f"Node({(self.freq, self.char)})"

def calculate_frequencies(data: str) -> dict[str, int]:
    """
    Calculate the frequency of each character in the given data.

    Parameters:
    -----------
    data : str
        The input string for which frequencies are calculated.

    Returns:
    --------
    Dict[str, int]
        A dictionary with characters as keys and their frequencies as values.
    """
    d = defaultdict(int)
    for char in data:
        d[char] += 1
    
    return d
    
def build_huffman_tree(frequency: dict[str, int]) -> HuffmanNode:
    """
    Build the Huffman Tree based on the character frequencies.

    Parameters:
    -----------
    frequency : Dict[str, int]
        A dictionary with characters as keys and their frequencies as values.

    Returns:
    --------
    HuffmanNode
        The root node of the constructed Huffman Tree.
    """
    # Create HuffmanNode for each dictionary item
    pq = [HuffmanNode(freq, char) for char, freq in frequency.items()]
    # Convert to a heap in O(k) time
    heapq.heapify(pq)

    while len(pq) > 1:
        node_1 = heapq.heappop(pq)
        node_2 = heapq.heappop(pq)
        new_freq = node_1.freq + node_2.freq
        new_node = HuffmanNode(new_freq)

        if node_1.freq <= node_2.freq:
            new_node.set_left_child(node_1)
            new_node.set_right_child(node_2)
        else:
            new_node.set_left_child(node_2)
            new_node.set_right_child(node_1)

        heapq.heappush(pq, new_node)
    
    # Return the root node of the Huffman Tree
    return heapq.heappop(pq)

def generate_huffman_codes(node: Optional[HuffmanNode], code: str, huffman_codes: dict[str, str]) -> dict[str,str]:
    """
    Generate Huffman codes for each character by traversing the Huffman Tree.

    Parameters:
    -----------
    node : Optional[HuffmanNode]
        The current node in the Huffman Tree.
    code : str
        The current Huffman code being generated.
    huffman_codes : Dict[str, str]
        A dictionary to store the generated Huffman codes.
    """
    
    if node:
        if node.is_leaf() and node.char is not None:
            # Special case: if this is the root node and it's a leaf (single character case)
            # assign it a code of "0" to ensure it has a code
            if code == "":  # This means we're at the root
                huffman_codes[node.char] = "0"
            else:
                huffman_codes[node.char] = code
        else:
            code_left = code + "0"
            generate_huffman_codes(node.left, code_left, huffman_codes)
            code_right = code + "1"
            generate_huffman_codes(node.right, code_right, huffman_codes)
    
    return huffman_codes
            
def huffman_encoding(data: str) -> tuple[str, Optional[HuffmanNode]]:
    """
    Encode the given data using Huffman coding.

    Parameters:
    -----------
    data : str
        The input string to be encoded.

    Returns:
    --------
    Tuple[str, Optional[HuffmanNode]]
        A tuple containing the encoded string and the root of the Huffman Tree.
    """
    # Special case: given an empty string to encode
    if not data:
        return ("", None)
    
    frequency_dict = calculate_frequencies(data)
    # Special case: if there's only one unique character
    if len(frequency_dict) == 1:
        char = list(frequency_dict.keys())[0]
        # Create a single node tree
        tree = HuffmanNode(frequency_dict[char], char)
        # Encode using "0" for each occurrence of the character
        encoded_string = "0" * len(data)
        return (encoded_string, tree)

    tree = build_huffman_tree(frequency_dict)
    huffman_codes = generate_huffman_codes(tree, "", {})

    encoded_string = ""
    for char in data:
        encoded_string += huffman_codes[char]

    return (encoded_string, tree)

def huffman_decoding(encoded_data: str, tree: Optional[HuffmanNode]) -> str:
    """
    Decode the given encoded data using the Huffman Tree.

    Parameters:
    -----------
    encoded_data : str
        The encoded string to be decoded.
    tree : Optional[HuffmanNode]
        The root of the Huffman Tree used for decoding.

    Returns:
    --------
    str
        The decoded string.
    """
    if not encoded_data or tree is None:
        return ""
    
    # Special case: single character tree (root is a leaf)
    if tree.is_leaf():
        # Each "0" in the encoded data represents one occurrence of the character
        return tree.char * len(encoded_data) if tree.char else ""
    
    decoded: str = ""
    node = tree

    for code in encoded_data:
        if code == "0":
            node = node.get_left_child() if node else None
        elif code == "1":
            node = node.get_right_child() if node else None
        
        if node and node.is_leaf():
            if node.char is not None:
                decoded += node.char
            node = tree

    return decoded

# Main Function
if __name__ == "__main__":
    # Test Case 1: Standard test case
    print("\nTest Case 1: Standard sentence 2")
    a_great_sentence = "The bird is the word"

    print(f"The size of the data is: {sys.getsizeof(a_great_sentence)}")
    print(f"The content of the data is: {a_great_sentence}")

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print(f"The size of the encoded data is: {sys.getsizeof(int(encoded_data, base=2))}")
    print(f"The content of the encoded data is: {encoded_data}")

    decoded_data = huffman_decoding(encoded_data, tree)

    print(f"The size of the decoded data is: {sys.getsizeof(decoded_data)}")
    print(f"The content of the encoded data is: {decoded_data}")

    # Test Case 2
    print("\nTest Case 2: Testing empty string input")
    # Edge case: empty string
    encoded, tree = huffman_encoding("")
    assert encoded == ""
    decoded = huffman_decoding(encoded, tree)
    assert decoded == "", f"Failed: expected an empty string"

    # Test Case 3
    print("\nTest Case 3: single character encoding")
    s = "aaaaaa"
    encoded, tree = huffman_encoding(s)
    print(f"encoded is: {encoded}")
    decoded = huffman_decoding(encoded, tree)
    assert decoded == s, f"Failed: test 3, encoded = {encoded}, decoded = {decoded}"

    # Test Case 4
    print("\nTest Case 4: Long string")
    s = "abcde" * 10000
    encoded, tree = huffman_encoding(s)
    assert len(encoded) > 0
    decoded = huffman_decoding(encoded, tree)
    assert decoded == s, f"Failed: Test Case 4 using a long string failed"