# https://www.acmicpc.net/problem/1874

def solution(sequence):
    resultStack = []
    result = []

    stack = []
    prevNum = 0
    try:
        for num in sequence:
            #오름차순으로 올라간다면 push
            if num == prevNum+1:
                stack.append(num)
                resultStack.append('+')
                result.append(stack.pop())
                resultStack.append('-')
                prevNum += 1
                continue
            elif num > prevNum:
                while num != prevNum:
                    prevNum += 1
                    stack.append(prevNum)
                    resultStack.append('+')
                result.append(stack.pop())
                resultStack.append('-')
            else:
                result.append(stack.pop())
                resultStack.append('-')
    except Exception as e:
        return None

    if result == sequence:
        return resultStack
    else:
        return None

    return result


count = int(input())

sequence = []
for i in range(count):
    sequence.append(int(input()))

result = solution(sequence)

if result:
    for re in result:
        print(re)
else:
    print("NO")