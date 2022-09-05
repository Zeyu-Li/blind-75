class Solution:
    def rob1(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        
        for i, num in enumerate(nums):
            rob1, rob2 = rob2, max(num + rob1, rob2)
            
        return rob2
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        return max(self.rob1(nums[:-1]), self.rob1(nums[1:]))
        