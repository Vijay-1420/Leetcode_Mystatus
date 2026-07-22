class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        v=len(haystack)
        m=len(needle)
        for i in range(v-m+1):
            j=0
            while j<v and haystack[i+j]==needle[j]:
                j+=1
                if j==m:
                    return i
        return -1