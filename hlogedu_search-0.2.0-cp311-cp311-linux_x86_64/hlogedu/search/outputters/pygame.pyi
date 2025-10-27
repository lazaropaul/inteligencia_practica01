from ..common import ClassParameter as ClassParameter
from ..search import SolutionOutputter as SolutionOutputter
from ..visualizer import visualize_solution as visualize_solution
from _typeshed import Incomplete

class PygameOutputter(SolutionOutputter):
    PARAMS: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def output(self, solution) -> None: ...
