class Solution:
    def maxArea(self, heights: List[int]) -> int:
        _maxWater = 0
        dist = len(heights)
        for i in range(dist):
            for j in range(dist):
                curArea = min(heights[i],heights[j])*(j-i)
                if  curArea> _maxWater:
                    _maxWater = curArea
        return _maxWater