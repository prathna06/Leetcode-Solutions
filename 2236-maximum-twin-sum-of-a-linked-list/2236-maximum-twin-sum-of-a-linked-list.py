# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        maxVal = []
        counter = 0
        curr = head
        while curr is not None:
            counter += 1
            curr = curr.next

        oppositeCounter = (counter//2)-1
        for i in range(counter):
            if i < counter//2:
                maxVal.append(head.val)
                head = head.next
            else:
               maxVal[oppositeCounter]= maxVal[oppositeCounter] + head.val 
               head = head.next
               oppositeCounter -= 1
        return max(maxVal)


            

            