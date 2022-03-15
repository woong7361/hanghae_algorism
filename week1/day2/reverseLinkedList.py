# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #노드가 존재하지 않는다면
        if not head:
            return None
        #노드가 존재 한다면
        else:
            originList = [head.val]
            while head.next:
                head = head.next
                originList.append(head.val)
                [1,2,3,4,5]

            pointer = None
            for value in originList:
                pointer = ListNode(val=value, next=pointer)

            return pointer


if __name__ == "__main__":
    pointer = None
    for i in range(5, 0, -1):
        pointer = ListNode(val=i, next=pointer)

    head = pointer

    sol = Solution()
    result = sol.reverseList(head)

    while result:
        print(result.val)
        result = result.next


