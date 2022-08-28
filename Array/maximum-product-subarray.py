class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best = max(nums)
        currMax, currMin = 1, 1
        
        for num in nums:
            if num == 0:
                currMax, currMin = 1, 1
                continue
                
            tmp = currMax*num
            currMax = max(num, tmp, currMin*num)
            currMin = min(num, tmp, currMin*num)
            
            best = max(best, currMax)
            
        return best
        