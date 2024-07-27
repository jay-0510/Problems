class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        # Initialize the base cases
        first = 1
        second = 2
        
        # Compute the number of ways to reach each subsequent step
        for i in range(3, n + 1):
            third = first + second
            first = second
            second = third
        
        return second

# Example usage
solution = Solution()
print(solution.climbStairs(2))  # Output: 2
print(solution.climbStairs(3))  # Output: 3
print(solution.climbStairs(4))  # Output: 5