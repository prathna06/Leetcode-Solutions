# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def goodNodes(self, root: TreeNode) -> int:
        counter = 0
        def dfs(root,maxNum):
            nonlocal counter
            if root is None:
                return          
            
            if maxNum <= root.val:
                maxNum = root.val
                counter += 1

            dfs(root.left,maxNum)
            dfs(root.right,maxNum)
        
        route =[]

        dfs(root,root.val)
        return counter

            
