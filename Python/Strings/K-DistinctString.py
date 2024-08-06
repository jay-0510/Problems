from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # Step 1: Count the occurrences of each string
        count = {}
        for s in arr:
            if s in count:
                count[s] += 1
            else:
                count[s] = 1
        
        # Step 2: Collect distinct strings
        distinct_strings = [s for s in arr if count[s] == 1]
        
        # Step 3: Return the k-th distinct string or an empty string if not enough distinct strings
        if k <= len(distinct_strings):
            return distinct_strings[k-1]
        else:
            return ""

# Example usage
solution = Solution()
print(solution.kthDistinct(["a", "b", "a", "c", "b"], 1))  # Output: "c"
print(solution.kthDistinct(["a", "b", "a", "c", "b"], 2))  # Output: ""
print(solution.kthDistinct(["a", "b", "c", "d", "e"], 3))  # Output: "c"
print(solution.kthDistinct(["a", "a", "a"], 1))            # Output: ""
