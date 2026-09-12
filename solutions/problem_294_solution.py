# LeetCode Problem 294 Solution
# Author: Sebagat Selim

class Solution:
    def solveProblem294(self, nums: list[int], target: int) -> int:
        # Solution implementation for LeetCode Problem 294
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
        return []
