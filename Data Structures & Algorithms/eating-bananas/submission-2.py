class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        numPiles = len(piles)
        if numPiles == h:
            return max(piles)
        left = 1
        right = max(piles)
        while(left<right):
            mid = left + (right - left)//2
            spent = 0
            for pile in piles:
                spent+= (pile + mid - 1) // mid
            if spent<=h:
                right = mid
            else:
                left = mid+1
        return left