# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        nextN=None
        length =0
        

        while curr is not None:
            length += 1
            curr = curr.next
       
        position =length//2
        current = head

        if length == 1:
            return None
        
        for i in range(1, position):
            if current is not None:
                current = current.next

        if current is None or current.next is None:
            return head

        temp = current.next

        current.next = current.next.next

        temp = None
        return head







        


        