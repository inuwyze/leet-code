# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
            
        ff=head
        pf=head
        while ff and ff.next:
            ff=ff.next.next
            pf=pf.next

        
        return pf