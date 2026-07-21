class Solution:
    def sumAndMultiply(self, n: int) -> int:
        a=""
        b=0
        for ch in str(n):
            if ch !='0':
                a+=ch
                b+=int(ch)
        if a=="":
            return 0
        return int(a)*b