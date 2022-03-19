import sys

iterNum = int(sys.stdin.readline().rstrip())
for i in range(iterNum):
    num = int(sys.stdin.readline().rstrip())
    count = 0

    stack = [num]
    while stack:
        popElement = stack.pop()
        if popElement == 0:
            count += 1
            continue

        if popElement - 3 >= 0:
            stack.append(popElement-3)
        if popElement - 2 >= 0:
            stack.append(popElement-2)
        if popElement - 1 >= 0:
            stack.append(popElement-1)
    print(count)



