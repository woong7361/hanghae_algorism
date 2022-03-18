# https://www.acmicpc.net/problem/2606
import sys
from pprint import pprint

computerNum = int(sys.stdin.readline().rstrip())
num = int(sys.stdin.readline().rstrip())

graph = [set() for _ in range(computerNum + 1)]
for i in range(num):
    temp = sys.stdin.readline().rstrip().split()
    graph[int(temp[0])].add(temp[1])
    graph[int(temp[1])].add(temp[0])

node = set(graph[1])
result = set('1')
while node:
    popElement = node.pop()
    if popElement not in result:
        node.update(graph[int(popElement)])
    result.add(popElement)

print(len(result)-1)
