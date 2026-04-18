class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for i in range(len(nums)):
            if(nums[i] not in count):
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1
        
        return max(count.keys(), key = count.get)
        