class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for val in range(len(nums),0,-1):
            if nums[val-1] in seen:
                continue
            seen[nums[val-1]] = nums.count(nums[val-1])
        seen = sorted(seen, key=seen.get,reverse=True)
        KFrequent = [seen[v] for v in range(k)]
        return sorted(KFrequent)