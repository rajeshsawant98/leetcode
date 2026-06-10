# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        self.res = 0

        def dfs(root):
            if not root:
                return 0
            
            LH = dfs(root.left)
            RH = dfs(root.right)

            self.res = max(self.res , LH+RH)

            return 1 + max(LH,RH)
        
        dfs(root)

        return self.res
