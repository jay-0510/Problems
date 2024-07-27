from typing import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        length = 0
        odd_found = False
        
        for char, freq in count.items():
            if freq % 2 == 0:
                length += freq
            else:
                length += freq - 1
                odd_found = True
        
        if odd_found:
            length += 1
        
        return length

# Example usage
solution = Solution()
print(solution.longestPalindrome("abccccdd"))  # Output: 7
print(solution.longestPalindrome("a"))         # Output: 1
print(solution.longestPalindrome("bb"))        # Output: 2