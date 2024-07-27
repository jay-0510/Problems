from typing import Counter, List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
         # Count the frequency of each element in nums
        freq = Counter(nums)
        
        # Sort based on frequency first (increasing order) and then by value (decreasing order)
        nums.sort(key=lambda x: (freq[x], -x))
        
        return nums

# Example usage
solution = Solution()
print(solution.frequencySort([1,1,2,2,2,3]))  # Output: [3,1,1,2,2,2]
print(solution.frequencySort([2,3,1,3,2]))    # Output: [1,3,3,2,2]
print(solution.frequencySort([-1,1,-6,4,5,-6,1,4,1]))  # Output: [5,-1,4,4,-6,-6,1,1,1]