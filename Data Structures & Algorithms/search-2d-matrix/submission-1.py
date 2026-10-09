
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        flat = [item for sublist in matrix for item in sublist]


        l, r = 0, len(flat) - 1

        while(l<=r):

            m = (l + r) // 2

            if target > flat[m]:

                l = m+1
            elif target < flat[m]:

                r = m - 1

            elif target == flat[m]:

                return True

        return False

                

        
