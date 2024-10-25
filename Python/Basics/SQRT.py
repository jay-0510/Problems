class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        left, right = 1, x
        
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        
        # Since we are rounding down, the result is right
        return right

# Example usage
solution = Solution()
print(solution.mySqrt(4))    # Output: 2
print(solution.mySqrt(8))    # Output: 2
print(solution.mySqrt(16))   # Output: 4
print(solution.mySqrt(0))    # Output: 0
print(solution.mySqrt(1))    # Output: 1