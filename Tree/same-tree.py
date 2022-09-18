# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # dfs at the same time
        if p == None:
            if q == None: return True
            else: return False
        else:
            if q == None: return False
            else: return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            
        # return (self.isSameTree(p.left) and self.isSameTree(q.left)) and (self.isSameTree(p.right) and self.isSameTree(q.right))