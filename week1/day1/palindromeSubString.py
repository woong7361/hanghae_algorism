# 문제
# 문자열 S의 부분 문자열 중에서 팰린드롬인 것 중 가장 긴 것의 길이를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 문자열 S가 주어진다. S는 알파벳 소문자로만 이루어져 있으며 길이는 1보다 크거나 같고, 100,000보다 작거나 같다.
#
# 출력
# 가장 긴 팰린드롬 부분 문자열의 길이를 출력한다.

wordList = list(map(str, input().split()))
word = wordList[0]

def findPalindrome1(string, idx1, idx2):
    count = 0
    while idx1 >= 0 and idx2 <= len(string) - 1 and string[idx1] == string[idx2]:
        idx1 -= 1
        idx2 += 1
        count += 1

    #3개짜리 슬라이드 index, index+2
    if abs(idx2 - idx1) % 2 == 0:
        return count*2 + 1
    #2개짜리 슬라이드 index, index+2
    else:
        return count*2

maxResult = 1
length = len(word)//2
maxResult = max(maxResult,
                findPalindrome1(word, length, length+1),
                findPalindrome1(word, length, length+2))

for index in range(1, length+1):

    left = length - index
    right = length + index

    if len(word) < 2 or word[::-1] == word:
        maxResult = len(word)
        break

    if maxResult == max(maxResult, left*2 + 2, (len(word) - right - 1)*2 + 2):
        break

    maxResult = max(maxResult,
                    findPalindrome1(word, right, right+1),
                    findPalindrome1(word, right, right+2),
                    findPalindrome1(word, left, left+1),
                    findPalindrome1(word, left, left+2))

print(maxResult)

# maxResult = 1
# for index in range(len(word) - 1):
#
#     if len(word) < 2 or word[::-1] == word:
#         maxResult = len(word)
#         break
#
#     maxResult = max(maxResult,
#                     findPalindrome1(word, index, index+1),
#                     findPalindrome1(word, index, index+2))
#
# print(maxResult)








def findPalindrome(string, index, maxResult):
    result = 1
    count = 1
    flag = 1

    try:
        while 1:
            if index - count == -1:
                raise IndexError('uu')
            # print(index)
            if flag:
                if string[index] == string[index - count] and string[index] == string[index + count]:
                    result += 2
                elif string[index] == string[index + count]:
                    result += 1
                    flag = 0
                else:
                    flag = 0

            if not flag:
                if result % 2 == 0:
                    idx1 = index
                    idx2 = index + 1
                    if string[idx1 - count] == string[idx2 + count]:
                        result += 2
                    else:
                        break

                else:
                    if string[index - count] == string[index + count]:
                        result += 2
                    else:
                        break

            count += 1

    except IndexError as e:
        # print(index, e)
        if index + count <= len(string) - 1 and flag:
            if string[index] == string[index + count]:
                result += 1

        return result

    return result

















