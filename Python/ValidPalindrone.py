class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Function to check if a character is alphanumeric
        def is_alphanumeric(c):
            return c.isalnum()
        
        # Convert string to lowercase and filter out non-alphanumeric characters
        filtered_chars = [c.lower() for c in s if is_alphanumeric(c)]
        
        # Use two pointers to check for palindrome
        left, right = 0, len(filtered_chars) - 1
        
        while left < right:
            if filtered_chars[left] != filtered_chars[right]:
                return False
            left += 1
            right -= 1
        
        return True

# Example usage
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
print(solution.isPalindrome("race a car"))  # Output: False