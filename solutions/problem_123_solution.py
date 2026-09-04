# LeetCode Problem 123 Solution
# Author: Sebagat Selim

class Solution:
    def solveProblem123(self, nums: list[int], target: int) -> int:
        # Solution implementation for LeetCode Problem 123
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
        return []
