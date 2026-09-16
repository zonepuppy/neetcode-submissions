# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack1 = [p]
        stack2 = [q]
        while stack1 and stack2:
            x = stack1.pop()
            y = stack2.pop()
            if x is None and y is None:
                continue
            elif x is None or y is None:
                return False
            if x.val != y.val:
                return False
            stack1.append(x.left)
            stack1.append(x.right)
            stack2.append(y.left)
            stack2.append(y.right)
        
        return True
