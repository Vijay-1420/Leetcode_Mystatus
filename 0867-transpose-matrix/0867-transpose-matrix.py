class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows=len(matrix)
        columns=len(matrix[0])
        result=[[0]*rows for _ in range(columns)]

        for row in range(rows):
            for col in range(columns):
                result[col][row]=matrix[row][col]
        return result