# LeetCode Problem 92
# Language: Python 3

class Solution:
    def solveProblem(self, s: str) -> bool:
        """
        LeetCode Problem 92: Stack-Based Evaluation
        Time Complexity: O(N) | Space Complexity: O(N)
        """
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                top = stack.pop() if stack else '#'
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)
        return not stack
