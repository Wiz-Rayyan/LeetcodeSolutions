
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # Initially set to infinity
        max_profit = 0  # Maximum profit found so far
        
        for price in prices:
            min_price = min(min_price, price)  # Update min price
            max_profit = max(max_profit, price - min_price)  # Calculate and update max profit

        return max_profit
