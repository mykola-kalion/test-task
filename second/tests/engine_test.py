import random

import pytest
from assertpy import assert_that

from second.src.common.color import Color
from second.src.engine.engine2d import Engine2D
from second.src.shapes.circle import Circle
from second.src.shapes.triangle import Triangle
from second.tests.helpers.capture import Capturing


@pytest.mark.parametrize("radius", [5])
@pytest.mark.second
def test_add_to_canvas(engine: Engine2D, radius):
    # Given
    circle = Circle(radius)

    # When
    engine.add_to_canvas(circle)

    # Then
    assert_that(engine.canvas).is_length(1).contains_only(circle)


@pytest.mark.parametrize("a,b,c,radius", [(4, 2, 4, 5)])
@pytest.mark.second
def test_add_all_to_canvas(engine: Engine2D, a, b, c, radius):
    # Given
    circle = Circle(radius)
    triangle = Triangle(a, b, c)

    # When
    engine.add_all_to_canvas([circle, triangle])

    # Then
    assert_that(engine.canvas).is_length(2)
    assert_that(engine.canvas).is_equal_to([circle, triangle])


@pytest.mark.parametrize("radius", [5])
@pytest.mark.second
def test_clean_canvas(engine: Engine2D, radius):
    # Given
    circle = Circle(radius)
    engine.add_to_canvas(circle)

    # When
    engine.clean_canvas()

    # Then
    assert_that(engine.canvas).is_length(0)


@pytest.mark.parametrize("a,b,c,radius", [(4, 2, 4, 5)])
@pytest.mark.second
def test_drawing(engine: Engine2D, a, b, c, radius):
    # Given
    circle = Circle(radius)
    triangle = Triangle(a, b, c)
    engine.add_all_to_canvas([circle, triangle])

    # When
    with Capturing() as output:
        engine.draw()

    # Then
    assert_that(output).is_equal_to([
        f"Drawing {engine.color.value.lower()} circle with radius 5",
        f"Drawing {engine.color.value.lower()} triangle with dimensions {a}x{b}x{c}"
    ])


@pytest.mark.parametrize("radius", [5])
@pytest.mark.second
def test_canvas_was_cleared_after_drawing(engine: Engine2D, radius):
    # Given
    circle = Circle(radius)
    engine.add_to_canvas(circle)

    # When
    engine.draw()

    # Then
    assert_that(engine.canvas).is_length(0)


@pytest.mark.parametrize("radius", [5])
@pytest.mark.second
def test_set_color(engine: Engine2D, radius):
    # Given
    circle = Circle(radius)
    engine.add_to_canvas(circle)

    # When
    available_colors = [e.name for e in Color]
    available_colors.remove(engine.color.name)
    new_color = Color[random.choice(available_colors)]
    engine.color = new_color

    with Capturing() as output:
        engine.draw()

    # Then
    assert_that(output).contains_only(f"Drawing {new_color.value.lower()} circle with radius {radius}")
