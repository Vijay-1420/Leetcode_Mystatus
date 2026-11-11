class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        out=0
        for i in digits:
            out=out*10+i
        out+=1

        return list(map(int,str(out)))