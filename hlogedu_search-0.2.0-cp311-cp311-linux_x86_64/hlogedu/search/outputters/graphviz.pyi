from ..algorithm import Node as Node
from ..common import ClassParameter as ClassParameter
from ..search import SolutionOutputter as SolutionOutputter
from _typeshed import Incomplete

SOLUTION_PATH_COLOR: str

class GraphvizOutputter(SolutionOutputter):
    PARAMS: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def output(self, solution): ...
    @staticmethod
    def get_node_attrs(node, problem, sol_path): ...
    @staticmethod
    def get_action_attrs(parent, child, path): ...
    @staticmethod
    def get_edge_attrs(parent, child, path): ...
