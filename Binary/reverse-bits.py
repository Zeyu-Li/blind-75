class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res |= ((n >> i) & 1) << (31-i)
            
        return res
        # one = 1
        # res = 0
        # curr = 31
        # while one != 0 and curr > 0:
        #     res |= ((n >> one) & 1) << (curr)
        #     curr-=1
        #     one <<= 1
        # return res