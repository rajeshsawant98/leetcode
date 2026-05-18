# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        maxSum = float("-inf")
        answerLevel = 1
        currentLevel = 1

        q = collections.deque([root])

        while q:
            levelSum = 0
            qLen = len(q)

            for _ in range(qLen):
                node = q.popleft()
                if node:
                    levelSum += node.val
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            
            if levelSum > maxSum:
                maxSum = levelSum
                answerLevel = currentLevel
            currentLevel += 1
            
        return answerLevel

        