from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return

        answer = []

        def find(currentPermutation: List, remainDigits: List):
            if not remainDigits:
                answer.append(currentPermutation)
                return

            for remainDigit in remainDigits:
                digits = remainDigits.copy()
                digits.remove(remainDigit)
                permutation = currentPermutation.copy()
                permutation.append(remainDigit)

                find(permutation, digits)

        find([], nums)
        return answer


