# https://www.acmicpc.net/problem/17219
import sys

siteNum, findNum = list(map(int, sys.stdin.readline().rstrip().split()))

siteDict = {}
for i in range(siteNum):
    siteDomain, password = list(map(str, sys.stdin.readline().rstrip().split()))
    siteDict[siteDomain] = password

for i in range(findNum):
    findDomain = list(map(str, sys.stdin.readline().rstrip().split()))
    print(siteDict.get(*findDomain))
