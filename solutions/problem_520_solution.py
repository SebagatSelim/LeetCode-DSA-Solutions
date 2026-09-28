# LeetCode Problem 520
# Language: Python 3

from collections import deque

class Solution:
    def solveProblem(self, grid: list[list[int]]) -> int:
        """
        LeetCode Problem 520: Breadth First Search (BFS)
        Time Complexity: O(M * N) | Space Complexity: O(M * N)
        """
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        queue = deque([(0, 0)])
        visited = set([(0, 0)])
        steps = 0
        
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == rows - 1 and c == cols - 1:
                    return steps
                for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            steps += 1
        return -1
