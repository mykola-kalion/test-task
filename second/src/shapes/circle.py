from second.src.common.color import Color
from second.src.common.exceptions import DrawingException
from second.src.shapes.drawable import Drawable


class Circle(Drawable):
    def __init__(self, radius: int):
        if radius <= 0:
            raise DrawingException("Wrong circle parameters")

        self.radius = radius

    def draw(self, color: Color):
        is_galaxy_ok = True

        if not is_galaxy_ok:
            raise DrawingException()

        print(f"Drawing {color.value.lower()} circle with radius {self.radius}")
