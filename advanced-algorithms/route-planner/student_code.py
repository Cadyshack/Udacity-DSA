import heapq
from typing import Optional

from helpers import Map

def heuristic(a: tuple[float, float], b: tuple[float, float]) -> float:
    """
    Calculate the Euclidean distance between two points.

    Args:
        a (tuple[float, float]): The coordinates of the first point (x1, y1).
        b (tuple[float, float]): The coordinates of the second point (x2, y2).

    Returns:
        float: The Euclidean distance between the two points.
    """
    pass

def reconstruct_path(came_from: dict[int, int], current: int) -> list[int]:
    """
    Reconstruct the path from the start node to the goal node.

    Args:
        came_from (dict[int, int]): A dictionary mapping each node to the node it came from.
        current (int): The goal node.

    Returns:
        list[int]: The reconstructed path from the start node to the goal node.
    """
    pass

def shortest_path(M: Map, start: int, goal: int) -> Optional[list[int]]:
    """
    Find the shortest path between two nodes in a map using the A* algorithm.

    Args:
        M (Map): The map containing the graph, intersections, and roads.
        start (int): The starting node.
        goal (int): The goal node.

    Returns:
        Optional[list[int]]: The shortest path from the start node to the goal node, or None if no path is found.
    """
    pass
