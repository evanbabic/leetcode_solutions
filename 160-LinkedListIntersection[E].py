# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
# If the two linked lists have no intersection at all, return null.

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        cursorA = headA
        cursorB = headB
        
        while cursorA != cursorB:
            if (cursorA != None):
                cursorA = cursorA.next
            else:
                cursorA = headB

            if (cursorB != None):
                cursorB = cursorB.next
            else:
                cursorB = headA
        
        return cursorA