class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        num=len(arr)
        for i in range(num):
            for j in range(num):
                if i!=j and arr[i]==2*arr[j]:
                    return True
        return False