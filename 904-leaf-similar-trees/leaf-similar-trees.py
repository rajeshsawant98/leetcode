# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(node,res):
            if not node:
                return
            
            if not node.left and not node.right:
                res.append(node.val)
                return 
            
            dfs(node.left,res)
            dfs(node.right,res)

        leaves1 = []
        leaves2 = []

        dfs(root1, leaves1)
        dfs(root2, leaves2)

        return leaves1 == leaves2
