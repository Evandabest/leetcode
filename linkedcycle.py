


#Leetcode 141. Linked List Cycle

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head: Optional[ListNode]) -> bool:
        
        p1 = head
        p2 = head

        while p1 and p2:
            if p1 and p2.next and p1.next and p2.next.next:
                p1 = p1.next
                p2 = p2.next.next
            else:
                print
                break

            if p1.next == p2.next:
                return True
        

        return False