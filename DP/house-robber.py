class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        
        for i, num in enumerate(nums):
            rob1, rob2 = rob2, max(num + rob1, rob2)
            
        return rob2