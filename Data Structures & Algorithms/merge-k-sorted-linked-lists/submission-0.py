# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from math import floor

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        if len(lists) == 1:
            return lists[0]

        if len(lists) == 2:
            return self.merge(lists[0], lists[1])

        lst1 = self.mergeKLists(lists[:floor(len(lists)/2)])
        lst2 = self.mergeKLists(lists[floor(len(lists)//2):])

        return self.merge(lst1, lst2)

    def merge(self, lst1: Optional[ListNode], lst2: Optional[ListNode]) -> Optional[ListNode]:
        if lst1 is None:
            return lst2
        if lst2 is None:
            return lst1
        
        curr1 = lst1
        curr2 = lst2

        if lst1.val > lst2.val:
            head = curr2
            curr2 = curr2.next
        else:
            head = curr1
            curr1 = curr1.next

        curr = head

        while curr1 is not None and curr2 is not None:
            if curr1.val > curr2.val:
                curr.next = curr2
                curr = curr.next
                curr2 = curr2.next
            else:
                curr.next = curr1
                curr = curr.next
                curr1 = curr1.next
        
        if curr1 is not None:
            curr.next = curr1
        else:
            curr.next = curr2

        return head
