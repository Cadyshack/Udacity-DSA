from typing import Optional

class Node:
    """
    A class to represent a node in a linked list.

    Attributes:
    -----------
    value : int
        The value stored in the node.
    next : Optional[Node]
        The reference to the next node in the linked list.
    """

    def __init__(self, value: int) -> None:
        """
        Constructs all the necessary attributes for the Node object.

        Parameters:
        -----------
        value : int
            The value to be stored in the node.
        """
        self.value: int = value
        self.next: Optional[Node] = None

    def __repr__(self) -> str:
        """
        Return a string representation of the node.

        Returns:
        --------
        str
            A string representation of the node's value.
        """
        return str(self.value)


class LinkedList:
    """
    A class to represent a singly linked list.

    Attributes:
    -----------
    head : Optional[Node]
        The head node of the linked list.
    """

    def __init__(self) -> None:
        """
        Constructs all the necessary attributes for the LinkedList object.
        """
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def __str__(self) -> str:
        """
        Return a string representation of the linked list.

        Returns:
        --------
        str
            A string representation of the linked list, with nodes separated by " -> ".
        """
        cur_head: Optional[Node] = self.head
        out_string: str = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value: int) -> None:
        """
        Append a new node with the given value to the end of the linked list.

        Parameters:
        -----------
        value : int
            The value to be stored in the new node.
        """
        new_node: Node = Node(value)
        # If the linked list is empty, set the new node as the head
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            if self.tail is None:
                self.tail = self.head
            # If the linked list is not empty, append the new node to the end
            assert self.tail is not None, "Tail should not be None when appending to a non-empty list."
            self.tail.next = new_node
            self.tail = new_node

    def size(self) -> int:
        """
        Calculate the size (number of nodes) of the linked list.

        Returns:
        --------
        int
            The number of nodes in the linked list.
        """
        size: int = 0
        node: Optional[Node] = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1: LinkedList, llist_2: LinkedList) -> LinkedList:
    """
    Compute the union of two linked lists.

    Parameters:
    -----------
    llist_1 : LinkedList
        The first linked list.
    llist_2 : LinkedList
        The second linked list.

    Returns:
    --------
    LinkedList
        A new linked list containing all unique elements from both input linked lists.
    """
    # Use a set to store all unique elements
    union_set = set()
    node_1: Optional[Node] = llist_1.head
    node_2: Optional[Node] = llist_2.head
    # Traverse the first linked list and add elements to the set_union
    while node_1:
        union_set.add(node_1.value)
        node_1 = node_1.next

    # Traverse the second linked list and add elements to set_union
    while node_2:
        union_set.add(node_2.value)
        node_2 = node_2.next

    # Create a new linked list to store the union
    union_linked_list = LinkedList()

    for value in union_set:
        union_linked_list.append(value)

    return union_linked_list

def intersection(llist_1: LinkedList, llist_2: LinkedList) -> LinkedList:
    """
    Compute the intersection of two linked lists.

    Parameters:
    -----------
    llist_1 : LinkedList
        The first linked list.
    llist_2 : LinkedList
        The second linked list.

    Returns:
    --------
    LinkedList
        A new linked list containing all elements that are present in both input linked lists.
    """
    # Use sets to find the intersection
    set_1 = set()
    set_2 = set()

    node_1: Optional[Node] = llist_1.head
    node_2: Optional[Node] = llist_2.head
    # Traverse the first linked list and add elements to the set_1
    while node_1:
        set_1.add(node_1.value)
        node_1 = node_1.next

    # Traverse the second linked list and add elements to set_2
    while node_2:
        set_2.add(node_2.value)
        node_2 = node_2.next

    # Find the intersection of both sets
    intersection_set = set_1 & set_2

    # Create a new linked list to store the intersection
    intersection_linked_list = LinkedList()
    for value in intersection_set:
        intersection_linked_list.append(value)

    return intersection_linked_list

if __name__ == "__main__":
    ## Test case 1
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]
    
    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print("Test Case 1:")
    print("Union:", union(linked_list_1, linked_list_2)) # Expected: 1, 2, 3, 4, 6, 9, 11, 21, 32, 35, 65
    print("Intersection:", intersection(linked_list_1, linked_list_2)) # Expected: 4, 6, 21

    ## Test case 2
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print("\nTest Case 2:")
    print("Union:", union(linked_list_3, linked_list_4)) # Expected: 1, 2, 3, 4, 6, 7, 8, 9, 11, 21, 23, 35, 65
    print("Intersection:", intersection(linked_list_3, linked_list_4)) # Expected: empty

    ## Test case 3
    linked_list_5 = LinkedList()
    linked_list_6 = LinkedList()
    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]

    for i in element_1:
        linked_list_5.append(i)
    for i in element_2:
        linked_list_6.append(i)

    print("\nTest Case 3:")
    print("Union:", union(linked_list_5, linked_list_6)) # Expected: 2, 3, 4, 6, 21, 35, 65
    print("Intersection:", intersection(linked_list_5, linked_list_6)) # Expected: 2, 3, 4, 6, 21, 35, 65

    ## Test case 4
    linked_list_7 = LinkedList()
    linked_list_8 = LinkedList()
    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = []

    for i in element_1:
        linked_list_7.append(i)
    for i in element_2:
        linked_list_8.append(i)

    print("\nTest Case 4:")
    print("Union:", union(linked_list_7, linked_list_8)) # Expected: 2, 3, 4, 6, 21, 35, 65
    print("Intersection:", intersection(linked_list_7, linked_list_8)) # Expected: empty
    ## Test case 5
    linked_list_9 = LinkedList()
    linked_list_10 = LinkedList()
    element_1 = []
    element_2 = []

    for i in element_1:
        linked_list_9.append(i)
    for i in element_2:
        linked_list_10.append(i)

    print("\nTest Case 5:")
    print("Union:", union(linked_list_9, linked_list_10)) # Expected: empty
    print("Intersection:", intersection(linked_list_9, linked_list_10)) # Expected: empty
