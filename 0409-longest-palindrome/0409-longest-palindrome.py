class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s).values()
        pairs = sum(c // 2 for c in counts)
        has_odd = any(c % 2 for c in counts)
        return pairs * 2 + (1 if has_odd else 0)