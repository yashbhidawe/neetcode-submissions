class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        nums.sort()

        currSmallPositive = 1

        for i in range(len(nums)):

            if nums[i] < currSmallPositive:
                continue

            if nums[i] == currSmallPositive:
                currSmallPositive += 1

        return currSmallPositive