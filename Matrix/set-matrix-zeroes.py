class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = [False for _ in range(len(matrix))]
        columns = [False for _ in range(len(matrix[0]))]
        
        for i, row in enumerate(matrix):
            for j, item in enumerate(row):
                if item == 0:
                    rows[i] = True
                    columns[j] = True
            
        for i, row in enumerate(rows):
            for j, column in enumerate(columns):
                if row or column:
                    matrix[i][j] = 0
                    
                
                