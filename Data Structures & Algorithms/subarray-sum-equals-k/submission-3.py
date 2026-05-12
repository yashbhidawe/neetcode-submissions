class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res, currSum, prefixSums = 0, 0, {0:1}



        for n in nums:
            currSum +=n
            diff = currSum - k

            if diff in prefixSums:
                res += prefixSums.get(diff, 0)
            prefixSums[currSum] = 1 + prefixSums.get(currSum, 0)
        return res