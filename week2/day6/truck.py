from collections import deque
from collections import defaultdict

def solution(bridge_length: int, weight: int, truck_weights: list):
    bridge = deque([0]*bridge_length)
    truck_weights.sort(reverse=True)
    dic = defaultdict(int)

    for truck_weight in truck_weights:
        dic[truck_weight] += 1

    truck_weight_set = sorted(set(dic.keys()), reverse=True)


    in_bridge_weight = 0
    count = 0
    while truck_weight_set:
        flag = 1
        for truck_weight in truck_weight_set:
            if in_bridge_weight + truck_weight <= weight:
                in_bridge_weight += truck_weight
                in_bridge_weight -= bridge.popleft()
                bridge.append(truck_weight)

                dic[truck_weight] -= 1
                if dic[truck_weight] == 0:
                    # dic.pop(truck_weight)
                    truck_weight_set.remove(truck_weight)

                flag = 0
                break

        if flag:
            in_bridge_weight -= bridge.popleft()
            bridge.append(truck_weight)

        count += 1

    answer = count + bridge_length
    return answer


