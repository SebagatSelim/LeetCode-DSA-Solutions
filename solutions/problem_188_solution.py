# LeetCode Problem 188 Solution
# Author: Sebagat Selim

class Solution:
    def solveProblem188(self, nums: list[int], target: int) -> int:
        # Solution implementation for LeetCode Problem 188
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
        return []
