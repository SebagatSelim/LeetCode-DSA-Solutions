# LeetCode Problem 600 Solution
# Author: Sebagat Selim

class Solution:
    def solveProblem600(self, nums: list[int], target: int) -> int:
        # Solution implementation for LeetCode Problem 600
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
        return []
