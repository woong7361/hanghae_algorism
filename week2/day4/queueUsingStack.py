from collections import deque

num = int(input())

for i in range(num):
    question = list(map(int, input().split()))
    priority = list(map(int, input().split()))

    maxList = [0]*9
    for p in priority:
        maxList[p-1] += 1

    count = question[1]
    printerOut = 0
    que = deque(priority)

    while que:
        while maxList[-1] == 0:
            maxList.pop()

        value = que.popleft()
        if value == len(maxList):
            maxList[-1] -= 1
            printerOut += 1
        else:
            que.append(value)

        if count == 0 and priority[question[1] == len(maxList)]:
            break
        elif count == 0:
            count = len(que)

        count -= 1

    print(printerOut)


