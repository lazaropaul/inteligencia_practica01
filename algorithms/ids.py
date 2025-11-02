from hlogedu.search.algorithm import Algorithm, Node, Solution
from hlogedu.search.containers import Stack


class IDS(Algorithm):
    NAME = "my-tree-ids"
    
    def __init__(self, problem):
        super().__init__(problem)
        self.fringe = Stack()
    
    def run(self):
        depth = 0
        while True:
            # Reset fringe per cada iteració del depth
            self.fringe = Stack()
            expand_counter = 0
            cutoff = False
            
            # Creem nodes a partir dels initial states
            roots = [Node(s) for s in self.problem.get_start_states()]
            
            # Comprovem si algun root es node
            for n in roots:
                if self.problem.is_goal_state(n.state):
                    return Solution(self.problem, roots, solution_node=n, cutoff=False)
                self.fringe.push(n)
            
            while self.fringe:
                n = self.fringe.pop()
                
                if n.depth >= depth:
                    cutoff = True
                else:
                    expand_counter += 1
                    n.expand_order = expand_counter
                    n.location = Node.Location.EXPANDED
                    
                    for s, a, c in sorted(
                        self.problem.get_successors(n.state), key=lambda x: x[0]
                    ):
                        ns = Node(s, a, cost=n.cost + c, parent=n)
                        n.add_successor(ns)
                        
                        if self.problem.is_goal_state(ns.state):
                            return Solution(
                                self.problem, roots, solution_node=ns, cutoff=cutoff
                            )
                        
                        self.fringe.push(ns)
            
            if not cutoff:
                return Solution(self.problem, roots, cutoff=False)
            
            depth += 1