class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        # Count the frequency of each element
        count = Counter(nums)
        
        # Return only the keys (elements) of the top k most common entries
        return [item[0] for item in count.most_common(k)]