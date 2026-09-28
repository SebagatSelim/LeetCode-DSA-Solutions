# LeetCode Problem 458
# Language: Python 3

class Solution:
    def solveProblem(self, nums: list[int], target: int) -> int:
        """
        LeetCode Problem 458: Binary Search
        Time Complexity: O(log N) | Space Complexity: O(1)
        """
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
