import pytest

from second.src.engine.engine2d import Engine2D
from second.src.shapes.circle import Circle


@pytest.fixture
def engine():
    yield Engine2D()
