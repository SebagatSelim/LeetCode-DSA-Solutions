# LeetCode Problem 310 Solution
# Author: Sebagat Selim

class Solution:
    def solveProblem310(self, nums: list[int], target: int) -> int:
        # Solution implementation for LeetCode Problem 310
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
        return []
