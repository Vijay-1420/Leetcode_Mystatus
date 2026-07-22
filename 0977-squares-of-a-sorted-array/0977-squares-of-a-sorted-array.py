class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans=list(sorted(map(lambda x:x**2,nums)))
        return ans