# LeetCode Problem 401
# Language: Python 3

class Solution:
    def solveProblem(self, nums: list[int], target: int) -> list[int]:
        """
        LeetCode Problem 401: Hash Map Approach
        Time Complexity: O(N) | Space Complexity: O(N)
        """
        seen = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in seen:
                return [seen[diff], i]
            seen[val] = i
        return []
