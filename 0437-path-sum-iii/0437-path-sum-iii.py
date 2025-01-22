# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
#         counter = 0
#         def dfs(root,targetSum):
#             nonlocal counter
#             leftVal = 0
#             rightVal = 0
#             if not root:
#                 return            
#             if leftVal == targetSum:
#                 counter += 1
#             if rightVal == targetSum:
#                 counter += 1          
#             leftVal = leftVal + root.val + root.left.val
#             dfs(root.left,targetSum)
#             rightVal = rightVal + root.val + root.right.val
#             dfs(root.right,targetSum)
            

#         dfs(root,targetSum)
#         return counter
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        counter = 0
        def dfs(root,resArr,targetSum):
            nonlocal counter
            total = 0
            if root is None:
                return
            resArr.append(root.val)

            for i in range(len(resArr)-1,-1,-1):
                total = total + resArr[i]
                if total  == targetSum:
                    counter += 1
                
            
            dfs(root.left,resArr,targetSum)
            dfs(root.right,resArr,targetSum)
            resArr.pop()
        resArr = []
        dfs(root,resArr,targetSum)
        return counter

