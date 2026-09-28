# LeetCode Problem 435
# Language: Python 3

class Solution:
    def solveProblem(self, s: str) -> int:
        """
        LeetCode Problem 435: Sliding Window / Char Count
        Time Complexity: O(N) | Space Complexity: O(1)
        """
        char_set = set()
        left = 0
        max_len = 0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len
