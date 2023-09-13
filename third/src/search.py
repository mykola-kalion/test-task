from third.src.common.priority_queue import PriorityQueue
from third.src.map.coordinates import Coordinates
from third.src.map.map import Map


def range_to_goal(a, b):
    (x1, y1) = a.x, a.y
    (x2, y2) = b.x, b.y
    return abs(x1 - x2) + abs(y1 - y2)


def find_path(_map: Map, start: Coordinates, destination: Coordinates):
    queue = PriorityQueue()
    queue.put(start, 0)
    came_from = {start: None}
    cost_so_far = {start: 0}

    while not queue.empty():
        current = queue.get()

        if current == destination:
            break

        for next_node in _map.neighbors(current):
            new_cost = cost_so_far[current] + 1
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + range_to_goal(destination, next_node)
                queue.put(next_node, priority)
                came_from[next_node] = current

    return came_from


def reconstruct_path(came_from, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path
