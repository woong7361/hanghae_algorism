# https://leetcode.com/problems/top-k-frequent-elements/submissions/

from typing import List

from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1

        t = sorted(dic.items(), key=lambda x: x[1], reverse=True)

        return [i[0] for i in t[:k]]