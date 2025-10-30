#We must create a subclass of the Algorithm base class:
#We can also define the NAME class attribute to modify the name of our algorithm,
from hlogedu.search.algorithm import Algorithm , Node , Solution
from hlogedu.search.containers import PriorityQueue , Queue

class TreeBfs(Algorithm):
    NAME = "my-tree-bfs"

 
# Next, we will define the constructor:

    def __init__(self, problem):
        super().__init__(problem)
        self.fringe = Queue()

#Next, we will implement the only method for the Algorithm class, the run method:

def run(self):
    expand_counter = 0
    roots = [Node(s) for s in self.problem.get_start_states()]

    for n in roots:
        if self.problem.is_goal_state(n.state):
            return Solution(self.problem, roots, solution_node=n)
        self.fringe.push(n)

    while self.fringe:
        n = self.fringe.pop()
        expand_counter += 1
        n.expand_order = expand_counter
        n.location = Node.Location.EXPANDED
        for s, a, c in self.problem.get_successors(n.state):
            ns = Node(s, a, cost=n.cost + c, parent=n)
            n.add_successor(ns)
            if self.problem.is_goal_state(ns.state):
                return Solution(self.problem, roots, solution_node=ns)
            self.fringe.push(ns)

    return Solution(self.problem, roots)