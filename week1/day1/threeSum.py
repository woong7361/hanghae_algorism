
input = [-1, 0, 1, 2, -1, -4]

class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        nums = sorted(nums)
        print(nums)

        result = []
        for i in range(len(nums) - 2):
            left = i+1
            right = len(nums)-1
            # print(i, left, right)
            if i > 0 and nums[i-1] == nums[i]:
                continue
            while left < right:
                print(i, left, right)
                numSum = nums[i] + nums[left] + nums[right]
                if numSum > 0:
                    right -= 1
                elif numSum < 0:
                    left += 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left = left+1

        return result

print(Solution().threeSum(input))


