class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # you can alternatively do a radix sort in O(n) then scan linearly
        
        # set with O(1) lookup
        cache = set(nums)
        
        _max = 0
        
        for num in nums:
            if num - 1 not in cache:
                currMax = 1
                currNum = num
                while currNum + 1 in cache:
                    currMax += 1
                    currNum += 1
                    
                
                _max = max(_max, currMax)
                
                
        return _max
        