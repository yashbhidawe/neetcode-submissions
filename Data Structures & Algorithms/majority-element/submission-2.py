class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        

        map = {}


        for i in range(len(nums)):

           
            
            map[nums[i]] = map.get(nums[i], 0) + 1

        

        return max(map, key=map.get)