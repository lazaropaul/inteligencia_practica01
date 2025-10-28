from hlogedu.search.problem import action, Problem, DRange


class VacuumProblem(Problem):
    NAME = "Vacuum"

    def __init__(self):
        super().__init__()
        self.initial_pos = 0

    def get_start_states(self):
        return [(self.initial_pos, (True, True))]

    def is_goal_state(self, state):
        _, (r1, r2) = state
        return r1 is False and r2 is False

    def is_valid_state(self, state):
        pos, _ = state
        if pos not in (0, 1):
            return False
        return True

    # Step 1:
    # Use a function for Left, one for Right, and one for Sweep

    # Step 2:
    # Use DRange to combine Left and Right into "move"

    # Approx 3:
    # Implement the actions such that no redundant actions
    # exist.

    @action(cost=1)
    def left(self, state):
        pos, rubbish = state
        if pos == 0:
            return None
        return (0, rubbish)

    @action(cost=1)
    def right(self, state):
        pos, rubbish = state
        if pos == 1:
            return None
        return (1, rubbish)

    @action(cost=1)
    def sweep(self, state):
        pos, rubbish = state
        rubbish = list(rubbish)
        rubbish[pos] = False
        return (pos, tuple(rubbish))
