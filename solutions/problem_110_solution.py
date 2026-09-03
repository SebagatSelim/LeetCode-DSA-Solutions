# LeetCode Problem 110 Solution
# Author: Sebagat Selim

class Solution:
    def solveProblem110(self, nums: list[int], target: int) -> int:
        # Solution implementation for LeetCode Problem 110
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
        return []
