# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def longestZigZag(self, root: Optional[TreeNode]) -> int:
    #     counter = 0
    #     maxVal = 0
    #     def calDepth(root,direction):
    #         nonlocal counter
    #         if direction and root.left :
    #             counter += 1
    #             calDepth(root.left,False)
    #         elif root.right and not direction:
    #             counter +=1
    #             calDepth(root.right,True)
    #         return counter    
            
    #     def dfs(root):
    #         nonlocal maxVal
    #         nonlocal counter 
    #         counter = 0
    #         if root is None:
    #             return
    #         maxVal = max(maxVal,calDepth(root,True))  
    #         counter = 0  
    #         maxVal = max(maxVal,calDepth(root,False))    
    #         dfs(root.left)
    #         dfs(root.right)           
    #     dfs(root)
    #     return maxValif not node:
    def longestZigZag(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, left_len: int, right_len: int, max_len: int) -> int:
            if not node:
                return max_len
            max_len = max(max_len, left_len, right_len)
            return max(
                dfs(node.left, 0, left_len + 1, max_len),
                dfs(node.right, right_len + 1, 0, max_len),
            )
        return dfs(root, 0, 0, 0)
        