# https://leetcode.com/problems/longest-substring-without-repeating-characters/


from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = defaultdict(int)
        start = 0
        result = 0
        for end, char in enumerate(s):
            dic[char] += 1
            while dic[char] == 2:
                dic[s[start]] -= 1
                start += 1
            result = max(result, end-start+1)
        return result


substring= Solution().lengthOfLongestSubstring("abcabcbb")

print(substring)