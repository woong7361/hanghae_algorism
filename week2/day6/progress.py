import math


def solution(progresses, speeds):
    answer = []
    finish = []

    if not progresses:
        return []

    for i in range(len(progresses)):
        fin = (100 - progresses[i]) / speeds[i]
        math.ceil(fin)
        finish.append(fin)

    MAX = 0
    for fin in finish:
        if fin > MAX:
            answer.append(1)
            MAX = fin
        else:
            answer[-1] += 1

    return answer
