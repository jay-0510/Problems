class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        count = 0  # Counter to track the number of flowers that can be planted
        length = len(flowerbed)
        
        for i in range(length):
            if flowerbed[i] == 0:
                # Check if the previous and next plots are empty or if the plot is at the boundary
                prev_empty = (i == 0) or (flowerbed[i - 1] == 0)
                next_empty = (i == length - 1) or (flowerbed[i + 1] == 0)
                
                if prev_empty and next_empty:
                    flowerbed[i] = 1  # Plant a flower here
                    count += 1
                    if count >= n:
                        return True
        
        return count >= n