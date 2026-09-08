# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def helper(node, running_sum):
            if not node:
                return False
            
            running_sum += node.val

            if not node.left and not node.right:
                return running_sum == targetSum
            
            return helper(node.left, running_sum) or helper(node.right, running_sum)

        return helper(root, 0)




