

nums = [6, 2, 6, 5, 1, 2]

class Solution:
    def arrayPairSum(self, nums: [int]) -> int:
        result = 0
        nums.sort()
        while nums:
            result += min(nums.pop(),nums.pop())


        return result

result = Solution().arrayPairSum(nums)
print(result)
