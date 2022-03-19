from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        aimLength = len(tickets)

        dic = defaultdict(list)
        for ticket in tickets:
            dic[ticket[0]].append([1])
        for d in dic:
            dic[d].sort()

        def find(path, dic: dict):
            if len(path) == aimLength + 1:
                return path

            if not dic.get(path[-1]):
                return None

            for index, forward in enumerate(dic.get(path[-1])):
                copyDic = dic.copy()
                copyDic[path[-1]] = copyDic[path[-1]][:index] + copyDic[path[-1]][index + 1:]
                result = find(path + [forward], copyDic)
                if result:
                    return result

        path = find(["JFK"], dic)

        return path