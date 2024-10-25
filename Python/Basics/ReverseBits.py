class Solution:
    def reverseBits(self, n: int) -> int:
         result = 0
         for i in range(32):
            # Extract the least significant bit of n and add it to result
            result = (result << 1) | (n & 1)
            # Shift n to the right to process the next bit
            n >>= 1
         return result

# Example usage
solution = Solution()
print(solution.reverseBits(43261596))  # Output: 964176192
print(solution.reverseBits(4294967293))  # Output: 3221225471