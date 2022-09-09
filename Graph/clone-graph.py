"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = dict()
        
#         root = Node(node.val)
        
#         visited[node.val] = root
        
        # dfs of graph
        def dfs(curr: 'Node') -> bool:
            if curr in visited: return visited[curr]
            
            copy = Node(curr.val)
            visited[curr] = copy
            
            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))
                
            return copy
        
        return dfs(node) if node else None
    