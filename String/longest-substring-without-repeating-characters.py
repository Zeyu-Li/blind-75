class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        biggest = 0
        items = set()
        
        l = 0
        
        for i, char in enumerate(s):
            while s[i] in items:
                items.remove(s[l])
                l+=1
                
            items.add(s[i])
            
            biggest = max(biggest, i-l+1)
            
        return biggest