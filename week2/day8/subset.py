from typing import List
from collections import deque

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        result = [[]]
        nums.sort()
        answer = deque([i] for i in nums)

        while answer:
            popElement = answer.popleft()
            result.append(popElement)
            if popElement[-1] == nums[-1]:
                continue

            index = nums.index(popElement[-1])
            for num in nums[index+1:]:
                answer.append(popElement + [num])
        return result


