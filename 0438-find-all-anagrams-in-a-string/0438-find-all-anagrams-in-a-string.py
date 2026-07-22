class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        target = Counter(p)
        win = Counter()
        k = len(p)

        for i in range(len(s)):
            win[s[i]] += 1

            if i >= k:
                out = s[i - k]
                win[out] -= 1
                if win[out] == 0:
                    del win[out]
                    
            if win == target:
                ans.append(i - k + 1)
                
        return ans