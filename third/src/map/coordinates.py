from dataclasses import dataclass


@dataclass
class Coordinates:
    x: int
    y: int

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.x + self.y < other.x + other.y

    def __le__(self, other):
        return self.x + self.y <= other.x + other.y

    def __sub__(self, other):
        return Coordinates(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f"({self.x},{self.y})"
