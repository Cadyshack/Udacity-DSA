class Group:
    """
    A class to represent a group which can contain sub-groups and users.

    Attributes:
    -----------
    name : str
        The name of the group.
    groups : list[Group]
        A list of sub-groups within this group.
    users : list[str]
        A list of users in this group.
    """

    def __init__(self, _name: str) -> None:
        """
        Constructs all the necessary attributes for the Group object.

        Parameters:
        -----------
        _name : str
            The name of the group.
        """
        self.name: str = _name
        self.groups: list[Group] = []
        self.users: set[str] = set()  # Use a set for O(1) lookup

    def add_group(self, group: 'Group') -> None:
        """
        Add a sub-group to this group.

        Parameters:
        -----------
        group : Group
            The sub-group to be added.
        """
        self.groups.append(group)

    def add_user(self, user: str) -> None:
        """
        Add a user to this group.

        Parameters:
        -----------
        user : str
            The user to be added.
        """
        self.users.add(user)

    def get_groups(self) -> list['Group']:
        """
        Get the list of sub-groups in this group.

        Returns:
        --------
        list[Group]
            A list of sub-groups.
        """
        return self.groups

    def get_users(self) -> set[str]:
        """
        Get the list of users in this group.

        Returns:
        --------
        list[str]
            A list of users.
        """
        return self.users

    def get_name(self) -> str:
        """
        Get the name of this group.

        Returns:
        --------
        str
            The name of the group.
        """
        return self.name


def is_user_in_group(user: str, group: Group) -> bool:
    """
    Check if a user is in the given group or any of its sub-groups.

    Parameters:
    -----------
    user : str
        The user to be checked.
    group : Group
        The group in which to search for the user.

    Returns:
    --------
    bool
        True if the user is found in the group or any sub-group, False otherwise.
    """
    if user is None or group is None:
        return False

    # Use a stack to implement an iterative depth-first search
    stack = [group]

    while stack:
        current_group = stack.pop()
        # Check if the user is directly in this group
        if user in current_group.get_users():
            return True

        # Add all subgroups to the stack for further exploration
        stack.extend(current_group.get_groups())

    return False

if __name__ == "__main__":
    # Testing the implementation

    # Creating groups and users
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    # Test Case 1: User is in a nested subgroup
    print("Test Case 1")
    print(is_user_in_group("sub_child_user", parent))  # Expected output: True

    # Test Case 2
    print("Test Case 2")
    print(is_user_in_group("nonexistent_user", parent))  # Expected output: False

    # Test Case 3
    print("Test Case 3")
    parent.add_user("parent_user")
    print(is_user_in_group("parent_user", parent))  # Expected output: True

    print("Test Case 4")
    print(is_user_in_group("", parent))  # Expected output: False

    child.add_user("child_1")
    child.add_user("child_2")
    child.add_user("child_3")
    print("Test Case 5")
    print(is_user_in_group("child_2", sub_child)) # Expected output: False

