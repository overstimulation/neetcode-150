from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_previous = dummy

        while True:
            kth_node = self.get_kth_node(group_previous, k)
            if not kth_node:
                break

            group_next = kth_node.next

            previous, current = kth_node.next, group_previous.next
            while current != group_next:
                temporary = current.next
                current.next = previous
                previous = current
                current = temporary

            temporary = group_previous.next
            group_previous.next = kth_node
            group_previous = temporary

        return dummy.next

    def get_kth_node(self, current: Optional[ListNode], k: int) -> Optional[ListNode]:
        while current and k > 0:
            current = current.next
            k -= 1
        return current
