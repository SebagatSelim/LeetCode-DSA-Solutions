# LeetCode Problem 142
# Language: Python 3

class Solution:
    def solveProblem(self, head) -> bool:
        """
        LeetCode Problem 142: Fast & Slow Pointer (Floyd's Cycle Detection)
        Time Complexity: O(N) | Space Complexity: O(1)
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
