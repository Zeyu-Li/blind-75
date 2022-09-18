class Solution:
    def isPalindrome(self, s: str) -> bool:
        # step 1 filter
        newStr = ''
        
        for char in s:
            if char.isalnum():
                newStr += char.lower()
                
        return newStr == newStr[::-1]