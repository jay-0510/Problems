from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            # Swap the elements at the left and right pointers
            s[left], s[right] = s[right], s[left]
            # Move the pointers towards the center
            left += 1
            right -= 1

# Example usage
solution = Solution()
arr = ["h", "e", "l", "l", "o"]
solution.reverseString(arr)
print(arr)  # Output: ["o", "l", "l", "e", "h"]