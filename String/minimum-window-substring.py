class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0: return ""
        
        counts, window = {}, {}
        
        for c in t:
            counts[c] = 1 + counts.get(c, 0)
        
        have, need = 0, len(counts)
        
        res, resLen = [-1, -1], 1000000
        
        l=0
        # window
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            
            if c in counts and window[c] == counts[c]:
                have += 1
                
            while have == need:
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                    
                window[s[l]] -= 1
                if s[l] in counts and window[s[l]] < counts[s[l]]:
                    have-=1
                l+=1
        
        
        return s[res[0]: res[1]+1] if resLen != 1000000 else ""
        