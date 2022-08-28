class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        _max = nums[0]
        candidate = _max
        for i in range(1, len(nums)):
            candidate = max(nums[i], candidate+nums[i])
            _max = max(_max, candidate)
            
        return _max