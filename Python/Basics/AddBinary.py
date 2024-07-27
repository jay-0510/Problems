class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        
        # Pointers for a and b
        i, j = len(a) - 1, len(b) - 1
        
        while i >= 0 or j >= 0 or carry:
            total_sum = carry
            if i >= 0:
                total_sum += int(a[i])
                i -= 1
            if j >= 0:
                total_sum += int(b[j])
                j -= 1
            
            # Compute the current bit and the new carry
            result.append(str(total_sum % 2))
            carry = total_sum // 2
        
        # Since we added bits in reverse order, reverse the result list
        return ''.join(result[::-1])

# Example usage
solution = Solution()
print(solution.addBinary("1010", "1011"))  # Output: "10101"
print(solution.addBinary("11", "1"))  # Output: "100"