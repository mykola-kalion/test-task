import pytest
from assertpy import assert_that

from second.src.common.color import Color
from second.src.common.exceptions import DrawingException
from second.src.shapes.circle import Circle
from second.src.shapes.rectangle import Rectangle
from second.src.shapes.triangle import Triangle
from second.tests.helpers.capture import Capturing


@pytest.mark.parametrize("radius", [1, 5])
@pytest.mark.second
def test_circle(radius):
    # Given
    circle = Circle(radius)

    # When
    color = Color.GREEN
    with Capturing() as output:
        circle.draw(color)

    # Then
    assert_that(output).is_length(1)
    assert_that(output).is_equal_to([f"Drawing {color.value.lower()} circle with radius {radius}"])


@pytest.mark.second
def test_invalid_circle():
    # Given
    radius = 0

    # When
    def circle(radius):  # assert_that().raises doesn't work with classes. __init__ also not working. lambda neither.
        return Circle(radius)

    # Then
    assert_that(circle).raises(DrawingException).when_called_with(radius)


@pytest.mark.parametrize("width, length", [(10, 5)])
@pytest.mark.second
def test_rectangle(width, length):
    # Given
    rectangle = Rectangle(width=width, length=length)

    # When
    color = Color.BLUE
    with Capturing() as output:
        rectangle.draw(color)

    # Then
    assert_that(output).is_length(1)
    assert_that(output).is_equal_to([f"Drawing {color.value.lower()} rectangle with dimensions {width}x{length}"])


@pytest.mark.parametrize("length, width", [
    (1, 0),
    (0, 1)
])
@pytest.mark.second
def test_invalid_rectangle(length, width):
    # Given length or width == 0

    # When
    def triangle(x, y):  # assert_that().raises doesn't work with classes. __init__ also not working. lambda neither.
        return Rectangle(x, y)

    # Then
    assert_that(triangle).raises(DrawingException).when_called_with(length, width)


@pytest.mark.parametrize("a, b, c", [
    (5, 2, 5)
])
@pytest.mark.second
def test_triangle(a, b, c):
    # Given
    triangle = Triangle(a=a, b=b, c=c)

    # When
    color = Color.GREEN
    with Capturing() as output:
        triangle.draw(color)

    # Then
    assert_that(output).is_length(1)
    assert_that(output).is_equal_to([f"Drawing {color.value.lower()} triangle with dimensions {a}x{b}x{c}"])


@pytest.mark.parametrize("a,b,c", [
    (10, 1, 1),
    (1, 10, 1),
    (1, 1, 10)
])
@pytest.mark.second
def test_invalid_triangle(a, b, c):
    # Given one side is bigger than sum of two sides

    # When
    def triangle(x, y, z):  # assert_that().raises doesn't work with classes. __init__ also not working. lambda neither.
        return Triangle(x, y, z)

    # Then
    assert_that(triangle).raises(DrawingException).when_called_with(a, b, c)
