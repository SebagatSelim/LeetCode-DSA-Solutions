# LeetCode Problem 573 Solution
# Author: Sebagat Selim

class Solution:
    def solveProblem573(self, nums: list[int], target: int) -> int:
        # Solution implementation for LeetCode Problem 573
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
        return []
