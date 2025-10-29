"""Implementation of the Jars problem."""

from hlogedu.search.problem import action, Problem, DDRange, Heuristic


class JarsProblem(Problem):
    """Jars problem.

    This class implements the Jars problem. In this problem
    we have two or more jars with different capacities. At
    the beginning each jar is empty and the objective is to
    have a desired amount of liquid in one of them.

    The possible actions are:
        - fill one jar to its maximum capacity
        - empty one jar
        - pour from one jar into another, until the first is
          empty or the latter is full.
    """

    NAME = "Jars"
    
    def __init__(self):
        self.capacities = (5, 3)
        self.n_jars = len(self.capacities)

    def get_start_states(self):
        """Creates the initial state.

        The state is defined as a tuple of integers. The indexes of the
        tuple refer to each one of the jars and the number in that positon
        the amount of liquid on the jar.
        """
        return [(0,) * self.n_jars]

    def is_goal_state(self, state):
        """Tests if the state is a goal state.

        In this implementation the goal state only depends on the
        first jar, which we want it to contain 4 liters.
        """
        return state[0] == 4

    def is_valid_state(self, state):
        """Verifies that the given state is valid.

        In this problem a state is valid if all jars contain an amount
        of liquid between 0 and their maximum capacity.
        """
        for jar_content, max_capacity in zip(state, self.capacities):
            if not 0 <= jar_content <= max_capacity:
                return False
        return True

    @action(DDRange(0, 'n_jars'), cost=1)
    def fill(self, state, jar):
        """Fills the specified jar to its maximum capacity."""
        print("Filing")
        if state[jar] == self.capacities[jar]:
            return None

        n_state = list(state)
        n_state[jar] = self.capacities[jar]
        return tuple(n_state)

    @action(DDRange(0, 'n_jars'), cost=1)
    def empty(self, state, jar):
        """Empties the specified jar."""
        print("Empting")
        if state[jar] == 0:
            return None

        n_state = list(state)
        n_state[jar] = 0
        return tuple(n_state)

    @action(DDRange(0, 'n_jars'), DDRange(0, 'n_jars'), cost=1)
    def pour(self, state, jar_s, jar_d):
        """Pours the content of one jar into another.

        This action must take into account that not all the content of
        one jar will fit into the other.
        """
        print("Pouring")
        cap_d = self.capacities[jar_d]

        if jar_s == jar_d or state[jar_s] == 0 or state[jar_d] == cap_d:
            return None

        to_pour = min(state[jar_s], cap_d - state[jar_d])

        n_state = list(state)
        n_state[jar_s] -= to_pour
        n_state[jar_d] += to_pour
        return tuple(n_state)



@JarsProblem.heuristic
class DiffFromTargetVolumeHeuristic(Heuristic):
    def compute(self, state):
        return abs(state[0] - 4)