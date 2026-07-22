class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(arr)

        value= {}
        current_val = 1

        for num in sorted_arr:
            if num not in value:
                value[num] = current_val
                current_val += 1

        return [value[num] for num in arr]