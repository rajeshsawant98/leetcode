# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        self.count = k

        self.res = -1

        def dfs(node):

            if not node:
                return

            # Traverse left

            dfs(node.left)
            # Process current node

            self.count -= 1
            if self.count == 0:
                self.res = node.val
                return

            # Traverse right
            dfs(node.right)

        dfs(root)
        return self.res