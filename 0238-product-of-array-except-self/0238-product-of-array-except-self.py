class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        l1=[1]*n
        left=1
        for i in range(n):
            l1[i]=left
            left*=nums[i]
        right=1
        for i in range(n-1,-1,-1):
            l1[i]*=right
            right*=nums[i]
        return l1