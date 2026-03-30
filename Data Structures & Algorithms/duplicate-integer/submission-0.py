class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        original_len = len(nums)
        sorted_len = len(set(nums))
        if original_len == sorted_len:
            return False
        else:
            return True 
        