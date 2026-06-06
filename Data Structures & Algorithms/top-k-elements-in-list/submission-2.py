class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}


        for i in range(0, len(nums)):

            if nums[i] in freq:

                freq[nums[i]] += 1

            else:
                freq[nums[i]] = 1
        

        return  heapq.nlargest(k, freq, key=freq.get) 
