# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        Node = head
        arr=[]
           
        while Node:
            arr.append(Node.val)
            Node = Node.next
        
        if len(arr)==0:
            return None

        rev = arr[::-1]

        print(rev)

        
        ansHead= ListNode(rev[0])
        ans = ansHead

        for n in range(1,len(rev)):
            tail = ListNode(rev[n])
            ans.next = tail
            ans = ans.next

        return ansHead
        
        