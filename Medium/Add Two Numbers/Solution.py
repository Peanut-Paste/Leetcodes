# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pwd, answer = 0, 0
        # get total value of l1 and l2
        while l1 or l2:
            # if both are not none
            if l1 and l2:
                # since the question stated that it is in reversed, then I need to have pwr
                answer += (l1.val + l2.val) * (10 ** pwd)
                # move to the next list
                l1, l2 = l1.next, l2.next
            # if l1 is not none
            elif l1:
                answer += l1.val * (10 ** pwd)
                l1 = l1.next
            # l2 is not none
            else:
                answer += l2.val * (10 ** pwd)
                l2 = l2.next 
            pwd += 1
        # get the len of the answer
        length = len(str(answer))
        # create and put the last num as the first node
        newli = ListNode(int(str(answer)[length - 1]))
        # create a variable so that the original won't be affected
        last = newli
        # -2 because the first node has already been stored
        for i in range(length - 2, -1, -1):
            # create new node for current number
            newnode = ListNode(int(str(answer)[i]))
            # place new node in the next variable in the linkedlist object
            last.next = newnode
            # move to the next node
            last = last.next
        return newli