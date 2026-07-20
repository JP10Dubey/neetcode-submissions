class Solution:
    def trap(self, height: List[int]) -> int:
        Width = len(height)
        _water = [0] * Width
        left = 0
        right = Width -1
        while left<right:
            _currentwater = 0
            minGap = min(height[left], height[right])
            if height[left]> height[right]:
                currentleft = left+1
                while currentleft < right:
                    _currentwater = minGap - height[currentleft]
                    if _currentwater > _water[currentleft]:
                        _water[currentleft] = _currentwater
                    currentleft +=1 
                right = right -1
            else:
                currentleft = left+1
                while currentleft < right:
                    _currentwater = minGap - height[currentleft]
                    if _currentwater > _water[currentleft]:
                        _water[currentleft] = _currentwater
                    currentleft +=1 
                left=left+1

        return sum(_water)

