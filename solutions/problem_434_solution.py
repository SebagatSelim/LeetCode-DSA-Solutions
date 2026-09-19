# LeetCode Problem 434 Solution
# Author: Sebagat Selim

class Solution:
    def solveProblem434(self, nums: list[int], target: int) -> int:
        # Solution implementation for LeetCode Problem 434
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
        return []
