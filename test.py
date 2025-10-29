from typing import List


def solveNQueens(n: int) -> List[List[str]]:
    solutions = []
    def solver(currentState, size):
        if len(currentState) == size:
            solutions.append(currentState[:])
            return currentState
        
        for i in range(n):
            if is_safe(currentState, len(currentState), i):
                print(currentState)
                currentState.append(i)
                solver(currentState, size)
                currentState.pop()
                
    def is_safe(board, row, col):
        for r in range(row):
            print(board)
            c = board[r]
            # Check same column
            if c == col:
                return False
            # Check diagonals
            if abs(c - col) == abs(r - row):
                return False
        return True

if __name__ == "__main__":
    solveNQueens(4)