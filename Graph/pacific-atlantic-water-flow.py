class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # cache each cell to not redo work
        # dp = [[0 for _ in range(len(heights))] for _ in range(len(heights[0]))]
        
        row, col = len(heights), len(heights[0])
        
        pac, atl = set(), set()
        
        def dfs(r: int, c: int, visit: set, prevHeight: int):
            # bound check
            if (r, c) in visit or r < 0 or c < 0 or r == row or c == col or heights[r][c] < prevHeight: return
            
            visit.add((r,c))
            # test all four directions
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])
        
        for i in range(col):
            dfs(0, i, pac, heights[0][i])
            dfs(row-1, i, atl, heights[row-1][i])
        for i in range(row):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, col-1, atl, heights[i][col-1])
                
        res = []
        
        for r in range(row):
            for c in range(col):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        
        return res
        