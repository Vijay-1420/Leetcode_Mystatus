class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort()

        days = len(pizzas) // 4
        odd = (days + 1) // 2

        total = sum(pizzas[-odd:])

        i = len(pizzas) - odd - 2

        for _ in range(days - odd):
            total += pizzas[i]
            i -= 2

        return total