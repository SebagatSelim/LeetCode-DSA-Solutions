# LeetCode Problem 97 Solution
# Author: Sebagat Selim

class Solution:
    def solveProblem97(self, nums: list[int], target: int) -> int:
        # Solution implementation for LeetCode Problem 97
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
        return []
