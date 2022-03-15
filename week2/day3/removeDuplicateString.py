# https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s):
        # distinctStrList = list(set(list(s)))
        # str = "".join(distinctStrList)
        last_appear = {}
        for i, char in enumerate(s):
            last_appear[char] = i

        string_list = []
        for i, char in enumerate(s):
            if not string_list:
                string_list.append(char)
                continue

            if char not in string_list:
                while string_list and char < string_list[-1] and last_appear[string_list[-1]] > i:
                    string_list.pop()
                string_list.append(char)

            if char in string_list:
                pass


        return "".join(string_list)

if __name__ == "__main__":
    string = "cbacdcbc"
    sol = Solution()
    result = sol.removeDuplicateLetters(string)
    print(result)

