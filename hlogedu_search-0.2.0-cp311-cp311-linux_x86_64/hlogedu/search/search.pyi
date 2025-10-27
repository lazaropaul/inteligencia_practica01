import abc
from .common import ClassParameter as ClassParameter
from .exceptions import ParameterException as ParameterException, ParameterValueException as ParameterValueException

class SolutionOutputter(metaclass=abc.ABCMeta):
    PARAMS: list[ClassParameter]
    def __init__(self, **kwargs) -> None: ...
    @abc.abstractmethod
    def output(self, solution): ...
