# LeetCode Problem 141
# Language: Python 3

class Solution:
    def solveProblem(self, nums: list[int]) -> int:
        """
        LeetCode Problem 141: Dynamic Programming / Maximum Subarray
        Time Complexity: O(N) | Space Complexity: O(1)
        """
        max_so_far = nums[0] if nums else 0
        curr_max = max_so_far
        for i in range(1, len(nums)):
            curr_max = max(nums[i], curr_max + nums[i])
            max_so_far = max(max_so_far, curr_max)
        return max_so_far
