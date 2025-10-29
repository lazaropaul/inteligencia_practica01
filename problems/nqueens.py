import pygame
import random

from typing import Any

from hlogedu.search.common import ClassParameter
from hlogedu.search.problem import Problem, action, DDRange, Heuristic
from hlogedu.search.visualizer import SolutionVisualizer

# Visualization (you do not have to modify this!)
##############################################################################


class NQueensVisualizer(SolutionVisualizer):
    """Pygame-based visualizer for the N-Queens problem."""

    def draw_state(self, state: Any) -> None:
        """Draw a board with queens placed according to the given state."""
        n = self.problem.n_queens
        cell_size = self.get_cell_size()

        # Clear screen
        self.screen.fill((255, 255, 255))

        # Draw chessboard
        for row in range(n):
            for col in range(n):
                rect = pygame.Rect(
                    col * cell_size, row * cell_size, cell_size, cell_size
                )
                color = (240, 217, 181) if (row + col) % 2 == 0 else (181, 136, 99)
                pygame.draw.rect(self.screen, color, rect)

        # Draw queens
        for col, row in enumerate(state):
            center = (
                col * cell_size + cell_size // 2,
                row * cell_size + cell_size // 2,
            )
            radius = cell_size // 3
            pygame.draw.circle(self.screen, (200, 0, 0), center, radius)

        pygame.display.flip()

    def animate_transition(self, state: Any, action: Any, new_state: Any) -> None:
        """Smoothly animate the transition from one state to another."""
        n = self.problem.n_queens
        cell_size = self.get_cell_size()
        delay = self.get_delay()

        # figure out which queens moved
        moved = [
            (col, state[col], new_state[col])
            for col in range(n)
            if state[col] != new_state[col]
        ]

        if not moved:
            return  # nothing changed

        # number of steps in animation
        steps = 10

        for step in range(steps + 1):
            # interpolate state
            intermediate = list(state)
            for col, old_row, new_row in moved:
                interp_row = old_row + (new_row - old_row) * (step / steps)
                intermediate[col] = interp_row

            # draw interpolated state
            self.draw_interpolated_state(intermediate)
            pygame.time.delay(delay // max(1, steps))

        # final draw (ensure exact new state)
        self.draw_state(new_state)

    def draw_interpolated_state(self, state) -> None:
        """Draw state where row positions can be floats (for animation)."""
        n = self.problem.n_queens
        cell_size = self.get_cell_size()

        # Draw board
        self.screen.fill((255, 255, 255))
        for row in range(n):
            for col in range(n):
                rect = pygame.Rect(
                    col * cell_size, row * cell_size, cell_size, cell_size
                )
                color = (240, 217, 181) if (row + col) % 2 == 0 else (181, 136, 99)
                pygame.draw.rect(self.screen, color, rect)

        # Draw queens (supports float rows)
        for col, row in enumerate(state):
            center = (
                col * cell_size + cell_size // 2,
                int(row * cell_size + cell_size // 2),
            )
            radius = cell_size // 3
            pygame.draw.circle(self.screen, (200, 0, 0), center, radius)

        pygame.display.flip()


# Problem
##############################################################################

"""
Command cheat sheet:
    source .venv/bin/activate
    hlogedu-search run -a hlog-graph-ucs -p NQueensIR -pp n_queens=4 -pp seed=3 -o pygame -op speed=0.5
"""

class NQueensIterativeRepair(Problem):
    """N-Queens problem

    This problem consists in placing n non-attacking queens on an
    nxn chessboard.

    This implementations starts with an nxn chessboard that already
    contains N queens on it, and tries to solve the problem by iteratively
    moving the queens to different possitions
    """

    NAME = "NQueensIR"
    VISUALIZER = NQueensVisualizer
    PARAMS = [
        ClassParameter(
            name="n_queens", type=int, default="8", help="Number of queens."
        ),
        ClassParameter(name="seed", type=int, default="123456", help="Random seed."),
    ]

    def __init__(self, n_queens: int = 8, seed: int = 123456):
        super().__init__()
        self.n_queens = n_queens
        self.seed = seed
        self.b_size = max(4, self.n_queens)
        random.seed(self.seed)

    def get_start_states(self):
        return [tuple(random.randint(0, self.b_size - 1) for _ in range(self.b_size))]

    def is_goal_state(self, state):
        #No cal comprovar a columna ja que sempre sera diferent (columna == posició en la llista)
        if len(set(state)) != self.b_size: # Si no hi ha duplicats el lenght ha de ser el mateix que la mida del board
            return False
        
        # Check diagonals
        for i in range(self.b_size):
            for j in range(i + 1, self.b_size):
                if abs(i - j) == abs(state[i] - state[j]):
                    return False
    
        return True

    def is_valid_state(self, state):
        return True

    # Actions go here...
    @action(DDRange(0, 'n_queens'), DDRange(0, 'b_size'), cost=1)
    def move(self, status, queenId, boardPos):
        n_board = list(status)
        n_board[queenId] = boardPos
        return tuple(n_board)     
        

# Heuristic
##############################################################################


@NQueensIterativeRepair.heuristic
class RepairHeuristic(Heuristic):

    def compute(self, state):
        raise NotImplementedError("Implement me!")
