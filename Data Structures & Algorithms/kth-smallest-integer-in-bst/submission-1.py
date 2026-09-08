# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        counter = 0
        smallest = -1
        
        def helper(node):
            nonlocal counter, smallest
            if not node:
                return
            
            helper(node.left)
            if counter < k:
                counter += 1
                smallest = node.val
            else:
                return
            helper(node.right)

        helper(root)
        return smallest


