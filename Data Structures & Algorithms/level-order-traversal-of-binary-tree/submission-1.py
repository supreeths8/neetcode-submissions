# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        level_queue = deque()

        level_queue.append(root)

        while len(level_queue):
            level_res = []
            for _ in range(len(level_queue)):
                curr = level_queue.popleft()
                level_res.append(curr.val)

                if curr.left:
                    level_queue.append(curr.left)
                if curr.right:
                    level_queue.append(curr.right)
            res.append(level_res)
        return res


                
        