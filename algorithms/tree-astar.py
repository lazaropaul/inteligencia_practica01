from hlogedu.search.algorithm import Algorithm, Node, Solution
from hlogedu.search.containers import PriorityQueue


class AStarTree(Algorithm):
    """
    A* Tree Search
    Utilitzem f(n) = g(n) + h(n) on:
        g(n) es el cost del inici des de n
        h(n) es la estimació heuristica desde n fins l'objectiu
    
        La heuristica ha de ser admissible
    """
    NAME = "my-tree-astar"
    
    def __init__(self, problem):
        super().__init__(problem)
        self.fringe = PriorityQueue()
    
    def run(self, heuristic):
        expand_counter = 0
        
        # Creem root nodes a partir dels estats inicials
        roots = [Node(s) for s in self.problem.get_start_states()]
        
        # Comprovem si root es un estat final i l'afegim a fringe
        for n in roots:
            if self.problem.is_goal_state(n.state):
                return Solution(self.problem, roots, solution_node=n)
            
            # f(n) = g(n) + h(n)
            f_n = n.cost + heuristic(n.state)
            self.fringe.push(n, f_n)
        
        # search loop
        while self.fringe:
            n = self.fringe.pop()
            
            # Expandim el node
            expand_counter += 1
            n.expand_order = expand_counter
            n.location = Node.Location.EXPANDED
            
            # Goal test quan expanding
            if self.problem.is_goal_state(n.state):
                return Solution(self.problem, roots, solution_node=n)
            
            # Generem successors en ordre lexicografic
            for s, a, c in sorted(
                self.problem.get_successors(n.state), key=lambda x: x[0]
            ):
                ns = Node(s, a, cost=n.cost + c, parent=n)
                n.add_successor(ns)
                
                 # Comprovem si es estat final
                if self.problem.is_goal_state(ns.state):
                    return Solution(self.problem, roots, solution_node=ns)
                
                # f(ns) = g(ns) + h(ns)
                f_ns = ns.cost + heuristic(ns.state)
                self.fringe.push(ns, f_ns)
        
        # No hem trobat solucio
        return Solution(self.problem, roots)