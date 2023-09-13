from second.src.common.color import Color
from second.src.common.exceptions import DrawingException
from second.src.shapes.drawable import Drawable


class Rectangle(Drawable):
    def __init__(self, width: int, length: int):
        if width <= 0 or length <= 0:
            raise DrawingException("Wrong rectangle parameters")

        self.width = width
        self.length = length

    def draw(self, color: Color):
        is_galaxy_ok = True

        if not is_galaxy_ok:
            raise DrawingException()

        print(f"Drawing {color.value.lower()} rectangle with dimensions {self.width}x{self.length}")
