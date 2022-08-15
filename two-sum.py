class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = dict()
        for i, num in enumerate(nums):
            if num in cache:
                return [cache[num], i]
            else:
                cache[target-num] = i
            