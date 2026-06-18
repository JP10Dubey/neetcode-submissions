class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for num in numset:
            if (num-1) not in numset:
                current = 1
                while num+current in numset:
                    current += 1
                longest = max(current,longest)
        return longest
            