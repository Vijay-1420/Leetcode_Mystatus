class Solution:
    def totalNQueens(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2 or n == 3:
            return 0
        self.a = 0
        def place_queen(row, state):
            if row == n:
                self.a += 1
                return
            
            for col in range(n):
                if col in state:
                    continue
                conflict = False
                for r in range(row):
                    if abs(col - state[r]) == abs(row - r):
                        conflict = True
                        break
                if conflict:
                    continue
                place_queen(row + 1, state + [col])
        place_queen(0, [])
        return self.a