# https://leetcode.com/problems/daily-temperatures/
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        resultList = [0]*len(temperatures)

        slideList = []
        for index, currentTemp in enumerate(temperatures):
            while slideList and currentTemp > slideList[-1][0]:
                resultList[slideList[-1][1]] = index - slideList[-1][1]
                slideList.pop()
                print(index, resultList)

            slideList.append([currentTemp, index])

        return resultList

if __name__ == "__main__":
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    sol = Solution()
    daily_temperatures = sol.dailyTemperatures(temperatures)
    print(daily_temperatures)