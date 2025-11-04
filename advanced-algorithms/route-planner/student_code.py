import heapq
import math
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
    distance = math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
    return distance

def reconstruct_path(came_from: dict[int, int], current: int) -> list[int]:
    """
    Reconstruct the path from the start node to the goal node.

    Args:
        came_from (dict[int, int]): A dictionary mapping each node to the node it came from.
        current (int): The goal node.

    Returns:
        list[int]: The reconstructed path from the start node to the goal node.
    """
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)

    return path[::-1]

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
    visited: set[int] = set()
    frontier: list[tuple[float, int]] = list()
    parent_dict: dict[int, int] = dict()
    g_score: dict[int, float] = {start: float(0)}
    f_score: dict[int, float] = {start: heuristic(M.intersections[start], M.intersections[goal])}
    heapq.heappush(frontier, (f_score[start], start))

    while frontier:
        current_f, current = heapq.heappop(frontier)

        if current in visited:
            continue # Skip if already processed (stale entry)
        if current == goal:
            # Reconstruct path
            path = reconstruct_path(parent_dict, current)
            return path
        
        visited.add(current)
        for neighbour in M.roads[current]:
            tentative_g = g_score[current] + heuristic(M.intersections[current], M.intersections[neighbour])
            if neighbour in g_score and tentative_g >= g_score[neighbour]:
                continue
            
            # Found a better path
            parent_dict[neighbour] = current
            g_score[neighbour] = tentative_g
            f_score[neighbour] = g_score[neighbour] + heuristic(M.intersections[neighbour], M.intersections[goal])
            heapq.heappush(frontier, (f_score[neighbour], neighbour))

    return None






    pass



