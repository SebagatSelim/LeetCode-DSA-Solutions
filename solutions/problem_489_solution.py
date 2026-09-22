# LeetCode Problem 489 Solution
# Author: Sebagat Selim

class Solution:
    def solveProblem489(self, nums: list[int], target: int) -> int:
        # Solution implementation for LeetCode Problem 489
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
        return []
