# LeetCode Problem 154
# Language: Python 3

# LeetCode Problem 154 Solution
# Topic: Data Structures & Algorithms

class Solution:
    def solveProblem(self, data: list) -> int:
        """
        Optimal implementation for LeetCode Problem 154
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        if not data:
            return 0
        
        # Algorithmic Logic
        result = 0
        left, right = 0, len(data) - 1
        while left < right:
            current_sum = data[left] + data[right]
            result = max(result, current_sum)
            left += 1
            right -= 1
            
        return result
