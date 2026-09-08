# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(node, left_limit, right_limit):
            if not node:
                return True

            if left_limit < node.val < right_limit:
                L = helper(node.left, left_limit, node.val)
                R = helper(node.right, node.val, right_limit)
                return L and R
            
            return False

        return helper(root, float('-inf'), float('inf'))

