class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        counts = dict()
        
        l = 0
        for r, char in enumerate(s):
            counts[char] = 1 + counts.get(char, 0)
            
            while (r-l+1) - max(counts.values()) > k:
                counts[s[l]] -= 1
                l+=1
            
            res = max(res, 1 + r-l)
        
        
        return res