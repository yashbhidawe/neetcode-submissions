class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        t = [list(row) for row in zip(*matrix)]
        return t
