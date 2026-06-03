# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        q = collections.deque()
        res = []
        if root:
            q.append(root)

        while q:
            qlevel = len(q)
            level =[]

            for _ in range(qlevel):
                node = q.popleft()
                if node:
                    level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(level)
        
        return res