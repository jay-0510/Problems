from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Helper function to merge two sorted arrays
        def merge(left: List[int], right: List[int]) -> List[int]:
            sorted_array = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    sorted_array.append(left[i])
                    i += 1
                else:
                    sorted_array.append(right[j])
                    j += 1
            # Append any remaining elements
            sorted_array.extend(left[i:])
            sorted_array.extend(right[j:])
            return sorted_array
        
        # Helper function to implement merge sort
        def merge_sort(arr: List[int]) -> List[int]:
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)
        
        return merge_sort(nums)

# Example usage
solution = Solution()
print(solution.sortArray([5, 2, 3, 1]))  # Output: [1, 2, 3, 5]
print(solution.sortArray([5, 1, 1, 2, 0, 0]))  # Output: [0, 0, 1, 1, 2, 5]