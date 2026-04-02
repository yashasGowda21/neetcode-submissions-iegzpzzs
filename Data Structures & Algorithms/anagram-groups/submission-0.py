class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        group_anagram = defaultdict(list)
        
        # loop through list of strs
        for word in strs:
            # sort each word within the strs
            sorted_str = ''.join(sorted(word))
            group_anagram[sorted_str].append(word)

        return list(group_anagram.values())

