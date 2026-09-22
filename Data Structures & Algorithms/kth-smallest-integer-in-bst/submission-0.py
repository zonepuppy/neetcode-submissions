# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        visited = []
        counter = 0
        node = root
        while node or root:
            while node:
                stack.append(node)
                node = node.left
            

            node = stack.pop()
            visited.append(node)
            counter += 1
            if counter == k:
                return node.val
            node = node.right
        return 0
            