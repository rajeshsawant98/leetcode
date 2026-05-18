# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        res = []
        q = collections.deque([root])

        while q:
            qLen = len(q)
            rightMost = None
            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightMost = node
                    q.append(node.left)
                    q.append(node.right)
            
            if rightMost:
                res.append(rightMost.val)

        
        return res
