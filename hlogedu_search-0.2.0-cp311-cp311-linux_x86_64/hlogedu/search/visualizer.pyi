import abc
import pygame
from .algorithm import Node as Node
from .problem import Problem as Problem
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from typing import Any

class SolutionVisualizer(ABC, metaclass=abc.ABCMeta):
    """Abstract base class for visualizing solutions in search problems."""
    CELL_SIZE: int
    DELAY: int
    screen: Incomplete
    problem: Incomplete
    zoom: Incomplete
    speed: Incomplete
    def __init__(self, screen: pygame.Surface, problem: Problem, zoom: float = 1.0, speed: float = 1.0) -> None: ...
    @abstractmethod
    def draw_state(self, state: Any) -> None:
        """Draw the given state on the screen."""
    @abstractmethod
    def animate_transition(self, state: Any, action: Any, new_state: Any) -> None:
        """Graphically animate the transition from state via action to new_state."""
    def get_cell_size(self): ...
    def get_delay(self): ...

def visualize_solution(solution: list[Node], visualizer: SolutionVisualizer) -> None: ...
