# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if not root:
            return []
        
        level_queue = deque()
        level_queue.append(root)

        while len(level_queue):
            curr = None
            for _ in range(len(level_queue)):
                curr = level_queue.popleft()
                
                if curr.left:
                    level_queue.append(curr.left)
                if curr.right:
                    level_queue.append(curr.right)
            if curr:
                res.append(curr.val)
        
        return res
                

            
