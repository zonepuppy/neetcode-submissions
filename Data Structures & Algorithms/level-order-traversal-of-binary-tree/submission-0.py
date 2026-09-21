# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = deque([root])
        result = []
        if root is None:
            return []
        
        while queue:
            current_level = []
            level_length = len(queue)
            for _ in range(level_length):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            result.append(current_level)
        return result
            
        
