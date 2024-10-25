class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            # Check the last bit of n
            count += n & 1
            # Shift n to the right by 1 to check the next bit
            n >>= 1
        return count

# Example usage
solution = Solution()
print(solution.hammingWeight(11))  # Output: 3, because 11 in binary is 1011, which has three 1s