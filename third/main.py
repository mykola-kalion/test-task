from third.src.map.map import Map
from third.src.search import find_path, reconstruct_path

_map = Map(10, 10)
_map.generate_obstructions()

ship = _map.deploy_unit(_map.get_random_passable_node())

destination = _map.get_random_passable_node()
start = _map.units[0].position

came_from = find_path(_map=_map, start=start, destination=destination)

path = reconstruct_path(came_from, start, destination)

ship.navigate(path)
