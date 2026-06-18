class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Setnums = set(nums)
        if len(Setnums) == len(nums):
            return False
        else:
            return True

        