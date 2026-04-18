class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            element = target - num
            if element in seen:
                return [seen[element], i]
            
            seen[num] = i 