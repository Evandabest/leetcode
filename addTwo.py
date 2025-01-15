

# Leetcode 2. Add Two Numbers

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        num1 = ""
        num2 = ""

        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        
        result = int(num1[::-1]) + int(num2[::-1])
        
        newResult = str(result)[::-1]

        newList = ListNode(int(newResult[0]))
        head = newList

        for i in range(1, len(newResult)):
            newList.next = ListNode(int(newResult[i]))
            newList = newList.next

        return head