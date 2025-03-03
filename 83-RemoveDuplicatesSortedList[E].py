from typing import Optional

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Solution: because it's a singly linked list, simply use a separate 'pointer' object to iterate through list and set next to next->next->
# when duplicate is found. 

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        current = head

        while (current and current.next):
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head


