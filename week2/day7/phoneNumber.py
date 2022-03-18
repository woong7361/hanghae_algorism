from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return

        dic = {'2': ['a','b','c'], '3': ['d','e','f'],
               '4': ['g','h','i'], '5': ['j','k','l'], '6': ['m','n','o'],
               '7': ['p','q','r','s'], '8': ['t','u','v'], '9': ['w','x','y','z']
               }

        answer = []
        def find(currentString :str, remainDigits: str):
            if not remainDigits:
                answer.append(currentString)
                return

            wordList = dic[remainDigits[0]]
            for word in wordList:
                find(currentString + word, remainDigits[1:])

        find("", digits)

        return answer

print(Solution().letterCombinations("34"))