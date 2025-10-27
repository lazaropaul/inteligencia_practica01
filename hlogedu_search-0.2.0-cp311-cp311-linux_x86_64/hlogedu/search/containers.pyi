import abc
import types
from _typeshed import Incomplete

class BaseInserter(metaclass=abc.ABCMeta):
    """Inserter class base interface."""
    def __init__(self, key) -> None: ...
    @abc.abstractmethod
    def begin(self):
        """Initiales an insertion context."""
    @abc.abstractmethod
    def end(self):
        """Terminates the insertion context."""
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...

class Inserter(BaseInserter, metaclass=abc.ABCMeta):
    """Simple container inserter interface."""
    @abc.abstractmethod
    def push(self, element):
        """Pushes an element into the insertion context."""

class Fringe(abc.ABC):
    def __init_subclass__(cls, **kwargs) -> None: ...
    @property
    def max_size(self): ...

class Stack(Fringe):
    """
    The elements of this collection will be retrieved and removed in the
    inverse order as they were pushed.
    """
    data: Incomplete
    def __init__(self, data=None) -> None:
        """
        Initializes a new empty Stack.
        """
    def extend(self, iterable) -> None:
        """extend(iterable) -> void

        Extends this stack pushing elements from the iterable.
        """
    def push(self, element) -> None:
        """push(element) -> void

        Inserts a new element at the top of the stack.
        """
    def peek(self):
        """peek() -> element

        Access the element at the top of the stack.
        """
    def pop(self):
        """pop() -> element

        Removes and returns the element at the top of the stack.
        """
    def length(self):
        """length() -> int

        The number of elements in the stack.
        """
    def is_empty(self):
        """is_empty() -> boolean

        Tests if the stack is empty.
        """
    def lexicographical(self, key):
        """Creates a new lexicographical inserter for this stack.

        :return: A new lexicographical inserter instance.
        :rtype: StackLexicographicalInserter
        """
    def __bool__(self) -> bool: ...
    def __iter__(self): ...

class StackLexicographicalInserter(Inserter):
    """Implementation of a lexicographical inserter for a Stack."""
    stack: Incomplete
    def __init__(self, stack, key) -> None: ...
    def begin(self) -> None: ...
    def end(self) -> None: ...
    def push(self, element) -> None: ...

class Queue(Fringe):
    """
    The elements of this collection will be retrieved and removed in the same
    order as they were pushed.
    """
    data: Incomplete
    def __init__(self, data=None) -> None:
        """
        Initializes a new empty Queue.
        """
    def extend(self, iterable) -> None:
        """extend(iterable) -> void

        Extends this queue pushing elements from the iterable.
        """
    def push(self, element) -> None:
        """push(element) -> void

        Enqueues the specified element.
        """
    def peek(self):
        """peek() -> element

        Access the next element in the queue.
        """
    def pop(self):
        """pop() -> element

        Dequeue and returns the next element in the queue.
        """
    def length(self):
        """length() -> int

        The number of elements in the queue.
        """
    def is_empty(self):
        """is_empty() -> boolean

        Tests if the queue is empty.
        """
    def lexicographical(self, key):
        """Creates a new lexicographical inserter for this queue.

        :return: A new lexicographical inserter instance.
        :rtype: QueueLexicographicalInserter
        """
    def __bool__(self) -> bool: ...
    def __iter__(self): ...

class QueueLexicographicalInserter(Inserter):
    """Implementation of a lexicographical inserter for a Queue."""
    queue: Incomplete
    def __init__(self, queue, key) -> None: ...
    def begin(self) -> None: ...
    def end(self) -> None: ...
    def push(self, element) -> None: ...

class PriorityQueue(Fringe):
    """
    Implements a priority queue data structure. Each inserted element
    has a priority associated with it. This data structure allows O(1)
    access to the lowest-priority item.
    """
    def __init__(self, key=None) -> None:
        """
        Initializes a new empty priority queue.
        :param key: If two elements have the same priority, they ordering
                    is broken using the value returned by the key function.
                    If the keys have also the same value, then the ordering
                    depends on the moment they where pushed into the queue.
        """
    def push(self, element, priority) -> None:
        """
        Enqueues and sorts the given element based on the specified priority.
        """
    def peek(self):
        """
        Access the element with the lowest-priority.
        """
    def pop(self):
        """
        Dequeue and returns the element with the lowest-priority.
        """
    def size(self):
        """
        The number of elements in the priority queue.
        """
    def is_empty(self):
        """
        Tests if this priority queue is empty.
        """
    def __bool__(self) -> bool: ...
    def __iter__(self): ...

class HashableList(list):
    """List wrapper that implements a hash method for lists.

    This class implementation is for demonstration purposes only, in languages
    such as Python this is dangerous when combined with dictionary like
    collections. Modifying the original list will change the key of the
    dictionary and thereby break the whole dictionary structure.
    """
    def copy(self): ...
    def __hash__(self): ...

class ImmutableStack:
    """ImmutableStack

    It behaves like a typical stack but all its methods return a copy
    of leaving the original one unaltered.
    """
    data: Incomplete
    def __init__(self, data=None) -> None:
        """
        Initializes a new immutable stack.
        """
    def push(self, element):
        """Adds an element at the top of the stack.
        :return: A new immutable stack with the new element.
        """
    def peek(self):
        """Access the element at the top of the stack.
        :return: The value of the element at the top of the stack.
        """
    def pop(self):
        """Removes the element at the top of the stack.
        :return: A new immutable stack without the element at the top.
        """
    def size(self):
        """
        The number of elements in the priority queue.
        """
    def is_empty(self):
        """
        Tests if this priority queue is empty.
        """
    def __eq__(self, other): ...
    def __hash__(self): ...
    def __bool__(self) -> bool: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...

class PermanentlyEmptySet(set):
    """PermanentlyEmptySet

    A naive set that remains always empty.
    """
    def add(self, data) -> None: ...
    def update(self, *args) -> None: ...
    def __ior__(self, other) -> None: ...
    def symmetric_difference_update(self, other) -> None: ...
    def __ixor__(self, other) -> None: ...

class PermanentlyEmptyDict(dict):
    """PermanentlyEmptyDict

    A naive dictionary that remains always empty.
    """
    def setdefault(self, key, default=None, **kwargs) -> None: ...
    def update(self, other=None, **kwargs) -> None: ...
    def __setitem__(self, key, value) -> None: ...
