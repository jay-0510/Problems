class Solution:
    def romanToInt(self, s: str) -> int:
         # Dictionary to map Roman numerals to integers
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        # Initialize the integer value
        total = 0
        # Iterate through the characters of the string
        for i in range(len(s)):
            # If this character is less than the next character, subtract its value
            if i + 1 < len(s) and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                total -= roman_to_int[s[i]]
            else:
                # Otherwise, add its value
                total += roman_to_int[s[i]]
        
        return total

# Example usage
solution = Solution()
print(solution.romanToInt("III"))    # Output: 3
print(solution.romanToInt("IV"))     # Output: 4
print(solution.romanToInt("IX"))     # Output: 9
print(solution.romanToInt("LVIII"))  # Output: 58
print(solution.romanToInt("MCMXCIV"))# Output: 1994