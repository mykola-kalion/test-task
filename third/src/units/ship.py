from third.src.map.coordinates import Coordinates


class Ship:
    def __init__(self, _map, position: Coordinates):
        if position in _map.obstructions:
            raise Exception

        self._map = _map
        self.position = position

    def move(self, coordinates: Coordinates):
        if self._map.is_passable(coordinates):
            self.position = coordinates
        else:
            print("Not passable")

    def move_top(self):
        node = Coordinates(self.position.x, self.position.y + 1)
        self.move(node)
        print(f"move top, coordinates: {node}")

    def move_bottom(self):
        node = Coordinates(self.position.x, self.position.y - 1)
        self.move(node)
        print(f"move bottom, coordinates: {node}")

    def move_left(self):
        node = Coordinates(self.position.x - 1, self.position.y)
        self.move(node)
        print(f"move left, coordinates: {node}")

    def move_right(self):
        node = Coordinates(self.position.x + 1, self.position.y)
        self.move(node)
        print(f"move right, coordinates: {node}")

    def navigate(self, path: list[Coordinates]):
        for node in path:
            move = self.__get_direction(node)
            move()

    def __get_direction(self, destination: Coordinates):
        directions = {
            Coordinates(0, 1): self.move_top,
            Coordinates(0, -1): self.move_bottom,
            Coordinates(1, 0): self.move_right,
            Coordinates(-1, 0): self.move_left,
            Coordinates(0, 0): lambda: print("Chewie we are home!")
        }

        return directions[destination - self.position]
