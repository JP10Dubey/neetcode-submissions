class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lenn = len(numbers)
        for i,num in enumerate(numbers):
            req = target - num
            print("Target:",req)
            if (req in numbers) and (req != num):
                for j in range(i,lenn):
                    if numbers[j] == req:
                        return [i+1,j+1]