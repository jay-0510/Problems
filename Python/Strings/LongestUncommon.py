class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        # If the strings are the same, there is no uncommon subsequence
        if a == b:
            return -1
        # If the strings are different, the longer string is the longest uncommon subsequence
        return max(len(a), len(b))

# Example usage
solution = Solution()
print(solution.findLUSlength("abc", "def"))  # Output: 3
print(solution.findLUSlength("aaa", "aaa"))  # Output: -1
print(solution.findLUSlength("abc", "abcd"))  # Output: 4