# https://www.acmicpc.net/problem/2667
import sys

size = int(sys.stdin.readline().rstrip())

danziMap = []
for i in range(size):
    line = list(sys.stdin.readline().rstrip())
    danziMap.append(line)

def find(x, y, size):
    #    [상  하  좌  우]순서
    dx = [0, 0, -1, 1];
    dy = [1, -1, 0, 0]

    count = 0
    if 0 <= x <= size-1 and 0 <= y <= size - 1 and danziMap[x][y] == '1':
        danziMap[x][y] = '0'
        count += 1
        for i in range(4):
            count += find(x + dx[i], y + dy[i], size)
        return count
    else:
        return 0

answer = []

for row in range(size):
    for column in range(size):
        if danziMap[row][column] == '1':
            temp = find(row, column, size)
            answer.append(temp)

print(len(answer))
answer.sort()
for ans in answer:
    print(ans)

