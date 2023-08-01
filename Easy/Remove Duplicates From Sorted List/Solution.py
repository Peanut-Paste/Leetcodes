# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newset = set()
        temp = head
        while temp and temp.next:
            # add current val to the set
            newset.add(temp.val)
            # initiate current next object
            nextobj = temp.next
            # if next object is none, break to prevent error
            if nextobj is None:
                break
            # if next obj value is already in newset, set current next to next obj's next to skip
            if nextobj.val in newset:
                temp.next = nextobj.next
            else:
                temp = temp.next
        return head