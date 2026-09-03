# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Longest path bw any two nodes must go through some node. At this node,
        left subtree height + right subtree height gives the diameter.

        Maintain the longest path as state and return the heights
        """
        self.res = 0

        def dfs(node):
            if not node:
                return 0
            
            L = dfs(node.left)
            R = dfs(node.right)

            self.res = max(self.res, L + R)
            return 1 + max(L, R)
        dfs(root)
        return self.res


        



