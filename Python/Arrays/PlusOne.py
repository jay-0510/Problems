from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # Start from the last digit and move backward
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If digit is 9, set it to 0
            digits[i] = 0
        
        # If all digits are 9, we need to add an extra digit at the beginning
        return [1] + digits

# Example usage
solution = Solution()
print(solution.plusOne([1, 2, 3]))  # Output: [1, 2, 4]
print(solution.plusOne([9, 9, 9]))  # Output: [1, 0, 0, 0]