# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

mx=0
class Solution:
    
    def dfs(self,node,c):
        global mx
        l=r=c
        
        if node.left:
            l=self.dfs(node.left,c+1)
        if node.right:
            r=self.dfs(node.right,c+1)
            
        if mx<l+r-2*c:
        
            mx=l+r-2*c
        return max(r,l)
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        global mx
        mx=0
        r=l=0
        
        if root:
            if root.left:
                l=self.dfs(root.left,1)
            if root.right:
                r=self.dfs(root.right,1)
        
        
        return max(mx,r+l)
        
