class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        _min = prices[0]
        best = 0
        for price in prices:
            best = max(best, price-_min)
            _min = min(price, _min)
            
        return best