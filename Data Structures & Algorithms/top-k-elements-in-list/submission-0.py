class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for value in nums:
            counts[value] = counts.get(value,0) + 1

        topkPairs  = sorted(counts.items(), key = lambda x: x[1],reverse=True)[:k]
        return [key for key,val in topkPairs]
        
        