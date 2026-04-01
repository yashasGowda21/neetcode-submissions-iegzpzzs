class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Map to store number: index
        num_map = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            # If complement exists, we found the pair
            if complement in num_map:
                # Return indices sorted: smaller first
                return [num_map[complement], i]
            # Otherwise, add current number and index to map
            num_map[num] = i

            