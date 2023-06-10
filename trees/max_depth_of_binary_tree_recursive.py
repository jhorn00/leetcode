#!/usr/bin/python3

# Time: O(n), must iterate over each node
# Space: O(n), stores 3 depth values for each node visited (in addition to recursive overhead)
# For worst case this is n.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if None, adds 0 to depth
        if not root:
            return 0
        # depth current node adds
        depth = 1

        # get each branch depth
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        # add the highest depth of the two branches
        depth += max(left, right)
        
        # return depth of entire (sub)tree from current root
        return depth
