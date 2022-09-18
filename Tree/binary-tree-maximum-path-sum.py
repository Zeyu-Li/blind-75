# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # take max of each branch and add root if it adds to max total
#         if not root: return 0
#         if not (root.left and root.right): return root.val
        
#         l = self.maxPathSum(root.left)
#         r = self.maxPathSum(root.right)
        
#         return max(root.val, l + root.val + r, l + root.val, r + root.val, l, r)# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

        res = [root.val]
        
        def dfs(root: Optional[TreeNode]):
            if not root: return 0

            l = max(dfs(root.left), 0)
            r = max(dfs(root.right), 0)

            # res[0] = max(root.val, l + root.val + r, l + root.val, r + root.val, l, r)
            res[0] = max(res[0], root.val + l + r)
            
            return root.val + max(l, r)
        
        dfs(root)
        
        return res[0]