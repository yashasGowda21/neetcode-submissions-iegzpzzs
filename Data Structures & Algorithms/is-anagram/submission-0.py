class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        count = defaultdict(int)
        for char in s:
            count[char] += 1
        for char in t:
            count[char] -= 1
        return all(val == 0 for val in count.values())
