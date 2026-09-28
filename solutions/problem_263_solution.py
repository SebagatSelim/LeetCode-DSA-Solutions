# LeetCode Problem 263
# Language: Python 3

class Solution:
    def solveProblem(self, root) -> int:
        """
        LeetCode Problem 263: Depth First Search (DFS) / Maximum Depth
        Time Complexity: O(N) | Space Complexity: O(H)
        """
        if not root:
            return 0
        left_depth = self.solveProblem(root.left)
        right_depth = self.solveProblem(root.right)
        return 1 + max(left_depth, right_depth)
