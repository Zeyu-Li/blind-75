class Solution:
    def canJump(self, nums: List[int]) -> bool:
        currMax = 1
        # paint in
        for i in range(len(nums) - 1):
            currMax-=1
            currMax = max(currMax, nums[i])
            if currMax == 0:
                return False
            
        return True