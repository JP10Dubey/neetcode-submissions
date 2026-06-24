class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        number = sorted(numbers)
        sumpair = []
        while left<right:
            s=number[left]+number[right]
            if s==target:
                sumpair.append([number[left],number[right]])
                right-=1
                left+=1
            elif s>target:
                right-=1
            else:
                left+=1
        return sumpair
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        Triplet = []
        for i in range(len(nums)):
            subTriplet = []
            couple = self.twoSum(nums[i+1:len(nums)],-nums[i])
            if couple:
                for k in range(len(couple)):
                    subTriplet = [nums[i]] + couple[k]
                    subTriplet = sorted(subTriplet)
                    if subTriplet not in Triplet:
                        Triplet.append(subTriplet)
        return Triplet
        


        