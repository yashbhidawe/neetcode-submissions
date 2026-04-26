class Solution:

        
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        countZero, countOne, countTwo = 0,0,0

        for num in nums:

            if num == 0:
                countZero+=1

            elif num == 1:
                countOne+=1

            else:
                countTwo+=1

        listZero = [0]*countZero
        listOne = [1]*countOne
        listTwo=[2]*countTwo

        nums.clear()

        nums += listZero+listOne+listTwo

            



