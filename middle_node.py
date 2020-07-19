# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        a=head
        b=head
        while(b!=None):
            b=b.next
            
            if b==None:
                return a
            a=a.next
            b=b.next
        
        return a