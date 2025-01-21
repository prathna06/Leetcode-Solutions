# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def goodNodes(self, root: TreeNode) -> int:
        counter = 0
        def dfs(root):
            nonlocal counter
            if root is None:
                return          
            route.append(root.val)
            if max(route) <= root.val:
                counter += 1
            dfs(root.left)
            dfs(root.right)
            route.pop()
        
        route =[]

        dfs(root)
        return counter

            
