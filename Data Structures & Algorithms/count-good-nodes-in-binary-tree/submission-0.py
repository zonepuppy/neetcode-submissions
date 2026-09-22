# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def helperDfs(root, high):
            nonlocal count
            if root is None:
                return
            if root.val >= high:
                count += 1
            high = max(root.val, high)
            helperDfs(root.left, high)
            helperDfs(root.right, high)
            return

        helperDfs(root, root.val)
        return count