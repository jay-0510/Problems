from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Pair each name with its corresponding height
        people = list(zip(names, heights))
        
        # Sort the list of pairs based on the height in descending order
        people.sort(key=lambda x: x[1], reverse=True)
        
        # Extract the sorted names
        sorted_names = [person[0] for person in people]
        
        return sorted_names

# Example usage
solution = Solution()
names = ["Mary", "John", "Emma"]
heights = [180, 165, 170]
print(solution.sortPeople(names, heights))  # Output: ['Mary', 'Emma', 'John']