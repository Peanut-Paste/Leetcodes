# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: if both the list is None return None
        if list1 is None and list2 is None:
            return None
        new_list = []
        # Append all values from first linked list
        while list1:
            new_list.append(list1.val)
            list1 = list1.next
        # Append all values from second linked list
        while list2:
            new_list.append(list2.val)
            list2 = list2.next
        # Sort the values
        new_list.sort()
        # Create a new linked list with value of first element in new list
        new_node = ListNode(new_list[0])
        # remove first element in new list
        new_list.remove(new_list[0])
        # using a temp node so it doesn't affect the original
        temp_node = new_node
        # create a new node every for every element and linked it
        for v in new_list:
                a = ListNode(v)
                temp_node.next = a
                temp_node = temp_node.next
        return (new_node)