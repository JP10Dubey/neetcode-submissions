class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        for j in range(len(nums)-k+1):
            temp = nums[j]
            for i in range (1,k):
                temp = max(temp,nums[j+i])
            ans.append(temp)
        return ans