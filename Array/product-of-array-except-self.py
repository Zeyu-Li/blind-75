class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1] * len(nums)
        
        for i in range(len(nums)-1):
            left.append(left[i] * nums[i])
            
        for j in range(len(nums)-1):
            right[len(nums)-j-2] = right[len(nums)-j-1] * nums[len(nums)-j-1]
            
        newList = []
        for a, b in zip(left, right):
            newList.append(a*b)
            
        return newList