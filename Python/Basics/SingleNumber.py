from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0
        for num in nums:
            single ^= num
        return single

# Example usage
solution = Solution()
print(solution.singleNumber([2, 2, 1]))  # Output: 1
print(solution.singleNumber([4, 1, 2, 1, 2]))  # Output: 4
print(solution.singleNumber([1]))  # Output: 1