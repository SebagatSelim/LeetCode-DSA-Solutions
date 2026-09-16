# LeetCode Problem 367 Solution
# Author: Sebagat Selim

class Solution:
    def solveProblem367(self, nums: list[int], target: int) -> int:
        # Solution implementation for LeetCode Problem 367
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
        return []
