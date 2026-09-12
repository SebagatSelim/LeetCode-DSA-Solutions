# LeetCode Problem 290 Solution
# Author: Sebagat Selim

class Solution:
    def solveProblem290(self, nums: list[int], target: int) -> int:
        # Solution implementation for LeetCode Problem 290
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
        return []
