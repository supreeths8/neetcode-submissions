# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.counter = 0
        self.smallest = None
        
        def helper(node):
            if not node:
                return
            
            helper(node.left)
            if self.counter < k:
                self.counter += 1
                self.smallest = node.val
            else:
                return
            helper(node.right)

        helper(root)
        return self.smallest


