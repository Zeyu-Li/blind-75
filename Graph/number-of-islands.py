class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def floodfill(grid: List[List[str]], i: int, j: int):
            stack = []
            
            stack.append((i, j))
            
            while len(stack):
                fill = stack.pop()
                
                # test if out of bounds or zero
                if not (0 <= fill[0] < len(grid)): continue
                if not (0 <= fill[1] < len(grid[0])): continue
                if (grid[fill[0]][fill[1]] == '0'): continue
                    
                grid[fill[0]][fill[1]] = '0'
                # flood fill the 4 directions
                stack.append((fill[0] + 1, fill[1]))
                stack.append((fill[0] - 1, fill[1]))
                stack.append((fill[0], fill[1] + 1))
                stack.append((fill[0], fill[1] - 1))
        
        count = 0
        
        for i, row in enumerate(grid):
            for j, item in enumerate(row):
                if item != "0":
                    count+=1
                    floodfill(grid, i, j)
                    
                    
        return count
    