#!/usr/bin/python3

# Time: O(n), iterates over each node in tree once
# Space: O(n), call stack size for recursive traversal grows linearly with n

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def inOrder(p, q):
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return inOrder(p.left, q.left) and inOrder(p.right, q.right)
            return False
        return inOrder(p, q)
