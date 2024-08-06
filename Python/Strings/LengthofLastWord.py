class Solution:
    def lengthOfLastWord(self, s: str) -> int:
         # Strip trailing spaces and split the string by spaces
        words = s.strip().split(' ')
        # Return the length of the last word
        return len(words[-1])

# Example usage
solution = Solution()
print(solution.lengthOfLastWord("Hello World"))  # Output: 5
print(solution.lengthOfLastWord("   fly me   to   the moon  "))  # Output: 4
print(solution.lengthOfLastWord("luffy is still joyboy"))  # Output: 6