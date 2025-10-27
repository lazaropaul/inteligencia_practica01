import abc
from .common import ClassParameter as ClassParameter
from .exceptions import ActionException as ActionException, HeuristicException as HeuristicException, ParameterException as ParameterException, ParameterValueException as ParameterValueException
from _typeshed import Incomplete

class Action:
    def __init__(self, fn, parameters) -> None: ...
    def __call__(self, *args, **kwargs): ...
    @property
    def name(self): ...
    @property
    def parameters(self): ...
    @property
    def wrapped_parameters(self): ...

class FixedCostAction(Action):
    cost: Incomplete
    def __init__(self, fn, parameters, cost) -> None: ...
    def __call__(self, *args, **kwargs): ...

def action(*parameters, cost=None):
    '''Decorator for defining an action in a search problem.

    This decorator converts a function into an `Action` or
    `FixedCostAction` object, depending on whether a fixed cost
    is specified. It also validates that all provided parameters
    are instances of `BaseActionParameter`.

    Args:
        *parameters (BaseActionParameter): One or more action parameters
            that define the behavior of the action.
        cost (float, optional): A fixed cost associated with the action.
            If ``None`` (default), the action cost will be determined
            dynamically.

    Returns:
        Callable: A decorator that transforms the decorated function into
        an `Action` or `FixedCostAction` instance.

    Raises:
        TypeError: If any provided parameter is not an instance of
            `BaseActionParameter`.

    Example:

        >>> @action(DRange(5), Categorical(["a", "b"]), cost=1.5)
        ... def move(self, state, p1, p2):
        ...     # implementation of the move action
        ...     return new_state
    '''

