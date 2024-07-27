from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        # Start with the first row
        row = [1]
        
        for i in range(1, rowIndex + 1):
            # Initialize the new row with 1s
            new_row = [1] * (i + 1)
            
            # Calculate the values for the new row
            for j in range(1, i):
                new_row[j] = row[j - 1] + row[j]
            
            # Move to the next row
            row = new_row
        
        return row

# Example usage
solution = Solution()
print(solution.getRow(3))  # Output: [1, 3, 3, 1]
print(solution.getRow(4))  # Output: [1, 4, 6, 4, 1]