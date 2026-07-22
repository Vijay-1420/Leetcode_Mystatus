class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val=-1
        num=len(arr)-1
        while num>=0:
            t=arr[num]
            arr[num]=max_val
            if t>max_val:
                max_val=t
            num-=1
        return arr