from hlogedu.search.algorithm import Algorithm, Node, Solution
from hlogedu.search.containers import Stack


class IDS(Algorithm):
    """
    Iterative Deepening Search
    Combines DLS with increasing depth limits until solution is found
    """
    NAME = "my-ids"
    
    def __init__(self, problem):
        super().__init__(problem)
        self.fringe = Stack()  # Required by framework
    
    def run(self):
        """
        Run IDS by repeatedly performing DLS with increasing depths
        until a solution is found or no cutoff occurs
        """
        depth = 0
        while True:
            # Reset fringe for each depth iteration
            self.fringe = Stack()
            expand_counter = 0
            cutoff = False
            
            # Create root nodes from initial states
            roots = [Node(s) for s in self.problem.get_start_states()]
            
            # Check if any root is a goal
            for n in roots:
                if self.problem.is_goal_state(n.state):
                    return Solution(self.problem, roots, solution_node=n, cutoff=False)
                self.fringe.push(n)
            
            # Depth-Limited Search at current depth
            while self.fringe:
                n = self.fringe.pop()
                
                # Check depth limit
                if n.depth >= depth:
                    cutoff = True
                else:
                    # Expand the node
                    expand_counter += 1
                    n.expand_order = expand_counter
                    n.location = Node.Location.EXPANDED
                    
                    # Generate successors in sorted order (lexicographical)
                    for s, a, c in sorted(
                        self.problem.get_successors(n.state), key=lambda x: x[0]
                    ):
                        ns = Node(s, a, cost=n.cost + c, parent=n)
                        n.add_successor(ns)
                        
                        # Goal test
                        if self.problem.is_goal_state(ns.state):
                            return Solution(
                                self.problem, roots, solution_node=ns, cutoff=cutoff
                            )
                        
                        self.fringe.push(ns)
            
            # If no cutoff occurred, we've exhausted the search space
            if not cutoff:
                return Solution(self.problem, roots, cutoff=False)
            
            # Increment depth for next iteration
            depth += 1