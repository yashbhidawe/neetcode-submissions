class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        

        map = {}

        nums.sort()

        for i in range(len(nums)):

            if nums[i] not in map:
                map[nums[i]] = 0

            
            map[nums[i]] = map.get(nums[i], 0) + 1

        

        return max(map, key=map.get)