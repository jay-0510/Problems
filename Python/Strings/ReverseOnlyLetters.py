class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # Convert the string to a list to allow in-place modifications
        s_list = list(s)
        
        # Initialize two pointers
        left, right = 0, len(s) - 1
        
        while left < right:
            # Move the left pointer if it's not pointing to a letter
            if not s_list[left].isalpha():
                left += 1
            # Move the right pointer if it's not pointing to a letter
            elif not s_list[right].isalpha():
                right -= 1
            # Both pointers are pointing to letters, so swap them
            else:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
        
        # Convert the list back to a string and return it
        return ''.join(s_list)

# Example usage
solution = Solution()
print(solution.reverseOnlyLetters("ab-cd"))      # Output: "dc-ba"
print(solution.reverseOnlyLetters("a-bC-dEf-ghIj"))  # Output: "j-Ih-gfE-dCba"
print(solution.reverseOnlyLetters("Test1ng-Leet=code-Q!"))  # Output: "Qedo1ct-eeLg=ntse-T!"