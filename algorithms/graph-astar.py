from hlogedu.search.algorithm import Algorithm, Node, Solution
from hlogedu.search.containers import PriorityQueue


class AStarGraph(Algorithm):
    """
    A* Graph Search
    Uses f(n) = g(n) + h(n) where:
    - g(n) is the cost from start to n
    - h(n) is the heuristic estimate from n to goal
    
    Requires h(n) to be consistent (monotonic):
    h(n) <= cost(n, n') + h(n') for all successors n'
    
    Tracks expanded states to avoid revisiting nodes
    """
    NAME = "my-astar-graph"
    
    def __init__(self, problem):
        super().__init__(problem)
        self.fringe = PriorityQueue()
    
    def run(self, heuristic):
        """
        Run A* Graph Search with a heuristic function
        
        Args:
            heuristic: Function that takes a state and returns h(n)
            
        Returns:
            Solution object
        """
        expand_counter = 0
        expanded = set()  # Track expanded states to avoid cycles
        
        # Create root nodes from initial states
        roots = [Node(s) for s in self.problem.get_start_states()]
        
        # Check if any root is a goal and add to fringe
        for n in roots:
            if self.problem.is_goal_state(n.state):
                return Solution(self.problem, roots, solution_node=n)
            
            # Calculate f(n) = g(n) + h(n)
            f_n = n.cost + heuristic(n.state)
            self.fringe.push(n, f_n)
        
        # Main search loop
        while self.fringe:
            n = self.fringe.pop()
            
            # Skip if already expanded (important for graph search!)
            if n.state in expanded:
                continue
            
            # Goal test when expanding
            if self.problem.is_goal_state(n.state):
                return Solution(self.problem, roots, solution_node=n)
            
            # Mark as expanded
            expand_counter += 1
            n.expand_order = expand_counter
            n.location = Node.Location.EXPANDED
            expanded.add(n.state)
            
            # Generate successors in sorted order (lexicographical)
            for s, a, c in sorted(
                self.problem.get_successors(n.state), key=lambda x: x[0]
            ):
                # Only generate successor if not already expanded
                if s not in expanded:
                    ns = Node(s, a, cost=n.cost + c, parent=n)
                    n.add_successor(ns)
                    
                    # Calculate f(ns) = g(ns) + h(ns)
                    f_ns = ns.cost + heuristic(ns.state)
                    self.fringe.push(ns, f_ns)
        
        # No solution found
        return Solution(self.problem, roots)
    
