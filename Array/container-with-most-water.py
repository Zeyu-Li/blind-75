class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_water = 0
        
        while l < r:
            canidate_max = min(height[l], height[r]) * (r-l)
            
            if canidate_max > max_water:
                max_water = canidate_max

            if height[l] > height[r]:
                r-=1
            else:
                l+=1
            
        return max_water
            