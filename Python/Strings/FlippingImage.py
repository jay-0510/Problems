class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            # Flip the row horizontally by reversing it
            row.reverse()
            
            # Invert the row: replace 0 with 1 and 1 with 0
            for i in range(len(row)):
                row[i] = 1 - row[i]  # Invert the bit using 1 - current value
        
        return image