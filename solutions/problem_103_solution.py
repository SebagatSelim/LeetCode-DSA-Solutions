# LeetCode Problem 103 Solution
# Author: Sebagat Selim

class Solution:
    def solveProblem103(self, nums: list[int], target: int) -> int:
        # Solution implementation for LeetCode Problem 103
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
        return []
