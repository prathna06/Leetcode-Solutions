# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.getLeftMostChild(root)

    def next(self) -> int:
        node = self.stack.pop()
        if node.right:
            self.getLeftMostChild(node.right)
        return node.val
            

    def hasNext(self) -> bool:
        return len(self.stack) > 0
        
    def getLeftMostChild(self,root: Optional[TreeNode]):
        while(root.left):
            self.stack.append(root)
            root = root.left
        self.stack.append(root)
    