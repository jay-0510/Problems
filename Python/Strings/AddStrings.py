class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # Initialize pointers and carry
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        result = []

        # Loop through both strings from end to start
        while i >= 0 or j >= 0 or carry:
            # Get the current digit from num1 and num2 if available
            digit1 = int(num1[i]) if i >= 0 else 0
            digit2 = int(num2[j]) if j >= 0 else 0

            # Calculate the sum of the current digits and the carry
            total = digit1 + digit2 + carry
            carry = total // 10  # Update carry
            result.append(str(total % 10))  # Append the current digit to result

            # Move to the next digits
            i -= 1
            j -= 1

        # Join the result in reverse order to form the final sum string
        return ''.join(result[::-1])

# Example usage
solution = Solution()
print(solution.addStrings("123", "456"))  # Output: "579"
print(solution.addStrings("11", "123"))   # Output: "134"
print(solution.addStrings("0", "0"))      # Output: "0"