class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        LOA = len(nums)
        loopCount = LOA-k+1
        ans = []
        for j in range(loopCount):
            temp = nums[j]
            for i in range (1,k):
                temp = max(temp,nums[j+i])
            ans.append(temp)
        return ans