class BaseActionParameter(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def iterator(self, problem): ...

class Categorical(BaseActionParameter):
    """A list of values for a parameter."""
    iterable: Incomplete
    def __init__(self, iterable) -> None:
        """Initialize a categorical parameter with a fixed list of values.

        Args:
            iterable (Iterable): An iterable of possible values for the parameter.

        Raises:
            TypeError: If `iterable` is not actually iterable.
        """
    def iterator(self, _): ...

class DynamicCategorical(BaseActionParameter):
    """A categorical parameter whose values can depend on the problem instance (alias `DCategorical`)."""
    iterable: Incomplete
    def __init__(self, iterable) -> None:
        """Initialize a dynamic categorical parameter.

        Args:
            iterable (Iterable or str): Either an iterable of possible values,
                or the name of an attribute of the problem providing the values.

        Raises:
            TypeError: If `iterable` is neither a string nor an iterable.
        """
    def iterator(self, problem): ...

class DiscreteRange(BaseActionParameter):
    """A discrete range of values for a parameter (alias `DRange`)."""
    start: Incomplete
    end: Incomplete
    def __init__(self, start, end=None) -> None:
        """Initialize a discrete range parameter.

        Args:
            start (int): The start of the range, or the end if `end` is None.
            end (int, optional): The end of the range (exclusive). Defaults to None.

        Raises:
            ValueError: If `start` is greater than `end`.
        """
    def iterator(self, _): ...

class DynamicDiscreteRange(BaseActionParameter):
    """A discrete range of values that can depend on the problem instance (alias `DDRange`)."""
    start: Incomplete
    end: Incomplete
    def __init__(self, start, end=None) -> None:
        """Initialize a dynamic discrete range parameter.

        Args:
            start (int or str): The start of the range, or the name of a problem
                attribute providing the start.
            end (int or str, optional): The end of the range, or the name of a problem
                attribute providing the end. Defaults to None.

        Raises:
            TypeError: If `start` or `end` is neither an integer nor a string.
        """
    def iterator(self, problem): ...

class DiscreteInterval(DiscreteRange):
    """A discrete interval of values for a parameter (alias `DInterval`)."""
    def __init__(self, start, end) -> None:
        """Initialize a discrete interval parameter.

        Args:
            start (int): The start of the interval.
            end (int): The end of the interval (inclusive).
        """

class DynamicDiscreteInterval(DynamicDiscreteRange):
    """A dynamic discrete interval of values for a parameter (alias `DDInterval`)."""
    def __init__(self, start, end) -> None:
        """Initialize a dynamic discrete interval parameter.

        Args:
            start (int or str): The start of the interval, or the name of a problem
                attribute providing the start.
            end (int or str): The end of the interval, or the name of a problem
                attribute providing the end (inclusive).
        """
DCategorical = DynamicCategorical
DRange = DiscreteRange
DDRange = DynamicDiscreteRange
DInterval = DiscreteInterval
DDInterval = DynamicDiscreteInterval

class ProblemMeta(abc.ABCMeta):
    def __new__(mcs, name, bases, namespace): ...

class Problem(metaclass=ProblemMeta):
    """Base class for defining search problems.

    A `Problem` defines the structure of a search task, including its
    initial states, goal conditions, and valid successor states.
    It also provides utilities for heuristics and visualization.

    Attributes:
        PARAMS (list[ClassParameter]): List of configurable class parameters.
    """
    PARAMS: list[ClassParameter]
    def __init_subclass__(cls, **kwargs) -> None: ...
    @classmethod
    def get_name(cls) -> str:
        """Get the problem's name.

        Returns:
            str: The name of the problem, either from the class attribute
            ``NAME`` (if defined) or the class name itself.
        """
    @classmethod
    def heuristic(cls, h_cls):
        """Register a heuristic for this problem.

        Should be used as a decorator for a sublclass of `Heuristic`.

        Args:
            h_cls (type): The heuristic class to register.

        Returns:
            type: The registered heuristic class (unchanged).
        """
    @classmethod
    def visualizer(cls):
        """Get the visualizer associated with this problem.

        Returns:
            SolutionVisualizer | None: The visualizer object if defined
            in the class attribute ``VISUALIZER``, otherwise ``None``.
        """
    @property
    def name(self) -> str:
        """str: The name of the problem instance."""
    @property
    def num_expanded(self) -> int:
        """int: Number of expanded nodes in the problem."""
    def get_successors(self, state):
        """Generate successor states from a given state.

        Each successor is represented as a tuple of
        ``(new_state, action, cost)``.

        Args:
            state (Any): The current state.

        Returns:
            list[tuple[Any, str, float]]: A list of successors, where each entry
            contains the next state, a descriptive action name, and the action cost.
        """
    @abc.abstractmethod
    def get_start_states(self):
        """Return the initial states of the problem.

        This is an abstract method that must be implemented in a subclass.

        Returns:
            list[Any]: A list of valid start states.
        """
    @abc.abstractmethod
    def is_goal_state(self, state):
        """Check if a state is a goal state.

        This is an abstract method that must be implemented in a subclass.

        Args:
            state (Any): The state to check.

        Returns:
            bool: ``True`` if the state is a goal state, ``False`` otherwise.
        """
    @abc.abstractmethod
    def is_valid_state(self, state):
        """Check if a state is valid in the problem domain.

        This is an abstract method that must be implemented in a subclass.

        Args:
            state (Any): The state to validate.

        Returns:
            bool: ``True`` if the state is valid, ``False`` otherwise.
        """

class Heuristic(metaclass=abc.ABCMeta):
    """Abstract base class for heuristics.

    A `Heuristic` represents a function that assigns an estimated value
    to a given state of a problem. Subclasses must implement the
    :meth:`compute` method to define the heuristic evaluation.

    Attributes:
        problem (Problem): The problem instance for which the heuristic is defined.
    """
    @classmethod
    def get_name(cls):
        """Get the name of the heuristic class.

        If the subclass defines a ``NAME`` attribute, it will be used.
        Otherwise, the class name is returned.

        Returns:
            str: The name of the heuristic.
        """
    problem: Incomplete
    def __init__(self, problem: Problem) -> None:
        """Initialize the heuristic with a problem instance.

        Args:
            problem (Problem): The problem instance on which the heuristic operates.
        """
    @abc.abstractmethod
    def compute(self, state):
        """Compute the heuristic value for a given state.

        This method must be implemented by subclasses.

        Args:
            state: The state of the problem to evaluate.

        Returns:
            float | int: The heuristic value associated with the state.

        Raises:
            NotImplementedError: If the method is not implemented in a subclass.
        """
    def __call__(self, state): ...

class NullHeuristic(Heuristic):
    NAME: str
    def __init__(self) -> None: ...
    def compute(self, state): ...

def register_heuristic(p_cls, h_cls) -> None: ...
def has_heuristic(problem_cls, heuristic_name): ...
def get_heuristics(problem_cls): ...
def get_heuristic(problem_cls, heuristic_name): ...
