# this is a stupid question, interally trivial in swe
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # some abitrary bitwise operation
        # while b != 0:
        #     carry = a&b # Carry value is calculated 
        #     a = a^b # Sum value is calculated and stored in a
        #     b = carry<<1 # The carry value is shifted towards left by a bit
        # return a

        # only solution fast enough
        mask = 0xffffffff

        while b != 0:
            tmp = (a & b) << 1
            a = (a ^ b) & mask
            b = tmp & mask

        if a > mask // 2:
            return ~(a ^ mask)
        else:
            return a