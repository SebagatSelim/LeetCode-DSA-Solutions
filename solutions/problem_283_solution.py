# LeetCode Problem 283 Solution
# Author: Sebagat Selim

class Solution:
    def solveProblem283(self, nums: list[int], target: int) -> int:
        # Solution implementation for LeetCode Problem 283
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
        return []
