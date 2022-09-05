class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}
        
        def dfs(i: int):
            if i in dp:
                return dp[i]
            if s[i] == '0': return 0
            
            
            res = dfs(i+1)
            # if second is valid
            if i+1<len(s) and (s[i] == '1' or (s[i] == '2' and int(s[i+1]) <= 6)): 
                res += dfs(i+2)
            
            dp[i] = res
            return res
            
        return dfs(0)