class Solution:

    def prefixMult(self, nums):

        prefix = [1]*(len(nums)+1)
        for i in range(len(nums)):
            prefix[i + 1] = prefix[i]*nums[i]

        return prefix
    
    
    def productExceptSelf(self, nums):
        n = len(nums)
        prefix = self.prefixMult(nums)  
        suffix = self.prefixMult(nums[::-1])  
        suffix.reverse()
    
        return [prefix[i] * suffix[i+1] for i in range(n)]

            




        