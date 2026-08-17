class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right = len(nums) - 1
        left = 0
        output = -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else: 
                return -1
        
        while left<=right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                output = mid
                return output
            elif nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid-1
        return output