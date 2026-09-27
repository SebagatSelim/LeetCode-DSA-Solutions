# LeetCode Problem 585 Solution
# Author: Sebagat Selim

class Solution:
    def solveProblem585(self, nums: list[int], target: int) -> int:
        # Solution implementation for LeetCode Problem 585
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
        return []
