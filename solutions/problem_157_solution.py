# LeetCode Problem 157 Solution
# Author: Sebagat Selim

class Solution:
    def solveProblem157(self, nums: list[int], target: int) -> int:
        # Solution implementation for LeetCode Problem 157
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
        return []
