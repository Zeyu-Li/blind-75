class Solution:
    def countBits(self, n: int) -> List[int]:
        nums = []
        for i in range(n+1): 
            count = 0

            while i:
                i &= (i - 1)
                count+=1

            nums.append(count)
        return nums
        