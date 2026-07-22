class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:   
        result = []
        i = 0
        
        while i < len(nums):
            j = i
            while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
                j += 1
            
            if i == j:
                result.append(str(nums[i]))
            else:
                result.append(f"{nums[i]}->{nums[j]}")
            
            i = j + 1

        return result