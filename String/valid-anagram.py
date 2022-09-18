class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        # count instances of letters
        a = dict()
        b = dict()
        for char1, char2 in zip(s,t):
            if char1 in a: a[char1] += 1
            else: a[char1] = 1
            if char2 in b: b[char2] += 1
            else: b[char2] = 1
                
        if len(a) != len(b): return False
        
        for k, v in a.items():
            if v != b.get(k, 0): return False
            
        return True