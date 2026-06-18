class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for num in numset:
            if (num-1) not in numset:
                root = num
                current = 0
                while root in numset:
                    current += 1
                    root +=1
                longest = max(current,longest)
        return longest
            