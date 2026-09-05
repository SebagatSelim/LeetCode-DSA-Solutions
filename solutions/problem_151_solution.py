# LeetCode Problem 151 Solution
# Author: Sebagat Selim

class Solution:
    def solveProblem151(self, nums: list[int], target: int) -> int:
        # Solution implementation for LeetCode Problem 151
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
        return []
