# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        queue.append(root)
        maxSum, maxSumLevel, levelIndex = float('-inf'), 0, 0
        while queue:
            queuelen = len(queue)
            level = []
            total = 0
            levelIndex += 1
            for i in range(queuelen):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                    total = total+node.val          
            if maxSum < total:
                maxSum = total
                maxSumLevel = levelIndex
        return maxSumLevel

