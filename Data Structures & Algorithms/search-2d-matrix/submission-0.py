class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])-1
        for i in range(row):
            print(matrix[i][col])
            if matrix[i][col] >= target:
                print(matrix[i])
                output = self.bubble(matrix[i], target, col)
                return output
        return False
                

    def bubble(self, nums : List[int], target: int,right: int ):
        left = 0
        if len(nums) == 1:
            if nums[0] == target:
                return True
            else: 
                return False
        while left<=right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid-1
        return False