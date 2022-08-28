class Solution:    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, num in enumerate(nums):
            # if equal to previous skip
            if i > 0 and num == nums[i-1]: continue
                
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = num + nums[l] + nums[r]
                
                if threeSum == 0:
                    res.append([num, nums[l], nums[r]])
                    l+=1
                    # shift more if they are the same
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
                elif threeSum > 0:
                    r-=1
                else:
                    l+=1
            
        return res