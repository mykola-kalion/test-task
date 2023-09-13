from abc import abstractmethod, ABC

from second.src.common.color import Color


class Drawable(ABC):
    @abstractmethod
    def draw(self, color: Color):
        pass
