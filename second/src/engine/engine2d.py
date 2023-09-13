from second.src.common.color import Color
from second.src.common.exceptions import DrawingException
from second.src.shapes.drawable import Drawable


class Engine2D:
    def __init__(self):
        self.canvas: list[Drawable] = []
        self.color: Color = Color.RED

    def add_all_to_canvas(self, elements: list[Drawable]):
        self.canvas.extend(elements)
        return self

    def add_to_canvas(self, element: Drawable):
        self.canvas.append(element)
        return self

    def draw(self):
        if len(self.canvas) == 0:
            raise DrawingException("Canvas is empty, nothing to draw")

        for shape in self.canvas:
            try:
                shape.draw(self.color)
            except DrawingException as error:
                print(error.message)

        self.clean_canvas()
        return self

    def clean_canvas(self):
        self.canvas.clear()
        return self
