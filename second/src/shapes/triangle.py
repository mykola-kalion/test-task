from second.src.common.color import Color
from second.src.common.exceptions import DrawingException
from second.src.shapes.drawable import Drawable


class Triangle(Drawable):
    def __init__(self, a, b, c):
        if a + b < c or a + c < b or b + c < a:
            raise DrawingException("Wrong triangle parameters")

        self.a = a
        self.b = b
        self.c = c

    def draw(self, color: Color):
        is_galaxy_ok = True

        if not is_galaxy_ok:
            raise DrawingException()

        print(f"Drawing {color.value.lower()} triangle with dimensions {self.a}x{self.b}x{self.c}")
