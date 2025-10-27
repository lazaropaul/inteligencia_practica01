class ActionException(Exception):
    """Exception raised when there is a problem with an action
    definition or result."""
class AlgorithmException(Exception):
    """Exception raised when there is a problem with an algorithm."""
class HeuristicException(Exception):
    """Exception raised when there is a problem with a heuristic."""
class ParameterException(Exception):
    """Exception raised when a required parameter has not been specified."""
class ParameterValueException(Exception):
    """Exception raised when a parameter value is not correct."""
class ProblemException(Exception):
    """Exception raised when the problem encounters an inconsistency.

    Possibles causes may be:
        - Incorrect state type.
        - Incorrect initialization.
        - ...
    """
