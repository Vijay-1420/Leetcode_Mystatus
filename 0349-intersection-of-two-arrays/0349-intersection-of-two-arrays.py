class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        value=set(nums1)
        result=[]
        
        for num in nums2:
            if num in value:
                result.append(num)
                value.remove(num)
                
        return result