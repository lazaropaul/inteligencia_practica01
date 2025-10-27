import abc
import enum
from .exceptions import AlgorithmException as AlgorithmException
from .problem import Problem as Problem
from _typeshed import Incomplete

HEURISTIC_PARAMETER: str
MAX_DEPTH_PARAMETER: str
SUPPORTED_PARAMETERS: Incomplete

def has_algorithm(name): ...
def get_algorithms(): ...
def get_algorithm(name): ...
def get_algorithm_parameters(cls): ...

class Algorithm(abc.ABC, metaclass=abc.ABCMeta):
    """Base class for defining a search algorithm to solve a problem.

    Subclasses must implement the `run` method and can optionally override
    the `NAME` attribute to define a custom name.
    """
    NAME: str | None
    def __init_subclass__(cls, **kwargs) -> None: ...
    problem: Incomplete
    fringe: Incomplete
    def __init__(self, problem: Problem) -> None:
        """Initialize an algorithm with a specific problem instance.

        Args:
            problem (Problem): The problem instance that the algorithm will solve.
        """
    @abc.abstractmethod
    def run(self, **kwargs):
        """Run the algorithm. Must be implemented by subclasses."""

class Node:
    """
    This class represents a node in a search tree.

    It carries information about the current state:
        - state      : Search state
        - action     : Action performed to reach 'state' from parent
        - cost       : Accumulated cost to reach this 'state'
        - hcost      : Heuristic cost of this node's state
        - parent     : This node's parent
        - depth      : This node's depth in the tree
        - children   : List of child nodes
    """
    class Location(enum.Enum):
        FRINGE = (0,)
        PRE_EXPANDED = 1
        EXPANDED = 2
    location: Incomplete
    def __init__(self, state, action=None, cost: int = 0, parent=None, h_cost=None, f_cost=None) -> None:
        """Initializes a new Search Node.

        It also modifies the data based on some parent's information. This node
        is set as a child of the parent and the depth of this child is
        set based on the parent's depth.

        Args:
            state (Any): The state represented by this node.
            action (Any, optional): The action taken to reach this state. Defaults to None.
            cost (float, optional): The cumulative cost to reach this node. Defaults to 0.
            parent (Node, optional): The parent node. Defaults to None.
            h_cost (float, optional): Heuristic cost of this node. Defaults to None.
            f_cost (float, optional): Estimated total cost (f = g + h). Defaults to None.
        """
    @property
    def state(self): ...
    @property
    def action(self): ...
    @property
    def cost(self): ...
    @property
    def parent(self): ...
    @property
    def h_cost(self): ...
    @property
    def f_cost(self): ...
    @property
    def depth(self): ...
    @property
    def successors(self): ...
    @property
    def expanded_order(self): ...
    @expanded_order.setter
    def expanded_order(self, value) -> None: ...
    def add_successor(self, node) -> None: ...
    def remove_successor(self, node) -> None: ...
    def compute_path(self):
        """Computes the path from the root node to this one.

        :return: A list with the secuence from the root node to this one.
        :rtype: list[SearchNode]
        """
    def compute_reverse_path(self):
        """Computes the path from this node to the root node.

        :return: A list with the secuence from this node to the root.
        :rtype: list[SearchNode]
        """
    def get_root_node(self):
        """getRootNode() -> Node

        Returns the root node (the one in the path with no parent).
        """
    def __lt__(self, other): ...

class Solution:
    """Represents a solution for a given problem.

    Stores the root nodes, the solution node (if found), and whether the search
    was cut off prematurely.
    """
    def __init__(self, problem, root_nodes, solution_node=None, cutoff: bool = False) -> None:
        """Initialize a solution container.

        Args:
            problem (Problem): The problem instance the solution corresponds to.
            root_nodes (list[Node]): The root nodes of the search tree.
            solution_node (Node, optional): The node representing the solution. Defaults to None.
            cutoff (bool, optional): Whether the search was terminated early. Defaults to False.
        """
    @property
    def problem(self): ...
    @property
    def root_nodes(self): ...
    @property
    def solution_node(self): ...
    def has_been_cutoff(self): ...
    def has_solution(self): ...
    def get_solution_path(self): ...
