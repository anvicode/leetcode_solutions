# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = set()
        while head:
            if head in s:
                return True
            else:
                s.add(head)
            head = head.next
        return False

    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        s, f = head, head
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                return True
        return False
