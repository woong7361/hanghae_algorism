# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        result = head
        evenHead = ListNode()   #adding temp node
        tempHead = evenHead
        while head.next:
            if head.next.next is None:
                evenHead.next = head.next
                evenHead = evenHead.next
                head.next = None

            evenHead.next = head.next
            evenHead = evenHead.next
            head.next = head.next.next
            head = head.next

        evenHead.next = None

        head.next = tempHead.next

        return result



if __name__ == "__main__":
    pointer = None
    for i in range(5, 0, -1):
        pointer = ListNode(val=i, next=pointer)

    sol = Solution()
    result = sol.oddEvenList(pointer)

    while result:
        print(result.val)
        result = result.next