class Solution:
    def maxProduct(self, n: int) -> int:
        d=sorted(str(n),reverse=True)
        return int(d[0])*int(d[1])