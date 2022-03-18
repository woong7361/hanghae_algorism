from typing import List
from collections import deque


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        maxLevel = k
        answer = []

        # 초기화 level = 0 -> 1
        que = deque([[i + 1] for i in range(n)])

        level = 1
        while level < maxLevel:
            while len(que[0]) == level:
                combinationElement = que.popleft()
                for i in range(combinationElement[-1] + 1, n + 1):
                    que.append(combinationElement + [i])
            level += 1

        return list(que)