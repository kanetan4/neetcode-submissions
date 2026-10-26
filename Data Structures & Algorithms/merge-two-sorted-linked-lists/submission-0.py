# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2: return None
        if not list1: return list2
        if not list2: return list1

        head = ListNode()
        temp = head
        if list1.val < list2.val:
            temp.val = list1.val
            list1 = list1.next
        else:
            temp.val = list2.val
            list2 = list2.next
        
        while list1 and list2:
            nextNode = ListNode()
            temp.next = nextNode
            if list1.val < list2.val:
                nextNode.val = list1.val
                list1 = list1.next
            else:
                nextNode.val = list2.val
                list2 = list2.next
            temp = temp.next
        temp.next = list1 or list2
        return head


