from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []
        
        # Initialize Pascal's triangle with the first row
        triangle = [[1]]
        
        for i in range(1, numRows):
            prev_row = triangle[-1]
            new_row = [1]
            
            # Generate the new row by summing adjacent elements from the previous row
            for j in range(1, len(prev_row)):
                new_row.append(prev_row[j - 1] + prev_row[j])
            
            # Append 1 at the end of the new row
            new_row.append(1)
            
            # Add the new row to the triangle
            triangle.append(new_row)
        
        return triangle

# Example usage
solution = Solution()
print(solution.generate(5))