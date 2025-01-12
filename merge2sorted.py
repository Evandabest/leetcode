

# leetcode #21. Merge Two Sorted Lists
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None and list2 is None:
            return list1
        elif list1 is None and not(list2 is None):
            return list2
        elif list2 is None and not(list1 is None):
            return list1

        if (list1.val >= list2.val):
            head = ListNode(list2.val, None)
            list2 = list2.next
        else:
            head = ListNode(list1.val, None)
            list1 = list1.next
        
        curr = head
        print(head, list1, list2)
        while list1 is not None and list2 is not None:
            if (list1.val >= list2.val):
                curr.next = ListNode(list2.val, None)
                curr = curr.next
                list2 = list2.next
            else:
                curr.next = ListNode(list1.val, None)
                curr = curr.next
                list1 = list1.next
        
        while list1 is not None:
            curr.next = ListNode(list1.val, None)
            curr = curr.next
            list1 = list1.next
        
        while list2 is not None:
            curr.next = ListNode(list2.val, None)
            curr = curr.next
            list2 = list2.next
        
        return head
