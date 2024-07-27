from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Pointer for the position of the next element that is not equal to val
        k = 0

        # Iterate over all the elements in the array
        for i in range(len(nums)):
            # If the current element is not equal to val
            if nums[i] != val:
                # Move it to the position pointed to by k
                nums[k] = nums[i]
                # Increment k
                k += 1
        
        # Return the number of elements that are not equal to val
        return k

# Example usage
solution = Solution()
nums = [3, 2, 2, 3]
val = 3
k = solution.removeElement(nums, val)
print(k)  # Output: 2
print(nums[:k])  # Output: [2, 2]

nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
k = solution.removeElement(nums, val)
print(k)  # Output: 5
print(nums[:k])  # Output: [0, 1, 3, 0, 4]