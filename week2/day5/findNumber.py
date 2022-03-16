# https://www.acmicpc.net/problem/1920
import sys

skip = sys.stdin.readline().rstrip()
origin = set(map(int, sys.stdin.readline().rstrip().split()))
dic = {}
for number in origin:
    dic[number] = 1

skip = sys.stdin.readline().rstrip()
find = list(map(int, sys.stdin.readline().rstrip().split()))
for elem in find:
    try:
        dic[elem]
        print(1)
    except:
        print(0)
