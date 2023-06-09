#!/usr/bin/python3

# Time: O(n), iterates over each node in tree once
# Space: O(n), stores a temp at each node (there would also be some recursive overhead for each function call)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # handle empty case and leaves
        if not root:
            return None
        # store one branch
        temp = root.left
        # assign branches on opposite side
        root.left = root.right
        root.right = temp
        # call for each branch, assign to nothing
        self.invertTree(root.left)
        self.invertTree(root.right)
        # return overall root
        return root
