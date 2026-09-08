# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.counter = 0

        def helper(root, path_max):
            if not root:
                return
            if root.val >= path_max:
                self.counter += 1
            helper(root.left, max(path_max, root.val))
            helper(root.right, max(path_max, root.val))
        
        helper(root, float('-inf'))
        return self.counter