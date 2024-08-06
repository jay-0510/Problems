class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0
        # XOR all characters in both strings
        for char in s + t:
            result ^= ord(char)
        # Convert the result back to a character
        return chr(result)

# Example usage
solution = Solution()
print(solution.findTheDifference("abcd", "abcde"))  # Output: "e"
print(solution.findTheDifference("", "y"))  # Output: "y"
print(solution.findTheDifference("a", "aa"))  # Output: "a"