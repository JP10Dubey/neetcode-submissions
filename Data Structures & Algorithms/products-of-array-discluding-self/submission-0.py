import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod = [1]* n
        left = 1
        for i in range(n):
            prod[i] = left
            left *= nums[i]
        right = 1
        for i in range(n-1,-1,-1):
            prod[i] *= right
            right *= nums[i]
        return prod
        