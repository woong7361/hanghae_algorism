from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        if list1 is None or list1.val <= list2.val:
            linkedList = list1
            tempList = list2
        if list2 is None or list2.val <= list1.val:
            linkedList = list2
            tempList = list1

        result1 = linkedList
        result2 = linkedList

        while linkedList or tempList:
            if linkedList.val < tempList.val:
                linkedList = linkedList.next
            else:
                nextNode = linkedList.next
                linkedList.next = tempList

                tempList = tempList.next
                linkedList.next.next = nextNode
                linkedList = linkedList.next

        if linkedList:
            while result1.next:
                result1 = result1.next
            result1.next = tempList

        return result2







if __name__ == "__main__":
    pointer1 = None
    for i in range(6, 0, -2):
        pointer1 = ListNode(val=i, next=pointer1)
    pointer2 = None
    for i in range(8, 0, -3):
        pointer1 = ListNode(val=i, next=pointer2)

    sol = Solution()
    result = sol.mergeTwoLists(pointer1, pointer2)

    while result:
        # print(result.val)
        result = result.next