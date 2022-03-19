from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        edge = defaultdict(list)
        for prerequisite in prerequisites:
            edge[prerequisite[0]].append(prerequisite[1])

        visit = [0]*numCourses+1
        for node in range(numCourses):
            if visit[node] == 1:
                continue

            temp = []
            path = [node]
            while path:
                element = path.pop()
                if visit[element] == 1:
                    continue
                if element in temp:
                    return False

                temp.append(element)

                visit[element] = 1
                path = path + edge[element]

        return True

