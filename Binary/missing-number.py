class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # use formula
        return n * (n+1) // 2 - sum(nums)
#         res = nums[0]
#         for i in range(1, len(nums)):
#             res ^= nums[i]
#         for item in range(len(nums)):
#             res ^= item
            
#         return res if res != 0 else len(nums)