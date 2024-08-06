from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
         # Sort both arrays and compare them
        return sorted(target) == sorted(arr)

# Example usage
solution = Solution()
print(solution.canBeEqual([1,2,3,4], [2,4,1,3]))  # Output: True
print(solution.canBeEqual([1,2,3,4], [2,4,1,5]))  # Output: False