from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Initialize the index for the unique elements
        unique_index = 1
        
        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # If the current element is different from the previous element
            if nums[i] != nums[i - 1]:
                # Place it at the unique_index and increment the unique_index
                nums[unique_index] = nums[i]
                unique_index += 1
        
        # Return the number of unique elements
        return unique_index

# Example usage
solution = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
k = solution.removeDuplicates(nums)
print(k)  # Output: 5
print(nums[:k])  # Output: [0, 1, 2, 3, 4]