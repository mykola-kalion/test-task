import random

from third.src.map.coordinates import Coordinates
from third.src.units.ship import Ship


class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.obstructions: list[Coordinates] = []
        self.units: list[Ship] = []

    def is_in_bounds(self, coordinates: Coordinates):
        return 0 <= coordinates.x < self.width and 0 <= coordinates.y < self.height

    def is_passable(self, coordinates: Coordinates):
        return (coordinates not in self.obstructions and
                coordinates not in list(map(lambda unit: unit.position, self.units)))

    def neighbors(self, coordinates: Coordinates):
        (x, y) = coordinates.x, coordinates.y
        results = [
            Coordinates(x + 1, y),  # right
            Coordinates(x, y - 1),  # bottom
            Coordinates(x - 1, y),  # left
            Coordinates(x, y + 1)  # top
        ]
        results = filter(self.is_in_bounds, results)
        results = filter(self.is_passable, results)
        return results

    def generate_obstructions(self, fulfill_percentage=30):
        map_square = self.width * self.height
        obstructions_quantity = int((map_square / 100) * fulfill_percentage)

        while len(self.obstructions) < obstructions_quantity:
            obstruction = Coordinates(random.randint(1, self.width), random.randint(1, self.height))
            if obstruction not in self.obstructions:
                self.obstructions.append(obstruction)

        self.obstructions.sort(key=lambda coordinate: coordinate.x)

    def get_passable_nodes(self):
        width = [x for x in range(0, self.width)]
        height = [x for x in range(0, self.height)]

        passable_nodes = []

        for w in width:
            nodes = [Coordinates(w, h) for h in height if self.is_passable(Coordinates(w, h))]
            passable_nodes.extend(nodes)

        return passable_nodes

    def get_random_passable_node(self):
        while True:
            coordinates = Coordinates(
                x=random.randint(0, self.width),
                y=random.randint(0, self.height)
            )

            if self.is_passable(coordinates):
                return coordinates

    def deploy_unit(self, position: Coordinates, unit_class=Ship):
        if position in self.obstructions:
            raise Exception("The node is obstructed")
        elif position in list(map(lambda x: x.position, self.units)):
            raise Exception("The node is busy with other unit")
        else:
            unit = unit_class(self, position)
            self.units.append(unit)

            return unit


