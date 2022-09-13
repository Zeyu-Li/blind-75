class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        done = []
        l, t = 0, 0
        r, b = len(matrix[0]), len(matrix)
        
        while l < r and t < b:
            # get every value in order
            for i in range(l, r):
                done.append(matrix[t][i])
            t +=1
            
            for i in range(t, b):
                done.append(matrix[i][r-1])
            r -=1
            
            # it might break halfway through so check condition again
            if not (l < r and t < b): break
            
            for i in range(r-1, l-1, -1):
                done.append(matrix[b-1][i])
            b -=1
            
            for i in range(b-1, t-1, -1):
                done.append(matrix[i][l])
            l +=1
        
        return done