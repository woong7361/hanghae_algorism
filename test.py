from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dic = [set() for _ in range(n)]

        for edge in edges:
            dic[edge[0]].add(edge[1])
            dic[edge[1]].add(edge[0])

        visit = [0] * n
        visit[source] = 1
        path = set(source)
        while path:
            popElement = path.pop()
            if popElement == destination:
                return True

            for element in dic[popElement]:
                if visit[element] == 0:
                    visit[element] = 1
                    path.add(element)

        return False