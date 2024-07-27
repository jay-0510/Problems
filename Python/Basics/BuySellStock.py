from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
         # Initialize the minimum price to a large value
        min_price = float('inf')
        # Initialize the maximum profit to 0
        max_profit = 0
        
        # Iterate through the list of prices
        for price in prices:
            # Update the minimum price if the current price is lower
            if price < min_price:
                min_price = price
            # Calculate the current profit and update the maximum profit if necessary
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit

# Example usage
solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))  # Output: 5
print(solution.maxProfit([7,6,4,3,1]))    # Output: 0