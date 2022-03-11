# 문제
# 평생 영어 단어를 암기한 준민이는 단어를 애너그램 그룹으로 나누려고 한다.
#
# 단어 w가 단어 v의 애너그램이 되려면, 단어 w의 알파벳 순서를 바꿔서 v를 만들 수 있어야 한다.
# 이렇게 애너그램인 단어들을 묶어서 애너그램 그룹이라고 한다. 그룹의 크기는 그 그룹에 포함된 단어의 수이다.
#
# 단어가 주어졌을 때, 크기가 가장 큰 애너그램 그룹 다섯 개를 구하는 프로그램을 작성하시오.

# 입력
# 입력은 최대 30,000 줄로 이루어져 있고, 각 줄에는 알파벳 소문자로 이루어진 단어가 하나씩 주어진다.
# 입력은 EOF로 끝난다.
#
# 출력
# 크기가 가장 큰 애너그램 다섯 개를 출력한다. 만약, 그룹의 수가 다섯개보다 작다면, 모두 출력한다.
# 그룹은 크기가 감소하는 순으로, 크기가 같을 때는 각 그룹에서 가장 사전 순으로 앞서는 단어의 사전 순으로 출력한다.
#
# 각 그룹을 출력할 때, 크기와 포함된 단어를 출력하며, 단어는 사전 순으로 출력해야 한다. 같은 단어는 한 번만 출력한다.
import sys

# def solution():
from pprint import pprint
from collections import OrderedDict

anagramDict = OrderedDict()
lengthDict = OrderedDict()
#입력 부분
while 1:
    try:
        word = list(map(str, input().split()))
        sortedWord = ''.join(sorted(str(*word)))

        if sortedWord not in anagramDict.keys():
            anagramDict[sortedWord] = [word[0]]
            lengthDict[sortedWord] = 1
        else:
            anagramDict[sortedWord] = [*anagramDict[sortedWord], word[0]]
            lengthDict[sortedWord] = lengthDict[sortedWord] + 1
    except Exception as e:
        break


tempDict= OrderedDict()
for keyWord in anagramDict:
    anagramDict[keyWord] = list(set(anagramDict[keyWord]))
    anagramDict[keyWord] = sorted(anagramDict[keyWord], key=lambda item:item)
    lengthDict[anagramDict[keyWord][0]] = lengthDict.pop(keyWord)
    tempDict[anagramDict[keyWord][0]] = anagramDict[keyWord]


sortedDict = sorted(lengthDict.items(), key=lambda item: item[0])
sortedDict = sorted(sortedDict, key=lambda item: item[1], reverse=True)

count = 0
for key, length in sortedDict:
    if count == 5:
        break
    anagramWordList = tempDict[key]

    anagramWordString = " ".join(word for word in anagramWordList)
    print('Group of size ' + str(length) + ": " + anagramWordString + " .")
    count += 1







